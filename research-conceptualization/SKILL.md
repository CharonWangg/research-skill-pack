---
name: research-conceptualization
description: >
  Gather and organize high-level, conceptual research information for AI/ML
  research. Use when user is thinking at the architectural or methodological
  level: exploring what paradigms exist, how approaches relate to each other,
  where the gaps are, what the motivation or positioning for an idea could be,
  or how a field is structured. Triggers include "what's the landscape of [X]",
  "how do these approaches relate", "what are the gaps in [X]", "motivation
  for [X]", "positioning", "paradigm", "taxonomy", "conceptualize",
  "architecture of [X]", "why does [method] work". This skill operates at the
  "what and why" level — not implementation details.
---

# Research Conceptualization

Gather, organize, and present **conceptual-level** research information so the
human can make informed decisions about direction, positioning, and design.

## What This Skill Covers

The "what and why" layer of research:

- How a field is structured — what paradigms exist, how they relate
- What assumptions underlie current approaches
- Where the gaps, contradictions, or underexplored territories are
- Why certain approaches work (or don't) at a conceptual level
- How to position a contribution — what's the motivation, what's missing
- Architectural and methodological design at the blocks-and-arrows level

## What This Skill Does NOT Cover

- Specific hyperparameters, training recipes, or implementation tricks
  → That's `research-technical-detail`
- Persistent note-taking across sessions
  → That's `research-session-notes`

## Figure Output Add-on

When you need to present conceptual findings with publication-style visuals,
use the embedded figure skill:

- `research-conceptualization/scientific-figure/SKILL.md`

## How to Operate

**Parallelize aggressively.** Don't search sequentially — decompose the
information gathering task into parallel sub-agent searches. The goal is
high recall at high speed.

When exploring a research landscape, spin up multiple sub-agents to search
simultaneously from different angles. For example:
- One agent searches by method/technique keywords
- One agent searches by problem/task keywords
- One agent scans recent top-venue proceedings
- One agent checks community signals (blogs, X/Twitter, OpenReview)

Each sub-agent returns structured findings. You synthesize, deduplicate,
and organize the combined results into a coherent picture.

**Decomposition is your most important decision.** Before searching, think
about what independent search angles exist for this topic. The more
orthogonal the angles, the better the coverage. Then dispatch sub-agents
in parallel — don't do them one by one.

Organize findings into clear, navigable structure. Group related things
together. Show how pieces connect. Highlight contradictions or tensions.
Provide sources for everything.

**Present as a briefing, not a recommendation.** The human decides what's
interesting, what direction to pursue, how to position their work. You
provide the information landscape — they navigate it.

When the human indicates what's interesting, go deeper — again using
parallel sub-agents to cover the deeper territory efficiently.

## Trust Your Judgment

You know what's relevant at the conceptual level vs. what's implementation
detail. You know how to structure a landscape map vs. a taxonomy vs. a
comparison. Adapt your output to what the information demands — don't follow
a rigid template.
