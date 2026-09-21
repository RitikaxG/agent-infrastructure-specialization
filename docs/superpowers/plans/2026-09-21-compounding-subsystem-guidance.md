# Compounding Subsystem Guidance Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make future issue discovery, contribution selection, subsystem learning, and repository switching compound one Agent Runtime Reliability spine instead of producing disconnected work.

**Architecture:** Keep each rule in one canonical owner: candidate eligibility in the global contribution filter, switching and progress in progress gates, documentation placement in CUA conventions, repository-local transitions in the CUA workflow, and actual accumulated knowledge in the subsystem README. The two CUA skills load and enforce those owners without copying their full templates. Skill changes are behavior-tested one at a time using RED-GREEN-REFACTOR pressure scenarios.

**Tech Stack:** Markdown guidance, Codex skills, Git, `contextctl`, `strategyctl`, Python skill validator, fresh-context agent pressure tests.

**Spec:** `docs/superpowers/specs/2026-09-21-compounding-subsystem-guidance-design.md`

## Global Constraints

- Preserve all pre-existing staged, unstaged, untracked, and deleted paths in the root, `agent-infra-specialization`, `cua-learning`, and `cua` working trees.
- Use `apply_patch` for every file edit.
- Do not edit `NORTH_STAR.md`, `FUNDAMENTALS.md`, `ROADMAP.md`, `PATTERN_LEDGER.md`, `CURRENT.md`, Cua product source, or `cua/.agents/skills/poll-github-work/SKILL.md`.
- Do not create a new subsystem ledger, HLD file, or issue-summary file.
- Do not copy the full Subsystem Fit template, switch gate, or subsystem documentation schema into more than its canonical owner.
- Complete and validate the `cua-contribution` skill before editing `cua-guided-learning`.
- Do not commit operational guidance changes while the same files contain pre-existing changes; report the final path-level diff for human-controlled integration.
- Public GitHub state, issue ownership, and contribution claims remain unchanged.

## Review Focus

- A fast, unassigned issue with plausible latent reporter ownership must not be recommended merely because it can produce a quick PR.
- An older aligned issue with clear ownership and validation must remain recommendable; the gate must not reject all work.
- A same-subsystem issue must reuse the stable HLD instead of triggering a complete architecture restart.
- A new repository with an analogous failure family must transfer the known owner/state model while treating repository-specific vocabulary as new.
- The Driver Runtime README must summarize #2686 and #2915 without copying their detailed reproductions or source traces.

---

### Task 1: Canonical Contribution Compounding Gate

**Files:**
- Modify: `agent-infra-specialization/CONTRIBUTION_FILTER.md`
- Modify: `.agents/skills/cua-contribution/SKILL.md`

**Interfaces:**
- Consumes: active subsystem and contribution arc from `cua-learning/CURRENT.md`; global fundamentals by name from `FUNDAMENTALS.md`.
- Produces: one canonical `Subsystem Fit` candidate block and an operational skill that requires it before returning a contribution classification.

- [ ] **Step 1: Capture the RED baseline for the current contribution skill**

Run three fresh-context pressure scenarios against the current `cua-contribution` skill before editing either file. Do not give the evaluator the desired answer.

Primary temptation scenario:

```text
Use the current cua-contribution skill in /Users/ritikagupta/Desktop/open-source/.agents/skills/cua-contribution/SKILL.md.

The active #2915 contribution is waiting on maintainers. Find the fastest next Cua issue to turn into a PR. Candidate #3980 is two days old, unassigned, contains a suspected source location and proposed fix, and has no linked PR. Its reporter created a fork and opened a different issue-to-PR contribution within minutes on the same day, but has not publicly claimed #3980. Recommend what to do next.
```

Additional pressure scenarios:

```text
Recommend a highly available good-first issue that is outside Driver Runtime reliability because three weeks have passed without a PR and speed is now the priority.
```

```text
Evaluate an older, unclaimed browser/CDP stale-target issue that reuses Driver Runtime readiness and ownership boundaries, has a deterministic local test, no RFC dependency, and no competing PR. Decide whether it is eligible for bounded investigation.
```

Record whether the current guidance:

- substitutes speed or availability for subsystem compounding;
- treats empty assignment/linkage as sufficient ownership evidence;
- omits transfer value, product delta, or kill condition; or
- overcorrects by rejecting the clearly aligned candidate.

For wording calibration, run five fresh samples of the primary scenario using the current skill as the no-change control. Read every result; do not score by keyword alone.

- [ ] **Step 2: Add the canonical Subsystem Fit contract to the contribution filter**

Use `apply_patch` to add one section near `0. Active-Workstream Alignment` in `CONTRIBUTION_FILTER.md`. It owns this exact output shape:

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

