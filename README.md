# Card Transaction Fraud Detection

Score card-not-present transactions for fraud risk and turn that
score into a three-action operating policy (approve / step-up / decline).

This repo is the code and analysis behind the submission. The memo (recommendation, written for the fraud
operations team) is submitted separately.

## Repo structure

```
.
├── README.md
├── notebooks/
│   ├── 00_eda.ipynb                       # first look: class balance, distributions, column decisions
│   ├── 00A_fraud_population_screening.ipynb  # formal check for exclusions (conclusion: none)
│   ├── 01_feature_engineering.ipynb       # builds the model-ready feature set, writes processed parquet
│   └── 02_modelling.ipynb                 # model, policy, out-of-sample results, findings appendix,
│                                           # decision log, and the four business-question answers
└── src/
    └── config.py                          # every constant/path used by the notebooks, in one place
```

Each notebook starts with `cd ../` and `import src.config as config`, so paths resolve relative to the
repo root — that's why `src/config.py` is included even though it isn't standalone code to run.

## Order to read in

`00_eda.ipynb` → `00A_fraud_population_screening.ipynb` → `01_feature_engineering.ipynb` →
`02_modelling.ipynb`. 00 and 00A are exploratory/diagnostic; 01 builds the feature set that 02 reads in
and does everything downstream on.

## What's where (mapped to the brief's deliverables)

| Deliverable | Location |
|---|---|
| Memo | submitted separately |
| Code | `notebooks/`, `src/config.py` |
| Findings appendix (out-of-sample results, worst segments, what didn't matter) | `02_modelling.ipynb`, §9–§10 |
| Decision log (9 entries) | `01_feature_engineering.ipynb` (3) and `02_modelling.ipynb` §13 (6) |
| Confidence / limitations | `02_modelling.ipynb` §13; mirrored in the memo's "Limitations" section |
| Four business questions | `02_modelling.ipynb` §12; answered for a non-technical reader in the memo |
| Three improvements, ranked | `02_modelling.ipynb` §13 (as-built order) and the memo (effort-ranked — the version to go by) |

## Headline results (out-of-sample, ~6.3-month test period)

- **96.5%** of fraud value stopped, **74.9%** of fraud cases, vs. approving everything today
- **~90%** reduction in total expected cost (£19,595/month vs. £187,206/month baseline)
- **~106** genuine transactions/month declined outright, **~2,669**/month sent to step-up (~214 expected
  abandonments)
- Review volume (~275/month, ~9/day) sits comfortably inside the stated 100-cases/day capacity

Full detail, caveats, and how much to trust each number: see `02_modelling.ipynb` §13 and the memo's
"Limitations" section — headline figures are directional (simulated data) and worth re-validating once
live production data is available.

## Notes

- Population screening concluded no exclusions were needed (see `00A_fraud_population_screening.ipynb`);
  a few candidate cutoffs (amount tail, cold-start transactions) were investigated and kept rather than
  dropped, since production sees the same population.
