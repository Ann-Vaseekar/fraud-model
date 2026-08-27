from pathlib import Path
import numpy as np

# Paths
RAW_DATA_DIR = Path("src/data/raw")
PROCESSED_DATA_DIR = Path("src/data/processed")

TRAIN_RAW_PATH = RAW_DATA_DIR / "fraudTrain.csv"
TEST_RAW_PATH = RAW_DATA_DIR / "fraudTest.csv"
TRAIN_PROCESSED_PATH = PROCESSED_DATA_DIR / "model_train.parquet"
TEST_PROCESSED_PATH = PROCESSED_DATA_DIR / "model_test.parquet"

# Target / IDs
TARGET_COL = "is_fraud"
ID_COLS = ["cc_num", "trans_time", "amt"]

# Columns
DROP_COLS = [
    "trans_num", "unix_time", "first", "last", "street", "gender", "state", "job", "zip",
]

# Feature engineering parameters
EVENING_RISK_HOURS = [22, 23]
LATE_NIGHT_RISK_HOURS = [0, 1, 2, 3]
CITY_POP_N_BINS = 5
AGE_BIN_EDGES = [0, 25, 35, 45, 55, 65, 100]
AMT_BIN_EDGES = [0, 50, 100, 200, 400, 600, 700, 800, 900, 1000, 1100, 1200, np.inf]


# Feature columns

CATEGORICAL_FEATURE_COLS = [
    "category", "merch_channel", "age_band", "city_pop_band", "amt_band",
]
NUMERIC_FEATURE_COLS = [
    "trans_hour", "trans_dayofweek",
    "is_evening_risk", "is_late_night_risk",
    "time_since_last_trans_mins", "is_first_transaction",
]
FEATURE_COLS = CATEGORICAL_FEATURE_COLS + NUMERIC_FEATURE_COLS

# Business cost assumptions (GBP)
FRAUD_CASE_HANDLING_COST = 25.0
WRONGFUL_DECLINE_COST = 15.0
STEP_UP_COST = 0.30
STEP_UP_GENUINE_ABANDON_RATE = 0.08
STEP_UP_FRAUD_STOP_RATE = 0.90
REVIEW_CAPACITY_PER_DAY = 100
REVIEW_COST_PER_CASE = 4.0
MAX_SCORING_LATENCY_MS = 200
# Step-up abandonment cost is proxied by the wrongful-decline cost.
STEP_UP_ABANDON_COST_PROXY = WRONGFUL_DECLINE_COST
# New assumption — the estimated cost of losing a customer who has been repeatedly declined. Ops flagged "declined
# more than twice in a year" as a material attrition risk; £500 is a proxy CLV estimate.
ATTRITION_COST_PROXY = 500.00
ATTRITION_DECLINE_THRESHOLD = 2   # prior declines in the trailing window that trigger the penalty
ATTRITION_WINDOW_DAYS = 365

RANDOM_SEED = 42
