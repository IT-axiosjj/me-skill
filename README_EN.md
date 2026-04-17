# me-skill

[中文](./README.md) | [English](./README_EN.md)

A Claude Code skill for building a structured personal self-profile.

`me-skill` turns your text materials into a reusable me profile, helping you capture:

- who you are
- how you speak
- what you value
- where your boundaries are
- what clearly does not sound like you

## Features

- import notes, chat, and correction materials
- generate `self.md`, `persona.md`, and `profile.md`
- support incremental updates
- keep version history automatically
- support single-file and multi-file inputs

## Output

Generated files are written to:

- `selves/<slug>/records.json`
- `selves/<slug>/self.md`
- `selves/<slug>/persona.md`
- `selves/<slug>/profile.md`
- `selves/<slug>/versions/`

Where:

- `self.md`: facts, preferences, values, boundaries
- `persona.md`: style, emotion/attitude, decision tendencies, anti-patterns
- `profile.md`: final summary and simulation rules
- `records.json`: accumulated source materials

## Installation

### Install as a Claude Code skill

Copy the mirrored directory into your Claude Code skills folder:

- project-level: `.claude/skills/me-skill/`
- global: `~/.claude/skills/me-skill/`

This repository already includes the mirror directory:

- `.claude/skills/me-skill/`

### Use as a local workflow tool

Clone the repository and run the Python scripts directly.

## Quick Start

### Run the built-in sample

```bash
python run_test_flow.py
```

### Use your own materials

```bash
python run_test_flow.py --name my_me --notes path/to/notes.txt --chat path/to/chat.txt --correction path/to/correction.txt
```

### Start with notes only

```bash
python run_test_flow.py --name my_me --notes path/to/notes.txt
```

### Use multiple files at once

```bash
python run_test_flow.py --name my_me --notes notes_a.txt notes_b.md --chat chat_a.txt chat_b.md --correction correction.txt
```

## Material Format

### notes
Good for:
- self description
- diary excerpts
- preferences
- principles and boundaries

### chat
Recommended format:

```text
Me: Let's define the problem first.
Friend: Your tone is direct, but not aggressive.
```

### correction
Recommended format:

```text
Not like me: too emotional, too exaggerated, too preachy.
More like me: explain clearly first, then act.
I would not say: just rush in blindly.
```

## Project Structure

- `SKILL.md`: skill entry
- `prompts/`: interview, analysis, build, merge, and correction templates
- `tools/`: import, generate, update, and backup scripts
- `templates/`: sample materials and helper docs
- `selves/`: generated me profiles

## Docs

- [Installation & Usage](./INSTALL_AND_USAGE.md)
- [What me-skill does](./WHAT_IS_ME_SKILL.md)
- [Skill entry](./SKILL.md)

## Current Limitations

- mainly supports txt / md text materials for now
- does not yet parse raw WeChat / QQ exports directly
- classification is heuristic, so manual review is still recommended
