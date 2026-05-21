# Markdown Workspace

This directory is the durable memory layer of an AI-assisted research
workspace. Use it to keep project state in files that both humans and AI
assistants can read at the start of a new session.

The folders are separated by responsibility. Avoid using one folder as a dump
for everything; the split is what makes the workspace recoverable.

## Folder Map

| Folder | What It Stores | Owner Workflow |
| ------ | -------------- | -------------- |
| `daily/` | Daily plans, factual logs, summaries, task status notes, and recovery points. | Daily workflow |
| `task/` | Task chains, task plans, execution logs, reviews, verification notes, pauses, and completion records. | Task workflow |
| `literature/` | Paper records, metadata, links, reading notes, and redistribution-safe attachments. | Library workflow |
| `repos/` | Notes about external repositories, reference implementations, APIs, licenses, and useful code paths. | Library workflow |
| `groups/` | Research group, lab, organization, or community profiles and update notes. | Library workflow |
| `topics/` | Topic maps, concept notes, route comparisons, background analysis, and open questions. | Research workflow |
| `projects/` | Project status, evidence, analysis, task handoff, result handback, and output plans. | Research workflow |

## Recommended Use

Start with `daily/` and `task/`. They make the workspace recoverable even
before you build a full research library.

Add `literature/`, `repos/`, and `groups/` when you need a material library.
These folders should preserve source facts and careful notes. They should not
silently decide project direction.

Add `topics/` and `projects/` when you need research judgment. Topic records
hold background maps and route comparisons. Project records hold the current
state of a concrete research effort.

## Task And Project Links

Project-owned work still lives under `task/`. Do not create a `tasks/` folder
inside a project. Instead, record the owner project and handback target in the
task chain `README.md`, then let the project files cite the task result when it
matters for research judgment.

This keeps execution history and research interpretation connected without
duplicating logs.

## Project Evidence Structure

A project can start with:

```text
projects/<project>/
  README.md
  status.md
  evidence/
  analysis/
  outputs/
    plan.md
```

Use `evidence/` for stable support that may be cited by project decisions or
future outputs. Each evidence note should point back to its source and state
what it supports, weakens, or leaves uncertain.

Use `analysis/` for live reasoning: comparisons, synthesis, metric design,
failure interpretation, task-result interpretation, and draft arguments.

Use `outputs/plan.md` as the first output planning file. Add report, paper,
slide, figure, or dataset folders only when the project actually needs them.

## Sharing Notes

If you make a public copy of your workspace, do not publish real daily logs,
private task records, unpublished project evidence, restricted source material,
or local runtime details. Use fictional projects and synthetic examples when
you want to demonstrate the workflow.

## Included Synthetic Example

This template includes one fictional project thread:

- `daily/260101.md`: sample daily note.
- `task/sample-literature-review/`: sample project-owned task chain.
- `literature/sample-paper/`: synthetic paper note.
- `repos/example-solver/`: synthetic repository note.
- `groups/example-lab/`: synthetic group profile.
- `topics/toy-solver-evaluation/`: synthetic topic map.
- `projects/toy-solver-benchmark/`: synthetic project status, evidence,
  analysis, and output plan.

These records are examples of shape and linkage only. They are not real
research claims.
