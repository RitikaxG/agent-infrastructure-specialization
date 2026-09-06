# Agent Infrastructure Specialization — Workflow

This workspace is the durable source of truth for my six-month agent-infrastructure specialization.

It sits above individual repository-learning workspaces such as `cua-learning/`.

The purpose of this workspace is to keep knowledge from becoming fragmented across repositories, issues, PRs, chats, investigations, technical writing, and future tooling.

---

## 1. Session Hierarchy

At any time there must be:

* exactly **one active repository**
* exactly **one active subsystem**
* exactly **one primary engineering question**

Do not create parallel repository workstreams.

Other repositories may be:

* briefly inspected for comparison
* recorded as future candidates
* referenced when a repeated pattern appears

But they do not become active until the current subsystem reaches its stopping boundary.

---

## 2. Strategic Source of Truth

Before making a strategic decision such as:

* whether a subsystem deserves deep study
* whether an issue or PR is worth several days of work
* whether to switch repositories
* whether a failure pattern should become reusable tooling
* whether a project idea fits the specialization
* whether a newly discovered repository should be added

read:

1. `NORTH_STAR.md`
2. `ROADMAP.md`
3. `CONTRIBUTION_FILTER.md`

Do not let:

* a new GitHub issue
* an interesting Discord discussion
* a new framework
* a repository release
* a hiring post
* an easier PR

silently change the specialization strategy.

---

# 3. File Responsibilities

Each file has a specific responsibility.

Avoid duplicating the same information across files.

---

## `NORTH_STAR.md`

Owns the long-term goal.

It should answer:

> What am I trying to become capable of after these six months?

It contains:

* primary specialization
* intended professional identity
* major agent-infrastructure areas
* definition of six-month success
* long-term failure-lab direction
* eventual agent-runtime/harness direction
* overall learning/contribution philosophy

### Update `NORTH_STAR.md` only when:

* the six-month primary goal materially changes
* the intended specialization changes
* the definition of success changes
* the overall project direction changes

### Do not update it for:

* individual bugs
* individual PRs
* daily progress
* temporary repo decisions
* newly discovered GitHub issues

This file should change rarely.

---

## `ROADMAP.md`

Owns the active specialization path.

It should answer:

> What repository and subsystem am I working on now, why am I there, and what must happen before I move?

It contains:

* active repository
* active subsystem
* current engineering objective
* subsystem stopping boundary
* next likely subsystem
* future repository candidates
* reasons for switching repositories

### Update `ROADMAP.md` when:

* a new subsystem becomes active
* the current subsystem's purpose changes
* stopping criteria are reached
* a subsystem becomes a dead end
* the active repository changes
* an important future subsystem should be recorded

Do not switch repositories simply because another issue looks interesting.

Record interesting future work without activating it.

---

## `CONTRIBUTION_FILTER.md`

Owns the reusable rules for deciding whether an investigation, issue, or PR deserves significant time.

It should answer:

> Is this problem valuable for my specialization, or am I just doing an available GitHub issue?

The rules should evaluate things such as:

* subsystem relevance
* architecture relevance
* failure impact
* reproducibility
* invariant clarity
* regression-test value
* maintainer alignment
* transferability across agent systems

### Update `CONTRIBUTION_FILTER.md` only when experience teaches a better selection rule.

Examples:

* a type of issue repeatedly produces little architecture learning
* certain maintainer workflows consistently matter before implementation
* a new type of contribution proves especially valuable
* a criterion becomes important for avoiding low-value work

Do not put individual GitHub issues here.

The rules should survive individual issues being opened and resolved.

---

## `PATTERN_LEDGER.md`

Owns generalized cross-repository engineering knowledge.

It should answer:

> What recurring failure patterns and system invariants am I discovering across agent infrastructure?

Organize it primarily by:

* invariant
* failure class
* architecture pattern

Not by repository.

Example:

```text
INV-001 — Process existence does not imply readiness

CUA evidence
Browser Use evidence
E2B evidence

General lesson
Failure-lab opportunity
```

### Update `PATTERN_LEDGER.md` when:

* an investigation reveals a reusable invariant
* the same failure pattern appears in another repo
* a design tradeoff repeats across implementations
* a useful cross-repository comparison becomes clear

