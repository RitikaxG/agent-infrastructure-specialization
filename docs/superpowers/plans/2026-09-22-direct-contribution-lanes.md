# Direct Contribution Lanes Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the overly broad maintainer-alignment default with four evidence-backed contribution lanes that favor small, reviewable external pull requests without weakening ownership, RFC, security, or validation gates.

**Architecture:** `agent-infra-specialization/CONTRIBUTION_FILTER.md` remains the canonical policy. `cua-learning/WORKFLOW.md` applies that policy to activation and learning transitions, while `.agents/skills/cua-contribution/SKILL.md` enforces the lane decision at task time. `cua-learning/CONTRIBUTION_DISCOVERY.md` and `CURRENT.md` retain only the live candidate consequences, not duplicate policy.

**Tech Stack:** Markdown policy/skill files, Python workspace validators, Git diff/whitespace checks.

**Spec:** `agent-infra-specialization/docs/superpowers/specs/2026-09-22-direct-contribution-lanes-design.md`

## Global Constraints

- Preserve all pre-existing user changes in the three Git worktrees; use narrow `apply_patch` edits and never reset or restore unrelated hunks.
- Do not commit a modified file that already contained uncommitted user changes before this task. The plan/spec files may be committed independently because they are new and isolated.
- No Cua product source, GitHub issue, pull request, comment, assignment, label, or external publication changes are authorized.
- Exactly one lane must be returned for a serious candidate: `PROCEED`, `CONTRIBUTE TO EXISTING WORK`, `SEEK ALIGNMENT`, or `STOP`.
- `PROCEED` means direct focused PR mode only when the gap is decisive, the patch is bounded, the regression is clear, validation is available, and no ownership/RFC/public-contract blocker exists.
- Opening a direct pull request creates a review surface; it does not itself establish maintainer selection.
- Public wording remains human-reviewed before posting.
- Multi-agent pressure testing is unavailable unless the human explicitly selects a subagent-driven execution method; use the real repeated-`SEEK ALIGNMENT` failure plus the four deterministic scenarios as the behavioral baseline otherwise.

## Review Focus

- **Unassigned but credibly claimed work:** must route to `STOP` or `CONTRIBUTE TO EXISTING WORK`, never direct PR merely because GitHub assignment is blank; Task 1 and Task 3 pin this.
- **Small change that alters a public contract or default policy:** must remain `SEEK ALIGNMENT` even if it is one file; Task 1 and Task 3 pin this.
- **Recent issue with no owner and a deterministic internal regression:** recency alone must neither block nor authorize it; all direct-lane predicates decide; Task 1 pins this.
- **Adjacent active PR owns a prerequisite or same source mechanism:** must route to existing work instead of a nominally distinct competing PR; Task 1, Task 3, and Task 4 pin this.
- **Direct candidate expands during implementation:** must stop and reclassify when the regression is unclear, policy choices appear, or validation disappears; Task 2 and Task 3 pin this.

---

### Task 1: Make contribution lanes canonical in the global filter

**Files:**
- Modify: `agent-infra-specialization/CONTRIBUTION_FILTER.md:10-66`
- Modify: `agent-infra-specialization/CONTRIBUTION_FILTER.md:201-228`
- Modify: `agent-infra-specialization/CONTRIBUTION_FILTER.md:268-303`

**Interfaces:**
- Consumes: the approved four-lane design and the existing Subsystem Fit, ownership, scorecard, and PR-submission gates.
- Produces: one canonical lane-selection contract consumed by the CUA workflow and contribution skill.

- [ ] **Step 1: Record the current failing policy behavior**

Run:

```bash
rg -n -C 3 'matching issue without active implementation|seek selection|maintainer selection|meaningful source implementation' \
  agent-infra-specialization/CONTRIBUTION_FILTER.md \
  .agents/skills/cua-contribution/SKILL.md
```

Expected RED evidence: the current policy routes a matching unowned issue toward selection/alignment and has no explicit direct-focused-PR lane for a bounded internal fix.

- [ ] **Step 2: Add the canonical lane decision after the Subsystem Fit gate**

Insert a `### Contribution execution lane` section containing this contract:

```markdown
Classify every eligible candidate into exactly one lane before final ranking:

| Lane | Use when | Next maintainer-visible artifact |
| --- | --- | --- |
| `PROCEED` — direct focused PR | Gap is reproduced/source-decisive; no owner or competing work; invariant and regression are clear; change is internal/additive; no RFC, policy, permission, compatibility, or cross-component decision is required; validation is available. | Failing regression, minimal patch, focused validation, then an early focused PR that remains unselected until review. |
| `CONTRIBUTE TO EXISTING WORK` | An active PR or selected owner controls the same implementation boundary. | Distinct test, evidence, review, or author-approved commit with authorship preserved. |
| `SEEK ALIGNMENT` | Implementation depends on a public contract, policy/default, compatibility/migration, permission/trust, cross-component architecture, multiple valid product choices, maintainer-owned environment, or inseparable latent ownership. | One bounded maintainer decision. |
| `STOP` | Duplicate, claimed without a distinct useful artifact, privately reportable security issue, unavailable validation, weak arc fit, or unbounded useful scope. | None until the recorded blocker changes. |
```

Follow it with these two binding rules:

```markdown
An issue's age and empty assignee field are evidence to inspect, not a reason to
wait and not permission to implement. Maintainer direction before source work is
conditional on the selected lane; it is not universal. A qualifying direct fix
uses the pull request as the first concrete review surface.
```

- [ ] **Step 3: Add the conversion preference to candidate ranking**

Immediately before the scorecard, add:

```markdown
### External-proof conversion gate

After removing blockers and scoring technical fit, prefer one strong `PROCEED`
candidate over an equally strong `SEEK ALIGNMENT` candidate. Recommend alignment
only when its strategic value and credible maintainer path justify waiting.
Availability alone never outranks contribution-arc fit, but architectural
interest alone never outranks a reviewable external artifact.
```

- [ ] **Step 4: Correct the Existing-Work-First outcomes**

Replace the current `matching issue without active implementation` outcome with:

```markdown
- matching issue without active implementation → choose `PROCEED` when the
  direct-focused-PR predicates all hold; otherwise reproduce/clarify and use
  `SEEK ALIGNMENT` only for the missing maintainer-owned decision;
```

Retain the active-PR, assignee/owner, accepted-design, no-record, and adjacent-work outcomes unchanged.

- [ ] **Step 5: Add the conversion timebox and direct-PR contract before the PR Submission Gate**

Add:

```markdown
## Direct-PR Conversion Gate

A `PROCEED` candidate gets one focused implementation slice to reach failing
regression → bounded source boundary → minimal passing patch → focused
validation → reviewable PR description. If the invariant cannot be expressed,
scope expands into policy/architecture, ownership appears, or validation is
unavailable, stop and reclassify; do not extend private investigation by default.

Open the PR once the change is meaningfully reviewable. State the concrete
impact, smallest behavior change, related work, red/green regression, focused
validation, compatibility/rollback boundary, and known gaps. The PR is an
unselected contribution until maintainer review, assignment, or merge.
```

- [ ] **Step 6: Verify the four canonical outcomes are present without weakening blockers**

Run:

```bash
rg -n -C 2 'PROCEED|CONTRIBUTE TO EXISTING WORK|SEEK ALIGNMENT|STOP|Direct-PR Conversion Gate|security|assigned or maintainer-selected owner' \
  agent-infra-specialization/CONTRIBUTION_FILTER.md
/usr/bin/git -C agent-infra-specialization diff --check -- CONTRIBUTION_FILTER.md
```

Expected: all four lanes and the conversion gate are present; security and ownership language remains; diff check exits 0.

- [ ] **Step 7: Preserve the dirty-worktree boundary**

Do not commit `CONTRIBUTION_FILTER.md`: it contained pre-existing uncommitted changes before this task. Record its final diff for handoff instead.

### Task 2: Apply the lane model to the CUA learning workflow

**Files:**
- Modify: `cua-learning/WORKFLOW.md:154-169`
- Modify: `cua-learning/WORKFLOW.md:399-430`

