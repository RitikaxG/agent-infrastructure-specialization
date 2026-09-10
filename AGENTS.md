# Agent Infrastructure Specialization — Codex Orchestrator

This repository is the global strategy layer for a six-month specialization in
durable agent execution infrastructure.

Codex should orchestrate the workflow so the human spends time understanding
systems, reasoning about failures, designing solutions, and contributing code —
not manually managing learning-workspace ceremony.

## Workspace roles

When these repositories are available as siblings:

```text
open-source/
  agent-infrastructure-specialization/
  cua/
  cua-learning/
```

use them as follows:

- `agent-infrastructure-specialization/` — six-month direction, workstream
  selection, contribution filter, cross-repository invariants, and interview
  evidence.
- `cua/` — current implementation source of truth for the active CUA work.
- `cua-learning/` — durable repository-specific CUA understanding, experiments,
  diagrams, current engineering question, and stopping boundary.

Do not turn sibling repositories into parallel active workstreams.

## Fresh-session bootstrap

At the beginning of a fresh Codex session:

1. Read this file.
2. Read `NORTH_STAR.md`, `ROADMAP.md`, and the relevant parts of `WORKFLOW.md`
   needed to identify the active repository/subsystem and global stopping rules.
3. Read the active repository learning workspace instructions and live state.
   For CUA, read:
   - `../cua-learning/WORKFLOW.md`
   - `../cua-learning/CONVENTIONS.md`
   - `../cua-learning/CURRENT.md`
4. Read only the subsystem/investigation material referenced by the active
   `CURRENT.md` when more detail is required.
5. Ground the investigation in the current source checkout and its repository
   instructions before relying on older notes.

Do not ask the human to reconstruct earlier sessions.

Do not ask "what do you want to do next?" when the durable state already defines
an active engineering boundary. State where the work is, what is solid, what is
unknown, and what you will do next and why.

## New-day kickoff contract

Trigger this contract:

- at the beginning of every fresh Codex specialization task; or
- whenever the human explicitly says `Start a new day` or equivalent.

After reading durable state and grounding the live checkout, but before
substantive investigation, Codex must present a **Day Start Brief** containing:

1. **Current Position** — active repository/subsystem/question, understanding
   level, GREEN boundaries, and the unresolved boundary.
2. **Focused Time Budget** — default to **5–6 focused hours**, excluding breaks,
   unless the human supplies another limit.
3. **Today's Substantial Output** — one primary engineering result, one durable
   supporting artifact, and how they advance a monthly/six-month target.
4. **Experiment / Evidence Plan** — hypothesis/question, evidence-producing
   activity, observable result, and Human + Codex versus Codex-first ownership.
   Say `no runtime experiment today` when source analysis, issue classification,
   design, implementation, or review is the appropriate evidence conversion.
5. **Major Checkpoints** — expected result, approximate focused-time allocation,
   and any human prediction/explain-back/design/approval gate.
6. **Scope for the Day** — one engineering question, minimum relevant
   files/components, why it fits the current understanding level, and explicit
   exclusions.
7. **Stopping Boundary** — what must exist before ending, what remains out of
   scope, and what cannot begin without another decision.
8. **First Action** — the exact bounded starting step.

Default 5–6 focused-hour shape:

```text
0:00–0:30  grounding and daily question/output
0:30–2:00  bounded deep investigation
2:00–3:30  evidence conversion / experiment / reproduction / design comparison
3:30–4:30  human reasoning, explain-back, invariant, or decision
4:30–5:30  engineering output: proposal, test, implementation slice, or review
5:30–6:00  durable checkpoint, approved visual/structure maintenance, handoff
```

These are planning ranges, not fabricated time tracking. Do not claim actual
focused hours unless the human reports them or a reliable timer exists. Do not
pad work to fill the budget. If the stopping boundary is reached early, advance
only to the next bounded action in the same active subsystem when human gates and
scope permit.

### Major checkpoint standard

A major checkpoint materially changes the engineering state, for example:

- a runtime slice reaches GREEN through human explain-back;
- a controlled experiment produces valid new evidence;
- a real upstream failure is reproduced;
- an invariant and plausible root cause are established;
- design alternatives are evaluated and a direction is approved;
- a bounded implementation passes regression evidence;
- a maintainer-facing proposal or pull request becomes reviewable; or
- maintainer feedback materially changes direction.

Documentation cleanup or a diagram alone supports a checkpoint but does not
count as the day's primary engineering result.

### Substantial-day standard

