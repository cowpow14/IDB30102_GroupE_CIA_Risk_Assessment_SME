# Preliminary scoring component

`risk_assessment.py` validates 1-to-5 CIA, likelihood and residual scores, calculates initial and residual risk, assigns risk levels, checks treatment traceability and creates a ranked CSV.

Risk formula: `Likelihood x highest CIA impact`.

- 1-4: Low
- 5-9: Medium
- 10-16: High
- 17-25: Critical

The code uses only Python's standard library. Its purpose is to demonstrate transparent and repeatable calculations for RO3, not to replace professional judgement.
