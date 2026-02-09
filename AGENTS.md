---
name: research-session-notes
description: >
  Persistent note-taking and knowledge compounding across research sessions.
  Use whenever working on any ongoing research task — experiments, coding,
  analysis, debugging, reading, or exploration. Ensures that insights,
  decisions, gotchas, and context are captured and available in future sessions.
  Triggers include any ongoing research work, "pick up where we left off",
  "continue working on [project]", "what did we figure out last time",
  or any session where knowledge should persist. Core purpose: take notes,
  compound knowledge, never lose context.
---

# Research Session Notes

Ensure knowledge compounds across sessions. Take notes so nothing useful
is lost between conversations.

## What You Do

1. **At the start of a session**: If notes exist for this project, read them
   first. Start from accumulated knowledge, not from zero.

2. **During the session**: When something noteworthy happens — a decision is
   made, something breaks, something surprising is found, something important
   is learned — note it. Don't wait until the end.

3. **At the end of every session**: Write or update notes capturing what
   happened, what was learned, and what's still open. This is non-negotiable.

## What to Note

Use your judgment. As orientation: capture anything that a fresh session
would benefit from knowing. This includes but is not limited to decisions
and their rationale, things that didn't work and why, gotchas and fixes,
updated understanding, and open questions.

Don't over-record trivial things. Don't under-record important things.
You're intelligent enough to know the difference.

## Where to Store

```
{project}/
└── agent_notes/
    ├── session_YYYY-MM-DD.md
    └── knowledge.md
```

`session_*.md` = what happened that day.
`knowledge.md` = durable insights, updated over time.

If the project already has a notes structure, use it. Don't impose yours.

## Key Rules

- Don't ask permission to take notes — just do it
- Don't use a rigid schema — adapt to what needs recording
- Don't make strategic decisions — the human decides direction, you remember context
- If new information contradicts old notes, update and flag the contradiction
