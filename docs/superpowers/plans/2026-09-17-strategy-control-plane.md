# Agent Infrastructure Strategy Control Plane Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Keep one coherent long-term Agent Runtime Reliability strategy synchronized with progressively independent, contribution-shaped repository learning without loading global context in every session.

**Architecture:** A machine-readable workstream registry identifies the single active source and learning workspace. A small `strategyctl` command validates routing and reports event-driven strategy files, while durable workflow and skills shape staged HLD/LLD learning, issue selection, post-reproduction study, and global evidence promotion.

**Tech Stack:** Python 3.9 standard library, JSON, Markdown, unittest, Codex filesystem skills.

**Spec:** `NORTH_STAR.md`, the user-approved strategy audit in the current task, and the user's staged-learning and coherent-contribution requirements from 2026-09-17.

## Global Constraints

- Preserve exactly one active repository, subsystem, primary engineering question, and contribution arc.
- Do not load the global strategy set during ordinary fresh-session resume.
- Keep exact issue state in the active learning workspace, not permanent strategy files.
- Teach unfamiliar systems before requesting independent architecture decisions; increase human ownership only when the recorded assistance level supports it.
- Reject assigned, actively owned, duplicative, or disconnected issue candidates before investing in them.
- Keep language study just-in-time to the active source path and contribution.
- Do not modify Cua source, publish externally, commit, or push.

---

### Task 1: Workstream registry and audit

**Files:**
- Create: `WORKSTREAMS.json`
- Create: `tools/strategyctl.py`
- Create: `tools/test_strategyctl.py`

**Interfaces:**
- Produces: `strategyctl status`, `strategyctl audit`, and `strategyctl due EVENT`.

- [x] Write failing tests for one-active-workstream validation, missing CURRENT paths, status resolution, and event-to-file routing.
- [x] Run the tests and confirm failures because `strategyctl.py` is absent.
- [x] Implement the minimum registry parser and commands.
- [x] Run the tests and confirm they pass.

### Task 2: Correct and de-duplicate global strategy state

**Files:**
- Modify: `AGENTS.md`
- Modify: `README.md`
- Modify: `ROADMAP.md`
- Modify: `PATTERN_LEDGER.md`
- Modify: `INTERVIEW_EVIDENCE.md`
- Modify: `TARGET_COMPANIES.md`

**Interfaces:**
- Consumes: active workstream registry and `../cua-learning/CURRENT.md`.
- Produces: durable strategy without stale issue-level “current” state.

- [x] Replace volatile Daemon/#2686 current-focus language with registry/CURRENT routing.
- [x] Promote the #2915 readiness invariant with bounded evidence.
- [x] Add #2915 interview evidence with honest human/AI ownership.
- [x] Refresh verified hiring rows and preserve access constraints.

### Task 3: Encode staged HLD/LLD and post-reproduction learning

**Files:**
- Modify: `../cua-learning/WORKFLOW.md`
- Modify: `../cua-learning/CONVENTIONS.md`
- Modify: `../cua-learning/CURRENT.md`
- Modify: `../.agents/skills/cua-resume/SKILL.md`
- Modify: `../.agents/skills/cua-bug-repro/SKILL.md`
- Modify: `../.agents/skills/cua-contribution/SKILL.md`
- Modify: `../.agents/skills/cua-checkpoint/SKILL.md`
- Create: `../.agents/skills/agent-infra-checkpoint/SKILL.md`

**Interfaces:**
- Produces: staged orientation, contribution-arc filtering, and a post-reproduction readiness gate.

- [x] Encode the concrete orientation → guided HLD → bounded LLD → prediction → experiment sequence.
- [x] Encode required post-reproduction understanding: package map, evidence provenance, relevant source landmarks, language concepts, and one bounded human-owned task.
- [x] Make language study task-specific and documentation-backed, never a parallel curriculum.
- [x] Fail closed on assignments, active PR ownership, duplication, and disconnected issue scope.
- [x] Add a contribution arc and post-reproduction learning state to CURRENT.
- [x] Validate every edited or new skill structurally.

### Task 4: Strengthen independence, maintainer, and hiring progression

**Files:**
- Modify: `PROGRESS_GATES.md`
- Modify: `WORKFLOW.md`
- Modify: `CONTRIBUTION_FILTER.md`
- Modify: `NORTH_STAR.md`

**Interfaces:**
- Produces: measurable implementation, review, operational, and maintainer-readiness progression.

- [x] Add implementation ownership, code review, operational judgment, and maintainer communication dimensions.
- [x] Add recall, prediction-first, test-intent-first, and retention/transfer checks.
- [x] Add a maintainer-readiness ladder and coherent contribution-arc rule.
- [x] Keep infrastructure topics just-in-time rather than creating separate courses.

### Task 5: Full verification

**Files:**
- Verify all modified files and both repositories.

- [x] Run `tools/test_strategyctl.py`.
- [x] Run `strategyctl audit`, `status`, and representative `due` events.
- [x] Run the complete `cua-learning` contextctl test suite and audit.
- [x] Run skill validation for every changed/new skill.
- [x] Run `git diff --check` in both repositories and confirm Cua source is unchanged.
- [x] Review the final diff against every approved requirement.