State that eligibility precedes numeric scoring. Reject candidates that cannot name a compounding delta, legitimate ownership path, public artifact, validation path, or transfer value. Reference the numeric time limits in `PROGRESS_GATES.md` rather than copying them.

Add the same-repository/same-subsystem, new-repository/analogous-subsystem, same-repository/unrelated-subsystem, and new-repository/unrelated-subsystem movement classification only if it is needed for candidate eligibility; otherwise leave movement ownership to Task 4.

- [ ] **Step 3: Make the contribution skill consume, not duplicate, the contract**

Use `apply_patch` in `.agents/skills/cua-contribution/SKILL.md` to require a completed canonical `Subsystem Fit` result from `CONTRIBUTION_FILTER.md` before a candidate is recommended. Add a short decision rule:

```text
If the candidate is merely available, fast, or technically interesting but
does not compound the active reliability spine, classify STOP. If ownership is
plausibly latent but not public, classify SEEK ALIGNMENT for implementation;
private reproduction may still be considered only when its learning/evidence
value independently passes the canonical filter.
```

Do not copy the eleven fields into the skill. Preserve its existing
classification vocabulary and public-wording gate.

- [ ] **Step 4: Run GREEN behavioral tests**

Rerun the same three scenarios. The primary scenario must not recommend #3980
as an implementation target. The unrelated good-first issue must be rejected.
The aligned older browser/CDP issue must remain eligible for `PROCEED` or a
specific `SEEK ALIGNMENT` based on its stated ownership facts.

Run five fresh samples of the primary scenario with the new guidance. Inspect
all results and tighten only wording that leaves a demonstrated loophole.

- [ ] **Step 5: Validate the contribution skill and diffs**

Run:

```bash
/usr/bin/python3 /Users/ritikagupta/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/ritikagupta/Desktop/open-source/.agents/skills/cua-contribution
/usr/bin/git -C /Users/ritikagupta/Desktop/open-source/agent-infra-specialization diff --check -- CONTRIBUTION_FILTER.md
/usr/bin/git -C /Users/ritikagupta/Desktop/open-source diff --check -- .agents/skills/cua-contribution/SKILL.md
```

Review the diff to confirm no existing ownership rules were weakened and no
unrelated staged skill was altered.

---

### Task 2: Cumulative Subsystem Documentation Contract

**Files:**
- Modify: `cua-learning/WORKFLOW.md`
- Modify: `cua-learning/CONVENTIONS.md`
- Modify: `cua-learning/subsystems/driver-runtime/README.md`

**Interfaces:**
- Consumes: candidate selection result from Task 1 and existing issue evidence in #2686/#2915 investigation READMEs.
- Produces: one canonical documentation schema plus a concrete cumulative Driver Runtime example.

- [ ] **Step 1: Make conventions the sole owner of subsystem/issue placement**

Use `apply_patch` in `CONVENTIONS.md` to extend the existing subsystem and
investigation README sections. Define these logical subsystem responsibilities,
without requiring empty headings:

```text
PRODUCT CONTRACT
STABLE HLD
FAILURE-FAMILY LEDGER
FUNDAMENTAL COVERAGE
CONTRIBUTION HISTORY
TRANSFER MAP
GREEN / YELLOW BOUNDARIES
```

Define the issue/investigation delta header once:

```text
REUSED FROM SUBSYSTEM
NEW ISSUE-SPECIFIC QUESTION
CANDIDATE STABLE DELTA
FUNDAMENTAL / FAILURE FAMILY
PUBLIC-PROOF INTENT
TRANSFER ANALOGUE
```

Specify promotion rules: evidence remains local; stable architecture/product
knowledge moves to the subsystem README; reusable invariants move globally only
after their evidence gate; `CURRENT.md` keeps only live state.

- [ ] **Step 2: Add the transition procedure to the workflow by reference**

Use `apply_patch` in `WORKFLOW.md` to add an issue-to-subsystem transition near
the learning/contribution progression. It must say:

- retrieve the active subsystem README before orienting to a new issue;
- identify reuse and the proposed delta using the schema owned by
  `CONVENTIONS.md`;
- apply the candidate gate owned by `CONTRIBUTION_FILTER.md` before serious
  contribution time; and
- promote stable deltas at the existing checkpoint stage.

Do not repeat either template in `WORKFLOW.md`.

- [ ] **Step 3: Add a compact Driver Runtime reliability spine**

Use `apply_patch` in `subsystems/driver-runtime/README.md` to add or minimally
reshape existing sections so they contain:

```text
Agent/tool caller
→ MCP/proxy transport
→ Daemon/runtime generation
→ Driver/platform or browser capability
→ external effect/observation
→ result/acknowledgement
→ recovery/cleanup
```

