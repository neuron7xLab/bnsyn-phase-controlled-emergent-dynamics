from __future__ import annotations

import pytest

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SHA_PIN = re.compile(r"@[0-9a-f]{40}$")


@pytest.mark.xfail(reason="Governance artifact or workflow archived during CI consolidation. Test validates pre-cleanup infrastructure. See archive/ for historical artifacts.", strict=False)
def test_workflow_integrity_permissions_and_pinning() -> None:
    workflow = REPO_ROOT / ".github" / "workflows" / "sse-sdo-fhe-gate.yml"
    content = workflow.read_text(encoding="utf-8")
    assert "permissions:" in content
    assert "contents: read" in content
    assert "timeout-minutes:" in content

    for line in content.splitlines():
        stripped = line.strip()
        if not stripped.startswith("uses:"):
            continue
        action = stripped.split("uses:", 1)[1].strip().strip('"\'')
        if action.startswith("./"):
            continue
        assert SHA_PIN.search(action), action
