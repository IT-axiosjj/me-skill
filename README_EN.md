# me-skill

[中文](./README.md) | [English](./README_EN.md)

`me-skill` is a **Claude Code personal-self skill** for turning your own materials into a structured, revisable me profile.

It is inspired by the direction of `yourself-skill`, but the current version is closer to a **practical MVP**:

- collect notes / chat / correction materials
- generate `self.md`, `persona.md`, and `profile.md`
- keep updating the profile as new materials arrive

## What problem it tries to solve

Many "digital self" projects focus too much on surface tone mimicry. The result is often:

- somewhat similar style, but unstable
- facts, values, and boundaries mixed together
- no clear idea of what sounds like you and what clearly does not

`me-skill` tries to separate these layers:

- **self**: who you are, your preferences, values, and boundaries
- **persona**: how you speak, how you express emotions, how you tend to decide
- **profile**: the final summary used for simulation and reuse

## Who this is for

- people who want to build their own Claude Code personal skill
- people who want to preserve long-term communication patterns
- people who want to turn scattered materials into structured personal assets
- people who want a repository that can later grow into a more complete skill product

## Documentation

- [Installation & Usage](./INSTALL_AND_USAGE.md)
- [What me-skill does](./WHAT_IS_ME_SKILL.md)
- [Skill entry](./SKILL.md)

## What this repository is

This repository is not just a collection of Python scripts.

More accurately, it has two layers:

### 1. Skill layer
- `SKILL.md`
- `.claude/skills/me-skill/`
- `prompts/`

This is the part that makes it a Claude Code skill project.

### 2. Workflow layer
- `tools/import_text.py`
- `tools/import_chat.py`
- `tools/generate_me.py`
- `tools/update_me.py`
- `run_test_flow.py`

This is the part that makes it runnable as a practical MVP.

## Current capabilities

- import plain text materials: `tools/import_text.py`
- import simple chat transcripts: `tools/import_chat.py`
- generate a me profile from one or more JSON record files: `tools/generate_me.py`
- update an existing me profile with new materials: `tools/update_me.py`
- run an end-to-end sample or real-material flow: `run_test_flow.py`
- back up current versions: `tools/version_manager.py`

## Quick start

### Option 1: run the built-in sample

```bash
python run_test_flow.py
```

### Option 2: use your own materials

```bash
python run_test_flow.py --name my_me --notes path/to/notes.txt --chat path/to/chat.txt --correction path/to/correction.txt
```

### Option 3: start with notes only

```bash
python run_test_flow.py --name my_me --notes path/to/notes.txt
```

## Install as a Claude Code skill

If you want to use it in skill form, copy the mirrored directory into your Claude Code skills folder:

- project-level: `.claude/skills/me-skill/`
- global: `~/.claude/skills/me-skill/`

This repository already includes the mirror directory:

- `.claude/skills/me-skill/`

## Output structure

By default, generated files are written to:

- `selves/<slug>/records.json`
- `selves/<slug>/self.md`
- `selves/<slug>/persona.md`
- `selves/<slug>/profile.md`
- `selves/<slug>/versions/`

## Current extraction logic

The generator currently uses lightweight heuristic rules to split materials into:

- facts
- stable preferences
- style signals
- values
- boundaries
- emotion / attitude
- decision tendencies
- anti-patterns / expressions that do not sound like you
- representative quotes

It is better described as a **runnable MVP skill repository**, not a fully mature persona intelligence system.

## Current limitations

- does not yet parse raw WeChat / QQ exports directly
- currently works best with txt / md style text materials
- classification is heuristic, so manual review is still recommended

## Typical workflow

1. start with notes
2. add chat samples
3. add correction materials
4. generate the first me profile
5. keep refining `profile.md`

## Repository positioning

On GitHub, this project is best described as:

- a Claude Code skill project
- a personal digital-self organizer
- a workflow template for building a me profile from text materials
- a foundation repository that can grow into a more complete skill product
