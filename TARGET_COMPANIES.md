# Agent Runtime Reliability — Target Companies

**Last market verification:** 2026-09-11

This is the living hiring-market layer for the six-month specialization.

It is **not** the application tracker and it does not change the active learning
roadmap by itself. Before applying or recommending outreach, check the user's
application tracker and current job page again.

The purpose is to answer:

- Which companies build infrastructure close to the specialization?
- Where is the user's current probability of getting hired highest?
- Which companies are better approached through open-source/founder visibility
  before a job exists?
- Which proof from CUA, Rivet, Browser Harness, E2B, or the Failure Lab should
  trigger outreach?

## 1. Priority Model

Use qualitative priority rather than fake numerical precision.

### `A — ACTIVE TARGET`

Strong specialization fit **and** a plausible hiring/access route from India or
with realistic relocation/sponsorship. Apply/outreach when the relevant proof is
ready.

### `A- — RELATIONSHIP FIRST`

Very strong specialization fit, usually a tiny/new team, but no ideal engineering
opening yet. Build technical visibility before the company starts hiring broadly.

### `B — STRETCH / CONSTRAINT`

Excellent technical fit, but current experience, visa, or location constraints
make immediate hiring less likely. Use these companies as market benchmarks and
future targets; contribute where useful.

### `C — ADJACENT INFRA / LONGER TERM`

Strong sandbox/browser/runtime infrastructure relevance, but less direct or less
accessible today. Keep on the radar without diverting the active roadmap.

## 2. Highest-Priority Targets

| Priority | Company | YC? | Layer | Current access / hiring signal | Best route | Why this specialization matters |
| --- | --- | --- | --- | --- | --- | --- |
| **A** | **Rivet** | W23 | durable agent runtime / actors / orchestration | Software Engineer: remote, any/new grads, US visa not required | **Apply when current CUA proof is public; strongest after Rivet block** | direct overlap with durable execution, sessions, cancellation, distributed state, Rust/Go systems |
| **A** | **The Company Company** | P26 | agent harness + actors + permissions + sandboxes | Founding Engineer: SF / Remote, any/new grads, sponsorship listed; confirm remote geography before applying | founder application/outreach with concrete OSS story | role explicitly wants harness, memory, actors, permissions, sandboxes, infrastructure, distributed backend evidence |
| **A / A-** | **Composio** | No | agent tool/control-plane infrastructure | current MTS Enterprise Platform role in Bangalore, onsite | apply only if location works; otherwise technical/founder watch | governance, auditability, observability, permissions, routing, control planes for agents |
| **A-** | **Sentient OS** | F26 | on-device computer-use runtime / proactive agents | team 2, no jobs currently | **relationship before hiring**; watch OSS/founder surface | computer use, local runtime lifecycle, background execution, state/memory, privacy/resource boundaries |
| **A-** | **Maritime** | F26 | isolated persistent computers for agents | team 3, no jobs | relationship/founder watch after sandbox/runtime proof | persistent agent computers, scaling, sleep/wake, lifecycle management |
| **A-** | **Ascii** | F26 | persistent cloud VMs for agents | team 3, no jobs | relationship/founder watch after E2B block | agent VMs, snapshots, fleet control, persistence, sandbox lifecycle |
| **A-** | **Mirrors** | F26 | agent regression / replay / failure testing | team 2, no jobs | relationship after Failure Lab or strong regression-testing proof | production trace replay, irreversible actions, regression testing, state/effect comparison |
| **A-** | **Workers IO** | F26 | fault simulation / software verification | team 2, no jobs | relationship after cross-repo Failure Lab evidence | explicit fault/timing/interleaving verification; highly aligned with failure-injection specialization |
| **A-** | **Truffle AI** | W25 | deployment/runtime infrastructure for agents | Bengaluru, team 2, no jobs | founder outreach when runtime proof is stronger | agent deployment/scaling/state infrastructure with India proximity |
| **A-** | **Ressl AI** | W26 | agent evaluation / production reliability | Bengaluru, team 3; current YC opening is GTM, not engineering | relationship/watch; do not apply to mismatched role | eval/production reliability is adjacent to failure analysis and agent quality |
| **A-** | **Hyperbrowser** | S21 | browser infrastructure for agents | team 4; current India-remote opening is Growth Engineer Intern, not target role | relationship/watch for engineering opening | browser sessions, scaling, CAPTCHA/proxy infrastructure; strong Browser Harness transfer |
| **A-** | **dari.dev** | F25 | durable agent sessions / production control plane | team 2, no jobs | founder relationship after Rivet block | durable sessions, retries, workspaces, event logs, version pinning, sandbox providers |

## 3. Strong Stretch / Market-Benchmark Targets

