# Compounding Subsystem Guidance Design

## Purpose

Prevent issue discovery, contribution selection, and learning from fragmenting
into unrelated tasks. The guidance must keep one active repository, one active
subsystem, and one primary engineering question while deliberately accumulating
the architecture, failure reasoning, product judgment, and public proof needed
to own agent-runtime repositories over time.

The system should make future work answer two questions before serious
investment:

1. How does this candidate deepen the active subsystem and reliability spine?
2. What reusable knowledge or public artifact can it add?

An issue that is merely open, interesting, recent, easy, or unassigned is not a
qualified contribution path.

## Desired outcome

Future issue-discovery and contribution-path requests should produce one
ownership-filtered candidate that:

- reuses an established subsystem model or intentionally activates a new one;
- strengthens a named Agent Runtime Reliability fundamental and failure family;
- adds a plausible stable architecture, product, operational, or test delta;
- has a credible maintainer-visible artifact and validation path;
- has an explicit transfer analogue in a planned repository or target system;
- has a bounded timebox and kill condition; and
- does not compete with assigned, claimed, or otherwise actively owned work.

Learning state should accumulate at the subsystem level. Issue records retain
evidence and issue-specific implementation detail; they should not each rebuild
the full HLD.

## Non-goals

- Do not optimize for PR count through cosmetic or disconnected issues.
- Do not preselect exact future issues months before their repository is active.
- Do not study several repositories or subsystems concurrently.
- Do not create a separate HLD, fundamentals file, or daily learning file for
  every issue.
- Do not turn every common systems feature into a generic checklist detached
  from observed failures.
- Do not change Cua product source, public issue state, or contribution
  ownership as part of this guidance update.

## Canonical ownership and duplication boundary

Each concept has exactly one canonical owner. Other files may require or link
to the concept but must not reproduce its full rule set.

| Concern | Canonical owner | Other files do |
| --- | --- | --- |
| Six-month identity and success outcome | `NORTH_STAR.md` | Reference only |
| Definitions of reliability fundamentals and mastery | `FUNDAMENTALS.md` | Name the applicable fundamentals |
| Repository sequence and intended transfer layers | `ROADMAP.md` | Reference the active/planned block |
| Candidate eligibility and required selection output | `CONTRIBUTION_FILTER.md` | Invoke the filter and consume its output |
| Daily/weekly/monthly proof, independence, and switch gates | `PROGRESS_GATES.md` | Record the current result |
| Cross-repository invariants supported by personal evidence | `PATTERN_LEDGER.md` | Promote only after its evidence gate |
| CUA investigation and transition procedure | `cua-learning/WORKFLOW.md` | Follow it; do not restate global criteria |
| Durable documentation placement and schema | `cua-learning/CONVENTIONS.md` | Apply the schema at checkpoints |
| Current CUA subsystem HLD, product contract, failures, and stable deltas | `cua-learning/subsystems/<subsystem>/README.md` | Issue records link to it |
| Issue-specific reproduction, evidence, LLD, and unresolved questions | Owning issue/investigation README | Promote only stable deltas upward |
| One live question, gate, next action, and stop boundary | `cua-learning/CURRENT.md` | Never use as a historical ledger |
| Contribution-task operational behavior | `cua-contribution` skill | Load canonical filter rather than copy it |
| New-subsystem and transfer teaching behavior | `cua-guided-learning` skill | Load repository-local workflow rather than copy it |

`NORTH_STAR.md`, `FUNDAMENTALS.md`, and `ROADMAP.md` already express the
approved strategy and do not need additional parallel prose for this change.

## Workstream model

The unit of continuity is an active subsystem and reliability spine, not an
individual issue.

```text
global fundamentals and cross-repository patterns
        ↓
repository subsystem model and product contract
        ↓
issue-specific failure evidence and implementation slice
        ↓
maintainer-visible artifact
        ↓
stable delta promoted back to subsystem/global knowledge
```

Movement is classified before starting:

| Movement | Default decision |
| --- | --- |
| Same repository, same subsystem | Prefer; deepen the active model |
| New repository, analogous subsystem/failure family | Deliberate transfer after the switch gate |
| Same repository, unrelated subsystem | Require a subsystem checkpoint and activation brief |
| New repository, unrelated subsystem | Avoid because both architecture and failure model reset |

