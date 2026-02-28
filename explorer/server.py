#!/usr/bin/env python3
"""Explorer server: serves the SPA shell, topics tree API, raw files, and SSE for live reload."""

import json
import os
import threading
import time
from http.server import HTTPServer, SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

SCRIPT_DIR = Path(__file__).resolve().parent
TOPICS_DIR = SCRIPT_DIR.parent / "topics"
PORT = 3117

# ---------------------------------------------------------------------------
# File watcher + SSE broadcast
# ---------------------------------------------------------------------------

sse_clients: list = []
sse_clients_lock = threading.Lock()

last_change_time = 0.0
DEBOUNCE_SECONDS = 0.5


class TopicsChangeHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        global last_change_time
        now = time.time()
        if now - last_change_time < DEBOUNCE_SECONDS:
            return
        last_change_time = now
        broadcast_reload()


def broadcast_reload():
    with sse_clients_lock:
        dead = []
        for wfile in sse_clients:
            try:
                wfile.write(b"data: reload\n\n")
                wfile.flush()
            except Exception:
                dead.append(wfile)
        for d in dead:
            sse_clients.remove(d)


# ---------------------------------------------------------------------------
# Directory tree builder
# ---------------------------------------------------------------------------

def build_tree() -> list[dict]:
    if not TOPICS_DIR.is_dir():
        return []
    tree = []
    for topic_dir in sorted(TOPICS_DIR.iterdir()):
        if not topic_dir.is_dir() or topic_dir.name.startswith("."):
            continue
        entry: dict = {"name": topic_dir.name, "files": [], "research": [], "outputs": []}

        # Top-level files
        for f in sorted(topic_dir.iterdir()):
            if f.is_file() and not f.name.startswith("."):
                entry["files"].append(f.name)

        # Research sub-topics
        research_dir = topic_dir / "research"
        if research_dir.is_dir():
            for sub in sorted(research_dir.iterdir()):
                if sub.is_dir() and not sub.name.startswith("."):
                    sub_entry = {
                        "name": sub.name,
                        "files": sorted(
                            f.name for f in sub.iterdir() if f.is_file() and not f.name.startswith(".")
                        ),
                    }
                    entry["research"].append(sub_entry)

        # Outputs
        outputs_dir = topic_dir / "outputs"
        if outputs_dir.is_dir():
            for f in sorted(outputs_dir.iterdir()):
                if f.is_file() and not f.name.startswith("."):
                    ftype = "html" if f.suffix == ".html" else "md" if f.suffix == ".md" else "other"
                    entry["outputs"].append({"name": f.name, "type": ftype})

        tree.append(entry)
    return tree


# ---------------------------------------------------------------------------
# HTTP handler
# ---------------------------------------------------------------------------

class ExplorerHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # Quieter logging — only show non-200 or interesting routes
        pass

    def do_GET(self):
        path = self.path.split("?")[0]

        if path == "/" or path == "/index.html":
            self._serve_file(SCRIPT_DIR / "index.html", "text/html")
        elif path == "/api/tree":
            self._serve_json(build_tree())
        elif path == "/api/events":
            self._serve_sse()
        elif path.startswith("/topics/"):
            rel = path[len("/topics/"):]
            file_path = (TOPICS_DIR / rel).resolve()
            # Security: ensure path is under TOPICS_DIR
            if not str(file_path).startswith(str(TOPICS_DIR)):
                self.send_error(403)
                return
            if file_path.is_file():
                ct = "text/html" if file_path.suffix == ".html" else \
                     "text/markdown; charset=utf-8" if file_path.suffix == ".md" else \
                     "application/octet-stream"
                self._serve_file(file_path, ct)
            else:
                self.send_error(404)
        else:
            self.send_error(404)

    def _serve_file(self, filepath: Path, content_type: str):
        try:
            data = filepath.read_bytes()
        except FileNotFoundError:
            self.send_error(404)
            return
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        self.wfile.write(data)

    def _serve_json(self, obj):
        data = json.dumps(obj).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        self.wfile.write(data)

    def _serve_sse(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Connection", "keep-alive")
        self.end_headers()
        with sse_clients_lock:
            sse_clients.append(self.wfile)
        # Keep connection alive
        try:
            while True:
                time.sleep(30)
                self.wfile.write(b": keepalive\n\n")
                self.wfile.flush()
        except Exception:
            pass
        finally:
            with sse_clients_lock:
                if self.wfile in sse_clients:
                    sse_clients.remove(self.wfile)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # Start watchdog
    observer = Observer()
    observer.schedule(TopicsChangeHandler(), str(TOPICS_DIR), recursive=True)
    observer.daemon = True
    observer.start()

    server = ThreadingHTTPServer(("localhost", PORT), ExplorerHandler)
    server.daemon_threads = True
    print(f"Explorer running at http://localhost:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
        observer.stop()
        server.shutdown()


if __name__ == "__main__":
    main()
