---
name: deep-research
description: Use when dispatched as a subagent to research a single topic using Gemini or OpenAI deep research API. Expects full context pasted in by recursive-research orchestrator. Do NOT invoke directly.
---

# Deep Research (Per-Topic Subagent)

## Overview

Handles a single deep research task. Dispatched by `recursive-research` with full context pasted in. Calls a deep research API via Python script, processes the result, extracts insights, and updates LOG.md.

## When to Use

- You are dispatched as a subagent by the `recursive-research` skill
- You receive a pasted context block containing: SESSION_PATH, TOPIC, SLUG, DESIRED_OUTPUT, API choice, current LOG, current TODO, and completed research summaries

Do NOT use this skill directly. It is subagent-only.

## The Pattern

### Step 1: Redundancy Check

Before doing any work:

1. Read the CURRENT LOG in your context. Search for `Deep research completed: deepresearch-{slug}` entries where the slug matches or is very similar to your topic.
2. Read the COMPLETED RESEARCH SUMMARIES in your context. If any summary covers substantially the same ground, abort early.
3. If redundant: append to LOG.md: `[{ISO8601 UTC}] Deep research SKIPPED (redundant): {slug}. Overlaps with: {existing_slug}` and exit.

### Step 2: Create Research Directory

Create `research/deepresearch-{slug}/` inside the session directory. Create:

**TOPIC.md:**

```markdown
# {Topic Title}

## API

{gemini, openai, or all}

## Prompt

{The complete prompt sent to the deep research API}
```

### Step 3: Construct the Deep Research Prompt

Build a focused, self-contained research prompt:

```
Research the following topic in depth:

TOPIC: {topic title}

CONTEXT: This research is part of a larger investigation into: {brief description from DESIRED_OUTPUT}

Please provide:
1. A comprehensive analysis of this topic
2. Key findings with supporting evidence
3. All source URLs for claims made
4. A list of open questions or areas that need further investigation

Focus on accuracy and cite your sources.
```

Write the prompt to `research/deepresearch-{slug}/_prompt.txt` for use with `--prompt-file`.

### Step 4: Update LOG and Call API

**Working directory:** Run all bash commands from **PROJECT_ROOT** (the git repo root). Use `{SESSION_DIR}/` prefix for session-relative paths (research files, LOG.md, etc.).

1. Append to LOG.md: `[{ISO8601 UTC}] Deep research started: deepresearch-{slug} (API: {api})`
2. Call the Python script(s). Output files are keyed by API name:

**If DEEP_RESEARCH_API is `"gemini"`:**

```bash
.venv/bin/python3 scripts/gemini_deep_research.py --prompt-file {SESSION_DIR}/research/deepresearch-{slug}/_prompt.txt --output {SESSION_DIR}/research/deepresearch-{slug}/RAW_GEMINI_OUTPUT.md
```

**If DEEP_RESEARCH_API is `"openai"`:**

```bash
.venv/bin/python3 scripts/openai_deep_research.py --prompt-file {SESSION_DIR}/research/deepresearch-{slug}/_prompt.txt --output {SESSION_DIR}/research/deepresearch-{slug}/RAW_OPENAI_OUTPUT.md
```

**If DEEP_RESEARCH_API is `"all"`:** Run both scripts (can be run in parallel):

```bash
.venv/bin/python3 scripts/gemini_deep_research.py --prompt-file {SESSION_DIR}/research/deepresearch-{slug}/_prompt.txt --output {SESSION_DIR}/research/deepresearch-{slug}/RAW_GEMINI_OUTPUT.md
.venv/bin/python3 scripts/openai_deep_research.py --prompt-file {SESSION_DIR}/research/deepresearch-{slug}/_prompt.txt --output {SESSION_DIR}/research/deepresearch-{slug}/RAW_OPENAI_OUTPUT.md
```

3. If a script exits non-zero:
   - Read stderr output
   - **Rate limit errors** (HTTP 429, "rate limit", "quota exceeded", or similar): Do NOT treat as failure. Wait with increasing backoff (60s, 120s, 240s) and retry the same script. No limit on retries — keep waiting and retrying until it succeeds.
   - **All other errors:** Append to LOG.md: `[{ISO8601 UTC}] Deep research FAILED: deepresearch-{slug} ({api}). Error: {error message}`. Write error details to `research/deepresearch-{slug}/ERROR.md`.
   - If DEEP_RESEARCH_API is `"all"` and only one API failed (non-rate-limit), continue with the successful output. If both fail, exit.

### Step 5: Verify the Raw Output

Read each `RAW_{API}_OUTPUT.md` file (e.g. `RAW_GEMINI_OUTPUT.md`, `RAW_OPENAI_OUTPUT.md`). Verify each contains substantive content (not empty, not an error, at least 500 characters). If malformed or empty, treat as failure (Step 4 error handling).

### Step 6: Write SUMMARY.md

Read through all raw output files carefully. When both `RAW_GEMINI_OUTPUT.md` and `RAW_OPENAI_OUTPUT.md` exist, synthesize insights from both. If `RAW_OPENAI_OUTPUT.md.citations.json` exists (written automatically by the OpenAI script), use it to enrich the Sources section with accurate titles and URLs. Write `research/deepresearch-{slug}/SUMMARY.md` with this structure:

```markdown
# Summary: {Topic Title}

## Abstract

{2-3 sentence summary of what was discovered}

## Key Insights

- **{Insight title}**: {Description} [Source: {url}]
- **{Insight title}**: {Description} [Source: {url}]

## Open Questions

- {Question 1}
- {Question 2}

## Primary Sources

1. [{title}]({url})
2. [{title}]({url})
```

### Step 7: Final Log Entry

Append to LOG.md:

```
[{ISO8601 UTC}] Deep research completed: deepresearch-{slug}. Summary: [SUMMARY](research/deepresearch-{slug}/SUMMARY.md)
```

## Common Mistakes

- **Skipping the redundancy check.** This is the primary mechanism preventing infinite recursion.

## Red Flags

| Signal                                | Action                                                 |
| ------------------------------------- | ------------------------------------------------------ |
| Raw output under 500 chars            | Treat as API failure                                   |
| Topic slug matches existing directory | Redundancy check failed -- abort                       |
| API call takes over 15 minutes        | Normal for deep research -- do not timeout prematurely |

## Integration

- **CALLED BY:** `recursive-research` orchestrator (never invoked directly)
- **CALLS:** `scripts/gemini_deep_research.py` or `scripts/openai_deep_research.py`
- **READS:** LOG.md, DESIRED_OUTPUT.md (all provided via pasted context)
- **WRITES:** LOG.md (append only), files in `research/deepresearch-{slug}/`
