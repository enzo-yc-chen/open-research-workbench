---
name: autonomous-runner
description: Long-running autonomous task runner. Use when the user asks the assistant to keep advancing a task chain across queued prompts, long commands, context compaction, polling loops, durable checkpoints, daily notes, and task records.
---

# Autonomous Runner

## Overview

Use this skill as a scheduling layer on top of the task workflow for long,
unattended, or queued continuation.

This skill does not replace task workflow. It reconstructs state from durable
records, chooses bounded batches, invokes the right workflow actions, runs safe
commands when appropriate, and writes checkpoints so a later session can
continue.

When the user asks the assistant to "keep going", "continue autonomously", or
"advance the task chain", assume they are delegating continuation until one of
these happens:

- A user-stated stop condition is reached.
- A task-recorded stop condition is reached.
- Work completes.
- A real blocker requires a user decision.
- No safe autonomous batch remains.

Do not stop merely because one batch finished. Stop when the state is durable
or continuing would be unsafe.

## Typical Actions

- `task-auto`: start or continue autonomous work toward a broad goal.
- `task-auto-continue`: reconstruct state and advance the next safe bounded
  batch.
- `task-auto-stop`: record a stop, pause, abandonment, split, or handoff state.

Natural-language requests can use this runner without naming an action.

## Recovery First

Every autonomous turn must be self-recovering. Treat a resumed or compressed
conversation as a cold start.

Before doing work:

- Read `markdown/daily/tasks.md` when present.
- Read the relevant task-chain `README.md`.
- Read the relevant task `README.md`.
- Read the active `plan*.md` and latest `exec.md`, `review.md`, or `verify.md`
  as needed.
- Read recent daily notes for pause, abandonment, supersession, split, and
  completion records.
- Check relevant version-control status before editing.

Conversation summaries and assistant session logs are hints, not the source of
truth. If the current task cannot be reconstructed from durable records, stop
and ask for clarification.

If the user provides an assistant session log for recovery, read only the
relevant parts needed to recover latest intent, changed files, command results,
checkpoints, and blockers. Then write recovered facts back into task records
before continuing.

## Batch Selection

Choose a useful, recoverable batch.

Good batch boundaries include:

- One file group.
- One module.
- One reading batch.
- One plan section.
- One build, test, or data-check milestone.
- One concrete task inside a chain.
- One chain-management action such as creating a follow-up task or marking a
  task paused.

Avoid open-ended work. If the next useful action is too broad, narrow it into a
batch and record the chosen scope.

## Autonomous Policy

Within the user's stated goal and workspace rules, the runner may:

- Create or update task-chain README files.
- Create follow-up tasks.
- Revise task plans when execution invalidates the old plan.
- Execute part of a plan instead of the whole plan.
- Run documented project commands.
- Poll long-running commands or jobs.
- Read logs and summarize failures.
- Mark tasks as paused, abandoned, superseded, split, or completed when records
  support that state.
- Use agents for bounded independent work with clear write scope.

Ask before continuing when:

- An operation may overwrite or delete user data.
- Dirty files overlap the intended write scope and cannot be safely attributed.
- The next direction has non-obvious consequences that records do not resolve.
- The needed command is not documented.
- The task should be abandoned, superseded, or split but records do not support
  the choice.

## Checkpoint Writes

After each meaningful batch, update durable records before ending the turn.

Write a checkpoint when:

- A module, file group, plan section, task, or command milestone finishes.
- A significant decision, deviation, blocker, split, pause, or supersession is
  discovered.
- A long command or agent result changes the next step.
- Roughly 30-45 minutes of unattended work have passed.
- The turn has accumulated enough state that losing conversation context would
  cause rediscovery.
- The assistant resumes and finds unrecorded progress in files or version
  control.

Update the appropriate files:

- Task-chain `README.md`: chain strategy, task list, deferred areas, latest
  checkpoint.
- Task `README.md`: current state, active plan, latest checkpoint, resume point.
- `exec.md`: executed batch, files changed, command evidence, deviations,
  recovery point.
- `verify.md`: only when verification was actually performed.
- `markdown/daily/<YYMMDD>.md`: factual daily status record.
- `markdown/daily/tasks.md`: last update and truthful status.

The checkpoint should include current task, batch goal, completed steps,
important decisions, deviations, command/test status, current state, and next
resume point.

## Agent Use

Use agents only when delegated work is bounded, independent, and recoverable
from written records.

Good agent tasks:

- Read-only module audits.
- Log or test summarization.
- Source comparison.
- Evidence-link checks.
- Bounded edits in disjoint files.

Do not delegate the immediate blocking decision for the main thread, broad
architectural direction, or multiple edits to the same file group.

Integrate agent results into task records before ending the autonomous turn.
