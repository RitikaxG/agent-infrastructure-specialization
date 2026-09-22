#!/usr/bin/env python3
"""Resolve and audit the active Agent Runtime Reliability workstream."""

import argparse
import json
import re
from pathlib import Path
from typing import Dict, List


EVENT_ROUTES: Dict[str, List[str]] = {
    "engineering-checkpoint": [],
    "assistance-change": ["PROGRESS_GATES.md"],
    "supported-invariant": ["PATTERN_LEDGER.md"],
    "public-proof": ["INTERVIEW_EVIDENCE.md", "PROGRESS_GATES.md", "TARGET_COMPANIES.md"],
    "maintainer-feedback": ["INTERVIEW_EVIDENCE.md", "CONTRIBUTION_FILTER.md"],
    "weekly": ["PROGRESS_GATES.md", "WORKSTREAMS.json"],
    "monthly": ["PROGRESS_GATES.md", "TARGET_COMPANIES.md", "WORKSTREAMS.json"],
    "repository-switch": ["WORKSTREAMS.json", "ROADMAP.md", "../AGENTS.md"],
    "objective-change": ["NORTH_STAR.md"],
}


def load_registry(root: Path) -> dict:
    path = root / "WORKSTREAMS.json"
    if not path.is_file():
        raise SystemExit(f"FAIL registry is missing: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as error:
        raise SystemExit(f"FAIL invalid registry: {error}")


def active_entry(root: Path, registry: dict) -> tuple:
    active_id = registry.get("active")
    workstreams = registry.get("workstreams", {})
    entry = workstreams.get(active_id)
    if not isinstance(entry, dict):
        raise SystemExit(f"FAIL active workstream is not defined: {active_id}")
    return active_id, entry


def current_path(root: Path, entry: dict) -> Path:
    learning = (root / entry["learning"]).resolve()
    return learning / entry.get("current", "CURRENT.md")


def extract_question(text: str) -> str:
    match = re.search(
        r"^## Exact engineering question\s*$([\s\S]*?)(?=^##\s|\Z)",
        text,
        re.MULTILINE,
    )
    if not match:
        return "Unavailable"
    quoted = re.findall(r"^>\s*(.+)$", match.group(1), re.MULTILINE)
    return " ".join(quoted) if quoted else "Unavailable"


def command_status(root: Path) -> int:
    registry = load_registry(root)
    active_id, entry = active_entry(root, registry)
    path = current_path(root, entry)
    if not path.is_file():
        raise SystemExit(f"FAIL active CURRENT is missing: {path}")
    question = extract_question(path.read_text(encoding="utf-8"))
    print(f"Active workstream: {active_id}")
    print(f"Role: {entry.get('role', 'unknown')}")
    print(f"Source: {entry.get('source', 'unknown')}")
    print(f"Learning: {entry.get('learning', 'unknown')}")
    print(f"Question: {question}")
    return 0


def command_audit(root: Path) -> int:
    registry = load_registry(root)
    workstreams = registry.get("workstreams", {})
    failures = 0

    def report(ok: bool, message: str) -> None:
        nonlocal failures
        print(f"{'PASS' if ok else 'FAIL'} {message}")
        if not ok:
            failures += 1

    active_ids = [
        key for key, value in workstreams.items() if value.get("status") == "active"
    ]
    report(len(active_ids) == 1, "exactly one active workstream")
    declared = registry.get("active")
    report(active_ids == [declared], "declared active workstream matches status")
    entry = workstreams.get(declared, {})
    source = (root / entry.get("source", "missing")).resolve()
    learning = (root / entry.get("learning", "missing")).resolve()
    current = learning / entry.get("current", "CURRENT.md")
    report(source.is_dir(), f"active source exists: {entry.get('source', 'missing')}")
    report(learning.is_dir(), f"active learning workspace exists: {entry.get('learning', 'missing')}")
    report(current.is_file(), f"active CURRENT exists: {current}")
    router = root.parent / "AGENTS.md"
    router_text = router.read_text(encoding="utf-8") if router.is_file() else ""
    source_label = f"active source:   {source.name}/"
    learning_label = f"learning state:  {learning.name}/"
    report(source_label in router_text, "workspace router matches active source path")
    report(
        learning_label in router_text,
        "workspace router matches active learning path",
    )
    roadmap = root / "ROADMAP.md"
    roadmap_text = roadmap.read_text(encoding="utf-8") if roadmap.is_file() else ""
    marker = entry.get("roadmap_marker", "")
    report(bool(marker) and marker in roadmap_text, "roadmap matches active workstream")
    return 1 if failures else 0


def command_due(event: str) -> int:
    paths = EVENT_ROUTES[event]
    print(f"Event: {event}")
    if not paths:
        print("No global strategy file is due; update only the active learning workspace.")
        return 0
    print("Inspect only:")
    for path in paths:
        print(f"- {path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="strategyctl")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help=argparse.SUPPRESS,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("status")
    subparsers.add_parser("audit")
    due = subparsers.add_parser("due")
    due.add_argument("event", choices=sorted(EVENT_ROUTES))
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.command == "status":
        return command_status(args.root)
    if args.command == "audit":
        return command_audit(args.root)
    if args.command == "due":
        return command_due(args.event)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
