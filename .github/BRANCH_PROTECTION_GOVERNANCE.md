# Branch Protection Governance Baseline (`main`)

## Mandatory repository settings

1. [ ] Enable Branch protection for `main`.
2. [ ] Disable direct push to `main` (PR-only merge path).
3. [ ] Enable **Require a pull request before merging**.
4. [ ] Enable **Require status checks to pass before merging**.
5. [ ] Add required check: `ci-pr-atomic`.
6. [ ] Add required check: `workflow-integrity`.
7. [ ] Add required check: `CodeQL`.
8. [ ] Add required check: `dependency-review`.
9. [ ] Enable **Require branches to be up to date before merging**.
10. [ ] Enable **Dismiss stale approvals**.
11. [ ] Do **not** allow administrators to bypass the required checks above.

## Required status contexts (job-level + matrix-level)

All contexts below MUST be green before merge:

- `Workflow Integrity / Validate workflow files`
- `CodeQL / Analyze`
- `ci-pr-atomic / build`
- `ci-pr-atomic / determinism`
- `ci-pr-atomic / finalize`
- `ci-pr-atomic / gate-profile`
- `ci-pr-atomic / quality`
- `ci-pr-atomic / security`
- `ci-pr-atomic / smoke-wheel-matrix (py3.11)`
- `ci-pr-atomic / smoke-wheel-matrix (py3.12)`
- `ci-pr-atomic / ssot`
- `ci-pr-atomic / tests-smoke`
- `dependency-review / dependency-review`

## Governance-proof evidence (blocking semantics)

| Requirement | Evidence URL (Checks tab / settings) | Timestamp (UTC) | Owner |
| --- | --- | --- | --- |
| Required checks block merge | PENDING | PENDING | PENDING |
| Matrix contexts enforced separately | PENDING | PENDING | PENDING |
| Branch protection has PR-only merge | PENDING | PENDING | PENDING |
| Dismiss stale approvals policy | PENDING | PENDING | PENDING |
| Up-to-date branch policy decision | PENDING | PENDING | PENDING |
| Admin bypass disabled for required checks | PENDING | PENDING | PENDING |

## CI baseline after consolidation

The following PR gates are now active on every pull request and push to `main`:

| Workflow | Purpose | Timeout |
| --- | --- | --- |
| `ci-pr-atomic.yml` | Install, lint, test, build, security | 20–30 min |
| `workflow-integrity.yml` | Enforce workflow governance contracts | 5 min |
| `codeql.yml` | Static security analysis (Python) | 15 min |
| `dependency-review.yml` | Dependency vulnerability scanning | 5 min |

All other workflows (`canonical-proof-spine.yml`, `math-quality-gate.yml`, `pr_gate.yml`,
`scientific_product_gate.yml`, etc.) have been moved to `workflow_dispatch`-only to eliminate
PR-gate noise. They remain available for manual or scheduled validation runs.

## Genesis Run protocol

Immediately after merge:

1. Trigger `canonical-proof-spine.yml` via `workflow_dispatch` on `main`.
2. Confirm `ci-pr-atomic`, `workflow-integrity`, `CodeQL`, and `dependency-review` are
   registered as required checks in branch protection settings.
3. Archive the resulting `canonical_run_bundle.tgz` as **The Baseline Bundle**.

## Control PR protocol (negative testing)

- [ ] **Control PR #1:** break property invariant → merge blocked.
- [ ] **Control PR #2:** break validation invariant → merge blocked.
- [ ] **Control PR #3:** break docs build → merge blocked.
- [ ] **Control PR #4:** introduce risky dependency diff → dependency-review blocks merge.
- [ ] **Control PR #5:** break install-from-wheel smoke → merge blocked.

### Control PR evidence log

| Control PR | PR URL | Expected failing check(s) | Observed failing check(s) | Merge blocked? | Evidence URL |
| --- | --- | --- | --- | --- | --- |
| #1 property invariant | PENDING | `ci-pr-atomic / property-tests-pr` | PENDING | PENDING | PENDING |
| #2 validation invariant | PENDING | `ci-pr-atomic / validation-tests-pr` | PENDING | PENDING | PENDING |
| #3 docs build | PENDING | `ci-pr-atomic / docs-pr` | PENDING | PENDING | PENDING |
| #4 risky dependency | PENDING | `dependency-review / dependency-review` | PENDING | PENDING | PENDING |
| #5 wheel smoke | PENDING | `ci-pr-atomic / smoke-wheel-matrix (py3.11)`, `ci-pr-atomic / smoke-wheel-matrix (py3.12)` | PENDING | PENDING | PENDING |
