---
name: research-technical-detail
description: >
  Gather and organize implementation-level technical details for AI/ML research.
  Use when user needs to understand how things are actually done in practice:
  what hyperparameters people use, what training tricks work, what the common
  gotchas are, how specific components are implemented, what evaluation setups
  look like concretely. Triggers include "how do people actually implement [X]",
  "what hyperparameters for [X]", "common gotchas with [X]", "best practices
  for training [X]", "how to set up evaluation for [X]", "what tricks does
  [paper] use", "implementation details", "technical setup". This skill operates
  at the "how" level — practical, concrete, implementation-focused.
---

# Research Technical Detail

Gather, organize, and present **implementation-level** technical information
so the human can make informed decisions about how to build and run things.

## What This Skill Covers

The "how" layer of research:

- How people actually implement methods in practice
- What hyperparameters, training recipes, and schedules are commonly used
- What tricks, heuristics, and engineering choices make things work
- What are the known gotchas, failure modes, and things to watch out for
- What evaluation setups, datasets, and metrics people actually use
- What's in the appendices and supplementary material of papers
- What the community has learned through trial and error

## What This Skill Does NOT Cover

- High-level paradigm relationships, motivation, or positioning
  → That's `research-conceptualization`
- Persistent note-taking across sessions
  → That's `research-session-notes`

## How to Operate

**Parallelize aggressively.** Technical details live in many different places
— papers, appendices, codebases, blog posts, community discussions. Don't
crawl these sources one by one. Spin up multiple sub-agents to search in
parallel across different source types and angles.

For example, when investigating how people implement a method:
- One agent searches paper appendices and supplementary material
- One agent searches GitHub repos for configs and default settings
- One agent searches for blog posts, tutorials, gotcha reports
- One agent checks community discussions (forums, X/Twitter, OpenReview)

Each sub-agent returns what it found. You synthesize across sources,
cross-reference (does the code match what the paper claims?), and organize
into a coherent reference.

**Think about decomposition before searching.** What independent source
types or search angles exist for this query? Dispatch them in parallel.
The more parallel work, the faster and more comprehensive the result.

Organize findings by what the human needs to act on. Group by component,
by decision point, or by stage of the pipeline — whatever makes the
information most actionable.

**Present as a reference, not a prescription.** The human decides what to
use and what to ignore. You surface what's out there — they choose.

## Trust Your Judgment

Every research area has different technical details that matter. You know
what's worth surfacing for a given method, dataset, or pipeline. Don't
follow a fixed checklist — adapt to what's actually important for this
specific context.