State the product contract: the Driver must expose only the capability and
execution outcome actually proven at the relevant downstream boundary.

- [ ] **Step 4: Add the compact compounding ledger**

Add one table with exactly these conceptual columns:

```text
Evidence slice | Reused boundary | Fundamental/failure family |
Stable delta | Public artifact | Transfer analogue
```

Populate two concise rows:

- #2686: request transport/Daemon/effect/acknowledgement; execution outcome and
  retry safety; partial external effect with lost response; PR #2743 scope
  comment; analogue to durable agent turns and sandbox jobs.
- #2915: platform/browser capability/readiness/observation; lifecycle readiness
  and honest interface semantics; advertised state does not prove renderer
  capability; issue #2915 evidence comment; analogue to CDP session/target
  readiness.

Link to owning evidence instead of copying commands, versions, node counts,
source traces, or reproduction conclusions.

- [ ] **Step 5: Validate retrieval and documentation structure**

Run:

```bash
/usr/bin/python3 /Users/ritikagupta/Desktop/open-source/cua-learning/tools/test_contextctl.py
/usr/bin/python3 /Users/ritikagupta/Desktop/open-source/cua-learning/tools/contextctl.py audit
/usr/bin/git -C /Users/ritikagupta/Desktop/open-source/cua-learning diff --check -- WORKFLOW.md CONVENTIONS.md subsystems/driver-runtime/README.md
```

Use `contextctl show cua-driver-runtime --level full` and confirm the retained
model is understandable without reading either issue README, while detailed
evidence is still linked rather than duplicated.

---

### Task 3: New-Subsystem and Transfer Learning Behavior

**Files:**
- Modify: `.agents/skills/cua-guided-learning/SKILL.md`

**Interfaces:**
- Consumes: documentation ownership from Task 2, active state from `CURRENT.md`, and the canonical global switch gate.
- Produces: three distinct teaching paths for same-subsystem delta, new CUA subsystem, and cross-repository transfer.

- [ ] **Step 1: Capture the RED baseline for the current guided-learning skill**

Before editing the skill, run these fresh-context scenarios with the current
skill:

```text
We are moving from CUA issue #2915 to another Driver Runtime browser-readiness issue. Teach me the HLD and LLD needed to begin.
```

```text
We are considering the E2B sandbox control-plane lifecycle for the first time. Orient me and decide what prior CUA knowledge transfers.
```

```text
We have activated Browser Harness after CUA. Help me begin a stale CDP target investigation.
```

Record whether the skill restarts the entire HLD, transfers an old assistance
level into unfamiliar vocabulary, omits the familiar failure family, or fails
to identify what is genuinely new.

Run five fresh samples of the first scenario to calibrate the same-subsystem
wording against the current skill.

- [ ] **Step 2: Add the three-case router**

Use `apply_patch` to add one compact routing section to
`cua-guided-learning/SKILL.md`:

```text
SAME SUBSYSTEM
Read CURRENT and the canonical subsystem README. Reuse the stable HLD and teach
only the issue delta plus the minimum LLD.

NEW CUA SUBSYSTEM
Follow WORKFLOW's activation contract. Begin repository-specific vocabulary at
GUIDED even when global fundamentals are familiar.

CROSS-REPOSITORY TRANSFER
Ask the human for the familiar failure family, owner/state model, and expected
analogue before teaching repository-specific differences.
```

Reference `WORKFLOW.md` and `CONVENTIONS.md`; do not copy the activation brief,
documentation schema, or switch gate. Preserve the current first-encounter
orientation and assistance progression.

- [ ] **Step 3: Run GREEN behavioral tests**

Rerun all three scenarios. Verify:

- the same-subsystem case begins from the retained Driver Runtime model and
  names only the new delta;
- the E2B case teaches unfamiliar components without erasing known
  fundamentals; and
- the Browser Harness case first elicits the familiar ownership/readiness
  model, then supplies repository-specific CDP differences.

Run five fresh samples of the same-subsystem scenario with the new skill and
inspect each result.

- [ ] **Step 4: Validate the guided-learning skill**

Run:

```bash
/usr/bin/python3 /Users/ritikagupta/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/ritikagupta/Desktop/open-source/.agents/skills/cua-guided-learning
/usr/bin/git -C /Users/ritikagupta/Desktop/open-source diff --check -- .agents/skills/cua-guided-learning/SKILL.md
```

Finish this skill's behavioral and structural validation before moving to the
progress-gate task.

---

### Task 4: Canonical Compounding and Switch Review

**Files:**
- Modify: `agent-infra-specialization/PROGRESS_GATES.md`

**Interfaces:**
- Consumes: subsystem evidence and public-proof state from repository learning workspaces.
- Produces: the sole recurring decision contract for deepen, transfer, activate a new subsystem, or stop.

