"""Preliminary CIA-triad risk scoring for the Group E proposal.

This script uses synthetic CSV data. It is not a certification, penetration-
testing, or production risk-management tool.
"""

from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path


REQUIRED = {
    "scenario", "risk_id", "asset", "threat", "weakness",
    "confidentiality", "integrity", "availability", "likelihood",
    "treatment", "mapped_outcome", "owner", "evidence",
    "residual_likelihood", "residual_impact",
}


def score_level(score: int) -> str:
    if score >= 17:
        return "Critical"
    if score >= 10:
        return "High"
    if score >= 5:
        return "Medium"
    return "Low"


def integer_1_to_5(row: dict[str, str], field: str) -> int:
    try:
        value = int(row[field])
    except (ValueError, TypeError) as exc:
        raise ValueError(f"{row.get('risk_id', 'unknown')}: {field} must be an integer") from exc
    if value not in range(1, 6):
        raise ValueError(f"{row.get('risk_id', 'unknown')}: {field} must be between 1 and 5")
    return value


def assess(row: dict[str, str]) -> dict[str, str | int]:
    cia = [integer_1_to_5(row, f) for f in ("confidentiality", "integrity", "availability")]
    likelihood = integer_1_to_5(row, "likelihood")
    residual_likelihood = integer_1_to_5(row, "residual_likelihood")
    residual_impact = integer_1_to_5(row, "residual_impact")
    impact = max(cia)
    initial = likelihood * impact
    residual = residual_likelihood * residual_impact
    result = dict(row)
    result.update({
        "cia_impact": impact,
        "initial_risk": initial,
        "initial_level": score_level(initial),
        "residual_risk": residual,
        "residual_level": score_level(residual),
        "risk_reduction_percent": round((initial - residual) / initial * 100, 1),
        "traceability_complete": "Yes" if all(row.get(f, "").strip() for f in
            ("treatment", "mapped_outcome", "owner", "evidence")) else "No",
    })
    return result


def main(source: Path, destination: Path) -> None:
    with source.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        missing = REQUIRED - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"Missing columns: {sorted(missing)}")
        assessed = [assess(row) for row in reader]

    assessed.sort(key=lambda row: (-int(row["initial_risk"]), str(row["risk_id"])))
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(assessed[0].keys()))
        writer.writeheader()
        writer.writerows(assessed)

    levels = Counter(str(row["initial_level"]) for row in assessed)
    print(f"Processed risks: {len(assessed)}")
    print("Initial levels:", dict(levels))
    print("Total initial risk:", sum(int(row["initial_risk"]) for row in assessed))
    print("Total residual risk:", sum(int(row["residual_risk"]) for row in assessed))
    print("Output:", destination)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python risk_assessment.py INPUT.csv OUTPUT.csv")
    main(Path(sys.argv[1]), Path(sys.argv[2]))
