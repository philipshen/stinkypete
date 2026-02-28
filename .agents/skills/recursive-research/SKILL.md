---
name: recursive-research
description: Use when the user wants to deeply research a topic using AI deep research APIs (Gemini, OpenAI). Triggers on requests to research, investigate, analyze, or explore a topic in depth.
---

# Recursive Research Orchestrator

## Overview

Orchestrates a multi-phase deep research workflow. Creates a structured research session, discovers initial topics with the user, dispatches parallel `deep-research` subagents, and synthesizes final outputs with citations.

Uses TODO.md as a work queue and LOG.md as an audit trail. Research terminates when no new relevant, non-redundant questions remain.

## When to Use

- User asks to "research", "investigate", "deep dive into", or "explore" a topic
- User wants a comprehensive report on a subject
- User needs multi-source analysis with citations

## The Pattern

### Phase 0: Preflight Check

**This phase runs BEFORE any files are created.** It validates that the environment is ready.

1. Read `config.yml` from the project root. Verify it exists and contains a valid `deep_research_api` value (`"gemini"`, `"openai"`, `"random"`, or `"all"`). If missing or invalid, stop and tell the user.
2. Based on `deep_research_api`, determine which APIs are needed:
   - `"gemini"` → Gemini only
   - `"openai"` → OpenAI only
   - `"random"` or `"all"` → both Gemini and OpenAI
3. For each required API, run the corresponding check script:

```bash
# Check Gemini (if needed)
.venv/bin/python3 -c "from dotenv import load_dotenv; load_dotenv('.env'); import os; assert os.environ.get('GEMINI_API_KEY'), 'GEMINI_API_KEY not set in .env'; from google import genai; print('Gemini OK')"

# Check OpenAI (if needed)
.venv/bin/python3 -c "from dotenv import load_dotenv; load_dotenv('.env'); import os; assert os.environ.get('OPENAI_API_KEY'), 'OPENAI_API_KEY not set in .env'; import openai; print('OpenAI OK')"
```

4. If any check fails, stop immediately and tell the user what's wrong:
   - Missing `.venv` → "Run `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt`"
   - Missing SDK → "Run `.venv/bin/pip install -r requirements.txt`"
   - Missing API key → "Set {KEY_NAME} in .env"
   - Missing `.env` → "Create .env with your API keys (see README)"

**Do NOT proceed to Phase 1 until all checks pass.**

### Phase 1: Session Setup

1. Generate a session directory: `topics/{yyyy-mm-dd}-{kebab-case-slug}/`
2. Create the full structure:
   ```
   topics/{yyyy-mm-dd}-{slug}/
   ├── DESIRED_OUTPUT.md
   ├── LOG.md
   ├── TODO.md
   ├── research/
   └── outputs/
   ```
3. Ask the user: "What would you like the final output to look like?" Write their response into `DESIRED_OUTPUT.md`.
4. Read `config.yml` from the project root for settings. See inline comments in that file for available options. Never modify this file — it is user-managed.
5. Initialize LOG.md from the template in `references/LOG_TEMPLATE.md`. Record session start.
6. Initialize TODO.md from the template in `references/TODO_TEMPLATE.md`.

### Phase 2: Root Topic Discovery

1. Enter plan mode. Use WebSearch to do 3-5 preliminary searches on the user's topic.
2. Based on results and the DESIRED_OUTPUT.md, propose 3-7 initial research topics with one-sentence descriptions.
3. Present as a numbered list. Ask the user which to pursue (they can select, add, or modify).
4. For each selected topic, add a TODO.md entry: `- [ ] {Title} | {description} | source: root`
5. Update LOG.md: `[{ISO8601 UTC}] Root topic discovery complete. {N} topics selected: {slug1}, {slug2}, ...`

### Phase 3: Recursive Deep Research Loop

Repeat until TODO.md has no unchecked items:

1. Read TODO.md. Collect all `- [ ]` items. (Treat `- [~]` items from interrupted runs as unchecked too.)
2. If none remain, proceed to Phase 4.
3. Select up to `max_parallel_agents` items (from project root config.yml). Mark them `- [~]` in TODO.md.
4. **Dispatch deep-research subagents in parallel.** For each topic, launch an Agent with `subagent_type: "general-purpose"` and paste the following context directly (do NOT tell the subagent to read files):

```
You are a deep-research subagent. Use the deep-research skill. Here is your full context:

SESSION_DIR: {path to session directory, e.g. topics/2026-02-28-iran-war/}
PROJECT_ROOT: {path to project root, i.e. the git repo root}
TOPIC: {topic title}
SLUG: {kebab-case slug}
DESCRIPTION: {one-sentence description from TODO.md}

DESIRED_OUTPUT:
{full contents of DESIRED_OUTPUT.md}

DEEP_RESEARCH_API: {resolved value: "gemini", "openai", or "all"}

CURRENT LOG (last 50 lines):
{tail of LOG.md}

CURRENT TODO:
{full contents of TODO.md}

COMPLETED RESEARCH (abstracts only):
{for each completed research: slug + Abstract from SUMMARY.md}

Execute the deep-research skill for this topic.
All file paths within the session (research/, TODO.md, LOG.md, etc.) are relative to SESSION_DIR.
```