**Interfaces:**
- Consumes: the canonical four lanes from Task 1.
- Produces: activation and implementation transitions for CUA investigations without duplicating the global predicates.

- [ ] **Step 1: Record the workflow's current missing transition**

Run:

```bash
rg -n -C 4 'Issue-to-subsystem transition|Contribution Progression|maintainer direction before creating public work' \
  cua-learning/WORKFLOW.md
```

Expected RED evidence: the workflow parks/replaces investigations and lists contribution stages, but does not say how `PROCEED` moves promptly from learning into a direct focused PR.

- [ ] **Step 2: Add lane ownership to issue activation**

After the existing instruction to apply `CONTRIBUTION_FILTER.md`, add:

```markdown
Record exactly one contribution lane for the candidate. Prefer a qualifying
direct-focused-PR candidate when it can convert the active reliability spine
into reviewable external proof. The lane does not activate a second workstream:
park the retained waiting path and rewrite `CURRENT.md` before executing the
replacement.
```

- [ ] **Step 3: Add lane-specific progression under Contribution Progression**

After the existing progression sequence, add:

```markdown
Lane-specific next action:

- `PROCEED`: complete the bounded learning/test-intent gate, write the failing
  regression first, implement the minimum patch, validate it, and open a
  focused PR early. Do not wait for a preliminary issue reply when all canonical
  direct-lane predicates hold; the PR remains unselected until review.
- `CONTRIBUTE TO EXISTING WORK`: produce only the distinct artifact accepted by
  the owner/PR boundary and preserve authorship.
- `SEEK ALIGNMENT`: ask for one missing maintainer-owned decision and do not
  implement through it.
- `STOP`: record the blocker/refresh trigger and move on.

If direct work expands into policy, architecture, unclear test intent,
ownership conflict, or unavailable validation, stop the slice and reclassify it.
```

- [ ] **Step 4: Verify workflow consistency**

Run:

```bash
rg -n -C 2 'Record exactly one contribution lane|Lane-specific next action|PROCEED|CONTRIBUTE TO EXISTING WORK|SEEK ALIGNMENT|STOP' \
  cua-learning/WORKFLOW.md
/usr/bin/git -C cua-learning diff --check -- WORKFLOW.md
```

Expected: all lane names and the reclassification boundary appear; diff check exits 0.

- [ ] **Step 5: Preserve the dirty-worktree boundary**

Do not commit `WORKFLOW.md`: it contained pre-existing uncommitted changes before this task.

### Task 3: Correct the repository contribution skill

**Files:**
- Modify: `.agents/skills/cua-contribution/SKILL.md:21-64`
- Validate: `/Users/ritikagupta/.codex/skills/.system/skill-creator/scripts/quick_validate.py`

**Interfaces:**
- Consumes: the canonical filter and lane names from Task 1.
- Produces: runtime instructions that select direct PRs correctly while preserving ownership and public-wording gates.

- [ ] **Step 1: Preserve the real behavioral RED case**

Record this observed baseline in the task notes before editing:

```text
Given an unowned, evidence-backed, bounded internal bug with a clear regression,
the current skill instructed the agent to seek maintainer selection before any
meaningful source implementation. Repeated candidate discovery therefore ended
at SEEK ALIGNMENT without a reviewable patch.
```

- [ ] **Step 2: Replace universal pre-implementation alignment with lane selection**

Replace existing-work check 7 with:

```markdown
7. Classify the candidate through the canonical contribution lane before source
   work. Prior maintainer direction is required for `SEEK ALIGNMENT`, not for a
   qualifying `PROCEED` direct-focused-PR slice. Opening that PR does not itself
   establish selection.
```

- [ ] **Step 3: Add a compact Lane selection section**

Insert before the waiting-path paragraph:

