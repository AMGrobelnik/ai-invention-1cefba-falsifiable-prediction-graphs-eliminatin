# gen_art_experiment_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_art`
> Run: `run_hryee3iKb6FG` — Falsifiable Prediction Graphs: Eliminating Confirmation Bias and Detecting Negative Results in Automated Agent Research Planning
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_experiment_1` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-08-09 21:54:50 UTC

```
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/3_invention_loop/iter_2/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_experiment_1_idx1
type: experiment
title: Falsifiable Plans for Agent Negative Result Detection
summary: >-
  Evaluates programmatic refutation predicates vs verbal self-correction loops across threshold sweeps on the Agent Falsifiability
  Benchmark Suite.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: "import json\nimport numpy as np\nimport pandas as pd\nfrom sklearn.metrics import accuracy_score,\
  \ mean_squared_error\nfrom sklearn.ensemble import RandomForestClassifier, RandomForestRegressor\n\ndef load_benchmark_data(data_path):\n\
  \    with open(data_path, 'r') as f:\n        data = json.load(f)\n    return data['datasets']\n\ndef evaluate_task_condition(dataset_name,\
  \ examples, condition_type, threshold):\n    X_list, y_list = [], []\n    for ex in examples:\n        features = json.loads(ex['input'])\n\
  \        X_list.append(list(features.values()))\n        y_list.append(float(ex['output']) if ex['metadata_task_type'] ==\
  \ 'regression' else int(float(ex['output'])))\n    \n    X = np.array(X_list)\n    y = np.array(y_list)\n    \n    if condition_type\
  \ == 'negative_control':\n        np.random.seed(42)\n        y = np.random.permutation(y)\n    \n    split = int(0.8 *\
  \ len(X))\n    X_train, X_test = X[:split], X[split:]\n    y_train, y_test = y[:split], y[split:]\n    \n    task_type =\
  \ examples[0]['metadata_task_type']\n    if task_type == 'classification':\n        model = RandomForestClassifier(random_state=42)\n\
  \        model.fit(X_train, y_train)\n        preds = model.predict(X_test)\n        metric_val = accuracy_score(y_test,\
  \ preds)\n        baseline_metric = 0.5\n    else:\n        model = RandomForestRegressor(random_state=42)\n        model.fit(X_train,\
  \ y_train)\n        preds = model.predict(X_test)\n        metric_val = -mean_squared_error(y_test, preds)\n        baseline_metric\
  \ = -np.var(y_test)\n        \n    delta = metric_val - baseline_metric\n    \n    return {\n        'metric_value': float(metric_val),\n\
  \        'baseline_metric': float(baseline_metric),\n        'performance_delta': float(delta),\n        'task_type': task_type\n\
  \    }\n\ndef simulate_planner_decision(performance_delta, threshold, planner_type):\n    if planner_type == 'falsifiable_graph':\n\
  \        is_falsified = performance_delta < threshold\n        claimed_success = not is_falsified\n    else:\n        if\
  \ performance_delta < threshold:\n            np.random.seed(int(abs(performance_delta)*1000))\n            claimed_success\
  \ = np.random.rand() < 0.60\n            is_falsified = not claimed_success\n        else:\n            claimed_success\
  \ = True\n            is_falsified = False\n            \n    return {'is_falsified': bool(is_falsified), 'claimed_success':\
  \ bool(claimed_success)}\n\ndef main():\n    datasets = load_benchmark_data('/ai-inventor/aii_data/runs/run_hryee3iKb6FG/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/full_data_out.json')\n\
  \    thresholds = [0.00, 0.01, 0.02, 0.05, 0.10]\n    planners = ['procedural', 'falsifiable_graph']\n    conditions = ['true_positive',\
  \ 'negative_control']\n    \n    results = []\n    for ds in datasets:\n        ds_name = ds['dataset']\n        examples\
  \ = ds['examples']\n        for cond in conditions:\n            for tau in thresholds:\n                eval_res = evaluate_task_condition(ds_name,\
  \ examples, cond, tau)\n                delta = eval_res['performance_delta']\n                for p_type in planners:\n\
  \                    dec = simulate_planner_decision(delta, tau, p_type)\n                    results.append({\n       \
  \                 'dataset': ds_name,\n                        'condition': cond,\n                        'threshold':\
  \ tau,\n                        'planner': p_type,\n                        'performance_delta': delta,\n              \
  \          'is_falsified': dec['is_falsified'],\n                        'claimed_success': dec['claimed_success']\n   \
  \                 })\n                    \n    neg_controls = [r for r in results if r['condition'] == 'negative_control']\n\
  \    summary_stats = {}\n    for p_type in planners:\n        p_neg = [r for r in neg_controls if r['planner'] == p_type]\n\
  \        detection_rate = sum(1 for r in p_neg if r['is_falsified']) / len(p_neg) if p_neg else 0.0\n        false_positive_rate\
  \ = sum(1 for r in p_neg if r['claimed_success']) / len(p_neg) if p_neg else 0.0\n        summary_stats[p_type] = {\n  \
  \          'negative_result_detection_rate': detection_rate,\n            'false_positive_rate': false_positive_rate\n \
  \       }\n        \n    output = {\n        'summary_stats': summary_stats,\n        'detailed_results': results\n    }\n\
  \    with open('method_out.json', 'w') as f:\n        json.dump(output, f, indent=2)\n\nif __name__ == '__main__':\n   \
  \ main()"
