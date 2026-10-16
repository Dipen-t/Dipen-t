<img src="./assets/dipen-talreja.svg" width="100%" alt="Dipen Talreja. Full-stack engineer building real-time SaaS and applied AI tools." />

<p>
  <a href="mailto:dipenntalreja@gmail.com"><strong>Get in touch</strong></a>
  &nbsp; / &nbsp;
  <a href="#selected-work">Selected work</a>
  &nbsp; / &nbsp;
  <a href="https://github.com/Dipen-t?tab=repositories">All repositories</a>
</p>

**I'm Dipen Talreja, a full-stack engineer building real-time SaaS products and applied AI tools.** I work across interfaces, APIs, data, and deployment, with a particular interest in tenant isolation, reliable background work, and AI systems with clear boundaries.

## Selected work

I built the four projects below independently.

### [LeadFlow](https://github.com/Dipen-t/LeadFlow) · Live demo

A CRM for mortgage brokerages, from lead intake to client onboarding.

<a href="https://github.com/Dipen-t/LeadFlow">
  <img src="./assets/leadflow-pipeline.jpg" width="100%" alt="LeadFlow's application-only view: role-aware navigation and a multi-stage lead pipeline" />
</a>

**My work:** frontend, backend, database integration, live updates, background workers, and deployment.  
**Engineering detail:** optimistic pipeline updates reconcile server-side version conflicts; Socket.IO keeps connected clients synchronized.

<sub>React · TypeScript · Node.js · MongoDB · Redis · BullMQ · Socket.IO</sub>

[Try the demo](https://lead-flow-umber.vercel.app) · [Architecture and setup](https://github.com/Dipen-t/LeadFlow#architecture-overview)

### [VoiceOps](https://github.com/Dipen-t/voice-ops) · Local prototype

A Hinglish voice assistant that retrieves answers from a fictional insurance FAQ and cites its sources.

<a href="https://github.com/Dipen-t/voice-ops">
  <img src="https://raw.githubusercontent.com/Dipen-t/voice-ops/main/docs/screenshots/liquid-assistant-desktop.jpg" width="100%" alt="VoiceOps Hinglish assistant interface with a voice conversation panel, transcript, and sample questions" />
</a>

**My work:** the voice interface, streaming speech pipeline, retrieval, and recorded-incident investigation mode.  
**Engineering detail:** PostgreSQL/pgvector retrieval supports sourced answers; scoped, read-only MCP tools support incident investigation.

<sub>TypeScript · React · Fastify · PostgreSQL/pgvector · Sarvam · MCP</sub>

[Setup and current limits](https://github.com/Dipen-t/voice-ops#local-setup) · [Voice assistant status](https://github.com/Dipen-t/voice-ops/blob/main/docs/hindi-assistant-status.md)

### [EvolveKit](https://github.com/Dipen-t/living-ai) · Working local demo

A runtime foundation for proposing changes to an application's registered capabilities, with review before activation.

<a href="https://github.com/Dipen-t/living-ai">
  <img src="./assets/evolvekit-workflow.svg" width="100%" alt="EvolveKit workflow: propose, preview, approve, publish, and roll back" />
</a>

**My work:** the TypeScript capability model, React adapter, proposal lifecycle, API, persistence, and planner integrations.  
**Engineering detail:** server validation, exact-revision approval, atomic publication, and rollback keep changes traceable.

<sub>TypeScript · React · Fastify · Prisma · PostgreSQL</sub>

[Run the demo and inspect the design](https://github.com/Dipen-t/living-ai#run-locally)

### [Checkpoint](https://github.com/Dipen-t/checkpoint) · Experimental developer tool

Architectural guardrails and local decision memory for AI coding agents.

**My work:** the rule-retrieval, decision, and verification workflow.  
**Engineering detail:** local BM25 retrieval surfaces relevant constraints; Git diff checks compare actual changes with the agent's claims.

<sub>TypeScript · CLI · BM25 · Git</sub>

[Quickstart and limitations](https://github.com/Dipen-t/checkpoint#-30-second-quickstart)

<details>
<summary><strong>More projects</strong></summary>

- **[Saathi](https://github.com/Dipen-t/Saathi)** — nearby discovery, real-time conversations, and plans that bring people together.
- **[Tracker](https://github.com/Dipen-t/Tracker)** — task management, server-side timers, productivity charts, and AI-assisted task creation. [Demo](https://tracker-chi-blue.vercel.app/)
- **[Dhanlaxmi Catering](https://github.com/Dipen-t/dhanlaxmi-ui)** — a responsive catering website with scroll-driven compositions and accessible motion.

</details>

## Production experience

Beyond these public projects, my professional work includes:

- **Municipal field operations:** offline surveys, GIS mapping, and synchronization across **150,000+ records and 50+ wards**.
- **Multi-tenant platforms:** organization isolation, review workflows, and access control for **10+ organizations**.
- **Browser automation:** structured extraction from dynamic websites for **100+ colleges**.
- **Construction operations:** GPS-linked check-ins, material approvals, and photo-verified dispatch.

Client code is private; I can discuss the engineering decisions and trade-offs.

## Core toolkit

**Frontend:** TypeScript, React, Next.js, Tailwind CSS  
**Backend & data:** Node.js, Fastify, PostgreSQL, MongoDB, Redis  
**Systems & AI:** WebSockets, BullMQ, RAG, pgvector, MCP  
**Delivery & automation:** Docker, Git, Playwright

## My contribution skyline

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/contributions-dark-depth.svg" />
  <source media="(prefers-color-scheme: light)" srcset="./assets/contributions-light-depth.svg" />
  <img src="./assets/contributions-light-depth.svg" width="100%" alt="A 3D skyline of my GitHub contributions over the past year" />
</picture>

<sub>Refreshes daily with <a href="https://github.com/yoshi389111/github-profile-3d-contrib">GitHub Profile 3D Contrib</a>.</sub>

---

🏆 **B.K. Birla College Hackathon winner** · AI-powered summarization tool

Got a product idea or a difficult engineering problem? [Let's talk.](mailto:dipenntalreja@gmail.com)
