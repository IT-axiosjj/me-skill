#!/usr/bin/env python3
import argparse
import shutil
import subprocess
from pathlib import Path


def run(command: list[str]) -> None:
    print('==>', ' '.join(command))
    subprocess.run(command, check=True)


def default_paths(root_dir: Path) -> dict[str, Path]:
    template_dir = root_dir / 'templates' / 'generated_test'
    return {
        'notes': template_dir / 'test_notes.txt',
        'chat': template_dir / 'test_chat.txt',
        'correction': template_dir / 'test_correction.txt',
    }


def derive_json_path(path: Path) -> Path:
    return path.with_suffix('.json')


def import_text(root_dir: Path, path: Path, source: str, kind: str, output: Path) -> None:
    run([
        'python',
        str(root_dir / 'tools' / 'import_text.py'),
        str(path),
        '--source', source,
        '--kind', kind,
        '--output', str(output),
    ])


def import_chat(root_dir: Path, path: Path, source: str, output: Path) -> None:
    run([
        'python',
        str(root_dir / 'tools' / 'import_chat.py'),
        str(path),
        '--source', source,
        '--output', str(output),
    ])


def main() -> None:
    parser = argparse.ArgumentParser(description='Run end-to-end me generation flow')
    parser.add_argument('--name', default='generated_case', help='Output me name')
    parser.add_argument('--notes', nargs='+', help='One or more notes text files')
    parser.add_argument('--chat', nargs='+', help='Optional one or more chat text files')
    parser.add_argument('--correction', help='Optional path to correction text file')
    parser.add_argument('--output-dir', help='Output selves directory')
    parser.add_argument('--notes-source', default='self_notes', help='Source label prefix for notes')
    parser.add_argument('--chat-source', default='chat_sample', help='Source label prefix for chat')
    parser.add_argument('--correction-source', default='correction_round', help='Source label for correction')
    args = parser.parse_args()

    root_dir = Path(__file__).resolve().parent
    defaults = default_paths(root_dir)
    output_dir = Path(args.output_dir) if args.output_dir else root_dir / 'selves'
    case_name = args.name
    case_dir = output_dir / case_name

    notes_paths = [Path(item) for item in args.notes] if args.notes else [defaults['notes']]
    chat_paths = [Path(item) for item in args.chat] if args.chat else []
    correction_path = Path(args.correction) if args.correction else None

    notes_jsons: list[Path] = []
    chat_jsons: list[Path] = []
    correction_json: Path | None = None

    print('==> Importing materials')
    for index, notes_path in enumerate(notes_paths, start=1):
        notes_json = derive_json_path(notes_path)
        import_text(root_dir, notes_path, f'{args.notes_source}_{index}', 'note', notes_json)
        notes_jsons.append(notes_json)

    for index, chat_path in enumerate(chat_paths, start=1):
        chat_json = derive_json_path(chat_path)
        import_chat(root_dir, chat_path, f'{args.chat_source}_{index}', chat_json)
        chat_jsons.append(chat_json)

    if correction_path is not None:
        correction_json = derive_json_path(correction_path)
        import_text(root_dir, correction_path, args.correction_source, 'correction', correction_json)

    print('==> Generating initial me')
    shutil.rmtree(case_dir, ignore_errors=True)
    generate_command = [
        'python',
        str(root_dir / 'tools' / 'generate_me.py'),
        *[str(path) for path in notes_jsons],
        *[str(path) for path in chat_jsons],
        '--name', case_name,
        '--output-dir', str(output_dir),
    ]
    run(generate_command)

    if correction_json is not None:
        print('==> Updating me with correction material')
        run([
            'python',
            str(root_dir / 'tools' / 'update_me.py'),
            str(case_dir),
            str(correction_json),
        ])

    print('==> Done')
    print(f'Output directory: {case_dir}')
    print('Files:')
    for path in sorted(case_dir.rglob('*')):
        relative = path.relative_to(case_dir)
        print(relative if relative != Path('.') else case_dir.name)


if __name__ == '__main__':
    main()
