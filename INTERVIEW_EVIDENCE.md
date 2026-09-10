# Interview Evidence

This file contains **only technical evidence from work I have actually performed**.

Do not pre-fill hypothetical achievements, infer contributions, or convert planning/repo research into personal evidence.

An entry should be added when I have enough direct investigation to defend the story under technical cross-questioning.

Possible statuses:

- `INVESTIGATION`
- `ISSUE / REPRODUCTION`
- `PR OPEN`
- `PR REVIEWED`
- `MERGED`

---

## Entry Template

### Repository / subsystem

...

### Status

`INVESTIGATION | ISSUE / REPRODUCTION | PR OPEN | PR REVIEWED | MERGED`

### Problem

What real problem or failure was I investigating?

### HLD

Which components and responsibility boundaries were involved?

### Lifecycle / data flow

What was the normal execution path?

### Relevant LLD

Which implementation paths/functions actually controlled the behavior?

### Failure reproduction

What did I do to reproduce or inject the failure?

### Violated invariant

What system property should always have remained true?

### Root cause

What incorrect assumption, ownership rule, ordering constraint, state model, or implementation behavior caused the failure?

### Alternatives considered

#### Option A

...

#### Option B

...

### Chosen approach / conclusion

...

### What I personally did

Be precise about my contribution versus maintainer suggestions, existing code, or AI assistance.

### Testing / evidence

How was the conclusion or fix verified?

### Maintainer feedback

What feedback changed or strengthened my reasoning/design?

### Result

Issue:

PR:

Outcome:

### Generalized lesson

What would transfer to another agent-infrastructure system?

### 2-minute spoken answer

Write only after the investigation is mature enough to explain clearly.

### Likely interviewer follow-up questions

- Why was the obvious fix insufficient?
- What invariant were you protecting?
- What happens under restart/concurrency/cancellation?
- Where should authoritative state live?
- How would the design change for a remote runtime?
- What would you monitor in production?

---

## Earned Evidence

### CUA — Driver Runtime / Daemon lifecycle and session recovery

### Status

`INVESTIGATION`

### Problem

Understand what survives, breaks, and recovers when the long-running CUA Driver
Daemon disappears while the MCP Proxy and logical session remain alive, both
between requests and during a side-effecting active request.

### HLD

```text
MCP Client
→ cua-driver mcp Proxy
→ Unix socket
→ Cua Daemon
→ Driver Runtime / platform tools
```

Important ownership split established during the investigation:

- **Proxy:** logical session identity, MCP/client continuity, request stamping, persistent control connection.
- **Daemon:** process-local lifecycle records, session activity/in-flight bookkeeping, cursor/config/runtime state, tool execution.

The Proxy and Daemon are independent process/failure domains linked by a `session_id`, not shared memory.

### Lifecycle / data flow

Healthy behavior:

- normal tool calls use fresh Unix data-plane connections;
- the Proxy mints one session id and stamps it on later calls;
- the Proxy also opens a persistent `session_begin(session_id)` control connection used for direct liveness/cleanup ownership.

Replacement behavior established:

```text
old Daemon disappears
→ Proxy + logical S1 survive
→ old Daemon memory/listener/control connection disappear
→ replacement Daemon starts at same socket path
→ later fresh per-call connection reaches replacement
→ old non-ended S1 can be lazily admitted
→ replacement creates fresh lifecycle/session state under S1
```

### Relevant LLD

Source tracing covered the paths responsible for:

- Proxy creation and persistence of one internal session id;
- persistent `session_begin` control connection and its lack of automatic reconnect after established control loss;
- per-tool fresh Unix connections;
- Daemon control-session handling;
- implicit/lazy session admission through lifecycle dispatch;
- `LifecycleRecord`, activity timestamp, and in-flight accounting;
- idle lifecycle maintenance and normal session-end fan-out;
- traced cursor/config cleanup hooks.

The main source areas included the Proxy path, Daemon serving/connection path, and core session-lifecycle implementation.

### Failure reproduction

Two useful manual lifecycle reproductions were performed.

**1. Daemon dead before the next request**

- preserved the existing MCP Proxy/session;
- terminated only the Daemon;
- verified the socket pathname could remain while no listener existed;
- later tool calls failed with `Connection refused`;
- no steady-state automatic Daemon restart was observed.

**2. Replacement Daemon with the same old session identity**

A clean baseline was established with:

- Proxy PID `14126`;
- old Daemon PID `48613`;
- session `mcp-14126-1788769126087137000`;
- successful pre-break session-owned cursor action.

Then only the old Daemon was terminated and replacement Daemon PID `19835` was started at the same socket path while preserving the same Proxy/session.

Observed after replacement:

