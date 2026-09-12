# CIA-Triad Risk Assessment Framework for Malaysian SMEs

**Course:** IDB30102 Research Methodology  
**Group:** Group E - Information Security  
**Research title:** Assessing Information Security Risks in Malaysian SMEs Using a CIA-Triad Framework Aligned with ISO/IEC 27001 and NIST CSF 2.0

## Group members

| Student | Student ID |
|---|---|
| Elis Karisha Binti Kamarul Hisam | 52215125885 |
| Siti NurDamia Afiqah Binti Azree | 52215251629 |
| Yusry Bin Zahid | 52215125710 |
| Alif Fayyad Bin Mohammad Nazri | 52215125967 |


## Research problem

1. Malaysian SMEs may find it difficult to translate broad security standards into a traceable process connecting assets, CIA requirements, threats, risk scores and affordable treatment actions.
2. Previous studies use inconsistent measures and limited organisational samples, making it difficult to determine whether a framework improves risk decisions across different SME situations.

## Aim and objectives

**Aim:** Design and evaluate a practical CIA-triad information-security risk assessment framework for Malaysian SMEs aligned with ISO/IEC 27001:2022, ISO/IEC 27005:2022 and NIST CSF 2.0.

- **RO1:** Analyse current risk-assessment practices, framework requirements and SME implementation gaps.
- **RO2:** Design an integrated CIA-triad framework linking assets, threats, likelihood, impact, treatment and recognised framework outcomes.
- **RO3:** Evaluate the framework using synthetic SME scenarios and consistent measures.

## Proposed solution

The framework follows this traceable chain:

`Business context -> Asset -> CIA impact -> Threat and weakness -> Initial risk -> ISO/NIST outcome -> Treatment -> Owner and evidence -> Residual risk -> Action roadmap`

The main methodology is **Threat Modelling and Risk Assessment**. The earlier 40-study systematic literature review supports requirements and gap analysis. A development model is **not applicable** because this research does not build a production software system. The Python file only demonstrates reproducible scoring.

## Repository structure

- `01_Research_Papers/`: 40-source APA reference list and important-study inventory.
- `02_Literature_Review/`: comparison table, synthesis and research gap.
- `03_Architecture_and_Flowchart/`: proposal architecture and process-flow images.
- `04_Source_Code/`: preliminary risk-scoring script and instructions.
- `05_Data_or_Sample_Input/`: synthetic SME asset and risk records.
- `06_Results_or_Expected_Output/`: generated sample risk register and evaluation plan.
- `07_References/`: standards, research links and attribution notes.

## Evaluation plan

The proposed framework will be compared with a basic unstructured checklist using the same three synthetic scenarios. Metrics are:

- Risk-record completeness: target at least 90%.
- Applicable-control coverage: target at least 80%.
- Treatment traceability: 100% of high and critical risks linked to a treatment, owner and evidence.
- Residual-risk reduction: positive reduction with no untreated critical risk.
- Repeatability: identical inputs produce identical risk levels.
- Baseline improvement: at least 20 percentage points in completeness and traceability.

## Tools

- Python 3 standard library (`csv`, `pathlib`, `collections`)
- CSV files for transparent input and output
- Microsoft Word/Excel/PowerPoint for proposal deliverables
- Git and GitHub for version history and contribution evidence

## Run the preliminary code

From the repository root:

```bash
python 04_Source_Code/risk_assessment.py \
  05_Data_or_Sample_Input/sample_risks.csv \
  06_Results_or_Expected_Output/generated_risk_register.csv
```

Expected console output includes the number of processed risks, counts by risk level and total initial/residual risk. The generated CSV is sorted from the highest initial risk to the lowest.

## Research-objective mapping

| Objective | Supporting evidence | Location |
|---|---|---|
| RO1 | Research papers, literature comparison and gaps | `01_Research_Papers/`, `02_Literature_Review/` |
| RO2 | Architecture, flowchart and transparent scoring logic | `03_Architecture_and_Flowchart/`, `04_Source_Code/` |
| RO3 | Synthetic inputs, generated register and evaluation measures | `05_Data_or_Sample_Input/`, `06_Results_or_Expected_Output/` |

## Group Member Contributions

### Elis Karisha Binti Kamarul Hisam
- Updated research objectives and methodology
- Refined README and repository structure
- Added literature review evidence

### Siti NurDamia Afiqah Binti Azree
- Added literature comparison and research gaps
- Updated supporting studies

### Yusry Bin Zahid
- Added framework architecture and flowchart
- Refined CIA risk-assessment process


## Ethics, limitations and attribution

All sample records are synthetic. No live systems, personal data, credentials or confidential company information are included. This repository does not reproduce copyrighted ISO standard text and does not claim ISO certification. External sources and standards are acknowledged in `07_References/`.

## Project Summary

This project proposes a practical information-security risk assessment framework for Malaysian SMEs based on the CIA triad and aligned with recognised security frameworks.

The framework focuses on making the relationship between business context, assets, security impact, threats, risk scores, security outcomes, treatment actions and residual risks easier to trace.

The framework will be evaluated using synthetic SME scenarios and compared against a basic unstructured checklist using consistent evaluation measures.



