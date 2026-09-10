# Agent Runtime Reliability — Progress Gates

This file answers four recurring questions:

- Am I actually becoming more independent?
- Is private understanding turning into external proof?
- What must happen by the end of a day/week/month?
- If I finish a checkpoint early, what should I deepen next?

## 1. Assistance Modes

Track assistance separately for:

- vocabulary / concepts;
- HLD reconstruction;
- LLD/source navigation;
- failure reasoning;
- test design;
- contribution/design decisions.

### GUIDED

Codex/ChatGPT may teach the term, locate the component, show the healthy path,
propose likely failure boundaries, identify nearby tests, and explain unfamiliar
language syntax.

The human must still connect the explanation to the real system and explain the
important relationship back in simple terms.

### SHARED

The human reconstructs part of the model or prediction first. AI verifies,
corrects, locates exact source, and offers alternatives where needed.

### USER-LED

The human originates the engineering question, HLD hypothesis, failure scenario,
invariant, or test intent. AI mainly gathers evidence, checks assumptions,
translates unfamiliar syntax, and accelerates implementation.

### TRANSFER

In a new or adjacent system, the human recognizes the familiar failure family,
forms the first architecture/failure questions, and uses AI primarily to verify
repository-specific details.

Using AI is not failure. **Unchanged ownership of the reasoning for months is.**

## 2. External Proof Ladder

Every active investigation should know its current stage:

```text
0  PRIVATE ORIENTATION
1  COHERENT SUBSYSTEM MODEL
2  USEFUL FAILURE REPRODUCTION / TECHNICAL EVIDENCE
3  CONTRIBUTION CANDIDATE OR EXISTING ISSUE MATCHED
4  MAINTAINER-VISIBLE EVIDENCE / DISCUSSION
5  REGRESSION TEST OR APPROVED DESIGN DIRECTION
6  PR OPEN
7  MAINTAINER REVIEW CYCLE
8  MERGED / ACCEPTED UPSTREAM RESULT
9  FOLLOW-UP CONTRIBUTION / REPEATED RECOGNITION
```

Do not inflate the stage. A private draft is not maintainer-visible. A PR opened
without review is not a review cycle. A reproduction can be valuable even if no
bug is ultimately confirmed.

## 3. Start-of-Day Gate

Before substantive work, produce a compact `DAY START BRIEF`:

```text
Current position
- repository / subsystem / exact question
- current proof stage
- current assistance levels

Fundamental being hardened
- one primary fundamental
- optional one secondary fundamental

Recall/orientation gate
- GUIDED: AI supplies the skeleton, human explains key relationships
- SHARED: human reconstructs the current HLD/failure first
- USER-LED/TRANSFER: human proposes the first model/question

Today's external movement
- current proof stage → desired next stage
- concrete artifact/evidence expected

Engineering scope
- one question
- minimum HLD/LLD slice
- one evidence-producing action

Stopping boundary
- what makes today enough
- what must not start yet
```

A normal day should not begin with `continue exploring the repo`.

## 4. End-of-Day Consolidation

Before a substantial day ends, close or ignore AI-generated prose and test human
understanding for 5–15 minutes.

Use 3–5 reasoning questions, not source-code trivia. Rotate among:

- redraw the relevant HLD from memory;
- explain ownership/state in plain language;
- trace the active request through the important LLD landmarks;
- explain why the observed failure happened;
- predict one nearby failure variation;
- state the invariant;
- say what the regression test must prove;
- explain which conclusion is observed, source-verified, inferred, or still
  unknown.

Record in the active repository `CURRENT.md`:

```text
What I can now explain unaided:
What still needs AI scaffolding:
Fundamental hardened today:
External proof movement:
Next exact engineering question:
Stopping boundary:
```

Do not turn this into memorizing function names. Retain the system model and
important implementation landmarks.

## 5. Weekly Checkpoint

At the start of each week, set one sentence:

> By the end of this week, move the active work from Proof Stage X to Y while
> improving one named independence dimension.

At week end, revise the same active engineering story through five lenses:

### HLD revision

Without notes, redraw the minimum subsystem architecture and answer:

- components and responsibilities;
- ownership;
- durable vs ephemeral state;
- lifecycle;
- failure/recovery boundaries.