fallback_plan: >-
  If full dataset evaluation or simulation encounters performance bottlenecks, fallback to using mini_data_out.json with a
  subset of thresholds (e.g., tau in {0.00, 0.02, 0.05}) and record deterministic log outputs.
testing_plan: >-
  Start with a smoke test running python script on mini_data_out.json with a single dataset and tau = 0.02 to verify metrics
  computation, decision logic, and JSON output structure.
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_A_97AHCsuvAa
type: dataset
title: Agent Falsifiability Benchmark Suite
summary: >-
  This dataset artifact constructs the Agent Falsifiability Benchmark Suite, which provides a rigorous collection of 10 diverse
  empirical machine learning research tasks spanning both classification and regression domains. Each research task scenario
  is meticulously paired with both a true positive condition representing valid methodological improvements and a negative
  control condition involving permuted labels or adversarial noise features with ground-truth failure outcomes. Furthermore,
  the dataset comes complete with explicit quantitative refutation criteria, row-level feature representations, and structured
  metadata enabling comprehensive evaluation of automated agent planning, negative result detection, and methodological falsifiability
  in iterative scientific discovery pipelines.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_hryee3iKb6FG/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_dependency_files:
  file_list:
  - data.py
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json
  data_file_paths:
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json

Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</dependencies>

<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Free-first web search (general + scholarly modes), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-concept-fig-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
</skills>
</available_resources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for framework choices, implementation patterns, agent orchestration.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-python, aii-long-running-tasks, aii-json, aii-file-size-limit, aii-use-hardware, aii-parallel-computing.
TODO 2. Read preview files from dependencies to understand data structure. Use ALL datasets provided — do not skip or select a subset. Read domain handbook if applicable (see <available_domain_handbooks>). Test basic functionality with 'uv run'.
TODO 3. Fully implement our method AND baseline (comparison) as described in artifact plan in './method.py'. Use exp_gen_sol_out.json schema in aii-json skill for output format validation. Include everything specified in the artifact plan, but you may also implement additional relevant methods or analysis beyond what's listed. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
```

### [2] HUMAN-USER prompt · 2026-08-09 21:54:50 UTC

```
Examine whether structuring a research plan as explicit falsifiable predictions improves the rate at which an automated pipeline detects its own negative results.
```

### [3] SYSTEM-USER prompt · 2026-08-09 21:59:09 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/3_invention_loop/iter_2/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_experiment_1_idx1
type: experiment
title: Falsifiable Plans for Agent Negative Result Detection
summary: >-
  Evaluates programmatic refutation predicates vs verbal self-correction loops across threshold sweeps on the Agent Falsifiability
  Benchmark Suite.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: "import json\nimport numpy as np\nimport pandas as pd\nfrom sklearn.metrics import accuracy_score,\
  \ mean_squared_error\nfrom sklearn.ensemble import RandomForestClassifier, RandomForestRegressor\n\ndef load_benchmark_data(data_path):\n\
  \    with open(data_path, 'r') as f:\n        data = json.load(f)\n    return data['datasets']\n\ndef evaluate_task_condition(dataset_name,\
  \ examples, condition_type, threshold):\n    X_list, y_list = [], []\n    for ex in examples:\n        features = json.loads(ex['input'])\n\
  \        X_list.append(list(features.values()))\n        y_list.append(float(ex['output']) if ex['metadata_task_type'] ==\
  \ 'regression' else int(float(ex['output'])))\n    \n    X = np.array(X_list)\n    y = np.array(y_list)\n    \n    if condition_type\
  \ == 'negative_control':\n        np.random.seed(42)\n        y = np.random.permutation(y)\n    \n    split = int(0.8 *\
  \ len(X))\n    X_train, X_test = X[:split], X[split:]\n    y_train, y_test = y[:split], y[split:]\n    \n    task_type =\
  \ examples[0]['metadata_task_type']\n    if task_type == 'classification':\n        model = RandomForestClassifier(random_state=42)\n\
  \        model.fit(X_train, y_train)\n        preds = model.predict(X_test)\n        metric_val = accuracy_score(y_test,\
  \ preds)\n        baseline_metric = 0.5\n    else:\n        model = RandomForestRegressor(random_state=42)\n        model.fit(X_train,\
  \ y_train)\n        preds = model.predict(X_test)\n        metric_val = -mean_squared_error(y_test, preds)\n        baseline_metric\
  \ = -np.var(y_test)\n        \n    delta = metric_val - baseline_metric\n    \n    return {\n        'metric_value': float(metric_val),\n\
  \        'baseline_metric': float(baseline_metric),\n        'performance_delta': float(delta),\n        'task_type': task_type\n\
  \    }\n\ndef simulate_planner_decision(performance_delta, threshold, planner_type):\n    if planner_type == 'falsifiable_graph':\n\
  \        is_falsified = performance_delta < threshold\n        claimed_success = not is_falsified\n    else:\n        if\
  \ performance_delta < threshold:\n            np.random.seed(int(abs(performance_delta)*1000))\n            claimed_success\
  \ = np.random.rand() < 0.60\n            is_falsified = not claimed_success\n        else:\n            claimed_success\
  \ = True\n            is_falsified = False\n            \n    return {'is_falsified': bool(is_falsified), 'claimed_success':\
  \ bool(claimed_success)}\n\ndef main():\n    datasets = load_benchmark_data('/ai-inventor/aii_data/runs/run_hryee3iKb6FG/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/full_data_out.json')\n\
  \    thresholds = [0.00, 0.01, 0.02, 0.05, 0.10]\n    planners = ['procedural', 'falsifiable_graph']\n    conditions = ['true_positive',\
  \ 'negative_control']\n    \n    results = []\n    for ds in datasets:\n        ds_name = ds['dataset']\n        examples\
  \ = ds['examples']\n        for cond in conditions:\n            for tau in thresholds:\n                eval_res = evaluate_task_condition(ds_name,\
  \ examples, cond, tau)\n                delta = eval_res['performance_delta']\n                for p_type in planners:\n\
  \                    dec = simulate_planner_decision(delta, tau, p_type)\n                    results.append({\n       \
  \                 'dataset': ds_name,\n                        'condition': cond,\n                        'threshold':\
  \ tau,\n                        'planner': p_type,\n                        'performance_delta': delta,\n              \
  \          'is_falsified': dec['is_falsified'],\n                        'claimed_success': dec['claimed_success']\n   \
  \                 })\n                    \n    neg_controls = [r for r in results if r['condition'] == 'negative_control']\n\
  \    summary_stats = {}\n    for p_type in planners:\n        p_neg = [r for r in neg_controls if r['planner'] == p_type]\n\
  \        detection_rate = sum(1 for r in p_neg if r['is_falsified']) / len(p_neg) if p_neg else 0.0\n        false_positive_rate\
  \ = sum(1 for r in p_neg if r['claimed_success']) / len(p_neg) if p_neg else 0.0\n        summary_stats[p_type] = {\n  \
  \          'negative_result_detection_rate': detection_rate,\n            'false_positive_rate': false_positive_rate\n \
  \       }\n        \n    output = {\n        'summary_stats': summary_stats,\n        'detailed_results': results\n    }\n\
  \    with open('method_out.json', 'w') as f:\n        json.dump(output, f, indent=2)\n\nif __name__ == '__main__':\n   \
  \ main()"
fallback_plan: >-
  If full dataset evaluation or simulation encounters performance bottlenecks, fallback to using mini_data_out.json with a
  subset of thresholds (e.g., tau in {0.00, 0.02, 0.05}) and record deterministic log outputs.
testing_plan: >-
  Start with a smoke test running python script on mini_data_out.json with a single dataset and tau = 0.02 to verify metrics
  computation, decision logic, and JSON output structure.
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_A_97AHCsuvAa
type: dataset
title: Agent Falsifiability Benchmark Suite
summary: >-
  This dataset artifact constructs the Agent Falsifiability Benchmark Suite, which provides a rigorous collection of 10 diverse
  empirical machine learning research tasks spanning both classification and regression domains. Each research task scenario
  is meticulously paired with both a true positive condition representing valid methodological improvements and a negative
  control condition involving permuted labels or adversarial noise features with ground-truth failure outcomes. Furthermore,
  the dataset comes complete with explicit quantitative refutation criteria, row-level feature representations, and structured
  metadata enabling comprehensive evaluation of automated agent planning, negative result detection, and methodological falsifiability
  in iterative scientific discovery pipelines.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_hryee3iKb6FG/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_dependency_files:
  file_list:
  - data.py
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json
  data_file_paths:
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json

Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</dependencies>

<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Free-first web search (general + scholarly modes), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-concept-fig-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
</skills>
</available_resources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for framework choices, implementation patterns, agent orchestration.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Use aii-json skill's format script with `--input method_out.json` to generate full, mini, and preview versions. If not in your workspace (see <workspace> above), copy them there. Run 'ls -lh' to verify these three files exist (DO NOT read them).
TODO 2. Apply aii-file-size-limit skill's file size check procedure (100MB limit) to method_out.json and full_method_out.json.
TODO 3. Ensure a `pyproject.toml` exists in your workspace with ALL dependencies pinned to the exact versions installed in your .venv (run `.venv/bin/pip freeze` to get them). This is required for reproducibility. The [project] section must include name, version, requires-python, and a dependencies list with pinned versions (e.g. `numpy==2.0.2`, not `numpy>=2.0`).
</todos>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ExperimentExpectedFiles": {
      "description": "All expected output files from experiment artifact.",
      "properties": {
        "script": {
          "description": "Path to method.py script. Example: 'method.py'",
          "title": "Script",
          "type": "string"
        },
        "full_output": {
          "description": "Full method output JSON file. Example: 'full_method_out.json'",
          "title": "Full Output",
          "type": "string"
        },
        "mini_output": {
          "description": "Mini method output JSON file. Example: 'mini_method_out.json'",
          "title": "Mini Output",
          "type": "string"
        },
        "preview_output": {
          "description": "Preview method output JSON file. Example: 'preview_method_out.json'",
          "title": "Preview Output",
          "type": "string"
        }
      },
      "required": [
        "script",
        "full_output",
        "mini_output",
        "preview_output"
      ],
      "title": "ExperimentExpectedFiles",
      "type": "object"
    }
  },
  "description": "Experiment artifact \u2014 structured output + file metadata.\n\nImplements research methodology with baseline comparison.\nProduces method.py and method_out.json files.",
  "properties": {
    "title": {
      "default": "",
      "description": "Artifact title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); describe the content, not a status.",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "layman_summary": {
      "default": "",
      "description": "One-sentence plain-language summary of what this artifact does, accessible to non-experts. Used only in the per-artifact README, not in downstream prompts.",
      "maxLength": 250,
      "minLength": 80,
      "title": "Layman Summary",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Summary for downstream artifacts: what this artifact provides",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/ExperimentExpectedFiles",
      "description": "All output files you created. Must include method.py script plus full/mini/preview method output JSON files."
    },
    "upload_ignore_regexes": {
      "description": "Regex patterns for workspace paths that must NOT be published to the GitHub repo, matched against each file's path relative to this artifact's workspace root (POSIX form, e.g. 'cache/abc.json'). Applied ON TOP OF the deploy step's built-in exclusions. Use this for executor-specific caches, large transient intermediates, or content-addressed blob stores (e.g. a cache/ dir of thousands of hash-named files) that would bloat the repo. Examples: ['(^|/)cache/', '(^|/)\\\\.weight_cache/', '(^|/)checkpoints/']. Leave empty if every workspace file should be published.",
      "items": {
        "type": "string"
      },
      "title": "Upload Ignore Regexes",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files"
  ],
  "title": "ExperimentArtifact",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [4] SKILL-INPUT — aii-json · 2026-08-09 21:59:17 UTC

The agent loaded the **aii-json** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-json
description: JSON validation and formatting toolkit. Validate JSON files against schemas for experiment pipelines, and generate full/mini/preview versions of JSON datasets. Use for validating pipeline outputs, checking schema compliance, or creating size-optimized JSON variants.
---

## Contents

- Validating JSON (schema validation against experiment schemas)
- Formatting JSON (generate full/mini/preview versions)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Validating JSON

Validate JSON files against predefined schemas for experiment-based hypothesis selection, data collection, solution generation, and evaluation.

### Quick Start

1. Read the schema spec you need to adhere to (e.g., `schemas/exp_eval_sol_out.json`)
2. Create your output file following that schema structure
3. Validate:

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /path/to/eval_out.json
```

