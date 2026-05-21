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
- Use smaller internal agents only for bounded, well-scoped work.
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

  .codex/
    config.example.toml
    agents/

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
| `.codex/config.example.toml` | Example project-level runtime configuration. Keep real local config private. |
| `.codex/agents/` | Optional bounded agent definitions used by skills for focused jobs. Users should not need to call these directly. |
| `markdown/README.md` | Human-readable map of the markdown workspace. |
| `markdown/daily/` | Daily notes and a task index. |
| `markdown/task/` | Task chains, plans, execution logs, reviews, verification notes, and archived tasks. |
| `markdown/literature/` | Paper records, metadata, links, PDFs when allowed, and reading notes. |
| `markdown/repos/` | Notes about external repositories and reference code. |
| `markdown/groups/` | Research group or organization profiles and update notes. |
| `markdown/topics/` | Topic maps, concept notes, route comparisons, and open questions. |
| `markdown/projects/` | Project status, evidence, analysis, task handoff, result handback, and output planning. |
| `scripts/` | Optional helper scripts for indexing, checking, generating summaries, or maintaining the workspace. |

## Skills And Agents

The workbench assumes two layers of assistant behavior.

Skills are the user-facing workflow layer. They live under `.agents/skills/`.
A user can ask to start the day, create a task, archive a paper, review a
project, or summarize current work. The skill interprets intent, chooses the
right action size, updates durable records, and decides whether agent work is
useful.

Agents are internal workers. In this template, project-level agent definitions
live under `.codex/agents/`. They are optional and should be small. An agent may
draft a paper note, inspect a task record for missing recovery information,
compare repository notes, or prepare a project refresh draft. Agents should
have a narrow write scope and should report back to the skill that called them.

The user should not have to think in agent names. The public interface is the
skill workflow.

## The `.codex/` Folder

The `.codex/` folder is an optional adapter layer for assistant tools that can
read project-level configuration and agent definitions.

For a new workspace, use it like this:

- Read `.codex/config.example.toml` as a starting point for project-level
  settings.
- Create your own private config from the example if your assistant runtime
  supports it.
- Put reusable, project-safe agent definitions in `.codex/agents/`.
- Let skills decide when an agent should run and what files it may read or
  write.

The example config is intentionally small. A real local config may contain
accounts, private paths, local service endpoints, or model/provider choices.
Keep those details out of any public template or shared repository.

The workspace model does not depend on this folder. Readers who use a different
assistant runtime can keep the markdown layout and skill design, then replace
`.codex/` with their own adapter.

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

## Sharing Your Workbench Safely

When you use this template, keep your live research workspace and any public
copy separate.

Your private workspace is where real work happens: daily notes, unfinished
ideas, local paths, private data, experiments, and project evidence. A public
copy should be a cleaned template or a deliberately prepared example. It should
teach the workflow without exposing the work itself.

For most users, a good sharing pattern is:

1. Keep your real workspace private.
2. Create a separate public template repository.
3. Copy only the directory structure, generic rules, reusable skills, safe
   agents, and synthetic examples.
4. Replace real project names with fictional ones.
5. Replace real results with small made-up examples or public-source examples.
6. Review the public copy before pushing it.

Usually safe to share:

- Directory conventions.
- Generic workflow rules.
- Example task and project records built from fictional material.
- Reusable skills and agents after removing local assumptions.
- Small scripts that do not contain private paths or credentials.

Keep private or replace:

- Personal names, emails, accounts, home paths, hostnames, and machine details.
- Private repository URLs, tokens, local services, and real runtime config.
- Compute access notes, queue names, job logs, and infrastructure details.
- Restricted source code, datasets, PDFs, and generated large files.
- Unpublished project names, benchmark results, hypotheses, evidence chains,
  and research claims.
- Chat transcripts, session logs, or assistant memory files that may contain
  sensitive context.

If a real detail helps explain the workflow, turn it into a fictional example.
For example, use `example-solver`, `sample-literature-review`, or
`toy-benchmark-study` instead of a real project.

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
7. Add skills and agents only after the directory responsibilities are clear.
8. Keep real runtime config private; publish only examples under `.codex/`.

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
- Optional agent definitions.
- Project-level runtime config examples.
- A privacy and publication checklist.
- Small maintenance scripts where they are useful.

The template should stay readable even without any particular assistant tool.
Project-specific runtime adapters can be replaced by users in their own
private workspaces.

## License

MIT License. See [LICENSE](LICENSE).
