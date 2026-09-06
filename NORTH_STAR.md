# Agent Infrastructure Specialization — North Star

## Primary Goal

Over the next ~6 months, specialize in durable agent execution infrastructure
through deep open-source work in systems such as CUA, OpenHands, Browser Use,
and E2B.

The goal is not to collect PRs or broadly "learn agent frameworks."

The goal is to become strong at understanding, reproducing, explaining,
testing, and fixing failures in:

- agent/runtime lifecycle
- resource ownership and generations
- process/daemon lifecycle
- durable state and event execution
- cancellation and recovery
- browser/computer execution
- browser/session/target identity
- action → execution → observation correctness
- sandbox lifecycle
- readiness/liveness
- reconciliation and cleanup
- observability of agent execution

The intended professional identity is:

> Agent Infrastructure Engineer focused on durable agent runtimes,
> browser/computer execution, and failure recovery.

## Evidence I Want After Six Months

- several meaningful upstream contributions, not random PRs
- deterministic reproductions of real runtime failures
- understanding of HLD and relevant LLD for the systems touched
- maintainer-visible technical participation
- 2–3 strong technical articles based on actual investigations
- a cross-repository ledger of recurring failure patterns
- an emerging reusable Agent Runtime Reliability / Failure Lab
- interview material grounded in real engineering work

## Long-Term Build Direction

Do not begin by building another agent harness.

First accumulate real failure cases across production agent systems.

As repeated patterns emerge, extract reusable fault-injection,
invariant-checking, lifecycle-testing, and observability primitives.

Only later, if justified by what has been learned, use those observations
to design a durable agent runtime/harness.

## Core Loop

understand subsystem deeply
→ model HLD and lifecycle
→ inspect relevant LLD
→ break it intentionally
→ reproduce a real failure
→ identify violated invariant
→ investigate alternatives
→ implement/test a fix
→ get maintainer feedback/merge
→ extract transferable pattern
→ preserve evidence for interviews

## Focus Rule — One Active Repository

I do not work effectively across multiple repositories simultaneously.

At any point there is exactly:

- ONE active repository
- ONE active subsystem
- ONE primary engineering question

Other repositories may be inspected briefly for comparison or future planning,
but they do not become active workstreams.

I switch repositories only after reaching an explicit stopping boundary in the
current subsystem.