- `list_apps` succeeded through the same Proxy;
- `set_agent_cursor_enabled` also succeeded using the same old S1 even though no new persistent `session_begin(S1)` had been established with the replacement.

After a later idle period, `get_agent_cursor_state(S1)` reported that the session had ended while both the same Proxy and replacement Daemon processes were still alive.

**3. Daemon death during an active request**

- established a fresh Proxy/Daemon/session and disposable Terminal baseline;
- invoked exact-window foreground `type_text` with a 200 ms character delay and
  a unique no-newline marker;
- armed a one-shot observer that sent `SIGKILL` only after Terminal visibly
  contained `CUA_MIDREQ2_`;
- observed that the strict prefix survived while the Daemon/listener vanished;
- observed the same Proxy call return `daemon closed connection without
  response`;
- performed no automatic or manual replay of the ambiguous action.

An earlier fixed-delay attempt killed the Daemon before connection and produced
`Connection refused` with no marker. It was correctly classified as NOT TESTED
for active execution rather than reinterpreted as the desired reproduction.

### Invariant / corrected mental model

The most important corrected model was:

```text
logical session identity continuity
!= Daemon runtime-state continuity
!= restored control-liveness continuity
```

The replacement behavior is **identity reuse + fresh state creation**, not restoration of old Daemon process memory.

The persistent control connection is not a universal admission gate for every session-owned action. Its important role is immediate owner-liveness cleanup through EOF. If that control relationship is lost during Daemon replacement and not restored, normal inactivity-based lifecycle cleanup still bounds lazily recreated state.

The active-request invariant is:

```text
no trustworthy completion response after request delivery begins
→ execution outcome is unknown
→ transport failure must not imply not-executed or safe-to-retry
```

The Proxy can know that no final response arrived; independent external-state
observation is required to determine or reconcile the effect.

### Root cause / corrected assumption

No upstream bug has been established from this completed slice.

My initial assumption was wrong: I expected session-owned/stateful work to be rejected by a replacement Daemon that had never received a new `session_begin(S1)`.

Runtime evidence contradicted that assumption. Source tracing then showed that an unknown, non-ended S1 can be implicitly admitted and receive a fresh lifecycle record/activity state.

A second concern — that recreated state might become permanently orphaned without restored control EOF — was also too strong. Source tracing established the idle lifecycle fallback, and runtime evidence later showed the S1 had ended while both processes remained alive.

### Alternatives considered

For the replacement-session behavior I reasoned about two possible contracts before the runtime result was known:

#### Option A — strict generation/control admission

Reject old session-owned work until the replacement receives an explicit fresh session/control registration.

Potential property: clearer generation boundary, but worse continuity for a surviving client/Proxy.

#### Option B — identity reuse with lazy state recreation

Allow a non-ended logical session identity to be admitted by the replacement and recreate process-local lifecycle/session state on demand.

Observed CUA behavior matched this model for the tested cursor operation.

For interrupted-action reporting, three contribution approaches were compared:

#### Option C — wording only

Improve comments/errors but leave agents and SDK callers without structured
completion knowledge.

#### Option D — SDK parity only

Reuse `ActionInterrupted` for ordinary SDK Daemon actions but leave MCP generic.

#### Option E — shared SDK and MCP classification

Classify `NotStarted` before the first write attempt and `Unknown` afterward in
the common Daemon client, then map that knowledge to existing SDK
`ActionInterrupted` and additive MCP error data. Keep retry decisions with the
agent.

### Chosen approach / conclusion

No fix was chosen for between-request replacement because that behavior was not
established as defective.

For active-request interruption, the human selected the shared SDK-and-MCP
classification direction as a maintainer discussion proposal. The approved
ownership model is: tools prevent predictable ambiguity where possible; the
transport reports conservative completion knowledge; a supervisor/host restores
availability only; the agent observes external state and reconciles intent. No
implementation or upstream claim has begun.

### What I personally did

- reasoned through Proxy vs Daemon ownership and process boundaries;
- formed explicit predictions before important lifecycle tests;
- ran/observed the clean-baseline manual process experiments;
- preserved exact Proxy/session identity while selectively replacing the Daemon;
- compared prediction against runtime evidence;
- corrected the mental model after the stateful replacement call succeeded;
- used bounded source traces to understand lazy admission, control-connection semantics, and idle cleanup;
- designed and interpreted an effect-conditioned active-request failure
  reproduction;
- separated failure cause from client-visible completion knowledge;
- explained why the agent, rather than transport or supervisor, owns semantic
  recovery;
- compared wording-only, SDK-only, and shared SDK/MCP contract alternatives;
- kept runtime observation, source-verified behavior, inference, and untested boundaries separate.

