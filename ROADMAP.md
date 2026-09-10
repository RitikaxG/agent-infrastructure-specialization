# Agent Runtime Reliability — Six-Month Roadmap

This roadmap defines the sequence of repositories and subsystems used to build
one coherent specialization. It does **not** reserve specific future issues;
issue state must be rescanned when each block becomes active.

The specialization is:

> **Agent Runtime Reliability — reliable execution across agent runtimes,
> computer/browser sessions, and sandbox environments.**

At any time there is exactly one active repository, one active subsystem, and
one primary engineering question.

## Repository Roles

- **Anchor community:** CUA
- **Transfer community 1:** Rivet agentOS
- **Transfer community 2:** Browser Harness
- **Systems-depth community:** E2B infra
- **Reserve/validation:** OpenHands software-agent-sdk
- **Capstone:** Agent Runtime Failure Lab v0.1

The goal is not equal PR distribution. Prefer repeated, related contribution in
the anchor community plus selective transfer work elsewhere.

---

## Months 1–2 — ACTIVE: CUA

### Repository

`trycua/cua`

### Role in specialization

Primary anchor community and first laboratory for runtime reliability.

### Selected subsystem

**Driver Runtime → Daemon lifecycle → execution/acknowledgement boundary →
ownership/recovery.**

The exact live engineering question remains in:

`../cua-learning/CURRENT.md`

### Fundamentals hardened

Primary:

- execution outcome & retries;
- lifecycle & readiness;
- ownership & generations.

Secondary:

- recovery/cleanup;
- interface/error semantics;
- observability of execution boundaries.

### What becomes concrete here

- SDK vs Proxy vs Daemon vs Driver/platform roles;
- logical session identity vs process-local runtime state;
- fresh request transport vs long-lived control connection;
- process death before dispatch vs after dispatch;
- external effect vs caller acknowledgement;
- replacement runtime generation and recovery semantics.

### Current external-proof direction

Use the already reproduced active-request Daemon-death case to decide whether to
seek maintainer direction on distinguishing pre-dispatch failure from
post-dispatch outcome-unknown failure.

Do not restart broad daemon learning. Continue from the current CUA stopping
boundary.

### Months 1–2 outcome target

Target, without manufacturing work:

- coherent HLD and relevant LLD explainable without repeating an AI summary;
- at least 3 meaningful lifecycle/failure experiments total;
- one or more important invariants established;
- at least one maintainer-visible reproduction/design discussion;
- 1–3 serious contribution attempts in the same broad Driver/runtime reliability
  area when real project needs exist;
- ideally multiple review/merge interactions so maintainers begin to associate
  the contributor with this subsystem/failure class;
- one interview-quality engineering story;
- one Failure Lab scenario specification earned from real evidence.

### Switch condition

Do not leave simply because the daemon model is understood. Apply the global
switch gate in `PROGRESS_GATES.md` and `WORKFLOW.md`.

---

## Month 3 — NEXT: Rivet agentOS

**Status: NOT ACTIVE**

### Repository

`rivet-dev/agentos`

### Role in specialization

Move from physical runtime/process reliability to **durable logical agent
execution**.

### Selected subsystem

**Agent session / prompt-turn lifecycle → cancellation → terminal/quiescent
state → execution ownership/recovery.**

Inspect underlying Rivet Actors only when the active agentOS execution path
requires it. Do not create a separate Actors learning track.

### Core engineering question

> When can a durable agent runtime truthfully say an execution has stopped and
> its session is safe to reuse?

### Fundamentals hardened

- durable vs ephemeral state;
- cancellation & quiescence;
- ownership & generations;
- recovery;
- exactly-one terminal outcome / event lifecycle.

### Transfer from CUA

```text
CUA:
transport acknowledgement does not establish execution certainty

Rivet:
cancellation acknowledgement does not establish execution quiescence
```

The repeated skill is distinguishing a **control-plane acknowledgement** from the
full lifecycle guarantee callers actually need.

### Activation gate

Before serious Month-3 investment, rescan:

- current session/cancellation/durable-execution issues and PRs;
- external contributor review/merge evidence;
- maintainer participation and community route;
- a locally reproducible or testable contribution surface.

If the surface no longer passes `CONTRIBUTION_FILTER.md`, keep the failure family
and substitute the best current repo rather than forcing Rivet.

### Expected output

- one coherent agent-session/turn HLD;
- one production-shaped cancellation/durability failure investigation;
- one serious maintainer-visible contribution path;
- 1–2 contribution attempts if real scope exists;
- first cross-repo comparison of a CUA reliability invariant.

---

## Month 4 — Browser Harness

**Status: NOT ACTIVE**

### Repository

`browser-use/browser-harness`

### Role in specialization

Study the agent ↔ browser control boundary where logical browser work depends on
live CDP connections, sessions, targets, and renderers.

### Selected subsystem

