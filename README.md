# Research Skill Pack

Codex-ready research skills bundle for high-recall AI/ML research workflows.

## Included

- `research-conceptualization/`: Concept-level research landscape mapping (`what` and `why`)
- `research-technical-detail/`: Implementation-level research detail gathering (`how`)
- `AGENTS.md`: Cross-session note-taking and knowledge compounding guidance

## One-Command Install (Remote Codex)

Run this on your remote machine to install both skills and pull `AGENTS.md`:

```bash
bash -lc 'set -euo pipefail; CH="${CODEX_HOME:-$HOME/.codex}"; python3 "$CH/skills/.system/skill-installer/scripts/install-skill-from-github.py" --repo CharonWangg/research-skill-pack --path research-conceptualization research-technical-detail --ref main; mkdir -p "$CH"; curl -fsSL https://raw.githubusercontent.com/CharonWangg/research-skill-pack/main/AGENTS.md -o "$CH/AGENTS.md"; echo "Installed. Restart Codex to pick up new skills/instructions."'
```

References:
- [Codex Skills](https://developers.openai.com/codex/skills)
- [AGENTS.md Guide](https://developers.openai.com/codex/guides/agents-md)

## Inspiration

Inspired by the LinkedIn blog post:

- Title: `I spent $10,000 to automate my research at OpenAI with Codex`
- Author: `Karel D'Oosterlinck`
- Published: `2026-02-06`
