# MLOps Project — Report

## Team members and roles

| Member | GitHub | Role |
|--------|--------|------|
| Talha  | hafiztalha1008-afk | Data Owner (repo owner) |
| Waqar  | waqi786 | Model Owner |

- **Dataset:** Wine Quality (Red) — UCI ML Repository
- **Source:** https://archive.ics.uci.edu/dataset/186/wine+quality
- **Starter code:** Written from scratch (scikit-learn examples referenced)

---

## Reproducibility table (model-v1.0)

| Field | Value |
|-------|-------|
| Commit SHA (main at tag) | f469b17 |
| Tag | model-v1.0 |
| seed | 42 |
| split.test_size | 0.3 |
| train.model | random_forest |
| train.n_estimators | 50 |
| train.max_depth | 10 |
| Data .dvc hash (raw) | 383e08e063a5646698afb33863d1771 |
| DVC lock | dvc.lock (committed) |
| Final accuracy | 0.6044226044226044 |
| Final f1_macro | 0.28690830730490785 |
| n_test | 407 |

**Independent reproduction:** Talha ran git clone into a fresh folder, dvc pull, dvc repro --force on a separate machine and got **identical metrics** (accuracy 0.6044226044226044, f1_macro 0.28690830730490785, n_test 407). Documented in PR #12.

---

## Experiments comparison (dvc exp show)

### Waqar — max_depth sweep

| Experiment | max_depth | accuracy | f1_macro |
|------------|-----------|----------|----------|
| erect-axon | 4 | 0.63100 | 0.25792 |
| flamy-ears | 8 | 0.64945 | 0.31753 |
| gemmy-razz | 10 | 0.66052 | 0.32201 |
| baseline | 6 | 0.62731 | 0.29668 |

**Winner:** gemmy-razz (max_depth=10). Promoted in PR #5.

### Talha — n_estimators sweep

| Experiment | n_estimators | accuracy | f1_macro |
|------------|--------------|----------|----------|
| cured-love | 50 | 0.67528 | 0.32987 |
| tarot-acre | 150 | 0.64945 | 0.31638 |
| azoic-song | 200 | 0.63838 | 0.30971 |
| baseline | 100 | 0.66052 | 0.32201 |

**Winner:** cured-love (n_estimators=50). Promoted in PR #6.

### Why these winners

- **max_depth=10**: monotonic improvement with depth on this range; overfitting risk acceptable for a small dataset.
- **n_estimators=50**: fewer trees → less overfitting AND faster CI. Accuracy and f1_macro both improved over baseline.

After both were merged, 	est_size was bumped to 0.3 (see conflict resolution below), so final metrics on model-v1.0 are lower (0.6044) but reflect a more honest evaluation on a larger test set.

---

## Pull request links

| Purpose | PR |
|---------|-----|
| Pre-commit hooks | https://github.com/hafiztalha1008-afk/MLOps_Project/pull/1 |
| Data versioning (DVC) | https://github.com/hafiztalha1008-afk/MLOps_Project/pull/2 |
| EDA notebook | https://github.com/hafiztalha1008-afk/MLOps_Project/pull/3 |
| Reproducible pipeline | https://github.com/hafiztalha1008-afk/MLOps_Project/pull/4 |
| Max_depth winner | https://github.com/hafiztalha1008-afk/MLOps_Project/pull/5 |
| n_estimators winner | https://github.com/hafiztalha1008-afk/MLOps_Project/pull/6 |
| **Data update** (remove duplicates) | https://github.com/hafiztalha1008-afk/MLOps_Project/pull/7 |
| test_size bump | https://github.com/hafiztalha1008-afk/MLOps_Project/pull/8 |
| **Conflict resolution** | https://github.com/hafiztalha1008-afk/MLOps_Project/pull/9 |
| CI workflow | https://github.com/hafiztalha1008-afk/MLOps_Project/pull/10 |
| **CI red demo** (closed, not merged) | https://github.com/hafiztalha1008-afk/MLOps_Project/pull/11 |
| **Release v1.0** (dev -> staging) | https://github.com/hafiztalha1008-afk/MLOps_Project/pull/12 |
| Metrics regeneration | https://github.com/hafiztalha1008-afk/MLOps_Project/pull/13 |
| Release to production (staging -> main) | https://github.com/hafiztalha1008-afk/MLOps_Project/pull/14 |