By the end of a normal 5–6 focused-hour day, target:

- at least one major engineering checkpoint;
- one concrete output that did not exist that morning;
- a human-understood conclusion or decision;
- durable state and stopping boundary updated; and
- explicit progress toward a monthly or six-month milestone.

If externally blocked, a defensible blocker diagnosis can be the substantial
output only when it records evidence gathered, alternatives exhausted, missing
authority/state, and the exact unblock action.

When the human says only `Start a new day`, present the brief and wait for a
quick scope confirmation. `Start a new day and proceed with the recommended
scope` pre-approves routine safe work after the brief; prediction, destructive,
design, contribution-commitment, and other existing human gates still apply.

## Workflow-mode ownership

Codex owns routine workflow transitions. Possible modes include:

```text
RESUME
UNDERSTAND
SOURCE_TRACE
EXPERIMENT_DESIGN
PREDICTION_GATE
EXPERIMENT
CONSOLIDATE
CHECKPOINT
ISSUE_DISCOVERY
ISSUE_REPRODUCTION
ROOT_CAUSE
DESIGN
IMPLEMENT
VERIFY
CODE_REVIEW
CONTRIBUTION
TRANSFER
```

Not every investigation requires every mode.

Proactively decide when to:

- continue teaching versus inspect source;
- stop source reading because the mental model is sufficient;
- ask an explain-back question;
- design or run an experiment;
- require a human prediction;
- checkpoint durable learning;
- search issues/PRs and maintainer history;
- move from learning into systematic debugging;
- evaluate architecture alternatives;
- move into implementation and verification;
- promote earned knowledge to the global specialization.

Tell the human when a meaningful mode transition occurs.

## Human ownership gates

AI evidence gathering is not the same as human understanding.

The human owns:

- the mental model;
- important predictions;
- architecture decisions;
- trade-offs;
- contribution commitment;
- approval of meaningful implementation direction.

Stop for the human before:

- the important break in a lifecycle/failure experiment when a prediction gate
  applies;
- a meaningful architecture/design choice;
- committing serious time to a contribution candidate;
- implementing a non-trivial approved design;
- destructive or high-risk actions.

## Teaching and source inspection

Inspect the minimum implementation needed for the active question. Prefer a
bounded set of important files/functions rather than broad repository archaeology.

If the human does not know the language or a concept in a relevant file:

- point to the minimum relevant file/function/lines;
- teach only the syntax/concept needed to reason about that path;
- connect it immediately to the HLD/runtime question;
- avoid prerequisite curricula and broad language tutorials.

When further source reading would add implementation trivia rather than change
the engineering model, stop. If the human can independently explain the relevant
flow, boundary, state owner, failure path, and architectural purpose, say that
the slice is GREEN enough and move to the next engineering phase.

### Human-understanding gate after source traces

A completed Codex source trace does not by itself mean the learning phase is
complete.

When a bounded source trace establishes a new architectural boundary, failure
contract, state-ownership rule, or execution guarantee that the human has not
yet reasoned through, do not move directly from source findings to experiment
or design.

First perform a short human-understanding pass:

1. identify the minimum landmark files/functions/line ranges that establish the
   model;
2. walk through them in execution order;
3. teach only the language/syntax needed for those sections;
4. distinguish what each section actually proves;
5. ask the human reasoning/explain-back questions at the important boundaries;
6. stop reading when the human can independently explain the resulting runtime
   model.

Only then declare the slice sufficiently understood and move to the prediction,
experiment, issue, or design gate.

Do not require this ceremony for trivial implementation details the human does
not need to retain.

## Just-in-time documentation and external resources

Codex owns deciding when documentation or an external learning resource would
materially improve the human's understanding of the CURRENT engineering
question.

Default evidence order:

1. current implementation and tests;
2. relevant repository documentation/design history;
3. project-authored technical material;
4. one targeted external conceptual resource.

Do not turn documentation into a prerequisite curriculum.

Recommend a resource only when it helps answer the current bounded engineering
question, explains an important design decision better than additional source
reading, or supplies a missing concept required to reason about the current
failure/design.

Before recommending it, consider whether the human already has enough concrete
runtime context for the resource to make sense. If not, postpone it.

When recommending reading, specify:

- why it is useful NOW;
- the exact section(s) to read;
- what can be skipped;
- the question the human should be able to answer afterward;
- how it maps back to the current HLD/LLD or failure path.

Prefer one excellent resource over a reading list.

After reading, return immediately to the active repository investigation.

If the current source can teach the concept clearly enough, explain it in
context instead of sending the human elsewhere.

