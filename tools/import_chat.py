#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


CHAT_SPLIT_RE = re.compile(r"^\s*([^:：]+)\s*[:：]\s*(.+?)\s*$")


def parse_lines(lines: list[str], source: str) -> list[dict]:
    records = []
    for index, raw_line in enumerate(lines, start=1):
        line = raw_line.strip()
        if not line:
            continue
        match = CHAT_SPLIT_RE.match(line)
        if match:
            speaker = match.group(1).strip()
            text = match.group(2).strip()
        else:
            speaker = "unknown"
            text = line
        records.append(
            {
                "id": index,
                "speaker": speaker,
                "text": text,
                "source": source,
                "kind": "chat",
                "meta": {"line": index},
            }
        )
    return records


def main() -> None:
    parser = argparse.ArgumentParser(description="Import simple chat transcript into me-skill JSON format")
    parser.add_argument("input", help="Path to chat transcript")
    parser.add_argument("--source", default="chat", help="Source label")
    parser.add_argument("--output", help="Path to output json file")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else input_path.with_suffix(".json")
    lines = input_path.read_text(encoding="utf-8").splitlines()
    records = parse_lines(lines, args.source)
    output_path.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    print(output_path)


if __name__ == "__main__":
    main()
