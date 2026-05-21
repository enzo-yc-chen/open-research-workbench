---
name: research-workflow
description: Research judgment workflow for topic maps, project status, evidence, analysis, task handoff, result handback, project refresh, and output planning under markdown/topics and markdown/projects.
---

# Research Workflow

## Overview

Use this skill for the research judgment layer. It answers what a topic or
project means, what evidence supports a judgment, what gaps should become
tasks, and how task results change project status.

This skill is not the material archive owner. Papers, repositories,
reference-code notes, and group profiles belong to the library workflow.
Research workflow may read those records, request material summaries, and link
them as evidence, but should not duplicate library metadata.

## Owned Directories

- `markdown/topics/`: topic maps, route comparisons, concept relationships,
  open questions, and cross-project background.
- `markdown/projects/`: project status, evidence, analysis, task handoff,
  result handback links, and project-local output planning.

## Project Structure

New or refreshed projects should stay light:

```text
markdown/projects/<project>/
  README.md
  status.md
  evidence/
  analysis/
  outputs/
    plan.md
```

Rules:

- `status.md` is the long-term project state: question, current judgment,
  confidence, evidence, gaps, metrics, failure interpretation, related tasks,
  and next refresh point.
- `evidence/` stores stable support that can be cited by project judgment or
  outputs. Each item should identify source path/date/version, supported or
  refuted question, evidence strength, boundary, and pending confirmation.
- `analysis/` stores dynamic reasoning: route comparison, gap analysis, metric
  design, failure interpretation, task-result interpretation, temporary
  derivations, and stage synthesis.
- `outputs/plan.md` stores output intent, audience, storyline, material gaps,
  and next writing or presentation steps.
- Do not create `tasks/` inside a project. Task entities and task ledgers stay
  in `markdown/task/`.

## Actions

- `topic-map`: update a topic map, route comparison, concept graph, or
  open-question list.
- `project-status`: update a project's long-term question, judgment,
  confidence, route, gaps, and next refresh point.
- `evidence-update`: connect a material, source finding, analysis note, or task
  result to a project judgment.
- `gap-analysis`: identify missing evidence, uncertainty, metric, threshold,
  and failure interpretation.
- `task-ownership-decision`: decide whether a task is independent or
  project-owned.
- `task-handoff`: turn a project gap into a task candidate with owner project,
  question/gap, expected evidence, metric, threshold, failure interpretation,
  and handback target.
- `research-task-dispatch`: when the user enters through research workflow,
  call or follow task workflow to create, plan, resume, or advance a
  project-owned task.
- `result-handback`: interpret completed or partial task results and update
  project status, evidence, or analysis as appropriate.
- `project-refresh`: check whether project status is stale relative to
  materials, tasks, or daily notes.
- `outputs-plan`: update `outputs/plan.md` for a project.

## Cross-Workflow Rules

- Material facts come from library workflow: literature, repository notes,
  group profiles, metadata, source freshness, and material summaries.
- Executable work goes through task workflow: task chain README, task README,
  plan, exec, review, verify, task index, and daily status.
- Daily notes are triggers, timelines, and recovery points. They do not replace
  material records, task results, project analysis, or project evidence.
- When a project-owned task is created or refreshed, ensure the task chain
  README records owner project, project path, research question or evidence gap,
  metric/threshold/failure interpretation, and result handback target.
- If a user directly uses task workflow on a project-owned task, research
  workflow may later perform result handback or project refresh. Do not require
  the user to restart through research workflow.
- If project ownership is plausible but not confirmed, record a candidate owner
  and pending confirmation rather than writing formal ownership.

## Confidence Gates

- High confidence: existing project path, exact source path, exact material ID,
  exact repository URL, task chain owner field, or user-stated ownership.
- Medium confidence: inferred project slug, topic phrase, partial paper title,
  repository nickname, or likely ownership from nearby notes. Ask or record as
  candidate before writing long-term facts.
- Low confidence: ambiguous author/group, conflicting sources, broad direction
  phrase, or stale external facts. Do read-only discovery or request library
  checks first.

For current external facts that may have changed, use live search or official
sources before citing or writing them.

## Agent Use

Agents are internal workers:

- `topic-mapper`: bounded topic mapping or route comparison.
- `research-cartographer`: read-only mapping of project evidence, task links,
  daily recovery points, gaps, and next task candidates.
- `project-steward`: single-project refresh drafter. It may write only after
  research workflow gives an explicit project-local write scope.
- `evidence-auditor`: read-only check that project judgments are supported by
  library records, task results, or project analysis.
- `handoff-planner`: draft task candidates from project gaps.

Do not create a separate project-refresh agent by default. Project refresh is a
research action and can use a project-steward working mode.
