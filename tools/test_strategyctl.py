import subprocess
import sys
import tempfile
import unittest
import json
from pathlib import Path


SCRIPT = Path(__file__).with_name("strategyctl.py")


class StrategyctlTests(unittest.TestCase):
    def run_cli(self, root: Path, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--root", str(root), *args],
            text=True,
            capture_output=True,
            check=False,
        )

    def make_workspace(self, directory: str) -> Path:
        workspace = Path(directory)
        strategy = workspace / "agent-infra-specialization"
        learning = workspace / "cua-learning"
        source = workspace / "cua"
        strategy.mkdir()
        learning.mkdir()
        source.mkdir()
        (workspace / "AGENTS.md").write_text(
            """# Workspace Router

active source:   cua/
learning state:  cua-learning/
""",
            encoding="utf-8",
        )
        (strategy / "ROADMAP.md").write_text(
            "# Roadmap\n\n## Months 1–2 — ACTIVE: CUA\n",
            encoding="utf-8",
        )
        (learning / "CURRENT.md").write_text(
            """# Current State

## Position

- subsystem: Driver Runtime

## Exact engineering question

> Does the runtime report readiness honestly?
""",
            encoding="utf-8",
        )
        (strategy / "WORKSTREAMS.json").write_text(
            json.dumps(
                {
                    "version": 1,
                    "active": "cua",
                    "reviews": {"weekly": "2026-09-17", "market": "2026-09-11"},
                    "workstreams": {
                        "cua": {
                            "role": "anchor",
                            "status": "active",
                            "source": "../cua",
                            "learning": "../cua-learning",
                            "current": "CURRENT.md",
                            "roadmap_marker": "ACTIVE: CUA",
                        },
                        "rivet": {
                            "role": "transfer",
                            "status": "planned",
                            "source": "../rivet",
                            "learning": "../rivet-learning",
                            "current": "CURRENT.md",
                        },
                    },
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        return strategy

    def test_status_resolves_active_current_question(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.make_workspace(directory)

            result = self.run_cli(root, "status")

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Active workstream: cua", result.stdout)
            self.assertIn("Role: anchor", result.stdout)
            self.assertIn("Does the runtime report readiness honestly?", result.stdout)

    def test_audit_requires_exactly_one_matching_active_workstream(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.make_workspace(directory)
            registry = root / "WORKSTREAMS.json"
            data = json.loads(registry.read_text(encoding="utf-8"))
            data["workstreams"]["rivet"]["status"] = "active"
            registry.write_text(json.dumps(data), encoding="utf-8")

            result = self.run_cli(root, "audit")

            self.assertEqual(result.returncode, 1)
            self.assertIn("FAIL exactly one active workstream", result.stdout)

    def test_audit_fails_when_active_current_is_missing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.make_workspace(directory)
            (root.parent / "cua-learning" / "CURRENT.md").unlink()

            result = self.run_cli(root, "audit")

            self.assertEqual(result.returncode, 1)
            self.assertIn("FAIL active CURRENT exists", result.stdout)

    def test_audit_fails_when_workspace_router_disagrees(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.make_workspace(directory)
            router = root.parent / "AGENTS.md"
            router.write_text(
                router.read_text(encoding="utf-8").replace(
                    "cua-learning/", "other-learning/"
                ),
                encoding="utf-8",
            )

            result = self.run_cli(root, "audit")

            self.assertEqual(result.returncode, 1)
            self.assertIn("FAIL workspace router matches active learning path", result.stdout)

    def test_audit_fails_when_roadmap_disagrees(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.make_workspace(directory)
            (root / "ROADMAP.md").write_text(
                "# Roadmap\n\n## Month 3 — ACTIVE: RIVET\n",
                encoding="utf-8",
            )

            result = self.run_cli(root, "audit")

            self.assertEqual(result.returncode, 1)
            self.assertIn("FAIL roadmap matches active workstream", result.stdout)

    def test_due_routes_supported_invariant_without_loading_market_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.make_workspace(directory)

            result = self.run_cli(root, "due", "supported-invariant")

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("PATTERN_LEDGER.md", result.stdout)
            self.assertNotIn("TARGET_COMPANIES.md", result.stdout)

    def test_due_ordinary_checkpoint_keeps_strategy_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self.make_workspace(directory)

            result = self.run_cli(root, "due", "engineering-checkpoint")

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("No global strategy file is due", result.stdout)


if __name__ == "__main__":
    unittest.main()
