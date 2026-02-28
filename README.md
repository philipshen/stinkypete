![Stinky Pete](https://static.wikia.nocookie.net/pixar/images/9/91/Stinky_Pete.png/revision/latest?cb=20241007180854)

# Stinky Pete

Recursive deep research powered by Gemini and OpenAI deep research APIs, orchestrated by any agent that can reference the skills (Claude Code, Codex, Gemini, Cursor should all work).

Some research examples can be found in topics/

Expect it to run for ~1hr before completing.

Warning: recursive API calls are gonna be made at the discretion of the agent. Watch out for your API bill. Since you're just using Codex or whatever to orchestrate, you can always interrupt it and say something like "that's good enough, skip the rest of the research and show me the results"

## Overview

This project uses two agent skills to automate deep, recursive research on any topic:

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

## Usage

### Basic Usage

1. Set up the .env with a GEMINI_API_KEY and/or OPENAI_API_KEY
2. Launch your coding agent of choice in this repo
3. Prompt it with something you want to research (if your agent has an explicit "Plan" mode, start in that mode)
4. It'll work with you to figure out the exit case for recursion, a base case of research topics to begin with, and what you want the output to look
5. Once it starts, it'll do all the research and then create the final output on its own

All the skills are agent-agnostic, so whatever orchestrator you prefer will work. If you really want it to run fully autonomously, pass in flags to make the agent bypass permissions e.g.

```bash
gemini --approval-mode=yolo
claude --dangerously-skip-permissions
codex --dangerously-bypass-approvals-and-sandbox
```

### Explorer

Once Python deps are installed you can launch the explorer:

```bash
./explorer/explorer.sh
```

This runs a really basic web GUI for browsing the research/outputs. It's for the lazy (like me), and isn't much more convenient than just using your IDE.

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

## TODO

- Follow-on research to drill deeper into existing topics
- Connections to gated data sources (CrunchBase, ahrefs, stuff like that)
- More detailed outputs. I suspect level-of-detail might be restricted by context windows - structured plans for creating the output would be simple and might help a lot