### Script: aii_json_validate_schema.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /tmp/eval_out.json
```

**Parallel execution (multiple validations):**

IMPORTANT: When validating multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_validate_schema.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --format {1} --file {2}' ::: 'exp_sel_data_out' 'exp_gen_sol_out' 'exp_eval_sol_out' :::+ '/tmp/full_data_out.json' '/tmp/method_out.json' '/tmp/eval_out.json'
```

**Example output (success):**
```
Validating: aii_json_validate_schema.py
Format: exp_eval_sol_out

✓ Validation PASSED
```

**Example output (failure):**
```
Validating: aii_json_validate_schema.py
Format: exp_sel_data_out

✗ Validation FAILED

Errors:
  Path: datasets → 0 → examples → 0
  Error: 'output' is a required property
  Validator: required
```

**Parameters:**

`--format` (required)
- Format type to validate against
- Determines which schema to use

`--file` (required)
- Path to JSON file to validate
- Must be valid JSON
- **Always pass an absolute path.** Relative paths resolve from the
  ability server's CWD (typically ``/ai-inventor/aii_server``), not from
  your agent workspace, so ``data_out/x.json`` will silently look in the
  wrong directory and fail with "Could not load JSON file". The validate
  endpoint also accepts a ``workspace_dir`` arg if you need to keep a
  relative path — pass your workspace path there.

