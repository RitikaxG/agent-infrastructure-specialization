# Contribution Selection Filter

An open issue is NOT automatically worth working on.

Before committing serious time, evaluate:

## 1. Subsystem relevance

Does this teach one of my target areas?

- lifecycle
- ownership
- generations
- state
- events
- cancellation
- recovery
- browser/session identity
- sandbox lifecycle
- reconciliation
- cleanup
- observability

If not, usually skip.

## 2. Architecture relevance

Prefer failures crossing important boundaries:

controller ↔ runtime
runtime ↔ daemon
daemon ↔ browser
agent ↔ tool
action ↔ observation
browser session ↔ target
control plane ↔ sandbox

## 3. Reproducibility

Can I produce a deterministic or useful reproduction?

A strong reproduction may itself be a valuable contribution.

## 4. Invariant

Can I express the expected property as:

"After X, Y must always remain true."

If I cannot identify the invariant, I probably do not understand
the issue deeply enough yet.

## 5. Agent impact

Prefer failures affecting:

- correctness
- availability
- false-success
- hangs
- stale state
- duplicated side effects
- resource leaks
- broken recovery
- isolation

over cosmetic or unrelated changes.

## 6. Regression value

Can this become a test that prevents the failure class from returning?

## 7. Maintainer alignment

Before a large implementation:

- search existing PRs
- inspect recent related changes
- reproduce first
- post evidence if useful
- confirm direction when blast radius is high

## 8. Transferability

Have I seen, or could I reasonably expect to see, this failure class
in another agent runtime?

High transferability = high learning value.