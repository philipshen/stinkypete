#!/usr/bin/env python3
"""Call OpenAI Deep Research API and write results to a file.

Usage:
    python3 scripts/openai_deep_research.py --prompt "PROMPT" --output PATH
    python3 scripts/openai_deep_research.py --prompt-file PATH --output PATH

Exit codes:
    0  Success
    1  API error (auth, quota, invalid request)
    2  Timeout
    3  Research failed (API returned terminal error state)
    4  Empty or malformed response
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


MIN_OUTPUT_CHARS = 500


def extract_output(response):
    texts = []
    annotations = []

    for item in getattr(response, "output", []) or []:
        for content in getattr(item, "content", []) or []:
            text = getattr(content, "text", None)
            if text:
                texts.append(text)
            content_annotations = getattr(content, "annotations", None)
            if content_annotations:
                annotations.extend(list(content_annotations))

    output_text = "\n".join(t for t in texts if t.strip())
    if not output_text:
        output_text = getattr(response, "output_text", "") or ""

    return output_text, annotations


def main():
    parser = argparse.ArgumentParser(description="OpenAI Deep Research API caller")
    prompt_group = parser.add_mutually_exclusive_group(required=True)
    prompt_group.add_argument("--prompt", type=str, help="Research prompt text")
    prompt_group.add_argument("--prompt-file", type=str, help="File containing research prompt")
    parser.add_argument("--output", type=str, required=True, help="Output file path")
    parser.add_argument("--timeout", type=int, default=900, help="Timeout in seconds (default: 900)")
    parser.add_argument("--poll-interval", type=int, default=5, help="Poll interval in seconds (default: 5)")
    parser.add_argument("--model", type=str, default="o3-deep-research-2025-06-26", help="Model name")
    args = parser.parse_args()

    # Resolve prompt
    if args.prompt_file:
        prompt = Path(args.prompt_file).read_text()
    else:
        prompt = args.prompt

    # Load API key
    load_dotenv(Path(__file__).resolve().parent.parent / ".env")
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found in environment", file=sys.stderr)
        sys.exit(1)

    # Create client and start research
    client = OpenAI(api_key=api_key)

    try:
        response = client.responses.create(
            model=args.model,
            input=[
                {
                    "role": "user",
                    "content": [{"type": "input_text", "text": prompt}],
                }
            ],
            tools=[{"type": "web_search_preview"}],
            reasoning={"summary": "auto"},
            background=True,
        )
    except Exception as e:
        print(f"Error creating response: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Research started: {response.id}", flush=True)

    # Poll for completion
    start_time = time.time()
    while response.status in ("queued", "in_progress"):
        elapsed = time.time() - start_time
        if elapsed > args.timeout:
            print(f"\nError: Timeout after {args.timeout}s. Response ID: {response.id}", file=sys.stderr)
            sys.exit(2)

        print(".", end="", flush=True)
        time.sleep(args.poll_interval)

        try:
            response = client.responses.retrieve(response.id)
        except Exception as e:
            print(f"\nError polling response: {e}", file=sys.stderr)
            sys.exit(1)

    # Check for failure
    if response.status != "completed":
        print(f"\nError: Research ended with status '{response.status}'", file=sys.stderr)
        sys.exit(3)

    # Extract output
    output_text, annotations = extract_output(response)

    if not output_text or len(output_text.strip()) < MIN_OUTPUT_CHARS:
        print(
            f"\nError: Output too short ({len((output_text or '').strip())} chars)",
            file=sys.stderr,
        )
        sys.exit(4)

    # Write output
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(output_text)

    # Write citations companion file
    if annotations:
        citations = [
            {
                "title": getattr(a, "title", ""),
                "url": getattr(a, "url", ""),
                "start_index": getattr(a, "start_index", None),
                "end_index": getattr(a, "end_index", None),
            }
            for a in annotations
        ]
        citations_path = output_path.with_suffix(".citations.json")
        citations_path.write_text(json.dumps(citations, indent=2))

    print(f"\nDone. Written to {args.output}")
    sys.exit(0)


if __name__ == "__main__":
    main()
