# me-skill

[中文](./README.md) | [English](./README_EN.md)

`me-skill` is a Claude Code skill / local workflow for building a structured personal profile from your own materials.

Its goal is not just to mimic tone. It tries to organize your materials into a more stable structure:

- who you are
- how you speak
- what you value
- where your boundaries are
- what clearly does **not** sound like you

Final outputs:

- `self.md`
- `persona.md`
- `profile.md`
- `records.json`

## What it is useful for

- building a first draft of your AI persona
- organizing your long-term communication style
- turning scattered notes, chats, and corrections into structured assets
- creating a foundation for stronger persona / memory systems later

## Documentation

- [Installation & Usage](./INSTALL_AND_USAGE.md)
- [What me-skill does](./WHAT_IS_ME_SKILL.md)
- [Skill entry](./SKILL.md)

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

## Project structure

- `SKILL.md`: skill entry description
- `prompts/`: interview, analysis, build, merge, and correction templates
- `tools/`: import, generate, update, and version backup scripts
- `templates/`: sample inputs, usage notes, and helper docs
- `selves/`: generated personal profiles

## Output structure

By default, generated files are written to:

- `selves/<slug>/records.json`
- `selves/<slug>/self.md`
- `selves/<slug>/persona.md`
- `selves/<slug>/profile.md`
- `selves/<slug>/versions/`

## Current extraction logic

The generator uses lightweight heuristic rules to split materials into:

- facts
- stable preferences
- style signals
- values
- boundaries
- emotion / attitude
- decision tendencies
- anti-patterns / expressions that do not sound like you
- representative quotes

This is not a deep LLM-driven analyzer. It is a practical, runnable MVP.

## Current limitations

- does not yet parse raw WeChat / QQ exports directly
- currently works best with txt / md style text materials
- classification is heuristic, so manual review is still recommended

## Recommended workflow

1. start with notes
2. add chat samples to improve style accuracy
3. add correction materials to define boundaries and anti-patterns
4. keep refining `profile.md`

## Built-in sample flow

This repository already includes a self-generated test case.

### Sample source files

- `templates/generated_test/test_notes.txt`
- `templates/generated_test/test_chat.txt`
- `templates/generated_test/test_correction.txt`

### Run the sample flow manually

```bash
python tools/import_text.py templates/generated_test/test_notes.txt --source self_notes --kind note --output templates/generated_test/test_notes.json
python tools/import_chat.py templates/generated_test/test_chat.txt --source chat_sample --output templates/generated_test/test_chat.json
python tools/import_text.py templates/generated_test/test_correction.txt --source correction_round --kind correction --output templates/generated_test/test_correction.json
python tools/generate_me.py templates/generated_test/test_notes.json templates/generated_test/test_chat.json --name generated_case --output-dir selves
python tools/update_me.py selves/generated_case templates/generated_test/test_correction.json
```

### Or run it with one command

```bash
python run_test_flow.py
```

## Multi-file input

You can also pass multiple notes or chat files at once:

```bash
python run_test_flow.py --name my_me --notes notes_a.txt notes_b.md --chat chat_a.txt chat_b.md --correction correction.txt
```

## Repository positioning

On GitHub, this project can be presented as:

- a Claude Code skill project
- a personal digital-self organizer
- a workflow template for building a structured me-profile from text materials