The current CUA subsystem remains **Driver Runtime reliability**. Linux
accessibility readiness and individual browser/daemon failures are slices
inside that subsystem rather than separate long-lived workstreams.

## Candidate selection contract

`CONTRIBUTION_FILTER.md` will become the sole owner of a required **Subsystem
Fit** candidate block:

```text
ACTIVE SUBSYSTEM / RELIABILITY SPINE
PRODUCT CAPABILITY AND USER IMPACT
EXISTING HLD PATH REUSED
FAILURE FAMILY
PRIMARY FUNDAMENTAL
NEW STABLE DELTA IF PROVEN
TRANSFER ANALOGUE
OWNERSHIP / DUPLICATION STATE
MAINTAINER-VISIBLE ARTIFACT
VALIDATION ENVIRONMENT
TIMEBOX / KILL CONDITION
```

The block is filled only after issue comments, assignments, linked and unlinked
PRs, fork branches or credible claims, RFC dependencies, and maintainer
direction are refreshed. Empty assignment or missing Development-panel linkage
is insufficient ownership evidence.

A candidate is rejected before scoring when it cannot identify a meaningful
subsystem delta, public artifact, transfer value, or legitimate ownership path.
Candidate scoring may compare otherwise eligible choices; it may not rescue a
fragmented or actively owned issue.

`cua-contribution` will require this canonical block and return the existing
`PROCEED`, `SEEK ALIGNMENT`, `CONTRIBUTE TO EXISTING WORK`, or `STOP`
classification. It will not duplicate the block's field definitions.

## Subsystem activation and switch contract

When a genuinely new subsystem is considered, the repository-local workflow
will require a compact **Subsystem Activation Brief** before broad source
orientation:

- product/user capability and why the subsystem exists;
- 3–7 component preliminary HLD and ownership boundaries;
- primary reliability question and two or three applicable fundamentals;
- likely repeated failure families;
- available contribution and validation surface;
- transfer hypothesis from the previous subsystem;
- evidence target; and
- exit/switch gate.

The brief is a bounded section in the subsystem README or active manifest, not
a new standalone file by default.

Repository or subsystem switching uses the canonical gate in
`PROGRESS_GATES.md`:

- **understanding:** defensible compact HLD, relevant LLD, and invariant;
- **external proof:** serious maintainer-visible artifact or contribution
  attempt;
- **transfer:** reusable lesson and next-layer analogue recorded; and
- **direction:** expected value of the next layer exceeds another adjacent
  investigation.

The escape hatch remains available when strong evidence plus two aligned
contribution surfaces still produce no credible maintainer path. Waiting on one
maintainer response alone is not a switch condition; the next search first
stays inside the same subsystem and failure family.

Exact future issues are selected only when a repository becomes active. The
roadmap fixes the sequence and intended subsystem role, not stale issue numbers.

## Cumulative subsystem knowledge model

`CONVENTIONS.md` will own the documentation schema. Every subsystem README
should retain, when evidence exists:

1. **Product contract** — the user/agent capability and safe caller
   expectations.
2. **Stable HLD** — components, ownership, communication, healthy lifecycle,
   independent failure boundaries, and recovery owner.
3. **Failure-family ledger** — healthy state, fault/variation, observation,
   invariant, recovery, and unknowns for personally investigated cases.
4. **Fundamental coverage** — which fundamentals are only understood,
   personally observed, implemented/tested, predicted independently, or
   transferred.
5. **Contribution history** — maintainer-visible evidence, PR/review state, and
   model-changing feedback.
6. **Transfer map** — equivalent roles expected in the next planned system.
7. **GREEN/YELLOW boundaries** — stable knowledge versus unresolved areas.

These are logical responsibilities, not mandatory empty headings. Existing
sections should be reused and minimally reshaped instead of duplicated.

Each issue/investigation README should state near its start:

```text
REUSED FROM SUBSYSTEM
NEW ISSUE-SPECIFIC QUESTION
CANDIDATE STABLE DELTA
FUNDAMENTAL / FAILURE FAMILY
PUBLIC-PROOF INTENT
TRANSFER ANALOGUE
```

At a checkpoint:

- raw and classified evidence remains in the issue README;
- only proven stable architecture/product/failure knowledge is promoted to the
  subsystem README;
- only reusable invariants supported by the required personal evidence move to
  `PATTERN_LEDGER.md`; and
- `CURRENT.md` is rewritten to represent the single live question.

The current Driver Runtime README will receive a compact reliability spine and
compounding ledger using the already established #2686 and #2915 evidence. It
will not copy their detailed reproductions or source traces.

## Fundamental concretization

The workflow will treat a fundamental as an evidence progression rather than a
topic checkbox:

```text
term
→ issue-specific example
→ personally observed failure
→ subsystem invariant
→ adjacent prediction
→ implementation/test decision
→ cross-repository recognition
→ production/product judgment
```

The subsystem README records the current evidence level. Global promotion is
earned when the lesson is supported by personal investigations and is reusable
beyond repository-specific names.

This lets source vocabulary remain local while the durable engineering
questions compound: readiness, ownership/generation, durable versus ephemeral
state, execution outcome, cancellation/quiescence, and reconciliation/cleanup.

## Progress and anti-fragmentation review

`PROGRESS_GATES.md` will own the recurring review questions. Weekly/monthly
reviews should determine whether:

- a new issue reused the existing subsystem HLD;
- orientation time decreased;
- the human predicted the owner/failure boundary earlier;
- implementation, review, product, or operational judgment increased;
- public proof advanced;
- the lesson maps to the planned next repository without relying on local
  component names; and
- the workstream should deepen, transfer, or stop.

The existing two-session evidence-conversion, two-week private-work, candidate
kill, and repository-switch rules remain canonical and should be referenced
rather than restated elsewhere.

## Skill enforcement and behavioral validation

Two existing skills need narrow changes:

### `cua-contribution`

Require the canonical Subsystem Fit result before recommending a candidate.
Reject issue-shopping that optimizes for availability while losing the active
reliability spine, transfer value, or product/contribution delta.

### `cua-guided-learning`

Distinguish three entry cases:

- same subsystem: retrieve the stable subsystem HLD, identify reuse, and teach
  only the issue delta;
- new subsystem in CUA: create the activation brief and begin at GUIDED for new
  repository-specific vocabulary;
- transfer to a new repository: ask for the familiar failure family/owner/state
  model first, then teach repository-specific differences.

Because these are skill edits, each skill is changed and validated separately:

1. run a realistic pressure scenario against the current skill and record the
   baseline failure;
2. apply the smallest guidance change that corrects that failure;
3. rerun the scenario and inspect the decision, not only wording;
4. run the skill validator; and
5. finish validation before editing the second skill.

The known baseline for contribution selection is the temptation to recommend a
fresh, apparently unassigned issue with weak transfer fit and plausible latent
reporter ownership because it appears capable of producing a fast PR.

## Files to modify

- `agent-infra-specialization/CONTRIBUTION_FILTER.md`
- `agent-infra-specialization/PROGRESS_GATES.md`
- `cua-learning/WORKFLOW.md`
- `cua-learning/CONVENTIONS.md`
- `cua-learning/subsystems/driver-runtime/README.md`
- `.agents/skills/cua-contribution/SKILL.md`
- `.agents/skills/cua-guided-learning/SKILL.md`

No new subsystem ledger or HLD file will be created. `CURRENT.md` will not be
changed until a new active engineering question or subsystem is actually
selected.

## Validation

The change is complete when:

- candidate selection has one canonical Subsystem Fit contract;
- switch timing has one canonical gate;
- documentation placement has one canonical schema;
- skills point to those owners instead of copying full criteria;
- the Driver Runtime README shows cumulative knowledge without reproducing
  issue evidence;
- skill pressure scenarios demonstrate corrected decisions;
- skill frontmatter and structure pass validation;
- `contextctl audit` passes;
- `strategyctl audit` passes; and
- diffs show no unrelated or overwritten pre-existing changes.