Do not add weak observations merely to increase the number of patterns.

The ledger should contain durable engineering knowledge.

---

## `INTERVIEW_EVIDENCE.md`

Owns technical evidence that can later support interviews.

It should answer:

> What real engineering work can I use to demonstrate that I understand this subsystem?

Update it after:

* meaningful failure investigations
* substantial issues
* important PRs
* maintainer feedback that changes the design
* architecture decisions
* useful cross-repository comparisons

For important work, record:

* problem
* HLD
* lifecycle/data flow
* relevant LLD
* reproduction
* violated invariant
* root cause
* alternatives considered
* chosen approach
* testing
* maintainer feedback
* result
* generalized lesson
* likely interview follow-up questions

Capture this while the investigation is fresh.

Do not wait until interview preparation to reconstruct months of engineering work.

---

# 4. Repository Workspaces vs Global Workspace

The specialization workspace and repository-learning workspaces operate at different abstraction levels.

Example:

```text
agent-infra-specialization/
├── WORKFLOW.md
├── NORTH_STAR.md
├── ROADMAP.md
├── CONTRIBUTION_FILTER.md
├── PATTERN_LEDGER.md
└── INTERVIEW_EVIDENCE.md
```

Repository-specific workspaces remain separate:

```text
cua-learning/
├── WORKFLOW.md
├── CURRENT.md
├── CONVENTIONS.md
├── subsystems/
├── investigations/
└── diagrams/
```

Later there may be:

```text
openhands-learning/
browser-use-learning/
e2b-learning/
```

Create those only when the repository becomes active.

Do not create multiple active learning workspaces in advance.

---

# 5. What Belongs in a Repository Workspace

Repository workspaces own detailed investigation state.

Use them for:

* exact code paths
* current hypotheses
* repo architecture
* subsystem mental models
* lifecycle diagrams
* commands
* local setup
* break scenarios
* reproduction steps
* test results
* failure observations
* unresolved questions
* relevant issues
* PR investigation
* maintainer-specific context
* next engineering question

For example, `cua-learning/CURRENT.md` should answer:

> Where exactly am I right now in the CUA investigation?

It should not attempt to describe the entire six-month career strategy.

---

# 6. What Belongs in the Global Workspace

Use `agent-infra-specialization/` for:

* six-month direction
* active specialization path
* repo-switching rules
* contribution-selection rules
* generalized failure patterns
* cross-repository comparisons
* interview evidence
* future reusable tooling
* eventual runtime/harness design insights

Do not copy entire repository investigation notes into this workspace.

Promote only the durable insight.

---

# 7. Knowledge Promotion Rule

Knowledge should move upward through these levels:

```text
raw investigation
        ↓
repo-specific subsystem understanding
        ↓
real failure / contribution
        ↓
generalized invariant
        ↓
cross-repository pattern
        ↓
reusable failure scenario
        ↓
automated failure-testing primitive
        ↓
future runtime/harness design
```

Do not jump directly from:

> I saw some code

to:

> I should build a library.

Repeated evidence should justify abstraction.

---

# 8. One Repository / One Subsystem Rule

I do not work effectively across multiple repositories simultaneously.

Therefore, at any time there must be:

```text
ONE active repository
ONE active subsystem
ONE primary engineering question
```

Example:

```text
Active repository: CUA

Active subsystem:
daemon/runtime lifecycle

Primary question:
What happens to runtime/session ownership when the daemon generation dies?
```

Do not work on:

```text
CUA Monday
OpenHands Tuesday
Browser Use Wednesday
E2B Thursday
```

That produces fragmented understanding.

The preferred progression is:

```text
deep subsystem
    ↓
failure investigations
    ↓
meaningful contribution
    ↓
extract invariant
    ↓
reach stopping boundary
    ↓
move to next repository
```

---

# 9. Repository Switching Rule

A repository switch is allowed when:

1. the active subsystem reaches its stopping boundary

or

2. meaningful contribution opportunities in the subsystem are exhausted after serious investigation

or

3. maintainers indicate the intended direction is not useful or feasible

or

4. evidence shows another subsystem is the natural next continuation of the same specialization thread

A repository switch is not justified by:

* novelty
* boredom
* another repo looking exciting
* an easier issue appearing elsewhere
* wanting another repository logo
* temporary difficulty
* fear of missing out
* wanting broader exposure

