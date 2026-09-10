# Contribution and Repository Selection Filter

This file decides whether a **repository, subsystem, issue, investigation, or PR**
deserves serious time.

An interesting issue is not automatically useful. A technically perfect
repository is not automatically a good six-month primary if outside contributors
cannot realistically get reviewed or recognized.

## 0. Active-Workstream Alignment

Before anything else, ask whether the work advances the current repository,
subsystem, and exact engineering boundary recorded in `ROADMAP.md` and the active
learning workspace `CURRENT.md`.

If not:

- strategically useful → record as a future candidate;
- weakly transferable → skip;
- do not create a second active workstream.

## 1. Primary Repository Activation Gate

Before a repository receives multi-week investment, verify all of these.

### Technical fit

The selected subsystem must harden one or more fundamentals in `FUNDAMENTALS.md`
and fit the Agent Runtime Reliability specialization.

### Live contribution surface

Require a bounded scan showing multiple recent issues/PRs in the intended
failure family or subsystem, with at least one credible contribution-shaped
surface.

Useful evidence includes:

- reproducible user bug;
- missing regression;
- active maintainer discussion;
- recent adjacent fixes;
- accepted design/RFC with bounded implementation gap;
- ready/unassigned issue;
- real reliability gap demonstrable from current source/runtime.

### External-contributor viability

Check that outside contributors actually receive review/merge or substantive
technical responses. Do not infer community openness solely from a
`CONTRIBUTING.md` file.

### Maintainer-relationship viability

A primary repository must offer a realistic path for repeated useful interaction
through issues, PR reviews, RFCs, Discord/community help, or similar legitimate
channels.

Prefer repositories where repeated related contributions can make the human
recognizable around one subsystem/failure class.

**Maintainer-relationship viability may not score zero for a primary repo.**

### Reproduction/test fit

There must be a plausible way to observe, reproduce, or regression-test the
selected behavior with available machines, CI, mocks, harnesses, or bounded
cloud spend.

### Career fit

The resulting proof should map clearly to current target roles: agent runtimes,
durable execution, browser/computer control, sandboxes, distributed systems,
retries/recovery, observability, or infrastructure debugging.

If a planned repo fails this activation gate when its month arrives, preserve the
failure family and choose a stronger current repository instead of forcing the
logo.

## 2. Subsystem / Issue Scorecard

Score `0–2` on each dimension:

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Market relevance | weak | adjacent | direct agent-runtime/startup relevance |
| Specialization fit | disconnected | partial | strengthens core reliability spine |
| Reproducibility | speculative | partial | deterministic/high-quality evidence possible |
| Architecture boundary | local/trivial | useful | important runtime/session/sandbox boundary |
| Maintainer evidence | none | some | active project/user/maintainer signal |
| Regression value | hard to assert | possible | clear invariant/test |
| PR-shaped scope | huge/vague | can narrow | focused first contribution |
| Transferability | isolated | plausible | repeated cross-runtime failure class |

Interpretation:

- **13–16:** strong candidate;
- **10–12:** bounded investigation before commitment;
- **<10:** usually skip.

Do not let a numeric score override an obvious blocker such as an active competing
PR, inaccessible test environment, or maintainer rejection.

## 3. Architecture Preference

Prefer failures crossing important boundaries:

```text
agent/controller ↔ runtime
session ↔ execution owner
SDK ↔ transport
runtime ↔ daemon/worker
request ↔ external side effect
runtime ↔ browser/CDP
browser session ↔ target/renderer
control plane ↔ sandbox/node
authoritative state ↔ cache/index
```

These teach more transferable systems judgment than cosmetic/local changes.

## 4. Agent Impact

Prefer work affecting:

- correctness;
- false success;
- hangs/unbounded waits;
- stale state;
- duplicated side effects;
- cancellation/recovery;
- resource leaks;
- isolation;
- observability needed to resolve uncertain execution.

## 5. Reproduction and Invariant Gate

Before serious implementation, be able to state:

```text
EXPECTED
ACTUAL
REPRODUCTION / SOURCE EVIDENCE
RUNTIME PATH
STATE / OWNERSHIP
FAILURE BOUNDARY
INVARIANT
```

A strong reproduction can itself be a meaningful contribution.

If the invariant cannot yet be expressed, continue the minimum necessary
investigation rather than guessing at a fix.

## 6. Existing-Work-First Gate

Before drafting or recommending a new public issue, RFC, or PR, inspect:

- exact and adjacent open issues;
- assignments/labels/milestones;
- active and recently merged PRs;
- relevant RFC/design decisions;
- recent maintainer direction.

Then choose the narrowest honest path:

- matching active PR → review/contribute there; do not compete;
- matching issue without active implementation → reproduce/clarify and seek
  selection;
- accepted design → inspect implementation/parity gaps;
- no matching durable record → new issue/RFC may be appropriate;
- merely adjacent work → keep the finding distinct.

Record the short inventory and exclusions in the active `CURRENT.md` before
external publication.

## 7. Maintainer Relationship Rule

Relationship-building is not separate networking. It is repeated useful
engineering work.

Preferred sequence:

```text
reproduce
→ add useful evidence / ask focused contract question
→ incorporate maintainer direction
→ regression/design
→ focused PR
→ respond carefully to review
→ follow an adjacent related problem when useful
```

Do not post comments merely for visibility.

A rejected direction can still be valuable if it teaches project intent and is
captured accurately.

## 8. Testing Value

Prefer contribution candidates where the change can protect a system property,
not only a happy-path example.

Ask:

- What must remain true under crash/restart/timeout/cancellation?
- What observable proves it?
- Can the pre-fix behavior fail the test?
- Does the test detect the real public effect rather than only a successful tool
  response?

The human should increasingly own the **test intent** even when Codex writes
unfamiliar Rust/Go/Python syntax.

## 9. PR Submission Gate

Before a serious PR, the human must be able to defend:

- real problem and user/system impact;
- reproduction/evidence;
- HLD boundary;
- relevant LLD path;
- violated invariant;
- why the fix belongs at this layer;
- alternatives/trade-offs;
- test strategy and important failure cases;
- related existing work and maintainer direction;
- which parts were human reasoning vs AI assistance.

Preferred PR story:

```text
problem
→ reproduction
→ root cause / contract gap
→ bounded change
→ rationale
→ regression + validation
→ known limits
```

Do not submit:

- speculative fixes for unobserved problems;
- broad AI-generated refactors;
- cosmetic PRs for contribution count;
- changes whose behavior the human cannot explain;
- changes with no clear usefulness to the project.

## 10. Proof-Velocity Review

Apply `PROGRESS_GATES.md` weekly.

If two consecutive weeks produce only private learning, rescore the candidate.
Try a narrower/adjacent issue in the same subsystem before abandoning a strong
repository, but do not sacrifice a month to a contribution surface with no
credible maintainer path.