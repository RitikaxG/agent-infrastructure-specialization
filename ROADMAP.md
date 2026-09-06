# Repository Roadmap

## ACTIVE — CUA

### Current subsystem

Daemon / runtime lifecycle

### Questions I must be able to answer

- Who owns the daemon?
- How is it spawned?
- How is readiness determined?
- What identifies a daemon/runtime generation?
- What survives disconnect/restart?
- Who owns session state?
- How is shutdown propagated?
- What resources can leak?
- How is recovery performed?
- How are failures surfaced to the caller?

### Required outputs before switching

- [ ] HLD mental model
- [ ] lifecycle/state-machine diagram
- [ ] relevant LLD paths understood
- [ ] at least 3 intentional failure scenarios tested
- [ ] at least 1 real issue reproduced or independently discovered
- [ ] invariant identified
- [ ] proposed fix/design evaluated
- [ ] meaningful maintainer interaction
- [ ] ideally one merged/reviewed contribution
- [ ] reusable failure pattern recorded in `PATTERN_LEDGER.md` if actually earned
- [ ] interview evidence recorded if actually earned

### Stopping boundary

Do not attempt to understand the entire CUA repository.

Stop once I have meaningful depth in runtime lifecycle / ownership / recovery and have converted that depth into engineering evidence.

### Switch gate

**Status: NOT REACHED**

See `WORKFLOW.md` for the repository-switching rule.

---

## NEXT — OpenHands

**Status: NOT ACTIVE**

Purpose:

Study the layer above the runtime:

```text
durable conversation execution
→ events
→ actions
→ tools
→ observations
→ pause / cancel / resume
```

OpenHands becomes active only after the CUA stopping boundary is reached or another switch condition in `WORKFLOW.md` is satisfied.

---

## Future Candidates

Record potentially valuable future subsystems/issues here without starting a second workstream.

Use this format:

```text
Repository:
Subsystem / issue:
Why relevant:
Potential invariant/pattern:
Status: FUTURE — DO NOT INVESTIGATE DEEPLY YET
```
