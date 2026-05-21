---
name: task-workflow
description: Recoverable task workflow for planning, executing, reviewing, verifying, pausing, resuming, and completing task chains under markdown/task/.
---

# Task Workflow

## Overview

Use this skill to manage executable work. A task can be a code change, reading
batch, benchmark run, design review, data check, writing pass, or any bounded
piece of work that needs a plan and recovery trail.

The workflow is not a fixed lifecycle. Planning, review, execution,
verification, pause, and completion can be repeated, skipped, or reordered when
the task record explains why.

## Core Concepts

- Task chain: a long-running goal under `markdown/task/<task-chain>/`.
- Task: a concrete work unit under `markdown/task/<task-chain>/<task>/`.
- Task action: planning, reviewing, executing, verifying, pausing, resuming, or
  completing work.
- Batch: the bounded amount of work to do now.
- Expected workflow: the current route for a task, recorded in the task
  `README.md`.
- Task line: the chain-level route, active task, completed tasks, deferred
  tasks, and next recovery point recorded in the chain `README.md`.

## Typical Structure

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

New tasks can add `data/`, `logs/`, `results/`, or `scripts/` when useful.
Keep large generated files out of the public repository unless they are small,
synthetic, and intentional examples.

## Actions

- `task-new`: create or update a task chain, task directory, task README, and
  task index entry.
- `task-plan`: write or revise the active plan.
- `task-review`: review a plan or implementation for risks, missing tests,
  unclear recovery state, or behavioral regressions.
- `task-exec`: execute a bounded batch and record what changed.
- `task-verify`: verify that the work matches the plan and record evidence.
- `task-pause`: record pause, abandonment, replacement, split, or uncertainty.
- `task-brief`: reconstruct current state for a new session.
- `task-done`: close a task only when the result and recovery records are
  complete.
- `tasks`: inspect or repair the task index.

## Dispatch Rules

At the start of a task action:

- Reconstruct state from the task chain README, task README, active plan,
  latest exec/review/verify notes, today's daily note, task index, and relevant
  version-control state.
- Identify the user's requested granularity: one step, one file group, one
  task, several tasks, or a whole chain.
- Choose a bounded batch that advances the goal to a durable checkpoint.
- If the chosen route differs from the recorded expected workflow, update the
  task record with the reason.
- Do not force verification or completion merely because execution happened.
- If the plan becomes invalid, replan, split, pause, or reduce the batch before
  continuing.

## Project-Owned Tasks

A task chain may be independent or project-owned.

For a project-owned task chain, record in the chain README:

- Owner project or topic.
- Project path, such as `markdown/projects/<project>/`.
- Research question or evidence gap.
- Expected metric, threshold, or failure interpretation.
- Result handback target.

Users may enter a project-owned task directly through task workflow. Do not
require them to restart through research workflow. When task results affect
research judgment, ask or follow research workflow for result handback or
project refresh.

Project ownership is a long-term fact. Write it only when the user states it,
existing records verify it, or the research workflow has judged it. Otherwise,
record candidate ownership and pending confirmation.

## Daily Logging

When task state changes, update today's daily note or task index with:

- Actual action scope.
- Completed work and important evidence.
- Current task or chain state.
- Blockers, deviations, abandoned directions, or newly split work.
- Next recovery point.

Daily notes summarize task progress; task files remain the source for execution
details.

## Agent Use

Agents are optional helpers. Use them only for bounded work with clear read and
write scope, such as:

- Inspecting one task record for missing recovery state.
- Reviewing one plan or implementation slice.
- Summarizing a specific log.
- Drafting a project handback note from a completed task.

The task workflow owns final task records and status changes.
