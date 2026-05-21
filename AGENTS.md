# Workspace Instructions

This repository is a public template for a recoverable AI-assisted research
workspace. It contains workflow rules, directory conventions, reusable skill
templates, optional agent definitions, and synthetic examples.

## Operating Principles

- Treat files as the durable source of project memory.
- Keep daily notes, task records, library records, and research judgment in
  separate places.
- Prefer small, recoverable batches over open-ended work.
- Preserve user edits and unrelated dirty files.
- Do not publish real private research records in this template.
- Mark uncertain facts as candidates instead of stable conclusions.

## Directory Responsibilities

| Path | Role |
| ---- | ---- |
| `markdown/daily/` | Daily plans, factual logs, summaries, and recovery points. |
| `markdown/task/` | Executable task chains, plans, execution notes, reviews, and verification records. |
| `markdown/literature/` | Paper records, metadata, links, and reading notes. |
| `markdown/repos/` | External repository and reference-code notes. |
| `markdown/groups/` | Research group, organization, or community profiles. |
| `markdown/topics/` | Topic maps, route comparisons, and background analysis. |
| `markdown/projects/` | Project status, evidence, dynamic analysis, handoff, handback, and output plans. |
| `.agents/skills/` | User-facing workflow instructions. |
| `.codex/agents/` | Optional bounded internal agent definitions. |

## Workflow Boundaries

Daily workflow owns the time ledger. It may mention tasks, materials, and
projects, but it should not become the only source for task execution or
research evidence.

Task workflow owns executable work. Project-owned tasks still live under
`markdown/task/`; project directories should link to task results rather than
copying task logs.

Library workflow owns material facts. It can identify candidate relevance to a
topic or project, but research workflow owns the final project judgment.

Research workflow owns topic and project judgment. It turns material facts and
task results into evidence, analysis, gaps, task handoff, and output planning.

## Recovery Rules

At the start of a new session, reconstruct state from files before acting:

- Read `markdown/README.md` for the workspace map.
- Read today's daily note and `markdown/daily/tasks.md` when they exist.
- Read the relevant task-chain README and active task README.
- Read active `plan.md`, recent `exec.md`, latest `review.md`, and latest
  `verify.md` as needed.
- For project-owned tasks, read the task-chain owner-project section and the
  relevant project `status.md` when the next action depends on project context.

Conversation summaries are hints. Durable workspace records are the source of
truth.

## Privacy Rules

Keep the public template separate from real private work.

Do not commit:

- Real personal names, accounts, tokens, private paths, or hostnames.
- Real daily logs, task records, unpublished evidence, or project claims.
- Restricted source code, proprietary datasets, PDFs, screenshots, or generated
  large files.
- Real runtime configuration, local service endpoints, or credentials.
- Compute access details, queue names, job logs, or infrastructure-specific
  access notes.

Use fictional projects and synthetic examples when demonstrating the workflow.

## Agent Use

Agents are internal helpers. Use them only for bounded work with clear scope.

Good agent tasks include:

- Drafting one paper note from a provided public source.
- Checking one task record for missing recovery state.
- Mapping one project for evidence links and gaps.
- Reviewing one plan or result note for contradictions.

The calling workflow owns final writes and status changes.
