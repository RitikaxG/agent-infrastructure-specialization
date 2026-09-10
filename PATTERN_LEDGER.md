# Cross-Repository Agent Infrastructure Pattern Ledger

This file stores **generalized invariants and repeated failure patterns derived from work I have actually investigated**.

Do not treat examples found during planning, repo research, or another person's PR as personal evidence.

Use the following statuses:

- `CANDIDATE` — plausible invariant seen during planning or a first investigation, not yet confirmed strongly enough
- `SUPPORTED` — backed by one meaningful investigation I personally performed
- `CONFIRMED CROSS-REPO` — backed by personal investigations in at least two systems

Uninvestigated systems may be listed only under **Comparison candidates**.

---

## INV-001 — Process existence does not imply readiness

**Status: CANDIDATE**

### General invariant

A process/resource should not be exposed as usable until the service contract required by consumers is actually ready.

### Evidence personally investigated

#### CUA

Subsystem: daemon lifecycle

Investigation: in progress

Observed failure / evidence:

_To be filled only from my actual CUA investigation._

### Comparison candidates

- E2B — envd process/service readiness
- Browser runtime — browser process vs usable CDP/control session

These are **not evidence yet**. Revisit only when those repositories become active.

### General lesson

Potential state distinction:

- spawned
- alive
- initializing
- ready
- degraded
- dead

### Failure-lab candidate

Potential reusable readiness scenario:

```text
process alive
+
required endpoint/control channel unavailable
→
assert system does not report READY
```

Do not automate until the pattern is supported by real investigations.

---

## INV-002 — Logical identity continuity must not be confused with runtime-state continuity

**Status: SUPPORTED**

### General invariant

If a logical session/handle is allowed to survive replacement of the physical runtime that originally owned its state, the system must make the continuity contract explicit:

- which identity is reused;
- which runtime-owned state is recreated;
- which old state is intentionally lost;
- which liveness/cleanup relationship is re-established or remains absent.

Reusing the same logical identifier must not be mistaken for preserving the old runtime's memory or control relationship.

### Evidence personally investigated

#### CUA

Subsystem: daemon / runtime lifecycle

Investigation: replacement Daemon with surviving MCP Proxy/session

Observed behavior:

- the Proxy retained the same logical session id after the old Daemon disappeared;
- the old Daemon's process-local lifecycle/runtime state and persistent control connection disappeared with that process;
- a manually started replacement Daemon at the same socket path accepted later calls from the surviving Proxy;
- the replacement accepted a clearly session-owned cursor operation using the old session id even though it had not received a new persistent `session_begin` for that id;
- current source showed the unknown, non-ended id could be lazily admitted, creating a fresh `LifecycleRecord` / activity state under the same logical identity;
- after inactivity, that replacement-created session later became ended while both the same Proxy and replacement Daemon were still alive; source inspection established the idle-TTL/reaper cleanup path, while the exact runtime end reason remained an inference because logs did not expose it directly.

Corrected mental model:

```text
logical identity continuity
!= old runtime-state continuity
!= restored control-liveness continuity
```

The important CUA behavior is therefore **identity reuse + fresh state creation**, not transparent recovery of the old Daemon generation.

### Comparison candidates

- Browser Use — stale or reusable logical browser/session/target handles after browser/control reconnect
- OpenHands — persisted logical runtime/conversation identity vs refreshed physical runtime connection/state
- E2B — sandbox/process incarnation identity during sandbox/runtime replacement

These are comparison targets, not completed evidence.

### General lesson

Generation changes do not automatically require rejection of every old logical identifier; some systems intentionally rebind or recreate state. The engineering requirement is to make the contract explicit and prevent callers from assuming that identity continuity implies state continuity.

Important questions for another runtime are:

- Is the old logical id rejected, rebound, or lazily admitted?
- What state is generation-local?
- What cleanup/liveness signal belongs to the old physical runtime?
- What fallback bounds recreated state if the original control relationship is gone?

### Failure-lab candidate

Potential reusable replacement scenario:

```text
capture logical identity
create runtime-owned state
replace physical runtime generation
reuse old logical identity
observe whether it is rejected / rebound / lazily admitted
assert the documented continuity contract
assert old generation-local state is not silently assumed to exist
assert replacement-created state still has a bounded cleanup path
```

Do not implement this generically until another personally investigated system confirms that a reusable abstraction is warranted.

---

## INV-003 — Post-dispatch transport failure means execution outcome is unknown

**Status: SUPPORTED**

### General invariant

If an action request may have crossed an execution boundary but no trustworthy
completion response arrives, the caller must treat execution as unknown. A
transport error must not imply “not executed” or “safe to retry.”

`NotStarted` is defensible only before the first write/delivery attempt begins.
After delivery begins, the recovery owner must observe authoritative external
state and reconcile the original intent before deciding on another action.

### Evidence personally investigated

#### CUA

Subsystem: Driver Runtime / active-request Daemon lifecycle

Investigation: Daemon death during delayed, non-idempotent `type_text`

Observed behavior:

- an effect-conditioned experiment killed only the Daemon after a disposable
  Terminal visibly contained the strict prefix `CUA_MIDREQ2_`;
- the Terminal effect survived while the Daemon/listener disappeared;
- the surviving Proxy returned only `daemon closed connection without response`;
- no automatic Proxy replay occurred;
- a separate invalid attempt in which the Daemon was already unavailable
  produced `Connection refused` with no marker, establishing the contrasting
  pre-dispatch boundary.

Source-verified context:

- the ordinary Daemon request has no request id, idempotency key, attempt number,
  or deduplication key;
- the Daemon executes `tool.invoke(...)` before constructing the final response;
- the Proxy sends one request and does not replay it;
- private-worker, remote, and trusted-service SDK topologies already expose
  `ActionInterrupted` with `NotStarted` / `Unknown` completion semantics, while
  ordinary Daemon/MCP transport errors remain collapsed.

### Comparison candidates

- OpenHands — action emitted versus observation lost across runtime interruption
- Browser Use — browser action applied versus CDP response/control loss
- E2B — sandbox command/effect committed versus stream/response loss

These are comparison targets, not completed evidence.

### General lesson

Separate three concerns:

```text
availability owner → restore the executor/runtime
transport          → report completion knowledge conservatively
agent/workflow     → observe external state and reconcile intent
```

Tool-specific prevention or progress reporting should reduce predictable
ambiguity, but unavoidable process/transport loss still needs an explicit
`Unknown` completion state.

### Failure-lab candidate

```text
begin non-idempotent observable action
wait until a strict external prefix/effect exists
kill the executor before its final response
assert external effect survives
assert caller reports completion = unknown
assert no automatic logical replay occurs
```

Do not generalize into reusable automation until another personally investigated
runtime confirms the same failure class.

---

## Entry Template

```markdown
## INV-XXX — <Invariant name>

**Status: CANDIDATE | SUPPORTED | CONFIRMED CROSS-REPO**

### General invariant

...

### Evidence personally investigated

#### <Repository>

Subsystem:
Investigation / issue / PR:
Observed behavior:
Root cause / corrected assumption:

### Comparison candidates

- ...

### General lesson

...

### Failure-lab candidate

...
```
