# Definition of Done (DoD) – AI Spam Classifier Homework

This document defines the release-ready criteria for the AI Spam Classifier project.

## 1. Code Requirements
- All Python code is properly structured in `/src`, `/pipelines`, and `/tests`.
- `__init__.py` files are added where needed for package recognition.
- Code passes **all unit tests** in `/tests`.

## 2. Documentation
- PRD (`/specs/PRD.md`) completed with project objectives, features, and scope.
- SRS (`/specs/SRS.md`) documents requirements.
- DataSpec (`/specs/DataSpec.md`) describes the dataset used.
- Monitoring and Risk/Safety (`/specs/Monitoring.md`, `/specs/RiskSafety.md`) updated.

## 3. Testing
- Unit tests for model predictions are written in `/tests/test_model.py`.
- All tests pass with **pytest**.
- CI workflow (`.github/workflows/ci.yml`) runs tests automatically and passes.

## 4. Reports
- Evaluation report (`/reports/eval_report.md`) includes metrics and results.
- Any data checks or thresholds are enforced by CI.

## 5. Git & PR Requirements
- All changes committed and pushed to GitHub.
- Homework submitted via a **Pull Request** with this branch.
- PR shows green CI status checks.