| Priority | Company | YC? | Layer | Current constraint | Why keep it |
| --- | --- | --- | --- | --- | --- |
| **B** | **Cua** | P25 | computer-use runtime + sandbox/cloud desktop | Founding Engineer currently SF, 1+ years, US citizen/visa only | **anchor OSS community**; contribution recognition can still create future hiring/referral leverage |
| **B** | **Browser Use** | W25 | browser-agent runtime/infrastructure | Software Engineer 1+ years but SF onsite; infra role 3+ | direct Browser Harness ecosystem; exceptional proof value even before location works |
| **B** | **CharacterQuilt** | P26 | computer-use agent reliability | MTS is new-grad eligible but NYC and US citizen/visa only | near-perfect JD benchmark: workers, sandboxes, authenticated browsers, durable state, retries, cancellation, recovery |
| **B** | **Runtime** | P26 | coding-agent harness + sandboxes | SF, 3+ years, sponsorship | roadmap match for reliable harnesses, sandbox providers, cloud infrastructure, observability |
| **B** | **Dedalus Labs** | S25 | persistent compute substrate for agents | new-grad eligible but SF / US citizen-or-visa only | distributed storage, virtualization, orchestration, scheduling, runtime reliability; strong systems benchmark |
| **B** | **Blaxel** | P25 | perpetual sandboxes / agent compute | current roles primarily SF; FDE new-grad eligible | agent sandbox lifecycle, serverless compute, observability, runtime infrastructure |
| **B** | **Metorial** | F25 | production MCP / integration infrastructure | remote and visa-flexible, but current backend/infra roles ask 3+ years | strong distributed-systems + Go/TS + agent/tool + observability target after stronger OSS proof |
| **B** | **Manufact** | S25 | MCP server/cloud infrastructure | product role asks 1+ but is SF; remote infra role asks 3+ | small OSS infra team; deployment, production MCP, agent tool infrastructure |
| **B** | **Kernel** | S25 | browser/agent cloud infrastructure | no current jobs | isolated browser VMs, persistent sessions, observability, agent runtime; strong browser/sandbox benchmark |

## 4. Non-YC / Adjacent Infrastructure Targets

| Priority | Company | Layer | Current access signal | Strategic use |
| --- | --- | --- | --- | --- |
| **B/C** | **E2B** | agent sandboxes / microVM runtime | no suitable current role verified during this scan | primary Month-5 learning repo; strong technical credibility and future employer target |
| **B/C** | **Browserbase** | browser infrastructure / agent platform | current engineering roles are SF full-time | market benchmark after Browser Harness work; Core Infrastructure + Agent Platform are directly relevant |
| **B/C** | **Steel** | open-source browser infrastructure | company is hiring, but exact suitable experience/location route must be rechecked before action | strong OSS/browser-infra relationship target after Browser Harness depth |
| **C** | **Runloop** | secure code sandboxes / agent infrastructure | current careers page confirms hiring organization but no suitable opening verified in this scan | strong long-term sandbox/runtime employer; especially relevant after E2B |
| **C** | **OpenHands / All Hands AI** | coding-agent runtime | no open positions currently | reserve OSS validation repo and future employer watch |
| **C / benchmark** | **Pydantic / Logfire** | agent runners, sandboxing, durable execution, observability | fully remote role exists but asks 5+ years | one of the clearest long-term syllabus benchmarks for isolation, retries, Kubernetes runners, durable state, cleanup, observability |
| **C / benchmark** | **Modal** | large-scale sandbox/compute substrate | role fit not verified here | deep sandbox/isolation/concurrency benchmark; increasingly central to coding-agent execution |
| **C** | **Daytona** | secure AI code sandboxes | current careers show product/design more than target engineering; OSS bounties remain | sandbox contribution/hiring watch, but do not replace E2B block just for the logo |

## 5. Evidence-Triggered Outreach

Do not send the same generic message to every company. Outreach should be
triggered by proof that maps to the company's layer.

| Earned proof | Companies to re-rank upward | Strongest angle |
| --- | --- | --- |
| **CUA daemon/runtime lifecycle contribution** | Cua, Sentient OS, CharacterQuilt, Browser Use, The Company Company | process/session ownership, execution uncertainty, computer-use reliability |
| **Rivet durable execution/cancellation contribution** | Rivet, The Company Company, Metorial, Runtime, dari.dev, Manufact | durable sessions, cancellation/quiescence, state ownership, distributed execution |
| **Browser Harness session/target recovery contribution** | Browser Use, Hyperbrowser, Kernel, Browserbase, Steel, Sentient OS | CDP/session/target liveness, stale state, bounded recovery, no false success/hangs |
| **E2B sandbox lifecycle/reconciliation contribution** | E2B, Maritime, Ascii, Blaxel, Runtime, Dedalus, Modal, Runloop, Pydantic | sandbox generations, authoritative state, pause/resume, reconciliation, cleanup, isolation |
| **Failure Lab / cross-repo invariant** | Mirrors, Workers IO, CharacterQuilt, Runtime, Pydantic | reproducible fault injection, replay/regression, invariant testing, reliability engineering |

## 6. Current Best Hiring Motions

### Apply / direct founder outreach when proof is ready

1. **Rivet** — clearest combination of role accessibility and specialization fit.
2. **The Company Company** — new-grad-friendly founding role; strongest after one
   serious OSS contribution story.
