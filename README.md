# Card Transaction Fraud Detection

Score card-not-present transactions for fraud risk and turn that
score into a three-action operating policy (approve / step-up / decline).

This repo contains the code and analysis.

## Repo structure

```
.
├── README.md
├── notebooks/
│   ├── 00A_eda.ipynb                       # first look: class balance, distributions, column decisions
│   ├── 00B_fraud_population_screening.ipynb  # formal check for exclusions (conclusion: none)
│   ├── 01_feature_engineering.ipynb       # builds the model-ready feature set, writes processed parquet
│   └── 02_modelling.ipynb                 # model, policy, out-of-sample results, findings appendix,
│                                           # decision log, and the four business-question answers
└── src/
    └── config.py                          # every constant/path used by the notebooks, in one place
```

## Order to read in

`00A_eda.ipynb` → `00B_fraud_population_screening.ipynb` → `01_feature_engineering.ipynb` →
`02_modelling.ipynb`. 00A and 00B are exploratory/diagnostic; 01 builds the feature set that 02 reads in
and does everything downstream on.

## What's where

| Deliverable | Location |
|---|---|
| Code | `notebooks/`, `src/config.py` |
| Findings appendix (out-of-sample results, worst segments, what didn't matter) | `02_modelling.ipynb`, §9–§10 |
| Decision log (9 entries) | `01_feature_engineering.ipynb` (3) and `02_modelling.ipynb` §13 (6) |
| Confidence / limitations | `02_modelling.ipynb` §13 |
| Four business questions | `02_modelling.ipynb` §12 |
| Three improvements, ranked | `02_modelling.ipynb` §13 (as-built order) and the memo  |

## Headline results (out-of-sample, ~6.3-month test period)

- **96.5%** of fraud value stopped, **74.9%** of fraud cases, vs. approving everything today
- **~90%** reduction in total expected cost (£19,595/month vs. £187,206/month baseline)
- **~106** genuine transactions/month declined outright, **~2,669**/month sent to step-up (~214 expected
  abandonments)
- Review volume (~275/month, ~9/day) sits comfortably inside the stated 100-cases/day capacity

Full detail, caveats, and how much to trust each number: see `02_modelling.ipynb` §13 and the memo's
"Limitations" section — headline figures are directional (simulated data).

## Notes

- Population screening concluded no exclusions were needed (see `00A_fraud_population_screening.ipynb`);
  a few candidate cutoffs (amount tail, cold-start transactions) were investigated and kept.
