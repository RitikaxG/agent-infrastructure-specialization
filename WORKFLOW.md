# Agent Infrastructure Specialization — Workflow

This file defines **how this specialization workspace is operated and maintained**.

It does not own the six-month goal, current roadmap, contribution-selection criteria, discovered patterns, or interview evidence. Those responsibilities belong to the files listed below.

---

## 1. Source-of-Truth Hierarchy

Use the files in this order depending on the question being answered:

- `NORTH_STAR.md` — **Why / destination**
- `AGENTS.md` — **How Codex orchestrates routine workflow transitions**
- `WORKFLOW.md` — **How the specialization workspace operates**
- `ROADMAP.md` — **Which repository/subsystem is active and what comes next**
- `CONTRIBUTION_FILTER.md` — **What deserves serious engineering time**
- `PATTERN_LEDGER.md` — **What generalizes across systems**
- `INTERVIEW_EVIDENCE.md` — **What I can prove I actually did**

Repository-specific workspaces such as `cua-learning/` own detailed investigation state: code paths, hypotheses, tests, failures, diagrams, and the **exact active engineering question**.

Do not duplicate detailed repository investigation notes into this repository. Promote only durable conclusions.

### Exact-question ownership

The global roadmap should remain stable at the repository/subsystem level.

For example:

```text
ROADMAP.md
→ active repository: CUA
→ active subsystem: daemon / runtime lifecycle

cua-learning/CURRENT.md
→ exact current engineering question
→ current stopping boundary inside that investigation
```

Do not copy every short-lived repository question into `ROADMAP.md`.

---

## 2. One Active Workstream

At any time there must be exactly:

- **one active repository**
- **one active subsystem**
- **one primary engineering question**

I do not work effectively across multiple repositories simultaneously.

Other repositories may be briefly inspected for comparison or recorded as future candidates, but they do not become active workstreams.

A new issue, release, hiring post, Discord discussion, or interesting repository is not by itself a reason to switch.

### Repository-switch rule

Switch only when one of these is true:

1. the active subsystem has reached the stopping boundary in `ROADMAP.md`;
2. meaningful contribution opportunities are exhausted after serious investigation;
3. maintainers indicate the intended direction is not useful or feasible; or
4. evidence shows another subsystem is the natural continuation of the same specialization thread.

Do not switch because of novelty, temporary difficulty, an easier issue elsewhere, or a desire to collect repository logos.

---

## 3. What Each Global File Owns

### `NORTH_STAR.md`

Owns the long-term specialization goal and definition of success.

Update only when the six-month objective, intended specialization, or overall build direction materially changes.

It should change rarely.

### `AGENTS.md`

Owns Codex's global orchestration behavior:

- fresh-session routing;
- routine workflow-mode transitions;
- when global strategy should be consulted;
- autonomous checkpoint routing;
- human approval gates;
- promotion from repository-specific evidence into global artifacts.

It should not duplicate repository-specific source paths or experiment details.

### `ROADMAP.md`

Owns:

- active repository;
- active subsystem;
- subsystem-level objective;
- global stopping boundary;
- next likely subsystem;
- future candidates worth remembering.

The exact active engineering question belongs to the active repository's `CURRENT.md`.

Update `ROADMAP.md` when the active subsystem changes, its stopping boundary is reached, or a future candidate should be recorded.

### `CONTRIBUTION_FILTER.md`

Owns the reusable criteria for deciding whether a subsystem, issue, investigation, or PR deserves significant time.

Do not store specific issue backlogs here. The rules should survive individual issues being opened and closed.

Update only when real experience reveals a better selection rule.

### `PATTERN_LEDGER.md`

Owns generalized engineering invariants and repeated failure patterns.

Organize by **invariant/failure class**, not by repository.

Only work I have personally investigated should be recorded as evidence. Uninvestigated cross-repo examples must be labeled as **comparison candidates**, not evidence.

### `INTERVIEW_EVIDENCE.md`

Owns evidence from work I have actually performed.

Do not pre-fill hypothetical achievements or infer contributions.

Capture interview-worthy investigations while they are fresh: problem, HLD, lifecycle, relevant LLD, reproduction, invariant, root cause or corrected assumption, alternatives, chosen design/conclusion, tests, maintainer feedback, result, and follow-up questions.

---

## 4. Fresh Session Startup

A fresh ChatGPT/Codex session should first establish:

1. the North Star;
2. the active repository;
3. the active subsystem;
4. the global stopping boundary;
5. the exact current engineering question from the active repository workspace.

Then read the active repository's `CURRENT.md` and only the subsystem/investigation material required for the current work.

Do **not** reload every global file for every coding step.

Read the global strategy files when making a strategic decision such as:

- choosing a subsystem;
- choosing or seriously evaluating an issue/PR;
- deciding whether to switch repositories;
- promoting a failure into a reusable pattern;
- deciding whether repeated observations justify tooling;
- reviewing overall progress.

Codex should follow `AGENTS.md` to make these routing decisions proactively rather than waiting for the human to request each transition.

---

## 5. Workflow Transition Ownership

Routine transitions are orchestration work, not something the human should have to micromanage.

Codex should proactively decide when to:

- continue explanation;
- ask the human to explain a model back;
- inspect the minimum relevant source;
- stop source inspection because further reading has diminishing value;
- design an experiment;
- require a prediction before a break;
- run the experiment or hand one command at a time to the human;
- checkpoint durable learning;
- inspect issue/PR/design history;
- begin systematic debugging;
- move from root cause into design alternatives;
- move from approved design into implementation/verification;
- extract transferable patterns or interview evidence.

The human still owns actual understanding, important predictions, architecture choices, contribution commitment, and approval of meaningful implementation direction.

---

## 6. Investigation → Update Routing

After a meaningful investigation, update only the files whose responsibility actually changed.

### Repository-specific understanding changed

Update the active repository workspace:

- `CURRENT.md`;
- subsystem note;
- investigation/failure notes;
- durable diagrams if useful.

Codex may do this autonomously at natural checkpoints. A separate handoff prompt is not required merely to keep routine state current.

### A reusable invariant emerged

Update `PATTERN_LEDGER.md`.

Do not promote a guess. Record evidence from the real investigation and mark untested comparisons as candidates.

### The work became interview evidence

Update `INTERVIEW_EVIDENCE.md`.

Only include work I actually performed and can defend technically.

### Active/next subsystem changed

Update `ROADMAP.md`.

### Experience changed how work should be selected

Update `CONTRIBUTION_FILTER.md`.

### The six-month objective itself changed

Only then update `NORTH_STAR.md`.

---

## 7. Knowledge Promotion Path

Knowledge should move upward through evidence, not through speculation:

```text
raw investigation
        ↓
repo-specific subsystem understanding
        ↓
real failure / issue / contribution
        ↓
generalized invariant
        ↓
cross-repository confirmation
        ↓
reusable failure scenario
        ↓
automated failure-testing primitive
        ↓
future runtime/harness design
```

Do not jump from reading code directly to building a generic library or framework.

The connected engineering model should remain:

```text
HLD
 ↓
lifecycle / data flow
 ↓
relevant LLD
 ↓
failure
 ↓
invariant
 ↓
root cause / corrected assumption
 ↓
design alternatives
 ↓
fix / experiment
 ↓
regression proof
 ↓
reusable lesson
```

---

## 8. Issue / PR Discovery Gate

Do not search for upstream work merely because something looks strange.

Before issue/PR discovery becomes the main activity, establish enough repository-specific understanding to answer:

- what behavior is expected;
- what behavior is actually observed/source-established;
- where the relevant failure/design boundary is;
- which active subsystem question this work advances.

Then read `ROADMAP.md` and apply `CONTRIBUTION_FILTER.md` before committing serious time.

An interesting but misaligned issue should normally be recorded as a future candidate rather than turning into a second active workstream.

---

## 9. Failure-Suite Promotion Rule

Failure-suite development happens **alongside real repository work**, but it must not become a second active project.

When a useful failure is discovered:

1. reproduce it in the real system;
2. understand the violated invariant;
3. investigate/fix/contribute where appropriate;
4. record the generalized failure scenario;
5. look for the same failure class when later working in another system;
6. only after repeated evidence, extract reusable automation.

A failure scenario can begin as documentation. Generic code is justified only when the pattern has repeated enough to support an abstraction.

The eventual failure lab and agent runtime/harness must be **evidence-derived**, not designed in advance from assumptions.

---

## 10. Periodic Strategy Review

Approximately every 3–4 weeks, review the specialization as a whole:

- Am I still going deep rather than hopping?
- Has understanding turned into failure reproduction or engineering evidence?
- Have investigations turned into useful maintainer-visible contributions?
- Are repeated invariants emerging across systems?
- Is interview evidence accumulating from real work?
- Am I documenting too much instead of investigating?
- Am I trying to abstract before enough repetition exists?

Do not reorganize the workspace unless the current structure is actually blocking the work.

---

## Primary Operating Principle

The goal is not to learn CUA, OpenHands, Browser Use, and E2B as four disconnected repositories.

The goal is to understand how durable agent-execution systems are designed, how important subsystem boundaries fail, how those failures are reproduced and prevented, and which invariants transfer across implementations.

The repositories are evidence sources for that connected engineering model.
