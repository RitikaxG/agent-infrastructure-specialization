# Agent Runtime Reliability — Fundamentals

This file defines the **small set of repeated engineering ideas** this six-month
specialization is meant to harden.

It is not a curriculum and it is not personal evidence. `PATTERN_LEDGER.md`
contains only invariants earned through real investigations.

## 1. The System Model

Treat agent infrastructure as a stack of execution boundaries:

```text
LLM / agent policy
      ↓
agent runtime / session / turn
      ↓
SDK / controller / driver
      ↓
browser or computer control
      ↓
sandbox / VM / worker environment
      ↓
external side effect
```

Different projects name these layers differently. The goal is to recognize the
**role** a component plays rather than memorize names such as daemon, actor,
sidecar, driver, target, worker, or orchestrator.

## 2. Six Deep Fundamentals

### A. Lifecycle & Readiness

Ask:

- What lifecycle states exist?
- What transition makes the resource actually usable?
- Does process existence imply readiness?
- Can shutdown/recovery hang indefinitely?
- What is the terminal state?

Common failures:

- process alive but endpoint unavailable;
- browser alive but renderer/session unusable;
- worker marked ready before dependencies are ready;
- teardown acknowledged while work/resources remain.

### B. Ownership & Generations

Ask:

- Who created and owns this resource/session?
- Who may mutate, cancel, replace, or destroy it?
- What identifies the current physical generation?
- What happens to handles from an older generation?
- Is an old logical identity rejected, rebound, or lazily admitted?

Common failures:

- stale owner still acts after replacement;
- logical session survives but old runtime state does not;
- two owners act concurrently;
- stale browser/sandbox handle is treated as current.

### C. Durable vs Ephemeral State

Ask:

- What lives only in process memory?
- What is persisted?
- What must be reconstructed after restart?
- What must never be assumed to survive?
- Can persisted `RUNNING` or `READY` state outlive the executor that made it true?

Common failures:

- persisted state points at a dead executor;
- restart restores identity but not liveness/control state;
- partial resume creates inconsistent state;
- stale cached state survives physical replacement.

### D. Execution Outcome & Retry Safety

Ask:

- Was the operation merely accepted, dispatched, executed, or acknowledged?
- What happens if the executor dies between effect and response?
- Can the caller know whether the side effect happened?
- Is retry safe, idempotent, deduplicated, or potentially destructive?
- Is an unknown outcome represented honestly?

Common failures:

- side effect happens but acknowledgement is lost;
- transport error is misreported as `not executed`;
- automatic retry duplicates a non-idempotent action;
- partial execution is mistaken for rollback.

### E. Cancellation & Quiescence

Ask:

- Does `cancel()` mean signal sent, signal acknowledged, or work stopped?
- Can tools/events/processes continue after cancellation returns?
- Is exactly one terminal outcome emitted?
- Is the session safe to reuse immediately?
- What happens when cancellation races normal completion?

Common failures:

- cancel acknowledged while old turn remains active;
- next prompt starts before old work is quiescent;
- duplicate terminal events;
- child process/tool survives cancellation.

### F. Recovery, Reconciliation & Cleanup

Ask:

- Which component owns recovery?
- What is authoritative when stored/cached state disagrees with reality?
- How are stale resources found and repaired?
- How is cleanup retried or bounded?
- What happens when the normal removal path is skipped?

Common failures:

- cache says `Running`, authoritative state says `Killing`;
- sandbox disappears but index entry remains;
- orphan process/session/resource leaks;
- recovery creates a second resource instead of reconciling the first.

## 3. Cross-Cutting Skills

### Observability

For every important failure, ask whether the system exposes enough evidence to
answer:

- logical session/run/request identity;
- physical runtime generation;
- state transitions and timestamps;
- dispatch/execution/acknowledgement boundaries;
- cancellation/terminal event;
- cleanup/reconciliation result.

If the system cannot distinguish these, observability may itself be part of the
reliability problem.

### Interface / Protocol Semantics

The boundary between layers must communicate guarantees honestly. An SDK error,
transport error, runtime refusal, driver refusal, browser failure, and sandbox
failure are not necessarily equivalent.

Always ask: **what does this result allow the caller to safely conclude?**

## 4. HLD Contract

For each active subsystem, the human should gradually be able to reconstruct
this without reading a generated architecture essay:

1. What problem does the subsystem solve?
2. What are the 3–7 important components?
3. What responsibility/state does each own?
4. What is one healthy request/execution path end to end?
5. What is durable vs process/generation-local?
6. What are the important lifecycle states?
7. Which boundaries can fail independently?
8. Who owns recovery and cleanup?

A useful HLD is small enough to redraw from memory. It should not be a map of the
whole repository.

## 5. LLD Contract

LLD is **the minimum implementation slice required to reason about the active
failure or feature**, not line-by-line knowledge of a repository.

For one active question, identify:

1. **Entry** — where does the request/action enter?
2. **Transport** — how does it reach the executor?
3. **State** — which types/records/locks/session state matter?
4. **Effect boundary** — where does consequential work actually occur?
5. **Result/error** — where is completion/failure represented?
6. **Recovery/cleanup** — what path runs after interruption/failure?
7. **Nearest tests** — what existing tests protect this contract?

Codex may initially locate these landmarks. Over time the human should become
better at predicting where they will be and tracing them independently.

## 6. Repeated Failure-Family Library

These are high-value fault families to reuse across repositories when they are
relevant—not a checklist that must be run everywhere:

```text
process / worker dies
transport disconnects
resource exists but is not ready
session/handle becomes stale
runtime generation is replaced
side effect occurs but acknowledgement is lost
timeout leaves outcome unknown
retry risks duplicate effect
cancel races completion
pause/resume restores only part of state
cached state disagrees with authoritative state
event/notification is lost
cleanup fails and resource is orphaned
```

A new failure should usually strengthen one of the six fundamentals rather than
create a new disconnected study topic.

## 7. Making Vocabulary Concrete

For an unfamiliar concept such as `daemon`, `driver`, `SDK`, `actor`, `sidecar`,
`CDP session`, `target`, `sandbox`, `orchestrator`, `lease`, or `reconciler`, use
this sequence:

```text
plain-language role
→ actual instance in the active system
→ who calls it / what it owns
→ observe its healthy behavior
→ inspect minimum source implementing that role
→ break or vary it when useful
→ explain what survives/fails
→ recognize the equivalent role in another system
```

Do not require the human to use an unfamiliar term in a failure prediction before
this grounding exists.

## 8. Cross-Repository Progression

| Repository | Selected layer | Fundamentals emphasized |
| --- | --- | --- |
| **CUA** | Driver/computer runtime and daemon lifecycle | lifecycle, ownership/generations, execution outcome, recovery |
| **Rivet agentOS** | durable session/turn execution | durable state, cancellation/quiescence, ownership, recovery |
| **Browser Harness** | browser/CDP session/target lifecycle | readiness, stale identity, effect certainty, bounded recovery |
| **E2B infra** | sandbox/control-plane lifecycle | authoritative state, orchestration, reconciliation, cleanup |

The value comes from seeing the **same engineering ideas under different failure
domains**.

## 9. Fundamental Mastery Test

A fundamental moves from conceptual knowledge toward engineering judgment when I
can:

- explain it using a failure I personally observed;
- locate the important HLD boundary;
- identify the relevant LLD landmarks;
- predict at least one nearby failure variation;
- state the invariant being protected;
- describe what a regression test should prove;
- recognize the same class in a different runtime without being told the exact
  repository-specific name.

Use `PROGRESS_GATES.md` to track this progression.