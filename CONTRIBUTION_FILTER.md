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

## 7. Existing-work and external-artifact gate

Before drafting or proposing a new public issue, RFC, or PR, first make a
read-only inventory of the active subsystem's exact and adjacent existing work:

- open issues and their assignments, labels, milestones, and linked work;
- active pull requests and recently merged pull requests that may already own the
  behavior;
- relevant RFCs, their decisions, and implementation/completion status; and
- recent maintainer direction or review feedback.

Classify the result before choosing an external artifact:

- matching active PR → review or contribute there;
- matching issue without an active PR → reproduce/clarify it, then seek selection;
- accepted RFC → inspect whether the observed gap is already implemented,
  deliberately deferred, or a genuine parity/follow-up gap;
- no matching durable record → a new issue or RFC may be considered; or
- only adjacent work → keep the finding distinct rather than forcing a false
  duplicate relationship.

Record the inventory, key exclusions, and chosen path in the active repository's
durable current state before asking for external-publication approval. This gate
does not replace subsystem alignment, reproducibility, or human contribution
commitment.

## 8. Maintainer alignment

Before a large implementation:

- search existing PRs
- inspect recent related changes
- reproduce first
- post evidence if useful
- confirm direction when blast radius is high

## 9. Transferability

Have I seen, or could I reasonably expect to see, this failure class
in another agent runtime?

High transferability = high learning value.

## 10. PR submission gate

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
