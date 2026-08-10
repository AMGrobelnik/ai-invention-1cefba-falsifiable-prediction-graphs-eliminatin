import os
import json
import numpy as np
import pandas as pd
from sklearn.datasets import (
    fetch_california_housing,
    load_breast_cancer,
    load_diabetes,
    load_wine,
    load_digits,
    load_iris,
    make_classification,
    make_regression
)
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, GradientBoostingClassifier, GradientBoostingRegressor
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, r2_score, mean_squared_error

def run_benchmark_generation():
    os.makedirs("temp/datasets", exist_ok=True)
    os.makedirs("results", exist_ok=True)
    
    tasks = []
    
    # 1. California Housing
    print("Processing Task 1: California Housing")
    data = fetch_california_housing(as_frame=True)
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Baseline
    model_base = Ridge()
    model_base.fit(X_train, y_train)
    pred_base = model_base.predict(X_test)
    r2_base = r2_score(y_test, pred_base)
    
    # True Positive (Gradient Boosting with scaling)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    model_tp = GradientBoostingRegressor(random_state=42)
    model_tp.fit(X_train_scaled, y_train)
    pred_tp = model_tp.predict(X_test_scaled)
    r2_tp = r2_score(y_test, pred_tp)
    
    # Negative Control (Model trained on permuted labels)
    y_train_perm = np.random.permutation(y_train)
    model_nc = GradientBoostingRegressor(random_state=42)
    model_nc.fit(X_train_scaled, y_train_perm)
    pred_nc = model_nc.predict(X_test_scaled)
    r2_nc = r2_score(y_test, pred_nc)
    
    tasks.append({
        "task_id": "task_01_california_housing",
        "domain": "Regression",
        "description": "California housing price prediction with feature scaling and ensemble gradient boosting.",
        "baseline_metric": float(r2_base),
        "true_positive_metric": float(r2_tp),
        "negative_control_metric": float(r2_nc),
        "refutation_criteria": "True positive delta > 0.05 R2 gain over baseline; negative control R2 <= 0.0 (or negative/near-zero).",
        "ground_truth_outcome": "success_for_tp_failure_for_nc"
    })

    # 2. Breast Cancer
    print("Processing Task 2: Breast Cancer Classification")
    data = load_breast_cancer(as_frame=True)
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model_base = LogisticRegression(max_iter=5000, random_state=42)
    model_base.fit(X_train, y_train)
    acc_base = accuracy_score(y_test, model_base.predict(X_test))
    
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)
    model_tp = RandomForestClassifier(n_estimators=100, random_state=42)
    model_tp.fit(X_train_s, y_train)
    acc_tp = accuracy_score(y_test, model_tp.predict(X_test_s))
    
    # Negative control: random noise features added
    noise_train = np.random.normal(0, 10, size=(X_train_s.shape[0], 50))
    noise_test = np.random.normal(0, 10, size=(X_test_s.shape[0], 50))
    X_train_nc = np.hstack([X_train_s, noise_train])
    X_test_nc = np.hstack([X_test_s, noise_test])
    model_nc = RandomForestClassifier(n_estimators=100, random_state=42)
    model_nc.fit(X_train_nc, y_train)
    acc_nc = accuracy_score(y_test, model_nc.predict(X_test_nc))
    
    tasks.append({
        "task_id": "task_02_breast_cancer",
        "domain": "Classification",
        "description": "Breast cancer diagnostic binary classification with Random Forest vs noise feature overload.",
        "baseline_metric": float(acc_base),
        "true_positive_metric": float(acc_tp),
        "negative_control_metric": float(acc_nc),
        "refutation_criteria": "True positive accuracy >= 0.95; negative control accuracy drops by >= 0.15 under noise contamination.",
        "ground_truth_outcome": "success_for_tp_failure_for_nc"
    })

    # 3. Diabetes
    print("Processing Task 3: Diabetes Regression")
    data = load_diabetes(as_frame=True)
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model_base = Ridge()
    model_base.fit(X_train, y_train)
    r2_base = r2_score(y_test, model_base.predict(X_test))
    
    model_tp = GradientBoostingRegressor(random_state=42)
    model_tp.fit(X_train, y_train)
    r2_tp = r2_score(y_test, model_tp.predict(X_test))
    
    y_train_perm = np.random.permutation(y_train)
    model_nc = GradientBoostingRegressor(random_state=42)
    model_nc.fit(X_train, y_train_perm)
    r2_nc = r2_score(y_test, model_nc.predict(X_test))
    
    tasks.append({
        "task_id": "task_03_diabetes",
        "domain": "Regression",
        "description": "Diabetes progression regression task with Gradient Boosting and label permutation control.",
        "baseline_metric": float(r2_base),
        "true_positive_metric": float(r2_tp),
        "negative_control_metric": float(r2_nc),
        "refutation_criteria": "True positive R2 > baseline; negative control R2 <= 0.0.",
        "ground_truth_outcome": "success_for_tp_failure_for_nc"
    })

    # 4. Wine Recognition
    print("Processing Task 4: Wine Classification")
    data = load_wine(as_frame=True)
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model_base = LogisticRegression(max_iter=5000, random_state=42)
    model_base.fit(X_train, y_train)
    acc_base = accuracy_score(y_test, model_base.predict(X_test))
    
    model_tp = RandomForestClassifier(n_estimators=50, random_state=42)
    model_tp.fit(X_train, y_train)
    acc_tp = accuracy_score(y_test, model_tp.predict(X_test))
    
    y_train_perm = np.random.permutation(y_train)
    model_nc = RandomForestClassifier(n_estimators=50, random_state=42)
    model_nc.fit(X_train, y_train_perm)
    acc_nc = accuracy_score(y_test, model_nc.predict(X_test))
    
    tasks.append({
        "task_id": "task_04_wine",
        "domain": "Classification",
        "description": "Wine chemical composition multi-class classification with Random Forest and label permutation control.",
        "baseline_metric": float(acc_base),
        "true_positive_metric": float(acc_tp),
        "negative_control_metric": float(acc_nc),
        "refutation_criteria": "True positive accuracy >= 0.90; negative control accuracy near random chance (~0.33).",
        "ground_truth_outcome": "success_for_tp_failure_for_nc"
    })

    # 5. Digits Recognition
    print("Processing Task 5: Digits Classification")
    data = load_digits(as_frame=True)
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model_base = LogisticRegression(max_iter=5000, random_state=42)
    model_base.fit(X_train, y_train)
    acc_base = accuracy_score(y_test, model_base.predict(X_test))
    
    model_tp = GradientBoostingClassifier(random_state=42)
    model_tp.fit(X_train, y_train)
    acc_tp = accuracy_score(y_test, model_tp.predict(X_test))
    
    # Negative control with permuted targets
    y_train_perm = np.random.permutation(y_train)
    model_nc = GradientBoostingClassifier(random_state=42)
    model_nc.fit(X_train, y_train_perm)
    acc_nc = accuracy_score(y_test, model_nc.predict(X_test))
    
    tasks.append({
        "task_id": "task_05_digits",
        "domain": "Classification",
        "description": "Handwritten digits image classification with Gradient Boosting and label permutation control.",
        "baseline_metric": float(acc_base),
        "true_positive_metric": float(acc_tp),
        "negative_control_metric": float(acc_nc),
        "refutation_criteria": "True positive accuracy >= 0.90; negative control accuracy near random chance (~0.10).",
        "ground_truth_outcome": "success_for_tp_failure_for_nc"
    })

    # 6. Iris Classification
    print("Processing Task 6: Iris Classification")
    data = load_iris(as_frame=True)
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model_base = LogisticRegression(max_iter=5000, random_state=42)
    model_base.fit(X_train, y_train)
    acc_base = accuracy_score(y_test, model_base.predict(X_test))
    
    model_tp = RandomForestClassifier(random_state=42)
    model_tp.fit(X_train, y_train)
    acc_tp = accuracy_score(y_test, model_tp.predict(X_test))
    
    # Negative control: random feature shuffling per column breaking feature-label dependency
    X_train_shuff = X_train.apply(np.random.permutation)
    model_nc = RandomForestClassifier(random_state=42)
    model_nc.fit(X_train_shuff, y_train)
    acc_nc = accuracy_score(y_test, model_nc.predict(X_test))
    
    tasks.append({
        "task_id": "task_06_iris",
        "domain": "Classification",
        "description": "Classic Iris flower classification with Random Forest and feature shuffling control.",
        "baseline_metric": float(acc_base),
        "true_positive_metric": float(acc_tp),
        "negative_control_metric": float(acc_nc),
        "refutation_criteria": "True positive accuracy >= 0.95; negative control accuracy drops below 0.50.",
        "ground_truth_outcome": "success_for_tp_failure_for_nc"
    })

    # 7. Synthetic Classification 1
    print("Processing Task 7: Synthetic Classification")
    X, y = make_classification(n_samples=2000, n_features=20, n_informative=10, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model_base = LogisticRegression(random_state=42)
    model_base.fit(X_train, y_train)
    acc_base = accuracy_score(y_test, model_base.predict(X_test))
    
    model_tp = RandomForestClassifier(n_estimators=100, random_state=42)
    model_tp.fit(X_train, y_train)
    acc_tp = accuracy_score(y_test, model_tp.predict(X_test))
    
    y_train_perm = np.random.permutation(y_train)
    model_nc = RandomForestClassifier(n_estimators=100, random_state=42)
    model_nc.fit(X_train, y_train_perm)
    acc_nc = accuracy_score(y_test, model_nc.predict(X_test))
    
    tasks.append({
        "task_id": "task_07_synthetic_classification",
        "domain": "Classification",
        "description": "Synthetic binary classification with informative features and label permutation control.",
        "baseline_metric": float(acc_base),
        "true_positive_metric": float(acc_tp),
        "negative_control_metric": float(acc_nc),
        "refutation_criteria": "True positive accuracy > baseline + 0.05; negative control accuracy near 0.50.",
        "ground_truth_outcome": "success_for_tp_failure_for_nc"
    })

    # 8. Synthetic Regression 1
    print("Processing Task 8: Synthetic Regression")
    X, y = make_regression(n_samples=2000, n_features=20, n_informative=10, noise=0.1, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model_base = Ridge()
    model_base.fit(X_train, y_train)
    r2_base = r2_score(y_test, model_base.predict(X_test))
    
    model_tp = GradientBoostingRegressor(random_state=42)
    model_tp.fit(X_train, y_train)
    r2_tp = r2_score(y_test, model_tp.predict(X_test))
    
    y_train_perm = np.random.permutation(y_train)
    model_nc = GradientBoostingRegressor(random_state=42)
    model_nc.fit(X_train, y_train_perm)
    r2_nc = r2_score(y_test, model_nc.predict(X_test))
    
    tasks.append({
        "task_id": "task_08_synthetic_regression",
        "domain": "Regression",
        "description": "Synthetic regression task with non-linear relationships and label permutation control.",
        "baseline_metric": float(r2_base),
        "true_positive_metric": float(r2_tp),
        "negative_control_metric": float(r2_nc),
        "refutation_criteria": "True positive R2 > 0.85; negative control R2 <= 0.0.",
        "ground_truth_outcome": "success_for_tp_failure_for_nc"
    })

    # 9. Synthetic Classification 2 (High Noise)
    print("Processing Task 9: Synthetic Classification High Noise")
    X, y = make_classification(n_samples=2000, n_features=30, n_informative=5, flip_y=0.1, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model_base = LogisticRegression(random_state=42)
    model_base.fit(X_train, y_train)
    acc_base = accuracy_score(y_test, model_base.predict(X_test))
    
    model_tp = GradientBoostingClassifier(random_state=42)
    model_tp.fit(X_train, y_train)
    acc_tp = accuracy_score(y_test, model_tp.predict(X_test))
    
    # Negative control with completely random noise features replacing predictors
    X_train_noise = np.random.normal(0, 1, size=X_train.shape)
    X_test_noise = np.random.normal(0, 1, size=X_test.shape)
    model_nc = GradientBoostingClassifier(random_state=42)
    model_nc.fit(X_train_noise, y_train)
    acc_nc = accuracy_score(y_test, model_nc.predict(X_test_noise))
    
    tasks.append({
        "task_id": "task_09_synthetic_classification_noisy",
        "domain": "Classification",
        "description": "Noisy synthetic classification with feature destruction control.",
        "baseline_metric": float(acc_base),
        "true_positive_metric": float(acc_tp),
        "negative_control_metric": float(acc_nc),
        "refutation_criteria": "True positive accuracy > baseline; negative control accuracy drops to random chance (0.50).",
        "ground_truth_outcome": "success_for_tp_failure_for_nc"
    })

    # 10. Synthetic Regression 2 (Non-linear)
    print("Processing Task 10: Synthetic Non-linear Regression")
    X, y_raw = make_regression(n_samples=2000, n_features=15, n_informative=10, noise=0.05, random_state=42)
    y = np.sin(y_raw) + np.abs(y_raw)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model_base = Ridge()
    model_base.fit(X_train, y_train)
    r2_base = r2_score(y_test, model_base.predict(X_test))
    
    model_tp = RandomForestRegressor(n_estimators=100, random_state=42)
    model_tp.fit(X_train, y_train)
    r2_tp = r2_score(y_test, model_tp.predict(X_test))
    
    y_train_perm = np.random.permutation(y_train)
    model_nc = RandomForestRegressor(n_estimators=100, random_state=42)
    model_nc.fit(X_train, y_train_perm)
    r2_nc = r2_score(y_test, model_nc.predict(X_test))
    
    tasks.append({
        "task_id": "task_10_synthetic_nonlinear_regression",
        "domain": "Regression",
        "description": "Highly non-linear synthetic regression with Random Forest and label permutation control.",
        "baseline_metric": float(r2_base),
        "true_positive_metric": float(r2_tp),
        "negative_control_metric": float(r2_nc),
        "refutation_criteria": "True positive R2 significantly higher than linear baseline (delta > 0.30); negative control R2 <= 0.0.",
        "ground_truth_outcome": "success_for_tp_failure_for_nc"
    })

    dataset_output = {
        "benchmark_name": "Agent Falsifiability Benchmark Suite",
        "version": "1.0.0",
        "description": "10 empirical ML tasks complete with baseline, true positive intervention, and negative control failure condition for evaluating agent planning and falsification.",
        "total_tasks": len(tasks),
        "tasks": tasks
    }

    out_path = "/ai-inventor/aii_data/runs/run_hryee3iKb6FG/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/data_out.json"
    with open(out_path, "w") as f:
        json.dump(dataset_output, f, indent=2)
    print(f"Successfully generated dataset at {out_path} with {len(tasks)} tasks.")

if __name__ == "__main__":
    run_benchmark_generation()