5. Wait for all dispatched subagents to complete.
6. **Dispatch synthesizer subagent.** Launch a single Agent with `subagent_type: "general-purpose"` and paste the following context:

```
You are a research synthesizer subagent. Your job is to evaluate open questions from recently completed deep research and decide which warrant further investigation.

SESSION_DIR: {path}
PROJECT_ROOT: {path}
JUST_COMPLETED: {list of slugs that just finished, e.g. deepresearch-oil-supply, deepresearch-defense-stocks}

DESIRED_OUTPUT:
{full contents of DESIRED_OUTPUT.md}

CURRENT LOG (last 50 lines):
{tail of LOG.md}

CURRENT TODO:
{full contents of TODO.md}

COMPLETED RESEARCH (abstracts only):
{for each completed research: slug + Abstract from SUMMARY.md}

INSTRUCTIONS:
1. For each slug in JUST_COMPLETED, read research/{slug}/SUMMARY.md from SESSION_DIR. If SUMMARY.md does not exist (subagent was skipped as redundant or failed), skip that slug.
2. Collect all Open Questions from the summaries that exist.
3. For each open question:
   a. Relevance check: Does it relate to DESIRED_OUTPUT? Be strict — only questions that would materially improve the final output.
   b. Redundancy check: Is it already in CURRENT TODO (checked or unchecked)? Already covered by a COMPLETED RESEARCH abstract? Substantially similar to an existing item? If so, skip.
4. For each relevant, non-redundant question, append to TODO.md:
   - [ ] {question as research topic title} | {one-sentence description} | source: {slug}
5. Append to LOG.md:
   [{ISO8601 UTC}] Synthesis of {slugs}: {N} open questions found, {M} added to TODO (filtered {N-M} as irrelevant/redundant)
All file paths within the session are relative to SESSION_DIR.
```

7. Wait for synthesizer to complete.
8. Mark the batch items `- [x]` in TODO.md. Re-read TODO.md (synthesizer may have appended new items).
9. Loop back to step 1.

**Resolving `deep_research_api` config:**

- `"gemini"` or `"openai"`: pass through directly
- `"random"`: randomly pick one per topic
- `"all"`: dispatch ONE subagent per topic with DEEP_RESEARCH_API set to `"all"`. The subagent runs both APIs and writes `RAW_GEMINI_OUTPUT.md` and `RAW_OPENAI_OUTPUT.md` into the same research directory.

**Failure handling:** If a subagent fails, retry up to 3 times. After 3 failures, mark the TODO item as `- [!] FAILED: {reason}` and continue.

### Phase 4: Final Output Synthesis

1. Append to LOG.md: `[{ISO8601 UTC}] All TODO items complete. Beginning output synthesis.`
2. Read DESIRED_OUTPUT.md to understand what the user wants.
3. Read every SUMMARY.md in `research/` subdirectories.
4. Synthesize final output into `outputs/`. Format depends on DESIRED_OUTPUT.md. Always also write `outputs/SOURCES.md` consolidating all citations.
5. Every claim MUST include a citation using markdown footnotes (`[^1]`, `[^2]`, etc.) with a references section at the bottom.
6. Append to LOG.md: `[{ISO8601 UTC}] Output synthesis complete. Files written: {list with relative links, e.g. [REPORT](outputs/REPORT.md), [SOURCES](outputs/SOURCES.md)}`
7. Present results to the user with a summary of the research process.

## Common Mistakes

- **Skipping preflight.** Phase 0 must run before ANY files are created. A missing API key discovered mid-research wastes time and leaves orphaned directories.
- **Dispatching subagents with file references instead of pasted context.** Subagents don't share your file-reading context. Always paste full content.
- **Not resolving `random` or `all` API setting before dispatch.** The subagent must receive a concrete API choice (`"gemini"`, `"openai"`, or `"all"`).
- **Exceeding `max_parallel_agents`.** Never dispatch more deep-research subagents than the config allows.
- **Writing outputs without citations.** Every factual claim must trace back to a deep research source.
- **Skipping the synthesizer step.** Every batch of completed deep-research must be followed by a synthesizer dispatch to evaluate open questions.

## Red Flags

| Signal                                     | Action                                                           |
| ------------------------------------------ | ---------------------------------------------------------------- |
| TODO.md exceeds `max_todo_items` (skip if 0) | Pause, log warning, ask user whether to continue or narrow scope |
| Same topic appears researched twice in LOG | Redundancy check failed -- investigate before continuing         |
| 10+ research rounds with no convergence    | Ask user if research scope should be narrowed                    |
| Subagent fails 3 times on same topic       | Mark `[!] FAILED`, log it, move on                               |

## Integration

- **REQUIRED SUB-SKILL:** `deep-research` -- dispatched for each research topic
- **Python scripts:** `scripts/gemini_deep_research.py` and `scripts/openai_deep_research.py` (called by deep-research subagents, not by this orchestrator)
- **Templates:** `references/LOG_TEMPLATE.md`, `references/TODO_TEMPLATE.md`
- **Config:** `config.yml` in the project root (user-managed, read-only for agents; see inline comments for options)
