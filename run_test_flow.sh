#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
TEMPLATE_DIR="$ROOT_DIR/templates/generated_test"
OUTPUT_DIR="$ROOT_DIR/selves"
CASE_NAME="generated_case"

printf '==> Importing test materials\n'
python "$ROOT_DIR/tools/import_text.py" "$TEMPLATE_DIR/test_notes.txt" --source self_notes --kind note --output "$TEMPLATE_DIR/test_notes.json"
python "$ROOT_DIR/tools/import_chat.py" "$TEMPLATE_DIR/test_chat.txt" --source chat_sample --output "$TEMPLATE_DIR/test_chat.json"
python "$ROOT_DIR/tools/import_text.py" "$TEMPLATE_DIR/test_correction.txt" --source correction_round --kind correction --output "$TEMPLATE_DIR/test_correction.json"

printf '==> Generating initial me\n'
rm -rf "$OUTPUT_DIR/$CASE_NAME"
python "$ROOT_DIR/tools/generate_me.py" "$TEMPLATE_DIR/test_notes.json" "$TEMPLATE_DIR/test_chat.json" --name "$CASE_NAME" --output-dir "$OUTPUT_DIR"

printf '==> Updating me with correction material\n'
python "$ROOT_DIR/tools/update_me.py" "$OUTPUT_DIR/$CASE_NAME" "$TEMPLATE_DIR/test_correction.json"

printf '==> Done\n'
printf 'Output directory: %s\n' "$OUTPUT_DIR/$CASE_NAME"
printf 'Files:\n'
ls -R "$OUTPUT_DIR/$CASE_NAME"
