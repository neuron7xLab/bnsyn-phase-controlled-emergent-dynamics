# BN-Syn: Phase-Controlled Emergent Dynamics

Spiking neural network simulator with AdEx neurons, STDP plasticity,
and neuromodulatory field dynamics.

Part of the NFI (Neuromodulatory Field Intelligence) stack:
MFN⁺ → DNCA → BN-Syn → NFI

## Install

```bash
pip install -e ".[dev,test]"
```

## Run tests

```bash
pytest tests/ -q
```

## Canonical proof path

```bash
bnsyn run --profile canonical --plot --export-proof
```

## Status

v0.x — research prototype, active development.

## Citation

See `CITATION.cff`.

## Interpretation and claim boundaries

Supported from the canonical proof bundle:
- Direct measured traces from one simulation run
- Derived summary statistics and reproducibility metadata
- Rendered report assets such as `index.html` and `artifacts/canonical_run/product_summary.json`

Not supported:
- No claim of biological equivalence to in vivo neural tissue
- Not supported from this proof command alone: claims about cognition, consciousness, or AGI-level capability
- Generalization beyond tested parameter settings