Then compare against durable notes and correct only material gaps.

### LLD revision

Trace one real operation through the 3–7 important implementation landmarks:
entry → transport → state → effect → result/error → recovery/cleanup → tests.

Do not reread the whole source tree.

### Failure revision

Re-explain every important failure reproduced that week:

```text
healthy baseline
→ break introduced
→ exact observation
→ what survived / disappeared
→ explanation
→ what remains unknown
```

Then predict one variation that has not been tested. Only run it if it advances
the active question or contribution.

### Bug / contribution revision

Answer:

- What is the real problem, if any?
- What invariant matters?
- Is it expected behavior, trade-off, test gap, bug, or design improvement?
- What evidence would a maintainer need?
- What is the smallest defensible contribution?

### PR / maintainer revision

For active public work, review:

- issue/discussion state;
- maintainer feedback and what changed in my model;
- current PR/review status;
- unaddressed review comments;
- next useful action that deepens the same relationship.

Do not comment merely to remain visible.

## 6. Weekly Scorecard

Score each dimension `0 / 1 / 2`:

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| HLD | cannot reconstruct | partial | explainable unaided |
| LLD | depends on AI summary | recognize landmarks | can trace/debug relevant path |
| Failure reasoning | repeats explanation | explains known case | predicts nearby variation |
| Test judgment | AI owns intent | shared | human states invariant + test intent |
| External proof | unchanged | prepared | visibly advanced |
| Maintainer relationship | none | one useful interaction | repeated substantive interaction |
| Transferability | isolated fact | maps to fundamental | recognizes reusable pattern |
| Independence | no ownership shift | one small shift | clear responsibility moved human-ward |

Maximum: 16.

Interpretation:

- **13–16:** strong week; keep the same direction unless the switch gate is met.
- **9–12:** useful week; identify the weakest dimension and correct next week.
- **0–8:** drift; do not continue unchanged without diagnosing why.

A week cannot score strongly through note-taking alone.

## 7. If the Weekly Checkpoint Finishes Early

Do **not** automatically start another repository or broad subsystem.

Use remaining focused time in this priority order:

1. respond to maintainer/review feedback on the active contribution;
2. strengthen or simplify the regression/reproduction;
3. reproduce one adjacent failure that tests the same invariant;
4. inspect one nearby existing issue/PR in the same subsystem for a natural
   follow-up contribution;
5. perform a no-notes HLD/LLD/failure explanation and targeted retention drill;
6. improve observability or cleanup evidence for the same engineering story;
7. write the public/technical story only after the engineering result is mature;
8. move to the next planned subsystem only if the repository switch gate is
   actually satisfied.

Finishing a weekly checkbox early is not permission to broaden.

## 8. Monthly Checkpoint

At month end, review outcomes rather than hours.

Required questions:

- What external artifact can another engineer inspect?
- Which maintainer(s) have seen my work and in what technical context?
- Which fundamental became materially stronger?
- Which HLD/LLD can I now reconstruct unaided?
- Which failure families can I recognize without being prompted?
- What test intent did I originate myself?
- Did at least one AI-owned responsibility move toward SHARED/USER-LED?
- What interview-quality engineering story exists now?
- Should the current repo/subsystem continue, switch, or be abandoned?

### If the monthly goal finishes early

Prefer depth before breadth:

1. complete follow-up review/merge work;
2. take one adjacent, related contribution in the same anchor subsystem if it is
   genuinely valuable;
3. confirm one important invariant under another scenario;
4. create the technical article/interview story from earned evidence;
5. begin the next roadmap block only after the switch gate passes.

Do not spend the remaining month farming easier PRs.

## 9. Course-Correction / Kill Rules

### Evidence-conversion rule

After at most two focused sessions dominated by source/docs orientation, the next
meaningful session must produce a prediction, explain-back, experiment,
reproduction, test, issue/PR analysis, or design decision.

### Weekly drift rule

If a full week advances neither external proof nor human independence, diagnose
and change the next week's approach before continuing.

### Two-week private-work rule

Two consecutive weeks may not end with only private understanding. If they do,
rescore the contribution candidate and choose one of:

