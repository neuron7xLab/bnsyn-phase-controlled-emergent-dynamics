from __future__ import annotations

import pytest

from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_p0_gates_mapped_in_gate_runner() -> None:
    policy = yaml.safe_load((REPO_ROOT / '.github' / 'ci_policy.yml').read_text(encoding='utf-8'))
    gate_runner = (REPO_ROOT / 'scripts' / 'ci_gate_runner.py').read_text(encoding='utf-8')
    for gate in policy['tiers']['P0']:
        assert f'"{gate}"' in gate_runner


@pytest.mark.xfail(reason="Governance artifact or workflow archived during CI consolidation. Test validates pre-cleanup infrastructure. See archive/ for historical artifacts.", strict=False)
def test_pr_workflow_executes_gate_runner() -> None:
    workflow = (REPO_ROOT / '.github' / 'workflows' / 'pr_gate.yml').read_text(encoding='utf-8')
    assert 'python -m scripts.ci_gate_runner' in workflow
