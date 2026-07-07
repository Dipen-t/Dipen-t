# Hey, I'm Dipen 👋

I'm a full stack engineer who ends up building the kind of software that has to deal with messy real-world stuff — real-time chat, multi-tenant systems, GIS data, browser automation, apps that need to work offline, and general "the data is huge and the requirements are unclear" problems.

Honestly, the part I enjoy most isn't writing the feature itself — it's figuring out what people actually need before I write it. Talking through vague requirements, sketching out how a system should behave, and then following it all the way from idea to something running in production (and then fixing it when production teaches me I was wrong about something).

Right now I'm building **Saathi**.

> Most of my client and production work is under NDA, so I can't share the actual code. What I can share is the engineering context — the problems, the architecture decisions, the trade-offs.

---

## What I'm building right now: Saathi

Saathi is a local social platform — the idea is to help people discover others near them, start conversations, make plans together, and actually meet up in real life instead of just scrolling past each other forever.

It's less "endless feed" and more "here's who's around, here's what's happening, go do something." There's a Karma Points system baked into every profile too, so reputation and participation actually mean something in the community.

**On the real-time side**, I've been leaning heavily on WebSockets and Supabase Realtime — live typing indicators, instant message sync, conversation updates that don't need a refresh. Getting that to feel *actually* instant across multiple connected users was one of the more fun problems here.

**Core stuff the product does:**
- Discover people nearby
- Start conversations with locals
- Create and join plans/activities
- Turn a chat into an actual meetup
- Build reputation through Karma Points

**Stack:** Next.js, TypeScript, Supabase, Supabase Realtime, WebSockets, Drizzle ORM

→ [Check out the repo](https://github.com/Dipen-t/Saathi)

---

## Stuff I've built professionally (mostly private repos, sorry)

I can't link most of this because it belongs to clients or employers, but here's a rundown of the problems I've actually shipped solutions for:

**GIS-based municipal survey platform** — Built a field operations tool handling 150,000+ consumer records across 50+ municipal wards. Field workers needed to collect property data, photos, and signatures *without reliable internet*, capture GPS + GIS IDs, and have it all sync up later into dashboards admins could actually use. Offline-first was non-negotiable here, which made a lot of "easy" features suddenly not easy.

**Multi-tenant education/career platform** — Worked on a system serving 10+ organizations, each with 7+ different staff roles, all needing clean data isolation and proper RBAC. On top of that: resume builders, essay review workflows with draft history, internship tracking, certifications, and PDF generation. The tricky part was less the individual features and more making sure ten different orgs never accidentally saw each other's data.

**Browser automation pipeline for 100+ colleges** — Needed structured data pulled from a bunch of JS-heavy, dynamically rendered sites. Built this with Playwright running headful, routed through proxies, with reusable extraction logic that fed straight into production systems. Automation like this breaks constantly for weird reasons, so a lot of the work was just making it *not* break.

**Construction operations system** — Attendance and dispatch management for construction sites — camera-based check-ins tied to GPS location, material request/approval flows, photo-verified dispatch, and RBAC across 5+ operational roles. Basically making sure the right person is where they say they are, and the right materials go where they're supposed to.

---

## What I actually use day to day

**Core:** JavaScript, TypeScript, PHP, SQL

**Frontend:** React, Next.js, HTML/CSS, Tailwind

**Backend:** Node.js, Fastify, PHP, REST APIs

**Data:** PostgreSQL, MySQL, Prisma, Drizzle, Supabase

**Real-time:** WebSockets, Supabase Realtime

**Automation:** Playwright, web scraping, proxy-based workflows

**Architecture:** Multi-tenancy, RBAC, JWT auth

**Infra:** Git, Docker, Linux, cPanel

**GIS:** QGIS, Mapbox, third-party APIs

---

## Questions I keep asking myself while building things

- What happens when the network drops mid-workflow?
- What happens when this dataset is 10x bigger next year?
- Can a non-technical field worker actually use this without training?
- What breaks first if a request fails halfway through?
- Is tenant data *actually* isolated, or does it just look that way in testing?

I don't always get the answers right the first time, but asking them early has saved me more than once.

---

## Currently learning / poking at

- Going deeper on backend architecture with Node + Fastify
- Real-time systems beyond basic pub/sub
- Distributed systems and system design in general
- Docker/Linux fundamentals I keep meaning to properly nail down
- AI-assisted product workflows
- Making browser automation less fragile
- Deployment and observability — the unglamorous stuff that actually matters in prod

---

## A win worth mentioning

Won the **B.K. Birla College Hackathon** — built an AI-powered summarization tool as part of the winning team.

---

## Get in touch

**Email:** dipenntalreja@gmail.com

Always up for talking through hard engineering problems, product-minded teams, or just software that's meant to be used by real people in the real world.
