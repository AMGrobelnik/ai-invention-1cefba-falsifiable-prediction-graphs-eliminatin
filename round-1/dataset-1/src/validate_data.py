import json

def validate():
    path = "/ai-inventor/aii_data/runs/run_hryee3iKb6FG/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/full_data_out.json"
    with open(path, "r") as f:
        data = json.load(f)
        
    assert "datasets" in data, "Root must have 'datasets' key"
    assert isinstance(data["datasets"], list), "'datasets' must be a list"
    
    forbidden_per_example_fields = {"split", "dataset", "context"}
    required_per_example_fields = {"input", "output"}
    
    for d_idx, ds in enumerate(data["datasets"]):
        assert "dataset" in ds, f"Dataset at index {d_idx} missing 'dataset' name"
        assert "examples" in ds, f"Dataset {ds.get('dataset')} missing 'examples'"
        assert isinstance(ds["examples"], list), f"Dataset {ds.get('dataset')} 'examples' must be a list"
        
        for e_idx, ex in enumerate(ds["examples"]):
            for req in required_per_example_fields:
                assert req in ex, f"Example {e_idx} in dataset {ds['dataset']} missing required field '{req}'"
            for forb in forbidden_per_example_fields:
                assert forb not in ex, f"Example {e_idx} in dataset {ds['dataset']} contains forbidden field '{forb}'"
            
            # Check metadata fields prefix
            for k in ex.keys():
                if k not in required_per_example_fields:
                    assert k.startswith("metadata_"), f"Non-required field '{k}' in example {e_idx} of dataset {ds['dataset']} must start with 'metadata_'"
                    
    print("Validation passed successfully! All datasets and examples comply with schema requirements.")

if __name__ == "__main__":
    validate()
