# AI Coding Evaluation Harness

An interview-ready, deterministic harness for evaluating AI-generated Python code. It grades functional, negative, boundary, and robustness behaviour across three practical challenges.

## What it evaluates

| Challenge | Target behaviour | Common weak implementation caught |
| --- | --- | --- |
| Discount calculator | Validate monetary inputs and cap discount | Allows negative values or discounts over 100% |
| Inventory reservation | Prevent overselling and invalid quantities | Deducts stock below zero |
| Email validator | Reject malformed / unsafe input | Accepts whitespace and malformed domains |

## Quick start

```bash
python -m pip install -r requirements.txt
pytest -q
python -m src.harness --solution correct
python -m src.harness --solution buggy
```

## Architecture

`src/harness.py` loads a candidate implementation, runs each case in isolation, and produces a JSON report with pass/fail evidence, category scores, and a final percentage. Candidate code lives under `solutions/`; the deliberately buggy candidates demonstrate that superficial “happy-path-only” solutions fail the benchmark.

## Limitations

This is a local deterministic evaluator, not a security boundary. The Docker image removes network access in CI usage, but untrusted code should run in a dedicated sandbox in production.