Depth comes before coverage.

---

# 10. Future Issue Capture Without Multitasking

If an important issue appears in another repository while another repo is active:

Do not start investigating it deeply.

Record it in `ROADMAP.md` as a future candidate.

Example:

```markdown
### Future Browser Use Candidate

Issue: #XXXX

Why relevant:
Possible stale CDP session after browser generation changes.

Potential pattern:
Runtime/session generation ownership.

Status:
DO NOT INVESTIGATE YET.

Re-evaluate when Browser Use becomes active.
```

This preserves the opportunity without creating a second workstream.

---

# 11. Subsystem Investigation Structure

For every important subsystem, connect three levels.

## Level 1 — HLD

Understand the major components and responsibility boundaries.

Example:

```text
Harness
   ↓
Runtime client
   ↓
Daemon
   ↓
Browser / Computer
```

Ask:

* Why do these components exist?
* Who owns what?
* Where is authoritative state?
* Which boundaries cross processes/machines?

---

## Level 2 — Lifecycle / Data Flow

Follow the relevant flow.

Example:

```text
start
 ↓
spawn
 ↓
ready
 ↓
attach
 ↓
execute
 ↓
observe
 ↓
shutdown
```

Ask:

* What state changes?
* What IDs are created?
* What is persisted?
* What operations may race?

---

## Level 3 — LLD

Trace the implementation.

Example:

```text
Runtime.start()
→ DaemonManager.ensure_running()
→ spawn()
→ wait_for_ready()
→ Session.connect()
```

Ask:

* Which function enforces the invariant?
* Where is state mutated?
* Where are retries implemented?
* Where are errors converted?
* Which code owns cleanup?

The final understanding should connect:

```text
HLD
 ↓
lifecycle/data flow
 ↓
LLD
 ↓
failure
 ↓
invariant
 ↓
fix/test
```

---

# 12. Failure-First Investigation Rule

Do not merely read subsystem code indefinitely.

The preferred learning loop is:

```text
understand normal path
        ↓
form mental model
        ↓
predict failure behavior
        ↓
introduce failure
        ↓
observe actual behavior
        ↓
find exact failure boundary
        ↓
inspect relevant implementation
        ↓
identify invariant
        ↓
evaluate possible fixes
        ↓
test
        ↓
contribute where appropriate
```

Understanding should eventually turn into engineering evidence.

---

# 13. Contribution Selection Rule

An open issue is not automatically worth working on.

Before spending serious time, ask:

## Subsystem relevance

Does it teach one of the target areas?

Examples:

* agent lifecycle
* runtime lifecycle
* ownership
* generations
* process/daemon lifecycle
* durable state
* event architecture
* cancellation
* browser/session identity
* action/observation correctness
* sandbox lifecycle
* readiness/liveness
* reconciliation
* cleanup
* observability

If not, usually skip.

---

## Architecture relevance

Prefer bugs around important boundaries:

```text
controller ↔ runtime
runtime ↔ daemon
daemon ↔ browser
agent ↔ tool
action ↔ observation
browser session ↔ target
control plane ↔ orchestrator
orchestrator ↔ sandbox
```

---

## Reproducibility

Can the failure be reproduced?

A strong deterministic reproduction can itself be valuable.

---

## Invariant

Can I state:

> After X, Y must always remain true.

If the invariant is unclear, understand the system further before implementing.

---

## Agent impact

Prefer failures affecting:

* correctness
* availability
* false-success
* hanging agents
* stale state
* duplicate side effects
* resource leaks
* broken recovery
* isolation
* lost events
* incorrect session state

over unrelated cosmetic changes.

---

## Regression value

Can a test be added that prevents the same failure class from returning?

---

## Maintainer alignment

Before large implementation work:

* search existing PRs
* inspect related changes
* reproduce first
* post evidence where useful
* ask about intended semantics when unclear
* avoid competing implementations without awareness

---

## Transferability

Ask:

> Is this failure class likely to exist in other agent runtimes?

High transferability usually means high learning value.

---

# 14. End-of-Investigation Update Rule

After a meaningful investigation, evaluate which files need updating.

Do not update every file automatically.

Ask:

