# Open Research Workbench

Open Research Workbench is a public template for building a recoverable
AI-assisted research workspace.

It is meant for projects that last longer than one chat window: literature
reviews, code experiments, design investigations, benchmark studies, research
notes, project planning, and writing preparation. The template helps a human
researcher and an AI assistant share the same working memory through files,
rather than relying on chat history alone.

The short version:

- Put durable state in the workspace, not only in conversation.
- Keep daily logs, task records, source materials, and project judgments in
  separate places.
- Let user-facing workflows decide what should happen next.
- Use smaller internal helpers only for bounded, well-scoped work.
- Keep publishable templates separate from private research records.

This repository is not a cleaned dump of a private workspace. It is a reusable
public design distilled from one.

## Why This Exists

AI assistants are strong at local work: reading files, comparing alternatives,
summarizing papers, drafting plans, writing code, and checking logs. They become
less reliable when the whole project state lives only in a long conversation.
Context windows fill up, summaries lose detail, and a new session may not know
which facts are stable, which tasks are active, or which research claims are
still uncertain.

Open Research Workbench treats the file system as the shared memory layer.
Every important state transition should be recoverable from local records:

- What is the active task?
- Which plan is current?
- What was done today?
- What evidence supports a project decision?
- Which materials were merely collected, and which were promoted into project
  reasoning?
- What should a new assistant session read before continuing?

The goal is not to make the assistant autonomous by giving it a longer prompt.
The goal is to give it a workspace where it can re-enter the project safely.

## Core Model

The workbench separates long-term state by responsibility.

| Area | Owns | Does not own |
| ---- | ---- | ------------ |
| Daily | Time-based facts, plans, summaries, recovery points | Long-term project judgment |
| Task | Executable work, plans, reviews, execution logs, verification notes | Source material curation or project strategy |
| Library | Papers, external repositories, group profiles, metadata, reading notes | Decisions about a project direction |
| Research | Topics, project status, evidence, analysis, output planning | Raw material intake or low-level task logs |

This separation keeps the workspace readable. A daily note can say what
happened today. A task record can say how work was executed. A library record
can preserve what a source says. A project record can explain what those facts
mean for the research direction.

## Directory Layout

The intended layout is:

```text
.
  README.md
  LICENSE
  AGENTS.md
  .gitignore

  .agents/
    skills/
    helpers/

  markdown/
    README.md
    daily/
    task/
    literature/
    repos/
    groups/
    topics/
    projects/

  scripts/
```

The first public version may not contain every directory yet. The layout is the
target shape for a full workspace.

| Path | Purpose |
| ---- | ------- |
| `AGENTS.md` | Workspace rules for AI assistants: what can be changed, how to recover state, and where durable facts belong. |
| `.agents/skills/` | User-facing workflow instructions such as daily planning, task execution, library management, and research planning. |
| `.agents/helpers/` | Optional bounded helper definitions used by workflows for focused jobs. Users should not need to call these directly. |
| `markdown/README.md` | Human-readable map of the markdown workspace. |
| `markdown/daily/` | Daily notes and a task index. |
| `markdown/task/` | Task chains, plans, execution logs, reviews, verification notes, and archived tasks. |
| `markdown/literature/` | Paper records, metadata, links, PDFs when allowed, and reading notes. |
| `markdown/repos/` | Notes about external repositories and reference code. |
| `markdown/groups/` | Research group or organization profiles and update notes. |
| `markdown/topics/` | Topic maps, concept notes, route comparisons, and open questions. |
| `markdown/projects/` | Project status, evidence, analysis, task handoff, result handback, and output planning. |
| `scripts/` | Optional helper scripts for indexing, checking, generating summaries, or maintaining the workspace. |

## Skills And Helpers

The workbench assumes two layers of assistant behavior.

Skills are the user-facing workflow layer. A user can ask to start the day,
create a task, archive a paper, review a project, or summarize current work.
The skill interprets intent, chooses the right action size, updates durable
records, and decides whether helper work is useful.

Helpers are internal workers. They are optional and should be small. A helper
may draft a paper note, inspect a task record for missing recovery information,
compare repository notes, or prepare a project refresh draft. Helpers should
have a narrow write scope and should report back to the skill that called them.

The user should not have to think in helper names. The public interface is the
skill workflow.

## Daily Workflow

Daily records are the time ledger of the workspace.

A daily note can contain:

- The plan for the day.
- Tasks advanced today.
- Materials noticed during a scan.
- Important command results or experiment facts.
- Recovery hints for the next session.
- End-of-day summaries.

Daily scanning should not hard-code literature search, repository inspection,
or group tracking logic inside the daily workflow. Instead, the daily workflow
asks the library workflow for material updates. If an update affects a research
direction, the daily workflow can ask the research workflow to refresh the
relevant topic or project.

Daily notes are useful because they preserve chronological facts. They should
not become the only source of research evidence.

## Task Workflow

Tasks are executable work. They can be software changes, data checks, benchmark
runs, reading batches, design reviews, writing passes, or any other bounded
activity that needs a plan and a recovery trail.

A typical task chain looks like this:

```text
markdown/task/<task-chain>/
  README.md
  <task>/
    README.md
    plan.md
    exec.md
    review.md
    verify.md
```

