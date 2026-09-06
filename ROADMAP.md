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
- [ ] reusable failure pattern recorded in PATTERN_LEDGER.md
- [ ] interview evidence recorded

### Stopping boundary

Do not attempt to understand the entire CUA repository.

Stop once I have meaningful depth in runtime lifecycle /
ownership / recovery and have converted that depth into engineering evidence.


## NEXT — OpenHands

Not active yet.

Purpose:
Study the layer above the runtime:

durable conversation execution
→ events
→ actions
→ tools
→ observations
→ pause/cancel/resume

## Repo Switching Rule

A new repository becoming interesting is not a reason to switch.

New issues, announcements, Discord discussions, or hiring relevance may be
recorded in the NEXT section, but must not create another active workstream.

Switch only when:

1. the current subsystem stopping boundary has been reached, OR
2. the subsystem proves to be a dead end for meaningful contribution after
   serious investigation, OR
3. maintainers explicitly indicate the work is not useful / feasible.

Do not switch because:
- another repo looks exciting
- an easier issue appears elsewhere
- progress feels temporarily difficult
- I want broader exposure