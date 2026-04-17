#!/usr/bin/env python3
from __future__ import annotations

import shutil
from datetime import datetime
from pathlib import Path

TARGETS = ["self.md", "persona.md", "profile.md"]


def backup_versions(me_dir: Path) -> list[Path]:
    version_dir = me_dir / "versions"
    version_dir.mkdir(exist_ok=True)
    created = []
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    for name in TARGETS:
        source = me_dir / name
        if not source.exists():
            continue
        target = version_dir / f"{timestamp}_{name}"
        shutil.copy2(source, target)
        created.append(target)
    return created


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Backup current me files into versions directory")
    parser.add_argument("me_dir", help="Path to me directory")
    args = parser.parse_args()

    created = backup_versions(Path(args.me_dir))
    for item in created:
        print(item)
