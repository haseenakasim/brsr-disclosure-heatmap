# BRSR Disclosure Quality Heatmap - Nifty 50 Companies

## Project Overview
This project analyzes the quality of BRSR disclosures across Nifty 50 companies. The output is a heatmap visualizing which companies and sectors are genuinely transparent versus those providing vague or missing data.

## Research Question
Do Nifty 50 companies meaningfully disclose ESG data as mandated under SEBI BRSR framework, or do they comply in form while avoiding substance?

## KPI Framework - 11 Indicators

### Environmental - 6 indicators
1. Energy intensity - P6 Q1 - Essential + Core
2. Water consumption - P6 Q3 - Essential + Core
3. GHG Scope 1 emissions - P6 Q7 - Essential + Core
4. GHG Scope 2 emissions - P6 Q7 - Essential + Core
5. Waste generation - P6 Q9 - Essential + Core
6. Scope 3 emissions - P6 Q2 - Leadership

### Social - 5 indicators
7. Health and safety LTIFR - P3 Q11 - Essential + Core
8. Women in workforce percent - P3 Q20 - Essential + Core
9. Differently abled employees - P3 Q20 - Essential
10. Human rights training percent - P5 Q1 - Essential
11. CSR beneficiary outcomes - P8 Q6 - Essential

## KPI Selection Criteria
1. SEBI mandate - All Essential indicators are mandatory under BRSR (SEBI circular May 2021, effective FY2022-23 for top 1000 listed companies).
2. BRSR Core overlap - 7 of 11 KPIs are part of BRSR Core (SEBI circular 2023), requiring third-party assurance for top 150 listed companies.
Governance indicators were excluded due to near-zero variation among large listed companies. Scope 3 was retained to test whether voluntary disclosure ambition correlates with Essential indicator quality.

## Scoring Methodology
Each company is scored 0 to 2 per KPI:
- 0 means not disclosed at all
- 1 means mentioned vaguely or qualitative only
- 2 means quantified with actual data and numbers

## Data Source
Annual reports FY2023-24 of Nifty 50 companies, sourced from BSE/NSE filings. BRSR section reviewed directly.

## Companies Covered
50 companies across sectors, scored alphabetically.

## Output
- data/raw/scores.csv
- data/processed/
- figures/
- notebooks/
