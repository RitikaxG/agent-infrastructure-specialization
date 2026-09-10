# Agent Infrastructure Specialization — North Star

## Specialization

Over the next ~6 months, specialize in **Agent Runtime Reliability** through deep,
maintainer-visible open-source work.

The central engineering question is:

> How do agents execute consequential work correctly when processes, sessions,
> browsers, transports, and sandboxes can fail, restart, become stale, or disagree
> about state?

The intended professional identity is:

> **Agent Infrastructure Engineer focused on reliable agent runtimes, durable
> execution, browser/computer control, sandbox lifecycle, and failure recovery.**

This is not a plan to broadly learn agent frameworks. It is a plan to become
strong at a small set of repeated systems problems and prove that strength in
public engineering work.

## Deep Core

Harden six connected fundamentals:

1. **Lifecycle & readiness** — alive vs usable, lifecycle state, bounded startup,
   shutdown, and recovery.
2. **Ownership & generations** — who owns a resource/session, fencing, replacement,
   and stale-generation behavior.
3. **Durable vs ephemeral state** — what survives restart, what is reconstructed,
   and what must be invalidated.
4. **Execution outcome & retries** — accepted, dispatched, executed,
   acknowledged, unknown; retry/replay/idempotency safety.
5. **Cancellation & quiescence** — cancellation requested vs old work truly
   terminal and safe to replace/reuse.
6. **Recovery, reconciliation & cleanup** — repairing state/reality divergence,
   restoring service, and reclaiming abandoned resources.

Cross-cutting skills:

- **Observability** — enough IDs/events/state transitions to determine what
  actually happened.
- **Interface/protocol semantics** — honest guarantees between SDK, controller,
  runtime, driver, browser, and sandbox layers.

See `FUNDAMENTALS.md` for the reusable engineering model.

## Repository Model

Use repositories sequentially as laboratories for the same reliability ideas:

- **Anchor community — CUA:** computer/driver runtime lifecycle, execution and
  acknowledgement boundaries, ownership, recovery.
- **Transfer — Rivet agentOS:** durable agent session/turn lifecycle,
  cancellation, terminal/quiescent state, execution ownership.
- **Transfer — Browser Harness:** browser/CDP session/target lifecycle, stale
  control state, bounded recovery, no false success/hangs.
- **Systems depth — E2B infra:** sandbox lifecycle, authoritative state,
  orchestration, reconciliation, cleanup.
- **Reserve — OpenHands software-agent-sdk:** use only if a planned repo loses
  contribution surface or a cross-repo invariant needs independent validation.

At any time there is exactly one active repository, one active subsystem, and
one primary engineering question.

## Evidence Required After Six Months

Target evidence, not course completion:

- **3–5 substantial reviewed/merged upstream PRs** if upstream circumstances
  allow, with more serious attempts than merges because maintainer decisions are
  outside my control;
- repeated related work in the anchor community rather than only drive-by PRs;
- meaningful maintainer interaction in at least 2 communities;
- deterministic or high-quality reproductions of real runtime failures;
- HLD and relevant LLD I can explain and defend without repeating an AI answer;
- test intent and failure reasoning increasingly originating from me;
- 2–3 reusable invariants confirmed through personal work, ideally across more
  than one system;
- 2 strong technical engineering stories/articles based on actual work;
- an evidence-derived **Agent Runtime Failure Lab v0.1**;
- interview evidence that maps directly to runtime, browser, sandbox,
  distributed-systems, recovery, and debugging work.

Merge count is not the only metric. A maintainer-visible reproduction, accepted
design direction, meaningful review cycle, or strong rejected hypothesis can be
valuable evidence when technically defensible.

## Independence Outcome

Using Codex throughout the six months is expected. The goal is not to stop using
AI; it is to change what AI owns.

Progress should move from:

```text
AI teaches vocabulary + finds architecture + suggests failures
→ human reconstructs model while AI verifies
→ human predicts and owns test intent while AI finds implementation
→ human identifies familiar failure classes in new systems
→ human forms first HLD, invariant, test strategy, and trade-offs independently
```

By Month 6, Codex may still accelerate repository search, unfamiliar syntax,
implementation, and verification. The engineering question, architecture model,
failure hypothesis, invariant, test intent, and major trade-off should
increasingly originate from the human.

See `PROGRESS_GATES.md` for how this is measured.

## External-Proof Principle

Subsystem understanding exists to produce one or more of:

- reproducible evidence;
- a useful issue/discussion;
- a regression test;
- a reviewed design decision;
- a focused PR;
- a merge/follow-up contribution;
- a transferable invariant.

Do not spend consecutive weeks accumulating only private understanding.

## Long-Term Build Direction

Do not begin by building another generic agent harness.

First accumulate real failures in production-shaped open-source runtimes. Only
after repeated patterns exist should fault injection, invariant checking,
lifecycle testing, recovery assertions, and observability primitives be
extracted into a reusable Failure Lab.

## Non-Goals

Do not create independent study tracks for:

- LangChain/LangGraph, RAG, prompt engineering, model training, or generic AI
  courses;
- all of Rust/Go/Python before contributing;
- generic Kubernetes/distributed-systems course marathons;
- all of CDP, Firecracker, networking, storage, or virtualization;
- random good-first-issues, cosmetic PRs, or contribution-count optimization;
- understanding an entire repository before testing or contributing.

Learn language and infrastructure concepts **just in time when the active
failure requires them**.

## Primary Success Test

At the end of six months, I should be able to enter an unfamiliar agent-runtime
problem and naturally ask:

- Who owns this execution/resource?
- What is the logical identity and physical generation?
- What state is durable and what is process-local?
- Is the resource alive, ready, stale, stopping, or dead?
- Was the action dispatched, executed, acknowledged, or left unknown?
- Is retry/replay safe?
- What does cancellation actually guarantee?
- Who reconciles stored/observed state with reality?
- What evidence would distinguish the failure cases?
- What regression test should protect the invariant?

If that judgment is backed by public contribution evidence, the specialization
has worked.