```markdown
## Lane selection

- `PROCEED`: use direct focused PR mode only when the gap is decisive, no active
  owner or competing work exists, the invariant/regression is clear, the change
  is internal or additive, no RFC/policy/permission/compatibility/architecture
  decision is needed, and focused validation is available. Write the failing
  regression first, implement the minimum patch, validate, and open the PR early.
- `CONTRIBUTE TO EXISTING WORK`: offer a distinct test, evidence, review, or
  author-approved commit; never compete or erase authorship.
- `SEEK ALIGNMENT`: ask for one bounded maintainer-owned decision before code.
- `STOP`: record the blocker and refresh trigger; do not keep investigating by
  default.

Prefer a strong `PROCEED` candidate over an equally strong alignment candidate
so learning converts into external proof. If a direct slice expands into policy,
architecture, unclear test intent, ownership conflict, or unavailable
validation, stop and reclassify it.
```

- [ ] **Step 4: Update Decision output and Common mistakes**

Keep the four existing output classifications. Require `PROCEED` output to name
`direct focused PR`, failing regression, bounded files, validation, and kill
condition. Add these common mistakes:

```markdown
- Treating lack of prior issue review as a blocker for every small,
  self-contained fix.
- Opening a direct PR when an adjacent active PR owns its prerequisite or source
  mechanism.
- Letting a direct slice expand into policy or architecture instead of
  reclassifying it.
```

- [ ] **Step 5: Run skill structure validation**

Run:

```bash
/opt/homebrew/bin/python3 \
  /Users/ritikagupta/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  /Users/ritikagupta/Desktop/open-source/.agents/skills/cua-contribution
```

Expected: validator exits 0 and reports the skill valid.

- [ ] **Step 6: Run the four scenario contract against the edited skill**

Read the lane section and verify each scenario has only one allowed result:

```text
A. Unowned bounded internal fix + deterministic regression + validation → PROCEED
B. Adjacent active PR owns mechanism → CONTRIBUTE TO EXISTING WORK
C. Public compatibility/default policy choice → SEEK ALIGNMENT
D. Credible owner with no distinct artifact → STOP
```

Run:

```bash
rg -n -C 3 'Lane selection|PROCEED|CONTRIBUTE TO EXISTING WORK|SEEK ALIGNMENT|STOP|lack of prior issue review|adjacent active PR' \
  .agents/skills/cua-contribution/SKILL.md
/usr/bin/git diff --check -- .agents/skills/cua-contribution/SKILL.md
```

Expected: each scenario maps unambiguously; diff check exits 0.

- [ ] **Step 7: Do not commit the root-workspace skill change**

The open-source root worktree contains unrelated state. Leave the narrow skill diff uncommitted and report it explicitly.

### Task 4: Synchronize live discovery and current state

**Files:**
- Modify: `cua-learning/CONTRIBUTION_DISCOVERY.md:9-58`
- Modify: `cua-learning/CURRENT.md:5-150`

**Interfaces:**
- Consumes: lane policy from Tasks 1–3 and the already inspected #2915/#3960 ownership state.
- Produces: resumable live state without activating a new issue or authorizing product implementation.

- [ ] **Step 1: Add the cache routing rule to CONTRIBUTION_DISCOVERY**

Add a short `## Lane preference` section before the current candidate table:

```markdown
After ownership and contribution-arc filtering, prefer one strong `PROCEED`
direct-focused-PR candidate over an equally strong candidate that can only wait
for alignment. The cache prevents repeated searches; it does not freeze a lane
when a recorded refresh trigger changes ownership, scope, or validation.
```

- [ ] **Step 2: Correct #3960's lane without changing its exclusion boundary**

Change #3960 from `SEEK ALIGNMENT` to `CONTRIBUTE TO EXISTING WORK / blocked as an independent PR` because active approved PR #3264 owns the adjacent completeness mechanism and same source path. Retain its refresh triggers and state that it may become a direct follow-up only after #3264 lands/closes or maintainers/author separate the slice.

- [ ] **Step 3: Update CURRENT to represent the policy checkpoint, not a candidate activation**

Make these bounded changes:

```text
desired movement: convert the active #2915 evidence into the correct lane and smallest reviewable artifact
human gate: policy correction approved; #2915 needs one refreshed lane check before source work
immediate next action: refresh #2915 exact/adjacent ownership, then test direct-lane predicates; if all hold, request human approval for the bounded implementation design
stop boundary: no Cua source or public action is authorized by the guideline change itself
```