### Did my repo-specific understanding change?

Update:

* `CURRENT.md`
* subsystem note
* investigation notes

inside the active repository workspace.

---

### Did I discover a reusable invariant?

Update:

`PATTERN_LEDGER.md`

---

### Did I create interview-worthy evidence?

Update:

`INTERVIEW_EVIDENCE.md`

---

### Did this change the active or next subsystem?

Update:

`ROADMAP.md`

---

### Did I learn a better way to select contributions?

Update:

`CONTRIBUTION_FILTER.md`

---

### Did the actual six-month specialization change?

Only then update:

`NORTH_STAR.md`

This should be rare.

---

# 15. Failure Suite Rule

Failure-suite development begins while doing real repository work.

It does not begin as a separate speculative project.

When a useful failure is found:

```text
real repository failure
        ↓
reproduce it
        ↓
understand root cause
        ↓
identify invariant
        ↓
contribute/fix when appropriate
        ↓
record generalized scenario
```

If the pattern appears again:

```text
same failure class
in another system
        ↓
compare implementations
        ↓
extract reusable primitive
```

Only after repetition should reusable tooling be built.

---

# 16. Failure-Lab Development Rule

The eventual failure-testing project should emerge from repeated observations.

Possible capabilities may eventually include:

* killing runtimes
* killing daemons
* killing browsers
* dropping CDP/WebSocket connections
* delaying responses
* injecting timeouts
* cancelling mid-action
* restarting between action and observation
* duplicating delivery
* testing stale generations
* injecting malformed tool arguments
* detecting leaked processes/resources
* checking lifecycle invariants
* measuring recovery timelines

But do not build these simply because they sound useful.

Each major feature should ideally correspond to failures observed in real systems.

---

# 17. Failure Scenario Capture

A failure scenario can initially be documentation.

Example:

```markdown
# Runtime dies after session attachment

## Seen in

CUA daemon lifecycle investigation.

## Setup

...

## Failure injection

Kill runtime after session attachment and before the next action.

## Expected invariant

A session belonging to generation N must not silently remain valid against generation N+1.

## Observed behavior

...

## Root cause

...

## General pattern

Stale logical handle crossing physical runtime generations.

## Possible generic automation

- launch runtime
- capture generation
- create session
- kill runtime
- restart
- attempt old session
- assert stale session is rejected
```

Later this may become an executable test.

---

# 18. Pattern Ledger Rule

A pattern becomes valuable when it can be generalized.

Example:

```text
CUA:
daemon exists but runtime not usable

Browser Use:
Chrome exists but CDP session is dead

E2B:
envd process exists but service listener is unavailable
```

General invariant:

> Resource/process existence does not imply readiness.

That is a stronger learning outcome than memorizing three separate bugs.

---

# 19. Interview Evidence Rule

Do not prepare interview stories months later from memory.

After an important investigation record:

```text
Problem
HLD
Lifecycle
LLD
Failure reproduction
Invariant
Root cause
Alternative solutions
Trade-offs
Chosen design
Testing
Maintainer feedback
Result
Generalized lesson
```

Also record:

```text
What would an interviewer ask next?
```

For example:

* Why wasn't restart enough?
* How do you detect stale generations?
* What if cleanup fails?
* How would this work across machines?
* Where should readiness be determined?
* What operation must be idempotent?
* What happens under concurrent cancellation?

---

# 20. Technical Writing Rule

Technical writing should be derived from real engineering work.

Do not write generic educational articles simply to maintain posting frequency.

Prefer:

> What I discovered while debugging daemon generations in a computer-use runtime

over:

> What is a daemon?

Prefer:

> The browser was alive but the agent had lost its control session

over:

> Introduction to browser agents.

A strong technical article should ideally contain:

* real problem
* architecture
* failure reproduction
* root cause
* system invariant
* implementation/fix
* broader lesson

---

# 21. Community Participation Rule

Maintainer recognition should come primarily from useful engineering work.

Preferred order:

1. strong reproductions
2. useful issue comments
3. meaningful PRs
4. thoughtful technical discussions
5. PR/review participation
6. Discord technical discussion
7. technical articles
8. X posts pointing to real engineering work

Do not optimize for visibility without substance.

The desired reputation is:

