"""Week 1 optional starter implementation: Customer Churn Prediction.
Uses synthetic data only. Actual code execution is NOT required for Week 1.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score

RANDOM_STATE = 42

def make_synthetic_data(n=1000, seed=RANDOM_STATE):
    rng = np.random.default_rng(seed)
    tenure = rng.integers(1, 73, n)
    monthly_spend = np.round(rng.uniform(300, 5000, n), 2)
    support_tickets = rng.poisson(2, n)
    active_days = rng.integers(1, 31, n)
    plan = rng.choice(["Basic", "Standard", "Premium"], n, p=[.35, .45, .20])
    score = (1.1 - 0.025 * tenure + 0.18 * support_tickets
             - 0.035 * active_days + (plan == "Basic") * 0.25
             + rng.normal(0, 0.6, n))
    probability = 1 / (1 + np.exp(-score))
    churn = (rng.random(n) < probability).astype(int)
    return pd.DataFrame({
        "tenure_months": tenure,
        "monthly_spend": monthly_spend,
        "support_tickets": support_tickets,
        "active_days": active_days,
        "plan": plan,
        "churn": churn,
    })

def build_pipeline():
    numeric = ["tenure_months", "monthly_spend", "support_tickets", "active_days"]
    categorical = ["plan"]
    numeric_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])
    categorical_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore")),
    ])
    preprocess = ColumnTransformer([
        ("num", numeric_pipe, numeric),
        ("cat", categorical_pipe, categorical),
    ])
    return Pipeline([
        ("preprocess", preprocess),
        ("model", LogisticRegression(max_iter=1000, random_state=RANDOM_STATE)),
    ])

def main():
    df = make_synthetic_data()
    X = df.drop(columns="churn")
    y = df["churn"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, stratify=y, random_state=RANDOM_STATE
    )
    model = build_pipeline()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]
    print(classification_report(y_test, predictions))
    print(f"ROC AUC: {roc_auc_score(y_test, probabilities):.3f}")
    y.value_counts().sort_index().plot(kind="bar")
    plt.title("Synthetic Churn Class Distribution")
    plt.xlabel("Churn")
    plt.ylabel("Customers")
    plt.tight_layout()
    plt.savefig("churn_distribution.png", dpi=160)
    plt.close()

if __name__ == "__main__":
    main()