Remove the stale statement that #3960 is the recommended replacement at `SEEK ALIGNMENT`. Keep #2915 active and preserve its evidence classifications and public-comment history.

- [ ] **Step 4: Keep CURRENT within its enforced limit**

Run:

```bash
/usr/bin/wc -l cua-learning/CURRENT.md
```

Expected: 150 lines or fewer, with exactly one primary engineering question.

- [ ] **Step 5: Validate the CUA learning workspace**

Run:

```bash
/opt/homebrew/bin/python3 cua-learning/tools/contextctl.py audit
/usr/bin/git -C cua-learning diff --check -- CONTRIBUTION_DISCOVERY.md CURRENT.md WORKFLOW.md
rg -n '^(<<<<<<<|=======|>>>>>>>)' \
  cua-learning/CONTRIBUTION_DISCOVERY.md \
  cua-learning/CURRENT.md \
  cua-learning/WORKFLOW.md
```

Expected: audit has no `FAIL`; diff check exits 0; merge-conflict search returns no matches.

- [ ] **Step 6: Preserve existing CUA-learning changes**

Do not commit `WORKFLOW.md` or `CURRENT.md`, which were already modified. Do not stage unrelated learning artifacts. Report `CONTRIBUTION_DISCOVERY.md` as the new task-owned file if it remains untracked.

### Task 5: Run the global checkpoint and final consistency review

**Files:**
- Possibly modify only files returned by `strategyctl.py due engineering-checkpoint`
- Inspect: all files from Tasks 1–4

**Interfaces:**
- Consumes: the completed policy, workflow, skill, and live-state changes.
- Produces: audited durable strategy and a final evidence-backed handoff.

- [ ] **Step 1: Ask the strategy control plane what this checkpoint requires**

Run:

```bash
/opt/homebrew/bin/python3 agent-infra-specialization/tools/strategyctl.py due engineering-checkpoint
```

Expected: a bounded list of files/checks. Read and update only the returned files; do not broaden into the whole strategy repository.

- [ ] **Step 2: Apply only required checkpoint synchronization**

If the command requires a durable strategy update beyond `CONTRIBUTION_FILTER.md`, use narrow `apply_patch` edits that state the same four lanes without duplicating their full predicates. If no additional file is due, make no additional edit.

- [ ] **Step 3: Run the global strategy audit**

Run:

```bash
/opt/homebrew/bin/python3 agent-infra-specialization/tools/strategyctl.py audit
```

Expected: no audit failures. Report any pre-existing warning separately rather than hiding it.

- [ ] **Step 4: Run final cross-file scenario consistency checks**

Run:

```bash
rg -n 'PROCEED|CONTRIBUTE TO EXISTING WORK|SEEK ALIGNMENT|STOP|direct focused PR|direct-focused-PR' \
  agent-infra-specialization/CONTRIBUTION_FILTER.md \
  cua-learning/WORKFLOW.md \
  .agents/skills/cua-contribution/SKILL.md \
  cua-learning/CONTRIBUTION_DISCOVERY.md \
  cua-learning/CURRENT.md
```

Manually verify:

```text
A → PROCEED; B → CONTRIBUTE TO EXISTING WORK; C → SEEK ALIGNMENT; D → STOP
```

Expected: no file reinstates universal pre-implementation maintainer approval; no file permits direct work through ownership, RFC, security, or validation blockers.

- [ ] **Step 5: Review the final diff against the approved spec**

Run:

```bash
/usr/bin/git -C agent-infra-specialization diff -- CONTRIBUTION_FILTER.md
/usr/bin/git -C cua-learning diff -- WORKFLOW.md CONTRIBUTION_DISCOVERY.md CURRENT.md
/usr/bin/git diff -- .agents/skills/cua-contribution/SKILL.md
```

Expected: only the approved lane strategy and live-state consequences are task-owned; unrelated pre-existing hunks remain untouched.

- [ ] **Step 6: Report completion without external publication**

The handoff must name modified files, validator/audit results, preserved dirty-worktree state, and the next human gate: refresh and classify #2915 under the corrected policy before any product implementation or public PR action.
