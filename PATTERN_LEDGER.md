# Cross-Repository Agent Infrastructure Pattern Ledger

## INV-001 — Process existence does not imply readiness

### General invariant

A process/resource should not be exposed as usable until the service contract
required by consumers is actually ready.

### CUA evidence

Subsystem:
Daemon lifecycle

Observed failure:
...

### E2B evidence

Subsystem:
envd startup

Observed failure:
process exists while listener is unavailable.

### General lesson

Separate:

- spawned
- alive
- initializing
- ready
- degraded
- dead

### Failure-lab opportunity

Reusable readiness probe:
process alive + endpoint unavailable + timeout classification.


---

## INV-002 — Logical sessions cannot silently cross runtime generations

### CUA
...

### Browser Use
...

### OpenHands
...

### Possible reusable primitive

generation token + stale handle assertion