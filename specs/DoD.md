# Definition of Done (DoD)

A release is considered READY when:

## Model
- [ ] Model is trained successfully
- [ ] Accuracy ≥ 90%
- [ ] Precision (Spam) ≥ 95%

## Code Quality
- [ ] All tests pass (pytest)
- [ ] No errors in training script

## Artifacts
- [ ] PRD.md completed
- [ ] Eval report موجود في /reports
- [ ] DataSpec, SRS, Monitoring filled

## Reproducibility
- [ ] Project runs with README instructions
- [ ] Dependencies installed correctly

## CI
- [ ] GitHub Actions passes (green check)
- [ ] Pipeline fails if metrics < threshold
