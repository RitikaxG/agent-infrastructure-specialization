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

## INV-002 — Logical sessions must not silently cross runtime generations

**Status: CANDIDATE**

### General invariant

A logical session/handle created against runtime generation N must not silently remain valid against a different physical runtime generation unless the system explicitly revalidates or rebinds it.

### Evidence personally investigated

#### CUA

Investigation: not yet sufficient to claim evidence.

### Comparison candidates

- Browser Use — stale CDP/session/target handles after reconnect or browser restart
- OpenHands — persisted logical runtime state vs refreshed physical connection/runtime
- E2B — sandbox/process incarnation identity if relevant during later investigation

These are comparison targets, not completed evidence.

### Failure-lab candidate

Potential reusable primitive:

```text
capture generation / incarnation
create logical handle
replace physical runtime
reuse old handle
assert stale handle is rejected or explicitly rebound
```

Do not implement generically until repeated evidence justifies it.

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
Root cause:

### Comparison candidates

- ...

### General lesson

...

### Failure-lab candidate

...
```
