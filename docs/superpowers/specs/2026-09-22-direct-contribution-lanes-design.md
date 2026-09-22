# Direct Contribution Lanes Design

## Purpose

Correct the Agent Runtime Reliability contribution workflow so it produces
maintainer-reviewable pull requests instead of routing every unselected issue
through indefinite maintainer alignment.

The current policy protects ownership and architectural legitimacy, but in
practice it over-classifies bounded fixes as `SEEK ALIGNMENT`. Recent merged Cua
contributions show another legitimate path: a small, evidence-backed patch and
regression may go directly to a focused pull request, with review of that pull
request serving as the maintainer selection event.

## Evidence behind the correction

The bounded 2026-09-22 review of merged outside-contributor work found these
recurring shapes:

- small internal or additive fixes were submitted directly with focused tests;
- the pull request, not a preceding issue reply, was often the first concrete
  maintainer review surface;
- successful authors kept scope narrow, named related work, stated missing
  platform evidence, and responded quickly to requested changes;
- larger contributions either extended an already selected feature or involved
  maintainer collaboration and substantially stronger validation; and
- an open pull request remained unselected until review, even when it was
  technically complete.

Representative merged examples include Cua PRs #3888, #3864, #3509, #1452,
#3248, and #3687. They are evidence for workflow shape, not universal authority
to bypass ownership, RFC, security, or platform gates.

## Desired outcome

Future contribution discovery must optimize for external proof conversion:

```text
evidence-backed problem
→ correct contribution lane
→ smallest maintainer-reviewable artifact
→ prompt response to review
→ merge or captured maintainer direction
```

A technically strong direct-PR candidate should normally be preferred over a
more ambitious candidate that can only wait for product or architecture
direction.

## Contribution lanes

Every serious candidate receives exactly one lane.

### Direct focused PR — `PROCEED`

Use when all of the following are true:

- the expected/actual gap is reproduced or source-decisive;
- no assignee, credible implementation claim, matching active pull request, or
  maintainer-selected owner controls the same change;
- the invariant and observable regression are clear;
- the change is internal or additive and does not require an RFC, compatibility
  policy, permission decision, or cross-component architecture choice;
- one bounded implementation is clearly preferable to multiple product-valid
  alternatives;
- the affected component has an available validation path; and
- the human can defend the problem, boundary, test intent, and limits.

The contributor writes the failing regression first, implements the smallest
change, and opens a focused pull request early. The pull request must state that
it is an unselected contribution until maintainer review. Review, assignment,
or merge supplies selection; opening the pull request does not.

### Contribute to existing work — `CONTRIBUTE TO EXISTING WORK`

Use when an active pull request or selected owner already controls the same
implementation boundary. Offer a distinct regression, platform evidence,
review, or author-approved commit instead of opening a competitor. Preserve the
existing contributor's authorship.

### Seek alignment — `SEEK ALIGNMENT`

Use only when implementation depends on a maintainer-owned decision, including:

- public SDK, CLI, MCP, protocol, compatibility, or migration contracts;
- security, permission, trust, or default-policy changes;
- cross-component or cross-platform architecture choices;
- multiple reasonable product behaviors with no source-owned answer;
- maintainer-controlled infrastructure or unavailable acceptance environments;
  or
- plausible latent ownership that cannot be separated from the intended patch.

The alignment request must ask for one bounded decision. It must not substitute
for a direct PR when the repository already permits a small self-contained fix.

### Stop — `STOP`

Use for duplicates, claimed work without a distinct useful artifact,
unavailable validation, security reports that require private handling, weak
contribution-arc fit, or candidates whose useful scope cannot be bounded.

## Candidate-selection preference

The canonical scorecard continues to measure technical value, but a new
conversion gate precedes final recommendation:

1. reject ownership, RFC, validation, and contribution-arc blockers;
2. classify each eligible candidate by lane;
3. prefer one strong direct-focused-PR candidate over an equally strong
   alignment candidate;
4. recommend an alignment candidate only when it is strategically more valuable
   and the waiting decision has a credible maintainer path; and
5. never create parallel active workstreams while another candidate waits.

Issue recency and an empty assignee field are evidence to inspect, not either a
permission grant or an automatic reason to wait.