> This contributor repeatedly understands and reproduces difficult runtime/reliability problems.

---

# 22. Fresh Session Rule

At the beginning of a fresh ChatGPT/Codex session, establish:

1. six-month North Star
2. active repository
3. active subsystem
4. stopping boundary
5. current engineering question

Then read:

* the active repository's `CURRENT.md`
* referenced subsystem notes
* relevant investigation notes

Do not reload every global file during every coding step.

Read global strategy files when:

* choosing a subsystem
* choosing an issue
* switching repositories
* extracting a pattern
* deciding whether to build tooling
* reviewing overall progress

---

# 23. AI Usage Rule

AI may help with:

* repository navigation
* evidence gathering
* alternative hypotheses
* implementation
* test generation
* debugging
* code review
* explaining unfamiliar concepts

But I must increasingly own:

* subsystem mental model
* failure hypothesis
* architecture boundaries
* invariant
* root-cause reasoning
* design choice
* trade-offs

The progression should move from:

> Explain this repository to me.

toward:

> I believe the failure is between X and Y because Z. Challenge this model.

Eventually:

```text
see issue
 ↓
form hypotheses
 ↓
inspect evidence
 ↓
reproduce
 ↓
identify invariant
 ↓
use AI to accelerate implementation/review
```

---

# 24. No Premature Abstraction Rule

Do not create:

* libraries
* MCPs
* workflows
* generic agent frameworks
* reusable reliability systems

merely because an abstraction seems elegant.

Use this threshold:

```text
observe problem once
        ↓
understand it

observe similar problem again
        ↓
compare

observe repeated pattern
        ↓
define invariant

then consider abstraction
```

The eventual failure suite and agent harness should be evidence-derived.

---

# 25. Eventual Harness Rule

The long-term harness may eventually contain concepts such as:

```text
AgentController
EventStore
StateStore
ModelGateway
ToolRegistry
ToolExecutor
PolicyEngine
RuntimeManager
SessionManager
RetryPolicy
CheckpointManager
Tracing
```

But do not finalize this architecture in advance.

Every abstraction should eventually be defensible using real failure cases.

Examples:

> Why does RuntimeManager need generation IDs?

Because stale session/runtime generation failures were observed.

> Why persist events?

Because interrupted execution and resume behavior require reconstructable state.

> Why separate tool execution from policy?

Because model intent must not equal permission to execute.

> Why centralize cancellation?

Because cancellation crossing async/process/runtime boundaries repeatedly caused leaks or zombie work.

The architecture should emerge from engineering evidence.

---

# 26. Periodic Strategy Review

Approximately every 3–4 weeks, review:

* Am I still going deep rather than hopping?
* Did understanding turn into failures/reproductions?
* Did failures turn into meaningful contributions?
* Are maintainers beginning to recognize my work?
* Are patterns appearing across systems?
* Is the pattern ledger becoming richer?
* Is interview evidence accumulating?
* Am I building real engineering judgment?
* Am I spending too much time documenting rather than investigating?
* Am I building abstractions before sufficient evidence exists?

Do not change direction merely because progress feels slow for several days.

---

# 27. Core Six-Month Knowledge Path

The intended progression is:

```text
runtime lifecycle
        ↓
resource ownership / generations
        ↓
failure detection / readiness
        ↓
durable agent state / events
        ↓
cancellation / resume
        ↓
action ↔ observation integrity
        ↓
browser/session/target lifecycle
        ↓
sandbox lifecycle
        ↓
reconciliation / cleanup
        ↓
cross-repo invariants
        ↓
failure-testing primitives
        ↓
agent-runtime/harness design
```

The repos support this path.

They are not the goal themselves.

---

# 28. Primary Principle

The goal is not:

> Learn CUA, OpenHands, Browser Use, and E2B.

The goal is:

> Understand how durable agent-execution systems should be designed, how their important subsystems interact, how they fail, how those failures are reproduced and prevented, and which architectural invariants transfer across implementations.

Every important investigation should ultimately connect:

```text
HLD
 ↓
lifecycle / data flow
 ↓
LLD
 ↓
failure
 ↓
invariant
 ↓
root cause
 ↓
design alternatives
 ↓
fix
 ↓
regression proof
 ↓
cross-repo lesson
```

That connected understanding is the specialization.