**Browser process / CDP connection / CDP session / target lifecycle and bounded
recovery.**

### Core engineering question

> When browser work logically continues but the control session, target, or
> renderer becomes stale or disappears, how does the runtime detect,
> classify, and recover without false success or indefinite hanging?

### Fundamentals hardened

- lifecycle & readiness;
- ownership/generation of browser sessions and targets;
- stale identity;
- execution/effect uncertainty;
- bounded recovery;
- observability.

### Transfer from earlier blocks

```text
CUA:
logical session may survive physical runtime replacement

Rivet:
durable agent session may outlive an execution owner/turn

Browser Harness:
logical browser workflow may outlive a live CDP session/target
```

### Activation gate

Rescan current stale-session/target/reconnect issues, recent PRs, maintainer
responses, outside-contributor merges, and available deterministic/live Chrome
reproduction paths before deep study.

### Expected output

- browser-control HLD understood as process → transport → session → target;
- one stale/dead-session or bounded-recovery investigation;
- 1–2 serious contribution attempts if the live surface supports them;
- a reusable failure comparison with CUA/Rivet.

---

## Month 5 — E2B infra

**Status: NOT ACTIVE**

### Repository

`e2b-dev/infra`

### Role in specialization

Move below the agent/browser runtime into sandbox and control-plane reliability.

### Selected subsystem

**Sandbox lifecycle state transitions → authoritative state → orchestration →
reconciliation → cleanup.**

Do not make Firecracker, Kubernetes, UFFD, networking, or storage independent
study tracks. Inspect them only when the active lifecycle problem crosses that
boundary.

### Core engineering question

> How does the control plane ensure observed sandbox state stays consistent with
> the lifecycle transition actually occurring in the data plane?

### Fundamentals hardened

- lifecycle and distributed state;
- ownership/generations;
- authoritative vs cached state;
- pause/resume/replacement semantics;
- reconciliation and cleanup;
- observability.

### Transfer from earlier blocks

The same pattern appears at a larger scale:

```text
logical/observed state
!= physical execution reality
```

Use CUA/Rivet/Browser reasoning about ownership, generations, readiness, and
stale state when entering the sandbox control plane.

### Activation gate

E2B is not guaranteed merely because it is technically relevant. Before Month 5,
rescan external contributor review/merge behavior, maintainer accessibility,
current lifecycle/reconciliation issues, and whether meaningful testing is
possible with available resources.

If maintainer-relationship viability or reproduction fit is weak, substitute a
better current sandbox/runtime-infrastructure repository while preserving the
same systems questions.

### Expected output

- one sandbox/control-plane lifecycle HLD;
- one state-divergence/reconciliation failure investigation;
- one substantial systems contribution attempt if viable;
- deeper distributed-systems evidence beyond application-level agent logic.

---

## Month 6 — CAPSTONE, NO NEW PRIMARY REPOSITORY

### Goal

Consolidate upstream work into an evidence-derived **Agent Runtime Failure Lab
v0.1** and convert the strongest investigations into hiring proof.

### Inputs

Only primitives earned from real investigations, for example:

```text
kill executor after dispatch
replace runtime generation
cancel during active execution
invalidate browser control session
drop/loss of state notification
assert no false success
assert unknown outcome conservatively
assert one terminal outcome
assert no work after quiescence
assert eventual reconciliation / cleanup
```

Do not design a generic agent framework.

### Month-6 work priority

1. finish active PR/review/merge/follow-up work from earlier repos;
2. confirm 2–3 important invariants across independent systems where possible;
3. implement the smallest useful Failure Lab primitives with provenance;
4. write 2 strong technical stories/articles from earned evidence;
5. rehearse HLD/LLD/failure/debugging stories under cross-questioning;
6. use the public evidence directly in targeted YC/startup outreach.

---

## Reserve — OpenHands software-agent-sdk

**Status: RESERVE, NOT A PLANNED FIFTH BLOCK**

Use only when:

- a planned repo loses contribution surface;
- an earlier block finishes early and a specific cross-repo invariant needs
  independent validation;
- a maintainer-supported durable-execution/ownership/recovery issue is a clearly
  better fit than the planned active surface.

Do not add OpenHands merely to collect another repository logo.

---

## Repository Switch Gate

Before activating the next block, require:

```text
UNDERSTANDING
HLD + relevant LLD + important invariant are defensible

EXTERNAL PROOF
maintainer-visible reproduction/discussion/PR/review/merge exists

TRANSFER
reusable lesson is recorded and connection to the next layer is clear

DIRECTION
continuing the current subsystem has lower expected value than the next layer
```

Use the escape hatch in `PROGRESS_GATES.md` when maintainer silence or exhausted
surface would otherwise consume the roadmap.

## Roadmap Principle

The sequence is stable; exact issue numbers are not.

Every future repository must pass a fresh contribution-surface and
maintainer-relationship scan at activation time.