The chain `README.md` explains the larger goal and current route. Each task
directory records the local plan, execution notes, review findings, and
verification evidence when verification is needed.

The workflow is intentionally flexible. Not every task needs every file. A
small task may go directly from plan to execution notes. A risky task may need
review before execution. A failed plan may be replaced, split, paused, or
abandoned. The important rule is that a new session can reconstruct the current
state from files.

## Project-Owned Tasks

Some tasks are independent. Others serve a research project.

A project-owned task does not have to start from the research workflow. A user
may enter through the task workflow directly. The task chain should still
record:

- Owner project or topic.
- Project path, such as `markdown/projects/<project>/`.
- Research question or evidence gap.
- Expected metric, threshold, or failure interpretation.
- Where the result should be handed back.

Task records stay under `markdown/task/`. Project directories do not contain a
`tasks/` subdirectory. Instead, project files refer to task results when those
results matter for project judgment.

This keeps execution history and research interpretation connected without
duplicating logs.

## Library Workflow

The library is the material layer. It stores source facts before they become
research judgment.

Library records may include:

- Papers and reading notes.
- Repository notes and source inspection notes.
- Research group or organization profiles.
- Metadata, links, identifiers, tags, and update history.
- Candidate relevance to topics or projects.

The library workflow should be careful about uncertainty. It can say that a
paper may be relevant to a project, or that a repository appears useful for a
topic. It should not silently update the project status as if that relation
were already a research conclusion.

## Research Workflow

The research workflow owns judgment.

It connects library materials, task results, daily observations, and project
goals into a stable research state. It can maintain:

- Topic maps.
- Project status.
- Evidence records.
- Gap analysis.
- Metric and threshold design.
- Task handoff.
- Result handback.
- Output planning.

Research records should distinguish between material facts and project
interpretation. A paper note belongs in the library. A claim that the paper
changes a project direction belongs in a project evidence or analysis record.

## Evidence, Analysis, And Outputs

A project directory should begin simple:

```text
markdown/projects/<project>/
  README.md
  status.md
  evidence/
  analysis/
  outputs/
    plan.md
```

Use `status.md` for the current project state: research question, current
judgment, active uncertainty, known gaps, and next decisions.

Use `evidence/` for stable supporting material that may be cited by project
decisions or future outputs. Evidence should point back to its source, explain
what question it supports or weakens, and state its limits.

Use `analysis/` for live reasoning: route comparisons, temporary synthesis,
metric design, failure interpretation, task-result interpretation, and draft
arguments. Analysis can be revised or superseded.

Use `outputs/plan.md` for the first output plan. Do not create a complex
output tree too early. Add paper, report, slides, figures, or dataset folders
only when the project really enters that production stage.

## A Typical Flow

One useful loop looks like this:

1. Start the day and read the active task index.
2. Pick a task or project gap.
3. If external material is needed, ask the library workflow to archive or scan
   papers, repositories, or groups.
4. If the material affects project judgment, ask the research workflow to
   update the topic or project.
5. If the project needs executable work, create a task handoff.
6. Execute the task in bounded batches.
7. Record results in the task log.
8. Hand research-relevant results back to the project.
9. Summarize the day and write a recovery point.

This loop is deliberately mundane. The reliability comes from doing the small
bookkeeping steps consistently.

## Privacy And Publication Boundary

Do not publish a working research workspace by accident. Use this repository as
a template, then decide what belongs in a public copy.

Before sharing, remove or replace:

- Personal names, emails, accounts, home paths, hostnames, and local machine
  details.
- Internal repository URLs, private remotes, tokens, and service configuration.
- Compute infrastructure details, job logs, queues, partitions, and access
  notes.
- Licensed source code, restricted datasets, PDFs without redistribution
  rights, and large generated files.
- Unpublished project names, benchmark results, hypotheses, evidence chains,
  and research claims.
- Any chat transcripts or session logs that may contain sensitive context.

When a detail is needed to explain the workflow, use a fictional project,
synthetic data, or a public source.

## Quick Start

1. Clone or copy the template.
2. Write an `AGENTS.md` that describes your workspace rules and privacy
   boundary.
3. Create `markdown/README.md` with your directory map.
4. Start using `markdown/daily/` and `markdown/task/` first. These two make the
   workspace recoverable.
5. Add `markdown/literature/`, `markdown/repos/`, and `markdown/groups/` when
   material intake becomes important.
6. Add `markdown/topics/` and `markdown/projects/` when you need research
   judgment, evidence tracking, and task handoff.
7. Add skills and helpers only after the directory responsibilities are clear.

## What This Repository Will Contain

The public template is being built in layers.

Planned contents:

- A complete public README.
- A generic `AGENTS.md`.
- A markdown workspace guide.
- Minimal directory placeholders.
- Example daily and task records.
- Example library and project records using fictional material.
- Generic workflow skills.
- Optional helper definitions.
- A privacy and publication checklist.
- Small maintenance scripts where they are useful.

The template should stay readable even without any particular assistant tool.
Tool-specific adapters can be added by users in their own private workspaces.

## License

MIT License. See [LICENSE](LICENSE).
