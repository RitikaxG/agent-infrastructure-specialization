# Agent Runtime Reliability Specialization

A six-month open-source specialization in **reliable agent execution runtimes**.

The goal is to become an Agent Infrastructure Engineer who can understand,
reproduce, test, and fix failures across agent runtimes, computer/browser
control, and sandbox environments—and prove that ability through
maintainer-visible upstream work.

## Specialization Spine

```text
lifecycle & readiness
+ ownership & generations
+ durable vs ephemeral state
+ execution outcome & retries
+ cancellation & quiescence
+ recovery / reconciliation / cleanup
                    ↓
                  CUA
                    ↓
             Rivet agentOS
                    ↓
            Browser Harness
                    ↓
                E2B infra
                    ↓
       Agent Runtime Failure Lab
```

The repositories are sequential laboratories for the **same recurring systems
problems**, not four independent technologies to learn.

## Current Focus

**Anchor repository:** CUA  
**Active subsystem:** Driver Runtime / Daemon lifecycle  
**Current proof direction:** convert reproduced active-request execution
uncertainty into maintainer-visible contribution evidence.

See the active `../cua-learning/CURRENT.md` for the exact live engineering
question.

## Global Files

| File | Responsibility |
| --- | --- |
| `NORTH_STAR.md` | six-month destination and professional identity |
| `FUNDAMENTALS.md` | the repeated agent-runtime fundamentals, HLD/LLD model, failure families |
| `PROGRESS_GATES.md` | independence ladder, proof stages, daily/weekly/monthly checkpoints |
| `ROADMAP.md` | CUA → Rivet → Browser Harness → E2B → capstone |
| `TARGET_COMPANIES.md` | living YC/non-YC hiring market, access constraints, evidence-triggered outreach |
| `CONTRIBUTION_FILTER.md` | repo/subsystem/issue + maintainer-viability selection rules |
| `PATTERN_LEDGER.md` | invariants earned from real personal investigations |
| `INTERVIEW_EVIDENCE.md` | externally defensible engineering work actually performed |
| `WORKFLOW.md` | how learning becomes evidence, contribution, and transfer |
| `AGENTS.md` | Codex orchestration rules |

## Primary Operating Rule

At any moment there is exactly:

- **one active repository**;
- **one active subsystem**;
- **one primary engineering question**.

Use AI heavily when needed, especially for unfamiliar repositories and Rust/Go
syntax. The six-month goal is not AI avoidance; it is for the engineering
question, HLD, failure hypothesis, invariant, test intent, and major trade-offs
to increasingly originate from the human.

## Success

Prefer a small set of substantial, related upstream contributions and real
maintainer relationships over many shallow PRs.

A strong six-month result is roughly:

- 3–5 substantial reviewed/merged PRs if upstream circumstances allow;
- repeated contribution recognition in the CUA anchor community;
- meaningful maintainer interaction in at least 2 communities;
- several production-shaped runtime failure investigations;
- 2–3 transferable invariants;
- Agent Runtime Failure Lab v0.1 derived from real failures;
- technical/interview stories that map directly to current agent-infrastructure
  roles.

Start with `NORTH_STAR.md`, then `ROADMAP.md`, then use `AGENTS.md` and
`PROGRESS_GATES.md` to run the work. Use `TARGET_COMPANIES.md` to decide where
earned proof should be directed; do not use it to create parallel learning
workstreams.