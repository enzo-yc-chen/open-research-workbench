---
name: daily-workflow
description: Daily planning and wrap-up workflow for a recoverable research workspace. Use when the user asks to start the day, summarize the day, update a daily note, maintain the task index, run a daily scan, or recover today's working context.
---

# Daily Workflow

## Overview

Use this skill for the day-level ledger. It coordinates daily plans, factual
updates, task index notes, scan summaries, and recovery points under
`markdown/daily/`.

Daily notes are a timeline and recovery aid. They should not become the only
source of project evidence, material records, or task execution history.

## Owned Files

- `markdown/daily/<YYMMDD>.md`: one daily note per day.
- `markdown/daily/tasks.md`: an optional active task index.

Use `date +%y%m%d` unless the user supplies a date.

## Actions

- `daily-start`: create or update today's note with a concise plan, active
  tasks, relevant projects, and recovery hints.
- `daily-log`: append factual progress, command outcomes, material findings,
  task state changes, or project-related observations.
- `daily-scan`: gather external material updates for the day. The daily
  workflow chooses targets, then asks the library workflow to perform material
  search, repository checks, or group/profile checks.
- `daily-end`: summarize the day, update task status, record unresolved
  questions, and leave a clear next recovery point.
- `daily-recovery`: reconstruct today's context from the daily note, task
  index, active task records, and relevant project records.

## Rules

- Preserve user-written sections and existing daily-note structure.
- Record facts, not guesses. Mark uncertain observations as candidates.
- Do not duplicate long task logs. Link to task records and summarize only what
  matters for daily recovery.
- Do not duplicate long research analysis. Link to project or topic records and
  summarize only the daily implication.
- Run a daily scan only when the user asks, the daily plan includes it, or an
  active task/project says a scan is needed.
- Write scan summaries into the daily note. Promote durable materials into
  `markdown/literature/`, `markdown/repos/`, or `markdown/groups/`.
- If a scan result affects a project judgment, ask or follow the research
  workflow for evidence update, gap analysis, project refresh, or task handoff.

## Agent Use

Agents are optional. Use them only for bounded, independent checks such as:

- Auditing whether the daily note and task index disagree.
- Summarizing a narrow set of scan results.
- Drafting a recovery summary from existing records.

The daily workflow owns final writes to daily files.
