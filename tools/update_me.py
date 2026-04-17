#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

from generate_me import load_records, write_me
from version_manager import backup_versions


def infer_name(me_dir: Path) -> str:
    return me_dir.name


def load_existing_records(me_dir: Path) -> list[dict]:
    records_path = me_dir / "records.json"
    if not records_path.exists():
        return []
    return json.loads(records_path.read_text(encoding="utf-8"))


def save_records(me_dir: Path, records: list[dict]) -> None:
    records_path = me_dir / "records.json"
    records_path.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Update an existing me profile from new JSON records")
    parser.add_argument("me_dir", help="Path to existing me directory")
    parser.add_argument("inputs", nargs="+", help="Path(s) to new json records")
    parser.add_argument("--name", help="Override me name")
    args = parser.parse_args()

    me_dir = Path(args.me_dir)
    me_dir.mkdir(parents=True, exist_ok=True)
    backup_versions(me_dir)
    existing_records = load_existing_records(me_dir)
    new_records = load_records([Path(item) for item in args.inputs])
    all_records = existing_records + new_records
    save_records(me_dir, all_records)
    write_me(me_dir, args.name or infer_name(me_dir), all_records)
    print(me_dir)


if __name__ == "__main__":
    main()
