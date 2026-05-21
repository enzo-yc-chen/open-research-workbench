# Privacy And Publication Checklist

Use this checklist before sharing a workbench or template publicly.

## Repository Scope

- [ ] The public repository is separate from the live private workspace.
- [ ] Only intended files are included.
- [ ] Real runtime config is excluded; only examples are published.
- [ ] Archive, scratch, logs, results, data, and private folders are ignored or
      absent.

## Identity And Paths

- [ ] No personal names, emails, usernames, accounts, or home paths appear.
- [ ] No machine names, hostnames, private URLs, tokens, or credentials appear.
- [ ] Absolute paths are replaced with examples such as `/path/to/workspace`.

## Research Content

- [ ] Real unpublished project names are removed or replaced.
- [ ] Real daily notes and task logs are absent.
- [ ] Real evidence chains, benchmark results, hypotheses, and conclusions are
      absent unless they are intentionally public.
- [ ] Synthetic examples are clearly fictional.

## Materials And Data

- [ ] Restricted PDFs, datasets, source code, screenshots, binary files, and
      generated outputs are absent.
- [ ] Public source references use links or small notes, not redistributed
      restricted files.
- [ ] Licenses are checked before including copied material.

## Runtime And Compute

- [ ] Private compute access notes are absent.
- [ ] Scheduler logs, queue names, account names, and infrastructure details are
      absent or generalized.
- [ ] Local service endpoints and private model/provider details are absent.

## Final Scan

Run text scans for project names, personal identifiers, absolute paths, private
URLs, and tool-specific secrets. Review every hit before publishing.