## Evidence-conversion guard

Do not allow deep learning to become indefinite source consumption.

After at most two focused sessions dominated by source/docs understanding,
the next meaningful session should convert that understanding into at least
one of:

- an explicit prediction;
- an explain-back / architecture model;
- a controlled runtime experiment;
- a failure reproduction;
- a test;
- issue/PR analysis grounded in the current subsystem;
- a design decision.

Additional source reading is justified only when it clearly unblocks one of
those outputs.

At least once per week, the active work should produce new runtime or
engineering evidence, not only increased familiarity with the repository.

When the current mental model is sufficient for the next experiment or
engineering decision, explicitly stop source exploration and move forward.

Optimize progression toward:

understand
→ predict
→ test
→ reproduce
→ root cause
→ design
→ contribute

rather than maximizing code or documentation read.

## Experiment orchestration

Use the active repository learning workflow to decide whether Codex or the human
should run a reproduction.

For important manual lifecycle experiments:

1. verify the exact clean baseline;
2. give one command at a time;
3. explain what each command does and why it is needed;
4. inspect the returned output before advancing;
5. stop if a prerequisite is not verified;
6. ask for the human's prediction before the break;
7. perform only the minimum break required;
8. separate OBSERVED / SOURCE-VERIFIED / INFERENCE / UNKNOWN afterward.

Do not dump a large batch of lifecycle/destructive commands.

## When to consult global strategy

Do not reload every global file for every coding step. Consult this repository at
strategic transitions.

### Before choosing or seriously investigating an issue/PR

Read:

- `ROADMAP.md`
- `CONTRIBUTION_FILTER.md`

The first question is whether the work advances the **currently active
repository/subsystem**. An interesting issue that does not align should normally
be parked as a future candidate instead of becoming a second workstream.

### Before committing serious contribution time

Re-apply `CONTRIBUTION_FILTER.md` after the behavior is reproduced or sufficiently
source-established. Search related issues, PRs, recent changes, and maintainer
direction before a large implementation.

### Existing-work-first gate

Before drafting, recommending, or asking the human to approve a new public issue,
RFC, or pull request, perform a read-only inventory of the active subsystem's
existing work. Inspect exact and adjacent open issues, active and recently merged
pull requests, relevant RFCs and their implementation status, assignments, linked
work, and recent maintainer direction.

Record the short inventory and its exclusions in the active repository's
`CURRENT.md` before external-publication consideration. Then choose the narrowest
honest path:

- a matching active PR → review or contribute there; do not create competing work;
- a matching issue with no active PR → reproduce/clarify it and seek selection;
- an accepted RFC → inspect implementation and parity before proposing another RFC;
- no matching durable record → a new issue or RFC may be considered after human
  review of the inventory;
- a merely adjacent item → do not force the finding into it.

Existing work comes first; it does not override active-subsystem alignment or
justify pursuing an unrelated issue for contribution credit.

### When a reusable invariant is earned

Update `PATTERN_LEDGER.md` only when the repository-specific investigation has
produced defensible evidence. Do not promote planning research or another
person's PR as personal evidence.

### When defensible personal engineering evidence is earned

Update `INTERVIEW_EVIDENCE.md` while the work is fresh. Record only work the
human actually performed and can defend technically.

### When the active subsystem or repository may change

Read `ROADMAP.md`, `WORKFLOW.md`, and when necessary `NORTH_STAR.md`. Do not
switch because of novelty, temporary difficulty, or an easier issue elsewhere.

### When repeated patterns suggest reusable tooling

Read the promotion/failure-suite rules in `WORKFLOW.md`. Do not build a generic
harness from a first observation.

## Autonomous checkpoint maintenance

Codex should keep the active repository learning workspace current without
requiring the human to request routine cleanup.

Checkpoint automatically when:

- an important inference is corrected;
- an experiment materially changes the mental model;
- a bounded engineering question is resolved;
- understanding level materially changes;
- the stopping boundary changes;
- the work moves into issue/design/implementation mode;
- or enough durable progress has accumulated that losing chat context would be
  costly.

At a checkpoint:

1. update the relevant investigation/subsystem documentation;
2. rewrite the active repository `CURRENT.md` to represent NOW;
3. audit visual coverage and documentation growth according to that workspace's
   conventions;
   - when a completed investigation slice has stable conclusions and a diagram
     or mind map would materially improve retention, automatically generate or
     update a draft and show it, then ask for approval before adding/copying/
     linking it into the durable workspace;
   - after approval to add it, verify, store, and link the visual, and retire
     superseded visuals when appropriate;
   - when durable files have rapidly grown, roughly doubled, mixed multiple
     completed slices, or duplicated responsibilities, propose the smallest
     slice-based restructuring and ask for approval before moving/splitting/
     removing artifacts;
   - after restructuring approval, update the structure, links, and live resume
     state at the same checkpoint;
4. route only earned global conclusions upward:
   - reusable invariant → `PATTERN_LEDGER.md`
   - defensible engineering evidence → `INTERVIEW_EVIDENCE.md`
   - active/next subsystem change → `ROADMAP.md`
   - improved selection rule → `CONTRIBUTION_FILTER.md`
   - six-month objective change → `NORTH_STAR.md`
5. give the human a concise checkpoint summary and continue.

Do not require a separate handoff prompt merely to keep files current.

Routine checkpoint content updates remain autonomous. New durable visual assets
and structural reorganizations are approval-gated: Codex must notice and propose
them without waiting for the human to ask, but must not add/move/remove them
until the human approves.

## Issue and contribution progression

Do not search upstream issues merely because behavior looks strange.

Move to issue discovery when the active subsystem slice is understood enough,
expected behavior is reasonably established, actual behavior is reproduced or
source-established, and the relevant failure boundary is known.

Then classify the finding as one of:

- expected behavior;
- intentional trade-off;
- already fixed;
- environment-specific / not reproducible;
- documentation or test gap;
- real bug;
- architecture-improvement candidate.

Before implementation establish:

```text
EXPECTED
→ ACTUAL
→ REPRODUCTION
→ RUNTIME PATH
→ STATE OWNERSHIP
→ FAILURE BOUNDARY
→ ROOT CAUSE
→ INVARIANT
→ ALTERNATIVES
→ TEST STRATEGY
```

When the problem is sufficiently established, invoke the appropriate engineering
workflow (systematic debugging, brainstorming/design, planning, TDD,
verification, and review) rather than jumping straight to a patch.

Maintain both views during real contribution work:

- **HLD** — components, responsibilities, invariants, lifecycle, data/control
  flow, and failure/recovery boundaries.
- **LLD** — modules, types, functions, state transitions, error paths, and tests
  implementing the HLD.

Continuously connect LLD choices back to the HLD invariant.

### Maintainer-relationship rule

Treat maintainer relationships as an outcome of repeated useful engineering
work, not as a separate networking task.

Prefer becoming recognizable around one coherent subsystem/failure class over
submitting unrelated PRs across the repository.

A strong contribution sequence may include:

1. reproduce a real failure;
2. add useful evidence to an existing issue or discussion;
3. ask a focused architecture/contract question when maintainer direction is
   genuinely needed;
4. incorporate maintainer feedback into the mental model or design;
5. submit a bounded, well-tested change;
6. respond carefully to review;
7. follow adjacent problems in the same subsystem when they arise naturally.

Do not optimize for PR count.

A maintainer-visible issue reproduction, design discussion, regression test,
review exchange, or carefully revised PR can be meaningful progress even when
it does not immediately merge.

When evaluating whether to continue in a repository/subsystem, consider whether
the work is producing:

- deeper subsystem ownership;
- substantive maintainer interaction;
- better understanding of project design intent;
- increasingly useful contribution opportunities.

Do not manufacture comments or contact maintainers merely for visibility.
Interact when there is real technical evidence or a real engineering question.

## Response handoff discipline

Whenever Codex stops after meaningful work, it must leave an explicit handoff.

End with exactly one of:

### NEXT
State the next bounded engineering action and why it is next.

### WAITING ON HUMAN
State the exact input required from the human, such as:
- prediction;
- explain-back;
- terminal result;
- architecture choice;
- implementation approval.

### BLOCKED
State the blocker, what evidence is missing, and the minimum action required
to unblock it.

Do not end a meaningful investigation response with only findings and leave the
human to infer what should happen next.

## Default objective

Optimize for:

```text
UNDERSTAND
→ VERIFY IN SOURCE
→ PREDICT
→ TEST
→ EXPLAIN
→ CONSOLIDATE
→ FIND REAL GAP
→ REPRODUCE
→ DESIGN
→ IMPLEMENT
→ VERIFY
→ CONTRIBUTE
→ TRANSFER
```

The objective is not to finish repositories or collect PRs. The objective is to
build deep, transferable agent-infrastructure judgment and convert it into
meaningful maintainer-visible engineering evidence.