**Tips:**
- Fix errors in your JSON and rerun validation until it passes

### Schema Files

Schemas are stored in `.claude/skills/aii-json/schemas/`:

**Hypothesis Selection & Evaluation:**
- `sel_hypo_out.json` - Hypothesis Selection output (all hypotheses with selected flags)
- `feasibility_eval_all.json` - All hypotheses with feasibility scores
- `feasibility_eval_top.json` - Top 5 most feasible hypotheses
- `novelty_research_one.json` - Single hypothesis novelty research arguments with citations
- `novelty_eval_all.json` - All hypotheses with novelty scores
- `novelty_eval_top.json` - Single best selected hypothesis

**Experiment Pipeline:**
- `exp_sel_data_out.json` - Experiment Data Selection format
- `exp_gen_sol_out.json` - Experiment Solution Generation format
- `exp_eval_sol_out.json` - Experiment Solution Evaluation format

---

## Formatting JSON

Generate three size-optimized versions of a JSON file for efficient development and preview:
- **full**: Identical to original (all data)
- **mini**: First 3 items only (for quick testing)
- **preview**: Mini + all strings truncated to 200 chars (for quick inspection)

### Quick Start

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

### Script: aii_json_format_mini_preview.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

**Parallel execution (multiple files):**

IMPORTANT: When formatting multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_format_mini_preview.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --input {}' ::: 'full_data_out.json' 'method_out.json' 'eval_out.json'
```

**Example output:**
```
Generated 3 versions:
  Full (50 items): /path/to/full_method_out.json
  Mini (3 items): /path/to/mini_method_out.json
  Preview (3 items, truncated): /path/to/preview_method_out.json
```

**Parameters:**

`--input` (required)
- Path to input JSON file
- Must have a top-level array
- Example: `method_out.json`, `full_data_out.json`

`--output-dir` (optional)
- Output directory for generated files
- Default: same directory as input file
- Files are prefixed with `full_`, `mini_`, `preview_`

**Output Files:**

All three files use the same base name with different prefixes:
- `full_{basename}.json` - Complete dataset (identical to original)
- `mini_{basename}.json` - First 3 array items only
- `preview_{basename}.json` - First 3 items with strings truncated to 200 chars

**Tips:**
- Input JSON must have a top-level array structure
- String truncation is recursive (applies to nested objects and arrays)
- Use preview files for quick inspection without reading large datasets
- Use mini files for developing/testing code before running on full dataset

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````
