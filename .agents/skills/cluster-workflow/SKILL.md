---
name: cluster-workflow
description: Remote compute workflow for project workspaces. Use when the user asks to inspect a remote workspace, run commands on a compute environment, submit or monitor scheduler jobs, read remote logs, or synchronize task records with remote results.
---

# Cluster Workflow

## Overview

Use this skill for remote compute environments. It is intentionally generic:
the public template does not assume any specific host, scheduler, partition,
queue, storage path, or login mechanism.

The goal is to make remote work recoverable and safe:

- Resolve the target environment before acting.
- Probe the remote workspace before modifying it.
- Use documented project commands.
- Record submitted jobs, logs, results, and recovery hints in task records.
- Keep private access details out of public files.

## What Belongs In Private Workspace Rules

Each real workspace should document its own remote environments in private
rules or private config:

- Remote aliases or hostnames.
- Workspace roots.
- Scheduler command names.
- Queue or resource names.
- Project command entry points.
- Log locations.
- Data transfer rules.
- Account, credential, or access constraints.

Do not put credentials, private hostnames, account names, or access notes into
a public template.

## Actions

- `cluster-probe`: check remote identity, current path, repository status, and
  available project commands.
- `cluster-run`: execute a documented command in the remote workspace.
- `cluster-submit`: submit a scheduler job through the project's documented
  entry point.
- `cluster-status`: inspect queued/running/completed jobs and recent logs.
- `cluster-log`: summarize relevant stdout, stderr, job metadata, and result
  files.
- `cluster-sync-note`: write remote outcomes back to task, daily, or project
  records.
- `cluster-cleanup`: remove only task-owned temporary files when records and
  user instruction make ownership clear.

## Safety Rules

Before any remote modification:

- Resolve the target environment and workspace root.
- Run a read-only probe such as hostname, current directory, and repository
  status.
- Check for dirty or untracked files that may be affected.
- Explain intended remote edits or job submissions.
- Use the remote workspace's own documentation as the command authority.

Never delete or overwrite remote dirty work unless the user explicitly asks for
that exact operation.

If target environment is ambiguous, ask which environment to use. For read-only
inspection, it is acceptable to compare multiple environments when useful.

## Command Rules

- Prefer project-provided scripts or documented command entry points.
- Do not invent scheduler commands from memory when the project has a documented
  wrapper.
- Keep compiled outputs, caches, and generated data environment-local unless the
  user asks for transfer.
- Record command paths, parameters, job identifiers, log paths, and result paths
  in task records.
- For long jobs, write a checkpoint before waiting or polling.

## Resource Selection

Choose resources based on the task, not habit.

Consider:

- Whether the command is a smoke test, validation run, benchmark, or production
  run.
- Expected runtime.
- Input size.
- Scaling behavior.
- Current queue pressure when visible.
- Cost of rerun.

Use small resources for smoke tests. Use larger resources only when the task can
benefit from them or the user asks for them.

## Failure Handling

- Login or remote command fails: report the failing step and concise stderr
  summary. Do not ask for credentials in chat by default.
- Remote workspace is missing: report it; do not create a replacement workspace
  unless the user asks.
- Repository is dirty: show the relevant status lines and ask before destructive
  cleanup.
- Scheduler submission fails: record command, parameters, stderr summary, and
  next retry candidate.
- Job fails: collect relevant logs, summarize the first likely failure point,
  and write the result into task records.

## Handoff

Remote compute results usually belong in task records first:

- `exec.md` for commands run, jobs submitted, logs inspected, and results found.
- `verify.md` when the remote run verifies a claim.
- Daily note for day-level status.
- Project analysis or evidence only when the result affects research judgment.

Cluster workflow owns remote execution hygiene. Task and research workflows own
the interpretation and durable status changes.
