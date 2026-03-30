from __future__ import annotations

import pytest

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.xfail(reason="Governance artifact or workflow archived during CI consolidation. Test validates pre-cleanup infrastructure. See archive/ for historical artifacts.", strict=False)
def test_required_checks_manifest_includes_sse_gate() -> None:
    manifest = json.loads((REPO_ROOT / "artifacts" / "sse_sdo" / "04_ci" / "REQUIRED_CHECKS_MANIFEST.json").read_text(encoding="utf-8"))
    assert "sse-sdo-fhe-gate" in manifest["required_checks"]