AI/Codex assisted with repository/source tracing and explanation; the runtime predictions, experiment interpretation, and resulting engineering model are the learning evidence being preserved here.

### Testing / evidence

**OBSERVED**

- Daemon absence before a later call produced connection refusal while Proxy/session survived;
- manually restored replacement Daemon was reachable through the same Proxy;
- old S1 was accepted for a clearly session-owned cursor operation;
- later the same S1 was ended/rejected while the same Proxy and replacement Daemon remained alive.
- delayed `type_text` left a strict Terminal prefix before Daemon death;
- the Proxy received EOF/no response and did not replay the action.

**SOURCE-VERIFIED**

- per-call fresh Unix data connections;
- persistent control-session behavior and no traced reconnect loop after established control loss;
- implicit/lazy session lifecycle admission;
- default 300-second idle TTL;
- roughly 30-second lifecycle maintenance sweep;
- in-flight protection and normal end/cleanup fan-out;
- cursor/config cleanup path.
- execution precedes final Daemon response construction;
- ordinary Daemon/MCP errors collapse transport phases;
- private-worker, remote, and trusted-service SDK paths already expose
  `ActionInterrupted(NotStarted|Unknown)` semantics.

**INFERENCE**

- the exact observed runtime S1 expiry was caused by the idle reaper; the session-specific end reason was not directly exposed in the checked logs.

### Maintainer feedback

None yet for this investigation slice.

Related upstream issues/PRs were used as design/history context, but they are not counted as maintainer feedback on my work.

### Result

Issue: none claimed yet

PR: none yet

Outcome: between-request replacement/session recovery and active-request
execution/acknowledgement ambiguity are GREEN enough. A deeper RFC audit found
that RFC 2549 already requires honest interrupted-action completion reporting;
the observed ordinary Daemon/MCP behavior is now framed as a focused
implementation/parity bug candidate rather than a new RFC. No upstream issue or
implementation has begun.

### Generalized lesson

A logical identifier surviving a physical runtime replacement does not imply that the old runtime's state or liveness relationship survived.

A response-less transport failure after request delivery begins also does not
imply non-execution. Availability restoration, completion reporting, and
semantic recovery are separate responsibilities.

When evaluating another agent runtime, explicitly ask:

- what identity survives a runtime generation change;
- what state is recreated versus restored;
- what control/liveness relationship is lost or rebound;
- what cleanup fallback bounds recreated state;
- what the caller can safely assume after recovery.

### 2-minute spoken answer

I investigated CUA's Driver Runtime lifecycle by separating the MCP Proxy from the long-running Daemon and intentionally killing only the Daemon while preserving the Proxy and session. The first result was straightforward: the socket pathname could remain even though no listener existed, so later calls got connection refused and the running Proxy did not automatically supervise/restart the Daemon.

The more interesting result came after manually starting a replacement Daemon. I originally expected stateless calls to recover but session-owned work to fail because the replacement had never received the Proxy's persistent `session_begin`. That prediction was wrong. The same old session id successfully performed a cursor-state operation. Tracing the lifecycle code showed the replacement can lazily admit an unknown non-ended session id and create fresh process-local lifecycle state under it.

That changed my model: the Proxy owns logical identity continuity, while the Daemon owns runtime state. Reusing the same session id is not state recovery. The persistent control connection is mainly an immediate liveness/cleanup signal; after replacement it was not re-established, but idle lifecycle cleanup still existed. Later the same session became ended while both Proxy and replacement Daemon were alive, consistent with that fallback. The next reliability question is what happens if the Daemon dies during an active side-effecting request, where the caller may not know whether the action happened before the response disappeared.

I then reproduced that active-request boundary with delayed typing into a
disposable Terminal. I killed the Daemon only after a strict prefix was visible.
The prefix survived, but the Proxy received only a response-less transport
error. That proved the response path cannot establish whether execution was
absent, partial, or complete. Source tracing showed the ordinary Daemon/MCP path
collapses these phases, while newer SDK worker, remote, and trusted-service
topologies already expose `ActionInterrupted` completion knowledge. The design
direction I selected is to align SDK and MCP reporting around conservative
`NotStarted` versus `Unknown` classification, without automatic retry or
exactly-once claims; the agent remains responsible for observing and reconciling
external state.

### Likely interviewer follow-up questions

- Why does the Proxy use fresh per-tool connections but also maintain a persistent control connection?
- Why can identity continuity be useful even without state continuity?
- What state should be generation-local versus recoverable?
- What would break if the idle fallback did not exist?
- How would you design explicit runtime generation/rebinding semantics?
- What changes when the Daemon dies after an external side effect but before returning the response?
- Which operations can be safely retried, and what idempotency mechanism would you need for the others?
