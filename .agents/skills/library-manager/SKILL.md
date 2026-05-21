---
name: library-manager
description: Material library manager for papers, repositories, reference-code notes, group profiles, source metadata, update scans, and material summaries under markdown/literature, markdown/repos, and markdown/groups.
---

# Library Manager

## Overview

Use this skill for the material and fact layer. It records what a source is,
where it came from, how reliable or fresh it is, and why it may matter.

Do not decide project strategy here. When a material may affect a topic or
project, return a candidate link and hand it to the research workflow for
judgment.

## Owned Directories

- `markdown/literature/`: papers, metadata, links, reading notes, and
  redistribution-safe attachments.
- `markdown/repos/`: external repository records, reference-code notes, source
  maps, license hints, and API observations.
- `markdown/groups/`: research group, lab, organization, or community profiles.

## Actions

- `paper-intake`: create or update a paper record with title, authors, year,
  DOI/arXiv/PubMed/URL when available, abstract or summary, tags, source path,
  and candidate project relevance.
- `repo-intake`: create or update a repository note with official URL,
  branch/commit when checked, scope, license hint, technical role, and candidate
  project relevance.
- `reference-code-note`: write deeper notes for source code or reference
  implementations, including source maps, input schemes, algorithms, API
  observations, and comparison points.
- `group-intake`: create or update a group/profile note with official pages,
  research directions, representative papers/repos, update checks, and
  ambiguity notes.
- `material-scan`: search or check literature, repositories, groups, or source
  updates for a daily or project request.
- `material-index`: rebuild or repair material indexes when the workspace uses
  them.
- `material-summary`: return a concise source-grounded summary for daily,
  research, or task workflows.
- `material-to-research-candidate`: propose topic/project links, evidence
  candidates, and uncertainty notes without updating project judgment.

## Write Rules

- State intended write paths before creating persistent records.
- For inferred bibkeys, slugs, group identities, repository matches, or
  conflicting sources, ask for confirmation or write a clearly marked candidate.
- Prefer exact source identifiers: DOI, arXiv ID, PubMed ID, official URL,
  owner/repo, local source path, commit, branch, source date, and access date.
- For current facts that can change, use live search or official pages before
  citing or writing long-term facts.
- Keep only user-provided files, lawful open copies, or links. Record
  provenance for attachments.
- Do not update `markdown/projects/` as if a material relation were already a
  research conclusion.

## Handoff Rules

- Daily workflow may ask for a dated material scan; return a concise summary
  suitable for a daily note.
- Materials worth keeping should be promoted into `literature/`, `repos/`, or
  `groups/`.
- Materials that may change project judgment should be handed to research
  workflow with source path, candidate implication, uncertainty, and suggested
  evidence target.
- Daily notes are not material evidence by themselves. Long-term evidence
  should point to material records, task results, or project analysis.

## Agent Use

Agents are optional and internal:

- `literature-curator`: bounded paper intake and note drafting.
- `repo-curator`: bounded repository or reference-code note drafting.
- `group-curator`: bounded group/profile creation or refresh.
- `source-auditor`: read-only check for source identifiers, links, and
  provenance consistency.

Give agents explicit read scope, write scope, and expected report format. Do
not let library agents update project status directly.
