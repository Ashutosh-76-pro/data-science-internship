"""Week 3 - Python-based ML model development and evaluation plan.

This project demonstrates a complete binary-classification workflow using
scikit-learn's built-in Breast Cancer Wisconsin dataset.
"""

from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    classification_report,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
    RocCurveDisplay,
)
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier


ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
ARTIFACTS.mkdir(exist_ok=True)


def build_models():
    """Create baseline and candidate models."""
    return {
        "Logistic Regression": Pipeline(
            [
                ("scaler", StandardScaler()),
                ("model", LogisticRegression(max_iter=2000, random_state=42)),
            ]
        ),
        "Decision Tree": DecisionTreeClassifier(max_depth=5, random_state=42),
        "Random Forest": RandomForestClassifier(
            n_estimators=300, max_depth=8, random_state=42, n_jobs=-1
        ),
    }


def main():
    # 1. Load data
    dataset = load_breast_cancer(as_frame=True)
    X = dataset.data
    y = dataset.target

    # 2. Inspect basic structure
    print("Dataset shape:", X.shape)
    print("Missing values:", int(X.isna().sum().sum()))
    print("Class distribution:\n", y.value_counts())

    # 3. Train/test split with stratification for classification balance
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )

    # 4. Candidate model comparison with stratified cross-validation
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    models = build_models()
    cv_rows = []

    for name, model in models.items():
        scores = cross_val_score(model, X_train, y_train, cv=cv, scoring="f1")
        cv_rows.append(
            {
                "Model": name,
                "CV F1 Mean": scores.mean(),
                "CV F1 Std": scores.std(),
            }
        )

    cv_results = pd.DataFrame(cv_rows).sort_values("CV F1 Mean", ascending=False)
    print("\nCross-validation results:\n", cv_results.to_string(index=False))
    cv_results.to_csv(ARTIFACTS / "cross_validation_results.csv", index=False)

    # 5. Select strongest candidate by CV F1 and train it on training data
    best_name = cv_results.iloc[0]["Model"]
    best_model = models[best_name]
    best_model.fit(X_train, y_train)

    # 6. Hold-out test evaluation
    y_pred = best_model.predict(X_test)
    y_prob = best_model.predict_proba(X_test)[:, 1]

    metrics = {
        "Model": best_name,
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred),
        "Recall": recall_score(y_test, y_pred),
        "F1": f1_score(y_test, y_pred),
        "ROC_AUC": roc_auc_score(y_test, y_prob),
    }

    print("\nTest metrics:")
    for key, value in metrics.items():
        if key != "Model":
            print(f"{key}: {value:.4f}")
        else:
            print(f"{key}: {value}")

    pd.DataFrame([metrics]).to_csv(ARTIFACTS / "test_metrics.csv", index=False)

    print("\nClassification report:\n", classification_report(y_test, y_pred, target_names=dataset.target_names))

    # 7. Save confusion matrix
    fig, ax = plt.subplots(figsize=(6, 5))
    ConfusionMatrixDisplay.from_predictions(
        y_test,
        y_pred,
        display_labels=dataset.target_names,
        cmap="Blues",
        ax=ax,
    )
    ax.set_title(f"Confusion Matrix - {best_name}")
    fig.tight_layout()
    fig.savefig(ARTIFACTS / "confusion_matrix.png", dpi=160)
    plt.close(fig)

    # 8. Save ROC curve
    fig, ax = plt.subplots(figsize=(6, 5))
    RocCurveDisplay.from_predictions(y_test, y_prob, ax=ax)
    ax.set_title(f"ROC Curve - {best_name}")
    fig.tight_layout()
    fig.savefig(ARTIFACTS / "roc_curve.png", dpi=160)
    plt.close(fig)

    # 9. Persist the trained pipeline/model
    joblib.dump(best_model, ARTIFACTS / "best_model.joblib")
    print(f"\nSaved model and reports in: {ARTIFACTS}")


if __name__ == "__main__":
    main()
