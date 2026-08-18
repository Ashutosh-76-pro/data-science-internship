# Week 3 — Python-Based Machine Learning Model Development and Evaluation

## Project Overview

This project implements the practical version of the Week 3 internship assignment. It demonstrates a complete binary-classification workflow in Python using the Breast Cancer Wisconsin dataset provided by scikit-learn.

The workflow covers:

1. Problem definition
2. Data loading and inspection
3. Train/test splitting
4. Feature scaling where required
5. Candidate model comparison
6. Stratified 5-fold cross-validation
7. Model selection using F1-score
8. Hold-out test evaluation
9. Accuracy, precision, recall, F1-score and ROC-AUC
10. Confusion matrix and ROC-curve generation
11. Model persistence with Joblib

## Problem Definition

The objective is to classify observations into malignant or benign classes from measured cell features. This is a supervised binary-classification problem. The example is suitable for demonstrating model development because the target is known and the dataset contains multiple numerical predictive features.

> Educational project only: this implementation is intended to demonstrate machine-learning workflow and is not a medical diagnostic system.

## Models Compared

- Logistic Regression — interpretable baseline and effective after feature scaling.
- Decision Tree — easy to interpret and captures non-linear rules.
- Random Forest — ensemble model that can capture non-linear relationships and reduce variance.

The selected model is the candidate with the highest mean cross-validated F1-score on the training split. The final model is then evaluated once on the held-out test set.

## Evaluation Strategy

A stratified 80/20 train-test split is used. The training data is evaluated using 5-fold StratifiedKFold cross-validation. F1-score is used for model selection because it balances precision and recall. The untouched test set is used for final evaluation with accuracy, precision, recall, F1 and ROC-AUC.

## Project Structure

```text
week3-ml-model/
├── README.md
├── requirements.txt
├── src/
│   └── train_model.py
└── artifacts/
    └── generated after execution
```

## How to Run

```bash
cd week3-ml-model
python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt
python src/train_model.py
```

The script automatically creates the `artifacts/` directory and saves:

- `cross_validation_results.csv`
- `test_metrics.csv`
- `confusion_matrix.png`
- `roc_curve.png`
- `best_model.joblib`

## Machine Learning Workflow

```text
Problem Definition
       ↓
Data Loading & Inspection
       ↓
Train / Test Split
       ↓
Preprocessing Pipeline
       ↓
Candidate Models
       ↓
5-Fold Stratified Cross-Validation
       ↓
Model Selection
       ↓
Hold-Out Test Evaluation
       ↓
Metrics + Error Analysis
       ↓
Save Model Artifact
       ↓
Future Deployment & Monitoring
```

## Reproducibility

Random seeds are fixed where applicable. The preprocessing and estimator are kept together in a scikit-learn Pipeline for the Logistic Regression candidate, reducing the risk of inconsistent preprocessing between training and inference.

## Limitations

This repository is a compact educational implementation. A production system would require domain-specific data validation, stronger hyperparameter search, experiment tracking, model governance, monitoring, security controls, drift detection, and an appropriate deployment architecture.
