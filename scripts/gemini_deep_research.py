#!/usr/bin/env python3
"""Call Google Gemini Deep Research API and write results to a file.

Usage:
    python3 scripts/gemini_deep_research.py --prompt "PROMPT" --output PATH
    python3 scripts/gemini_deep_research.py --prompt-file PATH --output PATH

Exit codes:
    0  Success
    1  API error (auth, quota, invalid request)
    2  Timeout
    3  Research failed (API returned failed status)
    4  Empty or malformed response
"""

import argparse
import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv
from google import genai


MIN_OUTPUT_CHARS = 500


def main():
    parser = argparse.ArgumentParser(description="Gemini Deep Research API caller")
    prompt_group = parser.add_mutually_exclusive_group(required=True)
    prompt_group.add_argument("--prompt", type=str, help="Research prompt text")
    prompt_group.add_argument("--prompt-file", type=str, help="File containing research prompt")
    parser.add_argument("--output", type=str, required=True, help="Output file path")
    parser.add_argument("--timeout", type=int, default=3600, help="Timeout in seconds (default: 3600)")
    parser.add_argument("--poll-interval", type=int, default=10, help="Poll interval in seconds (default: 10)")
    args = parser.parse_args()

    # Resolve prompt
    if args.prompt_file:
        prompt = Path(args.prompt_file).read_text()
    else:
        prompt = args.prompt

    # Load API key
    load_dotenv(Path(__file__).resolve().parent.parent / ".env")
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment", file=sys.stderr)
        sys.exit(1)

    # Create client and start research
    client = genai.Client(api_key=api_key)

    try:
        interaction = client.interactions.create(
            agent="deep-research-pro-preview-12-2025",
            input=prompt,
            background=True,
        )
    except Exception as e:
        print(f"Error creating interaction: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Research started: {interaction.id}", flush=True)

    # Poll for completion
    start_time = time.time()
    while True:
        elapsed = time.time() - start_time
        if elapsed > args.timeout:
            print(f"\nError: Timeout after {args.timeout}s. Interaction ID: {interaction.id}", file=sys.stderr)
            sys.exit(2)

        try:
            interaction = client.interactions.get(interaction.id)
        except Exception as e:
            print(f"\nError polling interaction: {e}", file=sys.stderr)
            sys.exit(1)

        if interaction.status == "completed":
            break
        elif interaction.status == "failed":
            error_msg = getattr(interaction, "error", "Unknown error")
            print(f"\nError: Research failed: {error_msg}", file=sys.stderr)
            sys.exit(3)

        print(".", end="", flush=True)
        time.sleep(args.poll_interval)

    # Extract output
    try:
        output_text = interaction.outputs[-1].text
    except (IndexError, AttributeError) as e:
        print(f"\nError: Could not extract output text: {e}", file=sys.stderr)
        sys.exit(4)

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

    print(f"\nDone. Written to {args.output}")
    sys.exit(0)


if __name__ == "__main__":
    main()