- different failure/issue in the same subsystem;
- narrower PR-shaped scope;
- maintainer clarification;
- switch if contribution surface/relationship viability has genuinely failed.

### Candidate kill rule

After roughly 7–10 focused days on one contribution candidate, stop investing if
there is still no credible combination of reproduction, invariant, PR-sized
scope, maintainer/project relevance, or externally useful artifact.

Do not confuse sunk cost with depth.

## 10. Repository Switch Gate

Do not switch simply because the subsystem feels understood.

Switch when all are true, or an explicit escape hatch applies:

```text
UNDERSTANDING
HLD + relevant LLD + important invariant are defensible

EXTERNAL PROOF
maintainer-visible reproduction/discussion/PR/review/merge exists

TRANSFER
the reusable lesson is recorded and relation to the next layer is understood

DIRECTION
remaining work is lower value than the planned next layer
```

Escape hatch: after strong reproduction, appropriate outreach, and a second
aligned contribution surface still produce no meaningful maintainer path, keep
the evidence and move rather than sacrificing the roadmap to silence.

## 11. Three-Month and Six-Month Tests

### Around Month 3

Target:

- one deep anchor subsystem story;
- serious upstream contribution/review evidence;
- second-runtime transfer underway;
- one invariant recognized in more than one system or a strong candidate for
  such transfer;
- clear movement from GUIDED toward SHARED/USER-LED in HLD/failure/test intent.

### Around Month 6

Target:

- 3–5 substantial reviewed/merged PRs if upstream circumstances allow;
- repeated contribution recognition in the anchor community;
- meaningful maintainer relationships in at least 2 communities;
- multiple production-shaped failure stories;
- HLD/LLD reconstruction and test intent increasingly human-led;
- 2–3 reusable invariants with cross-system evidence where possible;
- Agent Runtime Failure Lab v0.1 derived from real investigations;
- technical writing and interview narratives grounded in actual upstream work.

## 12. Throughput and Leverage

Do not use working hours, number of tabs, number of AI calls, or number of tasks
as the primary productivity metric.

The long-term productivity goal is to reduce the cycle time for one serious
engineering story:

```text
question
→ compact system model
→ relevant source path
→ failure evidence
→ invariant / test intent
→ maintainer-visible artifact
→ review / merge
```

### Output-density rule

A strong focused day may produce only one substantial result: a corrected HLD,
a deterministic reproduction, a regression design, a maintainer-facing problem
statement, a review response, or a focused patch. Prefer one result that moves
proof or judgment over many disconnected tasks.

A 10–12 hour day with no proof movement or independence gain is not automatically
more productive than a 5–6 focused-hour day that advances the engineering story.

### Orientation-tax rule

Track whether time is repeatedly spent relearning a concept or rediscovering the
same source/test path.

If the same orientation cost recurs across two or more sessions:

1. do a no-notes recall first;
2. identify the smallest missing mental model or landmark;
3. repair the compact durable note/diagram only if retrieval is genuinely poor;
4. avoid broad rereading;
5. automate mechanical rediscovery when appropriate.

The expected trend over months is:

```text
less time finding/remembering familiar boundaries
+
more time reproducing, testing, designing, reviewing, and contributing
```

### AI-leverage rule

Once the human understands the intent and important invariant, Codex should take
more of the mechanical load where useful: repository search, exact symbol
location, repetitive setup, test execution, log comparison, syntax translation,
and implementation scaffolding.

Do not make the human manually repeat work that teaches nothing new merely to
prove independence. Independence means owning the engineering judgment, not
refusing leverage.

### Compounding-leverage review

At each monthly checkpoint ask:

- Which task that took hours last month is now faster, and why?
- Which agent-infra question now occurs to me automatically?
- Which source/test workflow is now familiar enough to delegate mechanically?
- Where am I still repeatedly paying orientation cost?
- Did faster execution come from stronger mental models and reusable process, or
  only from asking AI to do more thinking for me?

If cycle time is not improving after repeated exposure to the same subsystem or
failure family, diagnose the bottleneck: weak retention, unclear HLD, excessive
source scope, poor test setup, contribution uncertainty, or too much context
switching. Fix the bottleneck rather than extending the workday.