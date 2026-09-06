# Agent Infrastructure Specialization

A six-month engineering specialization in **durable agent execution infrastructure** through deep open-source investigation and contribution.

The goal is not to collect PRs or broadly learn agent frameworks. The goal is to understand how production agent systems are designed, how important subsystem boundaries fail, how those failures are reproduced and prevented, and which invariants transfer across implementations.

## Current Focus

**Active repository:** CUA  
**Active subsystem:** daemon / runtime lifecycle

See `ROADMAP.md` for the current stopping boundary and next planned subsystem.

## Workspace

- `NORTH_STAR.md` — six-month goal and intended engineering identity
- `WORKFLOW.md` — how this specialization workspace is operated and updated
- `ROADMAP.md` — active repository/subsystem and progression
- `CONTRIBUTION_FILTER.md` — rules for deciding what work deserves serious time
- `PATTERN_LEDGER.md` — reusable invariants discovered from real investigations
- `INTERVIEW_EVIDENCE.md` — technical evidence from work actually performed

## Working Principle

The repositories are not independent learning tracks. They are used sequentially to study connected layers of durable agent execution infrastructure.

The intended progression is roughly:

```text
runtime lifecycle
→ ownership / generations
→ readiness / failure detection
→ durable state / events
→ cancellation / resume
→ action ↔ observation integrity
→ browser/session/target lifecycle
→ sandbox lifecycle
→ reconciliation / cleanup
→ cross-repo invariants
→ failure-testing primitives
→ evidence-derived agent runtime/harness design
```

Only **one repository, one subsystem, and one primary engineering question** are active at a time.

The eventual reliability tooling and runtime/harness should emerge from repeated real failure patterns rather than being designed speculatively in advance.