3. **Composio** — strong India engineering surface if Bangalore/on-site is
   acceptable.
4. **Metorial** — remote/global-friendly but experience filter makes it a stretch;
   use strong OSS evidence to challenge the filter rather than generic applying.

### Build visibility before an opening exists

Prioritize small/new teams where early technical recognition can compound:

- Sentient OS
- Maritime
- Ascii
- Mirrors
- Workers IO
- Truffle AI
- dari.dev
- Ressl AI
- Hyperbrowser

Do not message all of them at once. Contact a company only when there is a
specific technical bridge from earned work to what it is building.

## 7. Monthly Market Rescan

Run this **once per month**, and additionally when a major PR merges or the active
roadmap repo changes.

For every `A` / `A-` company, verify:

1. current engineering openings;
2. location, remote geography, visa/sponsorship, and experience floor;
3. team size/funding/batch if relevant;
4. current product direction — still the same runtime/browser/sandbox layer?;
5. OSS repositories, recent issues/PRs, contributor review/merge behavior;
6. founder/maintainer activity and legitimate technical interaction routes;
7. which new personal proof maps to the company;
8. application tracker state before recommending action.

Then reclassify:

```text
A   = real hiring/access route + strong fit
A-  = relationship-first opportunity
B   = strong fit but current hard constraint
C   = adjacent/longer-term
REMOVE = product/hiring direction no longer supports the specialization
```

### Rescan discipline

- Do not treat an old job page as current.
- Do not keep a company high priority because its logo is exciting.
- Do not let one new company change the four-repo learning roadmap unless it
  reveals a genuine missing market capability during the monthly strategy review.
- Prefer companies where earned proof creates a differentiated founder/engineer
  conversation.
- Promote a company when a new role removes a major access barrier.
- Demote it when location/visa/experience or product direction makes hiring
  unrealistic.

## 8. Company Addition Gate

Add a new company only if at least one is true:

- it builds agent runtime / durable execution infrastructure;
- it builds browser/computer execution infrastructure;
- it builds sandbox/VM/worker infrastructure for agents;
- it builds reliability, replay, fault-injection, or observability infrastructure
  for consequential agents;
- a current role explicitly asks for the same lifecycle/recovery/distributed
  systems skills being built here.

Then ask whether there is a plausible **hiring or relationship route**. A company
can be technically fascinating and still not deserve active attention.

## 9. Source-of-Truth Links for This Snapshot

These links are deliberately kept in the living file so a future monthly rescan
can re-verify rather than rely on memory.

### YC / company pages

- Rivet: https://www.ycombinator.com/companies/rivet/jobs
- The Company Company: https://www.ycombinator.com/companies/the-company-company
- Sentient OS: https://www.ycombinator.com/companies/sentient-os
- Ressl AI: https://www.ycombinator.com/companies/ressl-ai/jobs
- Manufact: https://www.ycombinator.com/companies/manufact/jobs
- Metorial: https://www.ycombinator.com/companies/metorial/jobs
- Truffle AI: https://www.ycombinator.com/companies/truffle-ai
- Cua: https://www.ycombinator.com/companies/cua/jobs
- Browser Use: https://www.ycombinator.com/companies/browser-use/jobs
- Runtime: https://www.ycombinator.com/companies/runtime
- CharacterQuilt: https://www.ycombinator.com/companies/characterquilt
- Dedalus Labs: https://www.ycombinator.com/companies/dedalus-labs
- Hyperbrowser: https://www.ycombinator.com/companies/hyperbrowser/jobs
- Kernel: https://www.ycombinator.com/companies/kernel
- Blaxel: https://www.ycombinator.com/companies/blaxel/jobs
- Maritime: https://www.ycombinator.com/companies/maritime
- Ascii: https://www.ycombinator.com/companies/ascii
- dari.dev: https://www.ycombinator.com/companies/daridev
- Mirrors: https://www.ycombinator.com/companies/mirrors
- Workers IO: https://www.ycombinator.com/companies/workers-io

### Non-YC / adjacent

- Composio careers: https://jobs.ashbyhq.com/composio
- E2B: https://e2b.dev/
- Browserbase careers: https://www.browserbase.com/careers
- Steel: https://steel.dev/
- Runloop careers: https://runloop.ai/careers
- OpenHands / All Hands AI careers: https://allhandsai.applytojob.com/
- Pydantic Agent Infrastructure Engineer: https://pydantic.dev/jobs/agent-infrastructure-engineer
- Modal Sandboxes: https://modal.com/products/sandboxes
- Daytona careers: https://www.daytona.io/careers

## 10. Strategic Rule

The market list answers **where to direct earned signal**.

The roadmap answers **how to create that signal**.

Keep them separate:

```text
CUA → Rivet → Browser Harness → E2B
              creates
                 ↓
maintainer-visible runtime reliability proof
                 ↓
TARGET_COMPANIES.md decides where that proof is most valuable
```

Do not chase a company by abandoning the specialization that is supposed to make
the candidate differentiated.