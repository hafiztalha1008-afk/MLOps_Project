# Contributing Guidelines

## Branch model
Work flows one direction: short-lived branches -> dev -> staging -> main.
Nobody pushes directly to dev, staging or main. All changes via reviewed PRs.

## Branch naming
- `feat/<name>` — new features / pipeline steps / refactors
- `data/<name>` — dataset changes tracked with DVC
- `exp/<member>-<idea>` — personal experiments (never merged directly)
- `fix/<name>` — urgent fixes to production (branch from main)

## Commit messages
Conventional Commits:
- `feat: add scaling step`
- `data: remove duplicate rows`
- `exp: try max_depth=8`
- `fix: correct typo in config`
- `chore: initial project scaffold`

## Merge strategy
We use **Squash Merge** for PRs into `dev`.
Release PRs (`dev` -> `staging` -> `main`) use **Merge Commit** so history is preserved.

## Reviewer rule
Every PR into dev/staging/main requires 1 approval from the other member.
Reviewer must check out the branch at least once if the pipeline changed.
At least one PR during the project must receive "changes requested".