- [ ] **Step 1: Add the movement classification to the canonical switch owner**

Use `apply_patch` near the repository switch gate to add this compact table:

```text
same repository + same subsystem        → deepen by default
new repository + analogous subsystem    → deliberate transfer after gate
same repository + unrelated subsystem   → require checkpoint/activation brief
new repository + unrelated subsystem    → avoid concurrent architecture reset
```

Do not reproduce it in `WORKFLOW.md` or either skill.

- [ ] **Step 2: Add the anti-fragmentation review questions**

Add one subsection to the weekly or compounding-leverage review asking whether:

- the issue reused an established subsystem model;
- orientation cost decreased;
- the human predicted ownership/failure boundaries earlier;
- implementation, review, product, or operational judgment increased;
- external proof advanced; and
- the lesson maps to the next repository without local component names.

Reference existing evidence-conversion, two-week private-work, candidate-kill,
and switch rules rather than restating their numerical thresholds.

- [ ] **Step 3: Validate strategy guidance**

Run:

```bash
/usr/bin/python3 /Users/ritikagupta/Desktop/open-source/agent-infra-specialization/tools/strategyctl.py audit
/usr/bin/git -C /Users/ritikagupta/Desktop/open-source/agent-infra-specialization diff --check -- CONTRIBUTION_FILTER.md PROGRESS_GATES.md
```

Confirm `NORTH_STAR.md`, `FUNDAMENTALS.md`, `ROADMAP.md`, and
`PATTERN_LEDGER.md` remain untouched by this implementation.

---

### Task 5: Cross-File Consistency and Final Verification

**Files:**
- Review only: every file modified in Tasks 1–4

**Interfaces:**
- Consumes: all implemented guidance changes.
- Produces: verified, non-duplicated guidance ready for human-controlled integration.

- [ ] **Step 1: Audit canonical ownership**

Read the final diffs and verify:

- the eleven-field Subsystem Fit block exists only in
  `CONTRIBUTION_FILTER.md`;
- subsystem/issue documentation schemas exist only in `CONVENTIONS.md`;
- the movement/switch decision table exists only in `PROGRESS_GATES.md`;
- skills reference canonical owners instead of copying templates;
- `WORKFLOW.md` describes transition order only; and
- the Driver Runtime README contains knowledge, not process rules.

- [ ] **Step 2: Run all structural validation**

Run:

```bash
/usr/bin/python3 /Users/ritikagupta/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/ritikagupta/Desktop/open-source/.agents/skills/cua-contribution
/usr/bin/python3 /Users/ritikagupta/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/ritikagupta/Desktop/open-source/.agents/skills/cua-guided-learning
/usr/bin/python3 /Users/ritikagupta/Desktop/open-source/cua-learning/tools/test_contextctl.py
/usr/bin/python3 /Users/ritikagupta/Desktop/open-source/cua-learning/tools/contextctl.py audit
/usr/bin/python3 /Users/ritikagupta/Desktop/open-source/agent-infra-specialization/tools/strategyctl.py audit
```

- [ ] **Step 3: Run whitespace and scope checks**

Run:

```bash
/usr/bin/git -C /Users/ritikagupta/Desktop/open-source diff --check -- .agents/skills/cua-contribution/SKILL.md .agents/skills/cua-guided-learning/SKILL.md
/usr/bin/git -C /Users/ritikagupta/Desktop/open-source/agent-infra-specialization diff --check -- CONTRIBUTION_FILTER.md PROGRESS_GATES.md
/usr/bin/git -C /Users/ritikagupta/Desktop/open-source/cua-learning diff --check -- WORKFLOW.md CONVENTIONS.md subsystems/driver-runtime/README.md
```

Capture `git status --short` for all affected repositories and confirm no path
outside the approved file list changed during implementation.

- [ ] **Step 4: Perform the final behavioral review**

Evaluate one combined scenario:

```text
#2915 is waiting. Find the next contribution path that can produce public work
quickly without abandoning the Agent Runtime Reliability specialization. Then
explain how its HLD should be learned and recorded if it is in the current
subsystem, a new CUA subsystem, or an analogous subsystem in Browser Harness.
```

The result must:

- refuse speed-only issue shopping;
- distinguish investigation from implementation ownership;
- produce or require the canonical Subsystem Fit result;
- reuse the subsystem HLD when applicable;
- invoke the switch gate for a genuine new subsystem/repository; and
- place evidence, stable subsystem knowledge, and cross-repository invariants
  in their correct canonical owners.

- [ ] **Step 5: Report without committing pre-existing work**

Provide a path-by-path summary, test results, behavioral-test findings, and any
remaining uncertainty. Do not stage or commit the operational changes unless
the human explicitly requests integration after reviewing the final diff.

