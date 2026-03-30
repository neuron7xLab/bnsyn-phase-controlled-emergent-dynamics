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
