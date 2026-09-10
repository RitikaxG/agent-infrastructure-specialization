# Agent Runtime Reliability — Workflow

This file defines **how the six-month specialization operates**.

It should keep the workspace focused on three outcomes:

1. transferable agent-runtime judgment;
2. maintainer-visible open-source proof;
3. progressive human independence in architecture, failure reasoning, and test
   intent.

## 1. Source-of-Truth Hierarchy

- `NORTH_STAR.md` — destination, professional identity, six-month success.
- `FUNDAMENTALS.md` — repeated agent-runtime concepts, HLD/LLD contracts,
  failure families.
- `PROGRESS_GATES.md` — assistance levels, proof stages, daily/weekly/monthly
  checkpoints, retention and course correction.
- `ROADMAP.md` — active repo/subsystem and future sequence.
- `CONTRIBUTION_FILTER.md` — what deserves serious time.
- `PATTERN_LEDGER.md` — invariants earned from real investigations.
- `INTERVIEW_EVIDENCE.md` — work the human actually performed and can defend.
- `AGENTS.md` — Codex orchestration behavior.

Repository-specific learning workspaces own detailed source paths, experiments,
exact live questions, diagrams, and current stopping boundaries.

Do not duplicate detailed investigation history into this global repository.

## 2. One Active Workstream

At any moment there is exactly:

- one active repository;
- one active subsystem;
- one primary engineering question.

Other repositories may be scanned briefly for roadmap validation or future
comparison, but do not become parallel learning tracks.

## 3. Primary Operating Loop

Every serious repository block should follow this direction:

```text
contribution / market surface scan
→ guided orientation
→ healthy execution path
→ small HLD
→ contribution-shaped failure question
→ reproduction / evidence
→ relevant LLD only
→ invariant / root cause / corrected assumption
→ maintainer alignment when needed
→ regression / design
→ implementation
→ review / merge / outcome
→ transferable pattern
```

This is not rigid chronology. For example, an existing issue may provide the
failure question before the HLD is complete. The rule is to learn only enough
architecture to reason correctly about the active engineering problem.

## 4. Future Repository Activation

Before spending a week learning a planned future repo, apply the primary-repo
activation gate in `CONTRIBUTION_FILTER.md`.

The scan should answer:

- Does the selected subsystem still map to current agent-runtime roles?
- Are there multiple current issues/PRs around the failure family?
- Do outside contributors receive substantive review/merge?
- Is there a real maintainer/community route?
- Can the failure be reproduced or regression-tested with available resources?
- Can repeated work make the contributor recognizable rather than anonymous?

Only after this scan should guided reverse engineering begin.

Do not spend two weeks understanding a subsystem and only then discover that no
credible contribution surface exists.

## 5. Learning Method by Assistance Level

The target is **progressive transfer of reasoning ownership**, not AI avoidance.

### GUIDED

Use when terms/system roles are unfamiliar.

Sequence:

```text
teach plain-language role
→ locate actual component/process/type
→ show who calls it and what it owns
→ observe healthy path
→ read minimum relevant source
→ human explains simple relationships back
```

Codex may suggest likely failure boundaries and nearest tests.

### SHARED

The human reconstructs part of the HLD, request path, failure prediction, or test
intent first. Codex verifies and fills exact repository details.

### USER-LED

The human originates the engineering question, invariant, failure variation, or
regression intent. Codex accelerates evidence gathering and implementation.

### TRANSFER

In a new system, the human recognizes familiar reliability questions before
being told the project-specific solution.

Track these levels in the active repository `CURRENT.md` and review them weekly
using `PROGRESS_GATES.md`.

## 6. HLD Rule

HLD is the **small durable model needed to reason about the subsystem**, not a map
of the whole repository.

The human should gradually be able to explain:

- problem solved by the subsystem;
- 3–7 important components;
- responsibilities and state ownership;
- healthy control/execution path;
- durable vs process/generation-local state;
- lifecycle/readiness states;
- important independent failure boundaries;
- recovery/cleanup owner.

If a diagram cannot be redrawn from memory at roughly this level, it is probably
too detailed for the HLD.

## 7. LLD Rule

LLD is **problem-shaped**.

For the active failure/feature, inspect only the important implementation
landmarks:

```text
entry
→ transport
→ state/types
→ effect boundary
→ result/error
→ recovery/cleanup
→ nearest tests
```

Codex may initially locate these landmarks and teach only the Rust/Go/Python
syntax needed to reason about them.

Do not make language learning a prerequisite course. Language knowledge should
accumulate through repeated real code paths.

## 8. Failure Discovery Training

Early in the specialization, Codex may teach/suggest failure families from
`FUNDAMENTALS.md` because the human does not yet know where systems usually
break.

Progressively move toward:

```text
AI proposes failure
→ human chooses/predicts one
→ human proposes nearby variation
→ human recognizes failure family in another repo
```

Do not require a prediction before the normal path and unfamiliar concepts are
concrete enough to support one.

## 9. Experiment Discipline

For meaningful lifecycle experiments:

1. verify the exact baseline;
2. state the property/question being tested;
3. make a prediction when the assistance level makes that useful;
4. introduce one bounded break;
5. independently observe the important external/runtime effect;
6. separate `OBSERVED`, `SOURCE-VERIFIED`, `INFERENCE`, and `UNKNOWN`;
7. explain what the result changes in the HLD/invariant;
8. preserve only evidence that helps reproduction or future contribution.

If a required precondition is missing, mark the experiment `NOT TESTED` rather
than reinterpreting the result.

## 10. Test-Design Training

Human ownership of test strategy is an **end-state**, not a Month-1 prerequisite.

Progression:

```text
GUIDED
AI locates existing harness/tests and explains what they protect
human explains the property that matters

SHARED
human states setup/fault/observable/assertion
AI translates into repo-native test code

USER-LED
human originates invariant + regression/failure cases
AI reviews and implements unfamiliar syntax

TRANSFER
human recognizes what must be tested in a new runtime before repository search
```

Measure who owns **test intent**, not who typed the syntax.

## 11. Evidence Conversion

Private understanding must move toward the proof ladder in
`PROGRESS_GATES.md`.

After at most two source/docs-heavy sessions, the next meaningful session should
produce at least one of:

- explain-back / HLD reconstruction;
- prediction;
- controlled experiment;
- failure reproduction;
- existing issue/PR analysis;
- regression test intent;
- design/contract decision;
- maintainer-facing evidence.

Additional source reading is justified only if it unblocks one of those.

## 12. Maintainer Relationship

Treat maintainer recognition as a result of repeated useful work, not networking
ceremony.

Prefer:

```text
reproduction
→ useful issue evidence / focused architecture question
→ maintainer feedback
→ bounded regression/fix
→ thoughtful review response
→ related follow-up when real
```

Do not optimize for comment count or PR count.

The anchor-community goal is repeated interaction around one coherent
subsystem/failure class.

## 13. Daily / Weekly / Monthly Operation

Use `PROGRESS_GATES.md` as the canonical checkpoint protocol.

### Daily

Start with current proof stage, assistance levels, fundamental, one engineering
question, and desired external movement. End with a no-notes consolidation and
update of what the human can explain unaided vs what still needs scaffolding.

### Weekly

Revisit the same engineering story through:

- HLD;
- LLD landmarks;
- reproduced failure(s);
- invariant/test intent;
- issue/PR/maintainer state;
- independence movement.

Set one proof-stage target for the week. If the weekly checkpoint finishes early,
depen the same active work before broadening, following `PROGRESS_GATES.md`.

### Monthly

Review externally inspectable proof, maintainer relationships, transferable
fundamentals, interview story quality, and whether one AI-owned responsibility
moved human-ward.

If the monthly checkpoint finishes early, prioritize follow-up contribution,
stronger regression/evidence, retention/transfer testing, and earned technical
writing before activating another repo. Switch only through the roadmap gate.

## 14. Course Correction

Do not continue a process just because time was already invested.

Trigger a review when:

- a week advances neither external proof nor independence;
- two consecutive weeks produce only private understanding;
- roughly 7–10 focused days on one candidate still produce no credible
  reproduction/invariant/PR-sized scope/maintainer path;
- maintainer direction clearly makes the candidate low value;
- required test infrastructure is unavailable.

Prefer first changing the **candidate within the same subsystem**. Switch the
repository only when the repository/subsystem gate genuinely fails or the global
switch condition is met.

## 15. Repository Switch Rule

Use the gate in `ROADMAP.md` and `PROGRESS_GATES.md`.

The default is:

```text
understanding
+
maintainer-visible external proof
+
transferable lesson
+
continuation no longer highest-value
→ switch
```

Do not switch for novelty or to collect repository logos.

## 16. Knowledge Promotion

Knowledge moves upward only after evidence:

```text
raw observation/source trace
→ repo-specific mental model
→ reproducible engineering result
→ contribution / maintainer feedback
→ supported invariant
→ cross-repo confirmation
→ reusable failure scenario
→ Failure Lab primitive
```

Routing:

- live repo state → active learning workspace `CURRENT.md`;
- reusable invariant → `PATTERN_LEDGER.md`;
- defensible personal engineering story → `INTERVIEW_EVIDENCE.md`;
- active/next repo change → `ROADMAP.md`;
- better selection rule → `CONTRIBUTION_FILTER.md`;
- changed six-month objective → `NORTH_STAR.md`.

Do not promote planning research or another contributor's PR as personal
evidence.

## 17. Workspace Cleanliness

Keep the global repo small.

Do not create files per day, per issue, or per concept. The durable global files
have fixed responsibilities. Detailed experiments belong in repository-specific
learning workspaces.

Update existing files instead of creating parallel versions such as
`ROADMAP_V2.md` or `FINAL_PLAN.md`.

## 18. Primary Operating Principle

The specialization is not:

> learn CUA → learn Rivet → learn Browser Use → learn E2B.

It is:

> repeatedly investigate lifecycle, ownership, state continuity, execution
> certainty, cancellation, and recovery across different agent execution layers,
> convert that work into upstream proof, and progressively own more of the
> engineering reasoning myself.