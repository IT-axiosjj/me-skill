<div align="center">

# me-skill

[中文](./README.md) | [English](./README_EN.md)

![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-7C3AED)
![Python](https://img.shields.io/badge/Python-3.x-3776AB)
![Status](https://img.shields.io/badge/Status-MVP-10B981)

**A Claude Code skill for building a personal self-profile**

_Turn scattered materials into a proper me profile._

_And clean up all the lines that definitely do not sound like you._

[Install](#install) · [Usage](#usage) · [Example](#example) · [Docs](#docs)

</div>

---

## Install

### Install as a Claude Code skill

Copy the mirror directory into your Claude Code skills folder:

```text
.claude/skills/me-skill/
```

Or the global directory:

```text
~/.claude/skills/me-skill/
```

This repository already includes the mirror directory:

```text
.claude/skills/me-skill/
```

### Use as a local workflow

Clone the repository and run the Python scripts directly.

Requirements:

- Python 3
- standard library only in the current version

---

## Usage

### Quick start

Run the built-in sample:

```bash
python run_test_flow.py
```

### Generate your own me profile

#### Notes only

```bash
python run_test_flow.py --name my_me --notes path/to/notes.txt
```

#### Notes + chat

```bash
python run_test_flow.py --name my_me --notes path/to/notes.txt --chat path/to/chat.txt
```

#### Notes + chat + correction

```bash
python run_test_flow.py --name my_me --notes path/to/notes.txt --chat path/to/chat.txt --correction path/to/correction.txt
```

#### Multiple files

```bash
python run_test_flow.py --name my_me --notes notes_a.txt notes_b.md --chat chat_a.txt chat_b.md --correction correction.txt
```

### Material format

#### notes

Good for:

- self description
- diary excerpts
- preferences
- principles and boundaries

#### chat

Recommended format:

```text
Me: Let's define the problem first.
Friend: Your tone is direct, but not aggressive.
```

#### correction

Recommended format:

```text
Not like me: too emotional, too exaggerated, too preachy.
More like me: explain clearly first, then act.
I would not say: just rush in blindly.
```

### Output files

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
- `versions/`: automatic backups before updates

---

## Example

A typical output structure looks like this:

```text
selves/generated_case/
├── records.json
├── self.md
├── persona.md
├── profile.md
└── versions/
```

Where:

- `self.md` describes who you are
- `persona.md` describes how you speak
- `profile.md` describes how to simulate you

---

## Features

### Supported input types

| Type | Purpose |
| --- | --- |
| notes | self description, preferences, principles, background |
| chat | real speaking style and interaction patterns |
| correction | anti-patterns and explicit corrections |

### Current capabilities

- import text materials
- import simple chat transcripts
- generate a me profile
- update an existing me profile incrementally
- keep version history automatically
- support single-file and multi-file input

### Current extraction dimensions

- facts
- stable preferences
- style signals
- values
- boundaries
- emotion / attitude
- decision tendencies
- anti-patterns / what does not sound like you
- representative quotes

---

## Project Structure

```text
me-skill/
├── SKILL.md
├── prompts/
├── tools/
├── templates/
├── selves/
├── run_test_flow.py
└── .claude/skills/me-skill/
```

| Path | Purpose |
| --- | --- |
| `SKILL.md` | skill entry definition |
| `prompts/` | interview, analysis, build, and correction templates |
| `tools/` | import, generate, update, and backup scripts |
| `templates/` | sample materials and helper docs |
| `selves/` | generated me profiles |
| `.claude/skills/me-skill/` | installable mirror directory |

---

## Notes

- currently works best with txt / md text materials
- does not yet parse raw WeChat / QQ exports directly
- classification is heuristic, so manual review is recommended
- the current version is best viewed as a runnable MVP skill repository

---

## Docs

- [Installation & Usage](./INSTALL_AND_USAGE.md)
- [What me-skill does](./WHAT_IS_ME_SKILL.md)
- [Skill entry](./SKILL.md)

---

## License

MIT
