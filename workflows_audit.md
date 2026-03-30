# Workflow Audit (Phase 1)

## Failing workflows diagnosis

| Failing check | Workflow file | Root cause category | Evidence |
|---|---|---|---|
| `ci-pr-atomic / determinism` | `.github/workflows/ci-pr-atomic.yml` | D (over-constrained gate logic + brittle high-cost checks) | Workflow runs three repeated determinism suites plus extra RNG assertions and multiple custom gates in one PR pipeline. |
| `ci-pr-atomic / launch-gate` | `.github/workflows/launch-gate.yml` + `.github/workflows/ci-pr-atomic.yml` | D/C (pipeline fragmentation and cross-workflow coupling) | Separate launch gate policy plus atomic CI gate create duplicated governance checks and failure surface. |
| `ci-pr-atomic / security` | `.github/workflows/ci-pr-atomic.yml` | D (heavy security gate in PR path) | Security job runs `make security` + SBOM and artifact uploads inside PR atomic pipeline. |
| `ci-pr-atomic / ssot` | `.github/workflows/ci-pr-atomic.yml` | D (strict generated-artifact sync gate) | Job enforces generated manifest synchronization with `git diff --exit-code` on computed files. |
| `ci-pr-atomic / test-integrity` | `.github/workflows/ci-pr-atomic.yml` | D (multiple policy scripts as hard gate) | Test-integrity job runs many custom policy scripts and `make test-gate`, increasing non-code failure risk. |
| `scientific-product-gate` | `.github/workflows/scientific_product_gate.yml` | C (missing referenced artifacts/files) | Workflow validates `artifacts/context_compressor/quality.json` but never creates it in this workflow. |
| `workflow integrity check` | `.github/workflows/workflow-integrity.yml` | D (allowlist policy drift) | Hardcoded allowlist and trigger policy checks conflict with current workflow sprawl and generated workflows. |

## Full workflow classification

| Workflow | Class | Rationale |
|---|---|---|
| `_reusable_benchmarks.yml` | NOISE | reusable benchmark-only path, not core library health |
| `_reusable_chaos_tests.yml` | NOISE | specialized chaos suite, non-essential PR baseline |
| `_reusable_formal_science.yml` | NOISE | formal-science meta workflow |
| `_reusable_gate_profile.yml` | GOVERNANCE | gate profile orchestration for CI policies |
| `_reusable_property_tests.yml` | NOISE | optional property-heavy suite |
| `_reusable_pytest.yml` | ESSENTIAL | reusable Python test runner for code in `src/` |
| `_reusable_quality.yml` | ESSENTIAL | reusable lint/type/test quality checks |
| `_reusable_ssot.yml` | GOVERNANCE | ssot governance checks |
| `_reusable_validation_tests.yml` | NOISE | validation-heavy suite excluded in baseline CI |
| `benchmarks.yml` | NOISE | benchmarks are non-essential for PR health |
| `canonical-proof-spine.yml` | GOVERNANCE | proof/artifact policy gate, not basic code CI |
| `ci-benchmarks-elite.yml` | NOISE | benchmark specialization |
| `ci-benchmarks.yml` | NOISE | benchmark specialization |
| `ci-pr-atomic.yml` | ESSENTIAL (bloated) | includes code tests but overloaded with policy/governance gates |
| `ci-pr.yml` | ESSENTIAL (duplicate) | another primary CI entrypoint; duplicates atomic path |
| `ci-smoke.yml` | ESSENTIAL | smoke checks of runnable package |
| `ci-validation.yml` | NOISE | slow validation path, not baseline |
| `codecov-health.yml` | DEAD | coverage/reporting gate not required for baseline CI health |
| `codeql.yml` | GOVERNANCE | security static analysis |
| `context_compressor_gate.yml` | DEAD | artifact-driven gate with external/generated dependencies |
| `dependency-review.yml` | GOVERNANCE | dependency security gate |
| `dependency-watch.yml` | NOISE | monitoring/notification style governance |
| `docs.yml` | NOISE | docs build/deploy is non-core to CI baseline |
| `dsio_gate.yml` | DEAD | project-specific governance gate without core test linkage |
| `formal-coq.yml` | NOISE | formal methods specialty workflow |
| `formal-tla.yml` | NOISE | formal methods specialty workflow |
| `launch-gate.yml` | DEAD | launch readiness gate not required for baseline CI |
| `math-quality-gate.yml` | NOISE | specialized quality gate beyond baseline |
| `perfection-gate.yml` | DEAD | non-executable governance strictness gate |
| `physics-equivalence.yml` | NOISE | domain-specific specialty validation |
| `pr_gate.yml` | GOVERNANCE | PR policy gate |
| `quality-mutation.yml` | NOISE | mutation suite not baseline |
| `release-pipeline.yml` | NOISE | release-only automation |
| `repo-governor-evidence.yml` | GOVERNANCE | repository governance evidence collection |
| `science.yml` | NOISE | broad scientific checks not baseline |
| `scientific_product_gate.yml` | DEAD | references artifacts not created in workflow |
| `smlrs_gate.yml` | DEAD | custom governance gate with non-core dependencies |
| `sse-sdo-fhe-gate.yml` | DEAD | custom gate unrelated to baseline src tests |
| `sse-sdo-max-gate.yml` | DEAD | custom gate unrelated to baseline src tests |
| `workflow-integrity.yml` | GOVERNANCE (failing) | workflow policy linting with brittle allowlist |

## Proposed baseline

- Keep only 3 active workflows:
  1. `ci.yml` (test + lint + dependency review job)
  2. `codeql.yml`
  3. `dependency-review.yml`
- Archive all other workflows under `.github/workflows/archive/`.