## Conversion timebox and kill condition

A direct candidate gets one focused implementation slice to reach:

```text
failing regression
→ bounded source boundary
→ minimal passing patch
→ focused validation
→ reviewable PR description
```

If the regression cannot express the invariant, the patch expands into policy
or architecture, adjacent ownership appears, or validation is unavailable,
stop implementation and reclassify the candidate. Do not turn a direct lane
into an open-ended private investigation.

## Pull-request contract

A direct contribution should expose the same information maintainers repeatedly
accepted in merged work:

- concrete problem and user/agent impact;
- smallest changed behavior;
- related issue, PR, or precedent without claiming to resolve broader work;
- regression and focused validation, including red/green evidence when
  practical;
- compatibility and rollback boundary;
- known gaps and platform evidence not established; and
- contributor/release metadata required by the repository.

Open the pull request once the change is meaningfully reviewable. Keep its
description current and respond to review with exact commits, tests, and
remaining limits. Do not wait for exhaustive platform certification when the
repository's normal CI or maintainer-owned environment is the authoritative
gate, but do not claim that missing evidence passed.

## Repository-policy integration

### Global contribution filter

Update `CONTRIBUTION_FILTER.md` to:

- introduce the four lanes and conversion preference;
- make clear that maintainer selection before implementation is conditional,
  not universal;
- preserve existing ownership, RFC, security, and public-wording gates; and
- add direct-PR conversion and kill conditions to the decision output.

### CUA learning workflow

Update `cua-learning/WORKFLOW.md` so issue discovery records the chosen lane.
For a direct candidate, park any waiting active path, activate one bounded
question, satisfy the learning/test-intent gate, then move promptly into
test-first implementation and an early focused pull request. For alignment,
existing-work, and stop lanes, retain their current boundaries.

### CUA contribution skill

Update `.agents/skills/cua-contribution/SKILL.md` so agents do not infer that
every unselected contribution needs an issue reply before code. Its decision
output remains `PROCEED`, `SEEK ALIGNMENT`, `CONTRIBUTE TO EXISTING WORK`, or
`STOP`; `PROCEED` explicitly names the direct-focused-PR execution mode.

### Live discovery state

Update `cua-learning/CONTRIBUTION_DISCOVERY.md` and `CURRENT.md` only enough to
record the corrected routing rule and the current candidate implications. Do
not silently activate or implement a candidate merely because the policy was
corrected.

## Behavioral regression scenarios

The updated policy and skill must classify these scenarios consistently:

| Scenario | Required result |
| --- | --- |
| Unowned, one-component bug; deterministic failing test; additive/internal fix; no RFC or competing work | `PROCEED` through direct focused PR; no preliminary maintainer reply required |
| Exact or adjacent active PR owns the mechanism | `CONTRIBUTE TO EXISTING WORK`; no competing PR |
| Change chooses a public compatibility/default policy or cross-component contract | `SEEK ALIGNMENT`; ask for the smallest missing decision |
| Assignee or credible contributor claim owns the slice and no distinct evidence/review artifact is useful | `STOP` |

The actual repeated `SEEK ALIGNMENT` outcome that triggered this correction is
the baseline failure. Multi-agent pressure testing is unavailable under the
current session policy, so validation will use this explicit decision table,
cross-file consistency checks, repository skill validation, and the workspace
strategy/context audits.

## Files to modify

- `agent-infra-specialization/CONTRIBUTION_FILTER.md`
- `cua-learning/WORKFLOW.md`
- `.agents/skills/cua-contribution/SKILL.md`
- `cua-learning/CONTRIBUTION_DISCOVERY.md`
- `cua-learning/CURRENT.md`

No Cua product source, GitHub issue, pull request, comment, assignment, or label
is changed by this policy update.

## Validation

- inspect existing diffs before editing and preserve unrelated user changes;
- verify the four scenario outcomes are stated identically across the global
  filter, workflow, and skill;
- run the repository skill validator against `cua-contribution`;
- run `contextctl.py audit` for the CUA learning workspace;
- run `strategyctl.py audit` for the global specialization workspace;
- run whitespace and merge-conflict checks on every modified artifact; and
- review the final diff against this design before reporting completion.
