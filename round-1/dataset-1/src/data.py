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

def build_full_dataset():
    datasets_list = []
    
    # Define dataset loader functions
    loaders = [
        ("california_housing", lambda: fetch_california_housing(as_frame=True)),
        ("breast_cancer", lambda: load_breast_cancer(as_frame=True)),
        ("diabetes", lambda: load_diabetes(as_frame=True)),
        ("wine", lambda: load_wine(as_frame=True)),
        ("digits", lambda: load_digits(as_frame=True)),
        ("iris", lambda: load_iris(as_frame=True)),
    ]
    
    for name, loader in loaders:
        data = loader()
        X, y = data.data, data.target
        if isinstance(X, np.ndarray):
            feature_names = [f"feature_{i}" for i in range(X.shape[1])]
            X = pd.DataFrame(X, columns=feature_names)
        else:
            feature_names = list(X.columns)
            
        examples = []
        # Limit rows per dataset to keep dataset size manageable and fast (e.g. max 500 rows per dataset)
        max_rows = min(len(X), 300)
        for idx in range(max_rows):
            row_features = X.iloc[idx].to_dict()
            # Convert numpy types to native Python types
            row_features_clean = {k: float(v) if isinstance(v, (np.floating, float)) else (int(v) if isinstance(v, (np.integer, int)) else v) for k, v in row_features.items()}
            
            input_str = json.dumps(row_features_clean)
            output_str = str(y[idx] if not isinstance(y, pd.Series) else y.iloc[idx])
            
            example = {
                "input": input_str,
                "output": output_str,
                "metadata_row_index": int(idx),
                "metadata_feature_names": feature_names,
                "metadata_task_type": "regression" if name in ["california_housing", "diabetes"] else "classification"
            }
            examples.append(example)
            
        datasets_list.append({
            "dataset": name,
            "examples": examples
        })
        
    # Add 4 synthetic datasets to make 10 total datasets
    for i in range(1, 5):
        if i % 2 == 1:
            X_syn, y_syn = make_classification(n_samples=250, n_features=10, random_state=42 + i)
            task_type = "classification"
            name = f"synthetic_classification_{i}"
        else:
            X_syn, y_syn = make_regression(n_samples=250, n_features=10, random_state=42 + i)
            task_type = "regression"
            name = f"synthetic_regression_{i}"
            
        feature_names = [f"feat_{j}" for j in range(X_syn.shape[1])]
        examples = []
        for idx in range(len(X_syn)):
            row_features = {feature_names[j]: float(X_syn[idx, j]) for j in range(X_syn.shape[1])}
            input_str = json.dumps(row_features)
            output_str = str(y_syn[idx])
            
            example = {
                "input": input_str,
                "output": output_str,
                "metadata_row_index": int(idx),
                "metadata_feature_names": feature_names,
                "metadata_task_type": task_type
            }
            examples.append(example)
            
        datasets_list.append({
            "dataset": name,
            "examples": examples
        })
        
    full_data = {
        "datasets": datasets_list
    }
    
    out_path = "/ai-inventor/aii_data/runs/run_hryee3iKb6FG/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/full_data_out.json"
    with open(out_path, "w") as f:
        json.dump(full_data, f, indent=2)
    print(f"Saved full_data_out.json with {len(datasets_list)} datasets.")

    # Generate preview (first 5 examples per dataset) and mini (first 10 examples total or 2 per dataset) versions
    preview_data = {
        "datasets": [{"dataset": d["dataset"], "examples": d["examples"][:5]} for d in datasets_list]
    }
    with open("/ai-inventor/aii_data/runs/run_hryee3iKb6FG/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/preview_data_out.json", "w") as f:
        json.dump(preview_data, f, indent=2)
        
    mini_data = {
        "datasets": [{"dataset": d["dataset"], "examples": d["examples"][:2]} for d in datasets_list]
    }
    with open("/ai-inventor/aii_data/runs/run_hryee3iKb6FG/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/mini_data_out.json", "w") as f:
        json.dump(mini_data, f, indent=2)
        
    print("Generated preview_data_out.json and mini_data_out.json successfully.")

if __name__ == "__main__":
    build_full_dataset()
