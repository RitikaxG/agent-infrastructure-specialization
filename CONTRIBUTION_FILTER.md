# Contribution Selection Filter

An open issue is NOT automatically worth working on.

Before committing serious time, evaluate:

## 0. Current workstream alignment

Before asking how interesting an issue is, ask whether it advances the **currently active repository/subsystem** in `ROADMAP.md` and the exact engineering boundary in the active repository's `CURRENT.md`.

If **yes**, evaluate it further.

If **no, but strategically interesting**, record it as a future candidate in `ROADMAP.md` and do not investigate it deeply now.

If **no and weakly transferable**, skip it.

Do not let a high-quality but misaligned issue create a second active workstream.

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

## 9. PR submission gate

Finding something that could be changed is not sufficient justification
for a pull request.

Before submitting a PR, I should be able to answer:

- What real problem does this solve?
- Can I reproduce the failure or demonstrate the need?
- What invariant is being violated?
- Why does the fix belong at this layer?
- What alternatives did I consider, and why did I choose this approach?
- What regression test or verification proves the change?
- Have I checked related issues, PRs, and recent maintainer direction?
- Can I explain and defend the important implementation decisions
  without relying on the coding agent?

For non-trivial architectural changes, prefer:
reproduce → gather evidence → discuss direction → implement.

The PR should normally communicate:

problem → reproduction → root cause → change → rationale → verification.

Do not submit:

- speculative fixes for unobserved problems;
- cosmetic changes for contribution credit;
- broad AI-generated refactors without demonstrated need;
- changes I cannot technically explain;
- fixes whose usefulness to the project is unclear.
