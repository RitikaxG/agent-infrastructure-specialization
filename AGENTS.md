# Agent Runtime Reliability — Codex Orchestrator

This repository is the global strategy layer for a six-month specialization in
Agent Runtime Reliability.

Optimize, in order, for:

1. maintainer-visible proof from real agent-infrastructure work;
2. progressive human independence in HLD, LLD, failure reasoning, test intent,
   and engineering decisions;
3. transferable depth in the reliability fundamentals.

Private understanding matters when it advances one of those outcomes.

## Always-on operating contract

- Keep exactly one active repository, one active subsystem, and one primary
  engineering question.
- Resolve current work through the active learning workspace's `CURRENT.md`.
- Use `GUIDED → SHARED → USER-LED → TRANSFER` separately by assistance
  dimension; do not demand independence before the recorded level supports it.
- In GUIDED work, make vocabulary concrete through the real component, process,
  state owner, healthy path, and relevant failure before prediction.
- Keep HLD to 3–7 important components and one reconstructable path. Keep LLD
  limited to entry, transport, state/types, effect, result/error,
  recovery/cleanup, and nearest tests for the active question.
- Separate `OBSERVED`, `SOURCE-VERIFIED`, `INFERENCE`, and `UNKNOWN / NOT
  TESTED`. Evidence precedes claims.
- Prefer depth, maintainer relationships, and repeated substantial work over
  unrelated PR count or repository breadth.
- Do not spend consecutive weeks only reading or documenting; convert knowledge
  into explain-back, prediction, experiment, reproduction, test intent, design,
  or maintainer-visible evidence.
- Human ownership is required for meaningful architecture/design choices,
  contribution commitment, high-risk actions, and public wording.

## Progressive strategy loading

Do not load the complete strategy set in every fresh session.

| Decision or event | Load |
| --- | --- |
| Repository/subsystem switch | relevant `ROADMAP.md` and `NORTH_STAR.md` |
| New or transfer reliability family | relevant `FUNDAMENTALS.md` |
| Daily, weekly, monthly, retention, or course-correction checkpoint | relevant `PROGRESS_GATES.md` |
| Serious contribution commitment | `CONTRIBUTION_FILTER.md` |
| Cross-repository invariant promotion | `PATTERN_LEDGER.md` as needed |
| Interview evidence extraction | `INTERVIEW_EVIDENCE.md` |
| Explicit target-company research | `TARGET_COMPANIES.md` |

The referenced documents remain canonical. Do not duplicate their procedures
here or rewrite mature strategy merely to reduce startup context.

## Active work resolution

Resolve the active repository through `WORKSTREAMS.json`, then read only that
workstream's `CURRENT.md`. `tools/strategyctl.py status` performs this lookup;
do not duplicate the resolved paths or issue-level state here.

Read CURRENT before deeper global material. Its exact question, proof and
assistance state, human gate, pointers, and stop boundary control the next
bounded action. Re-ground the source checkout before source/runtime claims.

Do not reset established subsystem understanding to broad orientation because a
chat is fresh. Do not run a new failure, implement, or publish merely because
deeper strategy material was loaded.

At a checkpoint, run `tools/strategyctl.py due <event>` and inspect only the
files it returns. Ordinary engineering checkpoints stay inside the active
learning workspace. Global strategy is due only for assistance movement,
supported invariants, public proof, maintainer feedback, weekly/monthly review,
repository switches, or objective changes.

## Evidence and progression

The default direction is:

```text
UNDERSTAND ENOUGH → OBSERVE / REPRODUCE → EXPLAIN → IDENTIFY INVARIANT
→ MATCH EXISTING WORK → MAINTAINER ALIGNMENT → REGRESSION / DESIGN
→ IMPLEMENT → VERIFY → REVIEW / MERGE → TRANSFER
```

At a natural checkpoint, update the owning durable artifact first and rewrite
CURRENT to represent now. Promote a global invariant, roadmap change, selection
rule, or interview story only when the evidence earns it.

When stopping meaningful work, state exactly one transition: `NEXT`, `WAITING
ON HUMAN`, or `BLOCKED`, with the smallest next action or unblock requirement.
