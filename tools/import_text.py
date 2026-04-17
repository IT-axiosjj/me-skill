#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def split_lines(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines() if line.strip()]


def build_records(lines: list[str], source: str, kind: str) -> list[dict]:
    records = []
    for index, line in enumerate(lines, start=1):
        records.append(
            {
                "id": index,
                "source": source,
                "speaker": "unknown",
                "kind": kind,
                "text": line,
                "meta": {"line": index},
            }
        )
    return records


def main() -> None:
    parser = argparse.ArgumentParser(description="Import plain text materials into me-skill JSON format")
    parser.add_argument("input", help="Path to input text file")
    parser.add_argument("--source", default="text", help="Source label")
    parser.add_argument("--kind", default="note", help="Material kind")
    parser.add_argument("--output", help="Path to output json file")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else input_path.with_suffix(".json")

    text = load_text(input_path)
    records = build_records(split_lines(text), args.source, args.kind)

    output_path.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    print(output_path)


if __name__ == "__main__":
    main()