### Changes requested review
Talha requested changes on PR #3 (asked for a regression test for the semicolon separator). Waqar added it in commit 6c79a4d, and Talha approved.

### Abandoned experiment branch
- **exp/waqar-max-depth** — kept (not merged). The experiments were cherry-picked into PR #5 via a fresh 
eat/tune-max-depth branch, per the assignment rule that exp/ branches are never merged directly.

---

## Screenshots

1. **Blocked fake AWS key** — detect-secrets hook blocked committing AKIA****EXAMPLE (fake key, demo only) (see Phase 3 output).
2. **Blocked 5 MB file** — check-added-large-files blocked igfile.bin (5120 KB) exceeds 1024 KB (see Phase 3 output).
3. **Failing CI** — PR #11: CI / test (pull_request) Failing after 52s. Log: 	ests/test_ci_demo.py::test_deliberately_broken FAILED — AssertionError: This test is intentionally broken to demo CI red.
4. **Passing CI** — PR #10: All checks have passed — 1 successful check.

*(Actual image files are attached separately in the assignment submission.)*

---

## Retrospective

### What broke
1. **BOM in pyproject.toml** — PowerShell's Out-File -Encoding utf8 added a UTF-8 BOM. jupytext and 	omllib refused to parse the file. Fixed by rewriting with Python's encoding='utf-8'.
2. **CSV separator** — the Wine Quality CSV uses ; not ,. pandas.read_csv default failed. Fixed by passing sep=";". Regression test added in 	ests/test_data.py.
3. **DVC remote credentials** — Talha's .dvc/config.local is gitignored, so Waqar could not dvc pull initially. Fixed by (a) Talha inviting Waqar to DagsHub as a collaborator, and (b) Waqar adding his own token locally.
4. **dvc push forgotten after 	est_size change** — PR #9 changed 	est_size to 0.3 but did not regenerate dvc.lock and metrics.json. Fixed in PR #13.
5. **CI needed data** — CI has no DVC access, so data_checks.py and prepare.py failed. Fixed by committing a 20-row data/raw/sample.csv and pointing CI at it.
6. **Branch protection was missing** — only added after Phase 8. Should have been part of Phase 1.

### What we added to CONTRIBUTING.md
We will standardise these going forward:
- **Always run dvc push BEFORE git push** if the pipeline or data changed.
- **Always regenerate metrics.json and dvc.lock** when params.yaml changes.
- **Always use --force-with-lease** for pushing rebased personal branches (never plain --force).
- **Commit a tiny sample** of any new dataset if CI needs to run data checks on it.
- **Never commit tokens or .dvc/config.local** — keep secrets local.
- **Use dvc repro --force** for reproducibility verification, not just dvc repro (cache hides bugs).

---

## Per-member contributions

### Talha (Data Owner)
Set up the GitHub repo, branches and protection rules. Owned DVC: initial dataset tracking, DagsHub remote configuration, and the data-update PR that removed 240 duplicate rows. Set up DagsHub integration and invited Waqar as a collaborator. Ran the 
_estimators experiments and promoted the winner via PR #6. Authored PRs #2, #6, #7, #8 and reviewed/merged PRs #1, #3, #4, #5, #9, #10, #12, #13, #14. Performed the independent reproducibility verification on PR #12 (fresh clone + dvc repro --force → identical metrics).

### Waqar (Model Owner)
Owned the training pipeline and configs. Wrote src/prepare.py, 	rain.py, evaluate.py and dvc.yaml. Led the max_depth experiments and promoted the winner via PR #5. Wrote the pre-commit config (PR #1), the EDA notebook (PR #3), the reproducible DVC pipeline (PR #4), the CI workflow (PR #10) and the deliberate-broken-test demo (PR #11). Resolved the 	est_size merge conflict with Talha (PR #9). Created the model-v1.0 tag. Authored PRs #1, #3, #4, #5, #9, #10, #11, #13, #14 and reviewed PRs #2, #6, #7, #8.

---

## Final deliverables

- Tagged release: **model-v1.0** at commit 
469b17 on main.
- Reproducible: independent teammate reran the pipeline and metrics matched exactly.
- Repository public: **yes**.
- Instructor added as viewer: **yes**.
