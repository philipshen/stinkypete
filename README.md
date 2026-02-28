# Researcher

Recursive deep research powered by Gemini and OpenAI deep research APIs, orchestrated by Claude Code.

Warning: recursive API calls are made at the discretion of the agents. This could murder your API usage

## Overview

This project uses two Claude Code skills to automate deep, recursive research on any topic:

1. **recursive-research** — The orchestrator. Sets up a research session, discovers initial topics with the user, dispatches parallel deep research subagents, and synthesizes cited final outputs.
2. **deep-research** — The per-topic worker. Runs as a subagent for each research topic. Calls a deep research API, processes the output, extracts insights, and feeds open questions back into the queue.

Research naturally terminates when no new relevant, non-redundant questions remain.

## Setup

1. **Python environment:**

   ```bash
   python3 -m venv .venv
   .venv/bin/pip install -r requirements.txt
   ```

2. **API keys:** Create a `.env` file in the project root:

   ```
   GEMINI_API_KEY=your-key-here
   OPENAI_API_KEY=your-key-here
   ```

3. **Usage:** Ask Claude Code to research a topic. The `recursive-research` skill triggers on requests like "research X", "investigate Y", or "deep dive into Z".

## How It Works

Each research session creates a structured directory under `topics/`:

```
topics/2026-02-28-iran-war-market-effects/
├── DESIRED_OUTPUT.md   # Freeform description of what you want produced
├── LOG.md              # Timestamped audit trail of all actions
├── TODO.md             # Running checklist of research topics
├── research/
│   ├── deepresearch-oil-supply/
│   │   ├── TOPIC.md                # API choice + exact prompt sent
│   │   ├── SUMMARY.md              # Abstract, Key Insights, Open Questions
│   │   ├── RAW_GEMINI_OUTPUT.md    # Verbatim Gemini API response (if used)
│   │   └── RAW_OPENAI_OUTPUT.md    # Verbatim OpenAI API response (if used)
│   └── deepresearch-defense-stocks/
│       └── ...
└── outputs/
    ├── REPORT.md       # Final output satisfying DESIRED_OUTPUT.md
    └── SOURCES.md      # Consolidated citations from all research
```

**The workflow:**

1. **Setup** — Creates the session directory, asks you to describe the desired output, initializes log/todo files.
2. **Root topic discovery** — Does preliminary web searches, proposes 3-7 initial research topics, you pick which to pursue.
3. **Recursive deep research** — For each topic in the TODO, dispatches a subagent that calls the Gemini or OpenAI deep research API. Each subagent writes a summary and may add new open questions back to the TODO. Multiple subagents run in parallel.
4. **Output synthesis** — Once the TODO is exhausted, reads all summaries and writes cited output files matching your DESIRED_OUTPUT.md spec.

**Deduplication:** Three layers prevent redundant research — subagent redundancy checks against the log and completed summaries, open-question filtering against existing TODOs, and directory-level slug uniqueness.

**Configuration:** Edit `config.yml` in the project root to control API selection, parallelism, and safety limits. See the inline comments in that file for details.
