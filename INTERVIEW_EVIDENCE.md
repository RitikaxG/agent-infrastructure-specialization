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

_No entries yet. Add the first entry only when the current CUA investigation produces defensible engineering evidence._
