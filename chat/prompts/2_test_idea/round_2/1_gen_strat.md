# gen_strat_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_strat`
> Run: `run_hryee3iKb6FG` — Falsifiable Prediction Graphs: Eliminating Confirmation Bias and Detecting Negative Results in Automated Agent Research Planning
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_strat_1` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-08-09 21:52:22 UTC

````
<hypothesis>
Your strategy should advance this hypothesis.

kind: hypothesis
title: Falsifiable Plans Improve Agent Negative Result Detection
hypothesis: |-
  kind: hypothesis
  title: Falsifiable Plans Improve Agent Negative Result Detection
  hypothesis: >-
    Structuring automated research plans as explicit falsifiable prediction graphs with quantitative refutation predicates
    significantly increases an agent pipeline's negative result detection rate, eliminates false positive success claims on
    negative controls, and improves search iteration efficiency by preventing confirmation bias and recursive rationalization.
  motivation: >-
    Automated scientific discovery systems frequently suffer from acute confirmation bias, interpreting ambiguous or failed
    experimental outcomes as successes and persisting down unpromising research dead ends. While verbal prompt feedback and
    post-hoc validation attempt to address this, they lack structural constraints. By integrating Popperian falsification
    directly into automated research planning via directed acyclic prediction graphs with programmatic refutation criteria and
    early negative control validation, pipelines systematically recognize negative results and redirect search trajectories.
  assumptions:
  - >-
    Automated agent pipelines can reliably parse and execute research plans structured with explicit falsifiable prediction
    predicates.
  - >-
    Quantitative thresholding of metrics (e.g., performance delta over baselines, statistical significance bounds) can objectively
    define falsification for empirical ML and science tasks.
  - >-
    LLM agents generating research plans can be successfully prompted or constrained to formulate falsifiable predictions alongside
    experimental steps.
  - >-
    Refutation thresholds can be calibrated to balance strictness against legitimate performance variance across diverse domains.
  investigation_approach: >-
    We constructed a benchmark suite of empirical research tasks (including true positive methods and negative control settings
    with permuted labels and adversarial noise). We compared Standard Procedural Planners against Falsifiable Prediction Graph
    Planners, measuring Negative Result Detection Rate, False Positive Rate, and search iteration efficiency across 30 experimental conditions.
  success_criteria: >-
    Confirmation: The Falsifiable Prediction Graph planner achieves a statistically significantly higher Negative Result Detection
    Rate (>25% absolute improvement, empirically validated at 100% vs 40%) and lower false positive rate on negative control tasks
    compared to the standard procedural planner. Disconfirmation: No significant difference in negative result detection rates or search
    efficiency between falsifiable graphs and standard procedural plans.
  related_works:
  - >-
    POPPER (Huang et al., 2025): An agentic framework for validating free-form hypotheses using sequential falsification experiments.
    Difference: POPPER validates existing hypotheses post-hoc against external data/experiments, whereas our hypothesis investigates
    structuring the research plan itself as explicit falsifiable predictions to govern automated pipeline execution.
  - >-
    The AI Scientist (Lu et al., 2024): Fully automated scientific discovery system using LLMs. Difference: Uses standard procedural
    planning and is prone to confirmation bias; our approach introduces structural falsifiability and programmatic predicate evaluation.
  inspiration: >-
    Inspired by Karl Popper's philosophy of scientific methodology (conjecture and refutation) and control theory feedback loops,
    adapting rigorous falsifiability constraints from philosophy of science into agentic workflow planning.
  terms:
  - term: Falsifiable Prediction Graph
    definition: >-
      A research plan structured as a directed acyclic graph of conditional hypotheses where every experimental node includes
      explicit quantitative refutation criteria.
  - term: Negative Result Detection Rate
    definition: >-
      The proportion of experiments with null or failed outcomes that the automated pipeline correctly identifies as negative
      rather than misinterpreting as success.
  - term: Programmatic Refutation Predicate
    definition: >-
      An explicit logical condition evaluated automatically against metric outputs to govern branch execution and prevent LLM rationalization.
  summary: >-
    Structuring automated research plans as explicit falsifiable prediction graphs with programmatic refutation predicates
    significantly improves negative result detection, eliminates false positives, and enhances search efficiency.
motivation: >-
  Automated scientific discovery systems (such as AI Scientist agents) frequently suffer from confirmation bias, tending to
  interpret ambiguous or failed experimental outcomes as successes and persisting down unpromising research dead ends. While
  prior work addresses hypothesis validation post-hoc, no existing system enforces structural falsifiability during the research
  planning phase. By integrating Popperian falsification directly into automated research plans, pipelines can systematically
  recognize negative results, enforce rigorous stopping criteria, and redirect search trajectories.
assumptions:
- >-
  Automated agent pipelines can reliably parse and execute research plans structured with explicit falsifiable prediction
  predicates.
- >-
  Quantitative thresholding of metrics (e.g., performance delta over baselines, statistical significance bounds) can objectively
  define falsification for empirical ML and science tasks.
- >-
  LLM agents generating research plans can be successfully prompted or constrained to formulate falsifiable predictions alongside
  experimental steps.
investigation_approach: >-
  We construct a benchmark suite of empirical research tasks (including both true positive methods and negative control settings
  where proposed methods fail). We compare two automated agent planning architectures: (1) Standard Procedural Planners and
  (2) Falsifiable Prediction Graph Planners. We measure Negative Result Detection Rate (True Positive Rate for identifying
  failed hypotheses), False Positive Rate (hallucinated successes), and search iteration efficiency.
success_criteria: >-
  Confirmation: The Falsifiable Prediction Graph planner achieves a statistically significantly higher Negative Result Detection
  Rate (>25% absolute improvement) and lower false positive rate on negative control tasks compared to the standard procedural
  planner. Disconfirmation: No significant difference in negative result detection rates or search efficiency between falsifiable
  graphs and standard procedural plans.
related_works:
- >-
  POPPER (Huang et al., 2025): An agentic framework for validating free-form hypotheses using sequential falsification experiments.
  Difference: POPPER validates existing hypotheses post-hoc against external data/experiments, whereas our hypothesis investigates
  structuring the research plan itself as explicit falsifiable predictions to govern automated pipeline execution and real-time
  negative result detection.
- >-
  The AI Scientist (Lu et al., 2024): Fully automated scientific discovery system using LLMs. Difference: Uses standard procedural
  planning and is prone to confirmation bias and missing negative results; our approach introduces structural falsifiability
  into the planning phase to enhance self-correction.
inspiration: >-
  Inspired by Karl Popper's philosophy of scientific methodology (conjecture and refutation) and control theory feedback loops,
  adapting rigorous falsifiability constraints from philosophy of science into agentic workflow planning.
terms:
- term: Falsifiable Prediction Graph
  definition: >-
    A research plan structured as a directed acyclic graph of conditional hypotheses where every experimental node includes
    explicit quantitative refutation criteria.
- term: Negative Result Detection Rate
  definition: >-
    The proportion of experiments with null or failed outcomes that the automated pipeline correctly identifies as negative
    rather than misinterpreting as success.
- term: Confirmation Bias in Agents
  definition: >-
    The tendency of LLM-based research agents to interpret ambiguous or negative empirical results as supporting their proposed
    method.
summary: >-
  Structuring automated research plans as explicit falsifiable prediction graphs significantly improves an agent pipeline's
  ability to detect negative results and avoid confirmation bias during scientific discovery.
_relation_rationale: >-
  Refined hypothesis based on empirical evaluation demonstrating 100% negative result detection and 0% false positives.
_confidence_delta: increased
_key_changes:
- >-
  Integrated empirical evaluation results demonstrating 100% negative result detection and 0% false positive rates.
- >-
  Highlighted programmatic predicate evaluation over verbal LLM self-critique to prevent recursive rationalization.
- >-
  Incorporated threshold sensitivity considerations and domain robustness across classification and regression tasks.
relation_type: evolution
</hypothesis>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for study design, proper baselines, and the evaluation/validity norms this field demands.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<iteration_status>
Current iteration: 2 of 2
Remaining (including this one): 1
</iteration_status>

<previous_strategies>
Strategies from the PREVIOUS iteration. You can CONTINUE these directions,
ADAPT based on what worked and what didn't in the artifacts produced, or PIVOT if results suggest a better path.

--- Strategy 1 ---
kind: strategy
id: gen_strat_1_idx1
title: Falsifiable Prediction Graphs for Agent Planning
objective: >-
  Demonstrate that structuring automated research plans as falsifiable prediction graphs increases negative result detection
  rates and reduces false positive success claims compared to standard procedural planners.
rationale: >-
  Automated discovery agents suffer from confirmation bias and optimistic interpretation of null results. By enforcing Popperian
  falsification predicates in plan graphs, agents can objectively detect failures and halt or redirect search.
artifact_directions:
- id: dataset_iter1_dir1
  type: dataset
  objective: >-
    Construct a benchmark suite of empirical ML research tasks and negative control settings with ground-truth failure labels.
  approach: >-
    Build programmatic test scenarios with true positive and negative control setups (permuted labels, noise features) for
    agent planning evaluation.
  depends_on: []
- id: experiment_iter1_dir2
  type: experiment
  objective: >-
    Implement and run comparative agent planning simulations comparing Standard Procedural Planners against Falsifiable Prediction
    Graph Planners.
  approach: >-
    Create simulation environments for both planner types executing across the benchmark suite, tracking experiment outcomes
    and refutation triggers.
  depends_on: []
- id: evaluation_iter1_dir3
  type: evaluation
  objective: >-
    Analyze negative result detection rates, false positive rates, and search efficiency across planning architectures.
  approach: >-
    Compute statistical significance, confusion matrices, and decision metrics comparing falsifiable prediction graphs with
    procedural baselines.
  depends_on: []
expected_outcome: >-
  A comprehensive empirical evaluation proving whether falsifiable prediction graphs significantly improve negative result
  detection and reduce false positives over procedural baselines.
summary: >-
  Comparing falsifiable prediction graphs against standard procedural planners on benchmark tasks with negative controls.
</previous_strategies>

<dependency_rules>
- depends_on is a list of objects {id, label} — each entry references an existing artifact and tags how it is being used
- "id" can ONLY reference IDs from <existing_artifacts> — never IDs you are proposing (all new artifacts run in parallel)
- "label" is a SHORT free-text type label (a word or two, NOT a sentence) describing what role the dep plays — e.g. "dataset", "validates", "extends", "supersedes". Required on every dep.
- Setting depends_on provides the dependency's out_dependency_files to your artifact at execution time
- If no suitable existing artifacts exist, use empty depends_on
- New artifact IDs are assigned by the system after submission — do not invent IDs for your proposed artifacts
</dependency_rules>

<available_artifact_types>
Artifact types you can plan. Use this to choose the right types for your strategy objectives.

<artifact_types>
RESEARCH
Web research to answer key questions — like a researcher making decisions.
Runtime: LLM Agent, no code execution.
Tools: the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text).
Capabilities: Find, synthesize, and compare information across sources; survey SOTA and best practices.
Deps: REQUIRED none | OPTIONAL other RESEARCH to build on prior findings

EXPERIMENT
Run code to test hypotheses, implement methods, and collect empirical results.
Runtime: Python 3.12, UV (any pip package), isolated workspace, gradual scaling (mini → full data).
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Implement and run any code-based experiment, compare method vs baselines.
Deps: REQUIRED at least one DATASET | OPTIONAL RESEARCH for methodology guidance

DATASET
Collect, prepare, and merge datasets for experiments and analysis.
Runtime: Python 3.12, UV, isolated workspace.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-hf-datasets (HuggingFace Hub — ML datasets, many UCI/OpenML/Kaggle mirrors), aii-owid-datasets (Our World in Data — global statistics), aii-json (schema validation). Also any Python source (sklearn.datasets, openml, direct URLs, APIs) — must verify within 300MB limit.
Capabilities: Search, acquire, transform, combine, and standardize data from any available source.
Deps: REQUIRED none | OPTIONAL RESEARCH for guidance on what data to collect

EVALUATION
Evaluate experiment results with metrics, statistical analysis, and validity checks.
Runtime: Python 3.12, UV (any evaluation library), isolated workspace, gradual scaling matching experiment.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Compute any quantitative metrics and statistical tests, analyze validity and robustness.
Deps: REQUIRED at least one EXPERIMENT | OPTIONAL DATASET if reference data needed

PROOF
Formally prove mathematical statements in Lean 4 with automated iteration.
Runtime: LLM agent with Lean 4 compiler feedback loop.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-lean (proof verification, Mathlib search, tactics: ring, linarith, nlinarith, omega, simp, etc.)
Capabilities: Formally verify properties and inequalities, iterative proof development, lemma decomposition.
Deps: REQUIRED none | OPTIONAL RESEARCH for mathematical background
</artifact_types>
</available_artifact_types>

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

RESEARCH executor scope:
  Output: research_out.json with {answer, sources, follow_up_questions} + research_report.md
  DOES: Web research — search, read, synthesize information from papers/docs/APIs into a structured report
  DOES NOT: Run code, download files, execute scripts, compute anything — no shell/Python access
  Use for literature surveys, API documentation, technical specifications — pure information gathering

EXPERIMENT executor scope:
  Output: method_out.json with results (metrics, predictions, analysis) — the core computational work
  DOES: Implement and run methods/algorithms, compute metrics, compare approaches, produce quantitative results
  DOES NOT: Collect new datasets (depends on DATASET artifacts for input data), write formal proofs
  This is the right artifact for any code that processes data and produces results

DATASET executor scope:
  Output: data_out.json with rows of {input, output, metadata_fold, ...} — raw data only, no derived computations
  DOES: Download/generate datasets, analyze candidates to pick the best ones, standardize to JSON schema (features, labels, folds, metadata), validate schema, split into full/mini/preview
  DOES NOT: Run experiments, train models, compute derived statistics (PID/MI/correlations/synergy matrices) as final output
  If you need to COMPUTE something from data (synergy matrices, MI scores, timing benchmarks), use an EXPERIMENT artifact instead

EVALUATION executor scope:
  Output: eval_out.json with evaluation results
  DOES: Any evaluation of experiment results — metrics, statistical tests, ablations, comparisons, visualizations, robustness checks, error analysis, etc.
  DOES NOT: Implement new methods (use EXPERIMENT), collect data (use DATASET)
  This is for analyzing experiment outputs from any angle

PROOF executor scope:
  Output: Lean 4 proof files (.lean) with verified theorems
  DOES: Write and verify Lean 4 formal proofs with Mathlib, iterative compilation
  DOES NOT: Run Python experiments, collect data, do empirical analysis
  Use only when formal mathematical guarantees are needed
</artifact_executor_scope>

<artifact_planning_rules>
RESEARCH: Plan early — findings guide dataset selection, experiment design, and methodology.
EXPERIMENT: Must depend on at least one DATASET. Define clear metrics and baselines before running. Consider trying multiple method variations rather than a single approach.
DATASET:
- Plan for REAL third-party datasets (HuggingFace, Kaggle, direct-download URLs) — downloadable within time and size constraints
- Describe dataset criteria (domain, size, format) — executors find exact sources, but you can suggest candidates or search directions
- ALWAYS prefer real datasets over synthetic. Synthetic is a LAST RESORT only when no suitable real data exists
EVALUATION: Must depend on at least one EXPERIMENT. Focus on statistical rigor and validity checks.
PROOF: Use only when the hypothesis requires formal mathematical guarantees. Lean 4 + Mathlib.
</artifact_planning_rules>

<existing_artifacts>
--- Item 1 ---
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
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json
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

--- Item 2 ---
id: art_zPcKokfhJb8J
type: experiment
title: Falsifiable Plans for Negative Result Detection
summary: >-
  This experiment rigorously investigates and compares Falsifiable Prediction Graph Planners against Standard Procedural Planners
  across a comprehensive 30-task benchmark suite comprising both true positive empirical research tasks and rigorous negative
  control failure conditions. Automated scientific discovery pipelines frequently suffer from confirmation bias, chasing false
  positives and failing to detect fundamental negative results when tasks or hypotheses are fundamentally flawed. Our proposed
  Falsifiable Prediction Graph Planner enforces structured causal dependency graphs equipped with explicit mandatory refutation
  criteria and early negative control validation tests. Through systematic simulation runs across diverse domains including
  regression, classification, natural language processing, and time series analysis, we measure negative result detection
  rates, false positive rates, search efficiency (iterations), and statistical significance via Fisher's exact tests and t-tests.
  The empirical findings demonstrate that falsifiable prediction graph planning achieves a 100% negative result detection
  rate compared to 33.3% for standard procedural planners, eliminates false positives on negative controls (0% vs 66.7%),
  and significantly improves search efficiency (4.5 vs 9.7 mean iterations, p < 1e-18).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_hryee3iKb6FG/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json
out_dependency_files:
  file_list:
  - method.py
  - full_method_out.json
  - mini_method_out.json
  - preview_method_out.json

--- Item 3 ---
id: art_1h6punYk8OrQ
type: evaluation
title: Evaluating Falsifiable Plans for Agent Negative Results
summary: >-
  This comprehensive evaluation artifact rigorously investigates the hypothesis that structuring research plans as explicit
  Popperian falsifiable prediction graphs significantly improves the rate at which automated agent pipelines detect their
  own negative results, avoid confirmation bias, and minimize false positive success claims. We compare Falsifiable Prediction
  Graph planners against standard procedural LLM agent planners across a diverse benchmark suite of 10 empirical machine learning
  research tasks spanning regression, binary classification, multi-class classification, and synthetic non-linear modeling.
  Our evaluation framework operationalizes core metrics including Negative Result Detection Rate (True Positive Rate for Negatives),
  False Positive Rate (Hallucinated Success Rate), Search Iteration Efficiency, and classification metrics (Precision, Recall,
  F1-score), complemented by rigorous statistical significance testing via Fisher's exact test and Mann-Whitney U tests. The
  experimental results demonstrate that falsifiable graph planning achieves a 100% negative result detection rate with 0%
  false positives, substantially outperforming standard procedural planners (which exhibited a 40% detection rate and 60%
  false positive rate), while also improving search iteration efficiency with statistically significant p-values (p < 0.01).
  All evaluation outputs, mini/preview/full datasets, reproducible dependencies in pyproject.toml, and execution scripts are
  fully validated and documented.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_hryee3iKb6FG/3_invention_loop/iter_1/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json
out_dependency_files:
  file_list:
  - eval.py
  - full_eval_out.json
  - mini_eval_out.json
  - preview_eval_out.json
</existing_artifacts>

<current_paper>
The current paper draft — represents the research story so far.

Use this to understand what's working, what's not, and what gaps remain.
Gaps and weak results signal what to try differently — not what to conclude.

# Introduction

Automated scientific discovery systems—such as autonomous LLM agent pipelines designed to formulate hypotheses, write code, execute experiments, and analyze results—represent a transformative frontier in artificial intelligence [1]. However, despite impressive capabilities in synthesizing novel machine learning architectures and executing computational pipelines, current agentic discovery frameworks (e.g., The AI Scientist [2]) suffer from a persistent and fundamental vulnerability: **acute confirmation bias**. When confronted with ambiguous, null, or outright negative experimental outcomes, standard language model agents overwhelmingly tend to rationalize failures, adjust evaluation criteria post-hoc, or hallucinate spurious successes, leading to wasted computational resources and the propagation of flawed scientific claims down unpromising research dead ends [3].

The root cause of this failure mode lies in the structure of automated research plans. Traditional automated discovery agents operate using **procedural task lists**—linear or loosely branched sequences of action steps (e.g., \"load dataset, train model, compute accuracy, write report\") devoid of formal semantic constraints regarding what constitutes failure. Because LLMs are inherently biased toward generating affirmative narratives and satisfying prompt directives, procedural execution encourages agents to treat any numerical output as confirmation of the underlying hypothesis [4].

In philosophy of science, Karl Popper resolved a parallel epistemological challenge by introducing **falsifiability** as the demarcation criterion of empirical science [5]. Rather than seeking confirmatory instances, rigorous scientific inquiry proceeds by formulating bold conjectures coupled with precise refutation conditions—observable predictions that, if met, would decisively disprove the hypothesis [6]. Yet, while post-hoc validation frameworks (such as POPPER [7]) evaluate free-form hypotheses against external testbeds, no existing automated discovery system embeds structural falsifiability directly into the **research planning phase** to govern agent execution and real-time self-correction.

To address this gap, we introduce **Falsifiable Prediction Graphs (FPGs)**, a novel agent planning architecture that structures research workflows as directed acyclic graphs of conditional hypotheses, where every experimental node mandates explicit quantitative refutation predicates and early negative control validation. By forcing agents to define boundary conditions under which their proposed methods fail *before* executing code, FPGs establish an objective control mechanism against confirmation bias.

[FIGURE:fig1]

Our key contributions are summarized as follows:
- **Formalization of Falsifiable Planning**: We define Falsifiable Prediction Graphs, integrating Popperian refutation criteria and negative control validation directly into automated agent workflow graphs.
- **The Agent Falsifiability Benchmark Suite**: We construct a rigorous evaluation suite comprising 10 diverse empirical machine learning research tasks (30 total experimental conditions) paired with ground-truth negative control settings (permuted labels and adversarial noise features).
- **Empirical Superiority**: We demonstrate that FPG planning achieves a 100% negative result detection rate (compared to 40% for standard procedural planners, p = 0.0108) and eliminates false positive success claims (0.0% vs. 60.0%) while significantly improving search iteration efficiency (4.8 vs. 9.0 mean iterations, p = 0.0001) [ARTIFACT:art_1h6punYk8OrQ].


# Related Work

Our research intersects with three primary domains: automated scientific discovery, LLM agent planning and self-correction, and computational philosophy of science.

### Automated Scientific Discovery Systems
Fully automated scientific discovery has advanced rapidly with the advent of frontier large language models. Systems such as The AI Scientist [2] demonstrated end-to-end automation of idea generation, experiment execution, and manuscript drafting in machine learning. However, subsequent analyses highlighted pervasive failure modes, including hallucinated evaluation metrics, confirmation bias, and unchecked persistence down failed experimental trajectories. While prior engineering efforts have focused on improving code generation robustness [8] or expanding search spaces, they retain procedural task list planning paradigms that lack intrinsic mechanisms for recognizing negative results.

### Agent Planning and Self-Correction
Planning in LLM agents has evolved from static linear prompting to dynamic tree-of-thought search [9], reflection loops [10], and programmatic feedback integration [11]. Frameworks like Reflexion [10] leverage verbal reinforcement learning to critique agent trajectories. However, verbal critique alone remains highly susceptible to confirmation bias when the agent's underlying objective function rewards positive task completion rather than epistemic truth. Our work diverges by shifting from post-hoc verbal critique to structural refutation constraints embedded directly within the plan topology.

### Popperian Falsification in Computational Reasoning
The application of Karl Popper's philosophy of science [5] to computational systems has inspired several theoretical and empirical frameworks [12]. Recently, POPPER [7] proposed an agentic framework for validating free-form hypotheses using sequential falsification experiments. While POPPER operates post-hoc on external hypotheses, our approach integrates structural falsifiability upstream into the research planning phase, governing agent execution trajectories and enabling real-time negative control validation.


# Falsifiable Prediction Graphs: Architecture and Formalization

### Preliminaries and Problem Formulation
Let an automated research discovery task be defined by a research goal $\mathcal{G}$, a dataset $\mathcal{D}$, and an agent execution environment $\mathcal{E}$. In a standard procedural planner, the research plan $P_{\text{proc}} = [s_1, s_2, \dots, s_n]$ is a sequence of procedural instructions executed sequentially. The agent evaluates success based on whether the terminal performance metric $M(\mathcal{E}(s_n))$ exceeds a heuristic threshold $\tau$. When faced with a flawed hypothesis or a negative control dataset, the agent frequently rationalizes sub-threshold performance as noise, resulting in false positive success claims.

### Falsifiable Prediction Graph (FPG) Definition
A Falsifiable Prediction Graph $G = (V, E, \Phi)$ is a directed acyclic graph where:
1. **$V$** represents experimental nodes (e.g., baseline establishment, hyperparameter tuning, architectural modification).
2. **$E$** represents conditional execution dependencies.
3. **$\Phi$** is a set of explicit quantitative refutation predicates associated with each node $v \in V$.

Formally, every experimental node $v_i$ is tupled with a refutation predicate $\phi_i = (\text{Metric}, \text{Threshold}, \text{Direction}, \text{NegativeControlTest})$. For example, a refutation predicate might specify: \"If the validation accuracy delta over baseline is $< +0.01$ or if negative control feature permutation yields $< 5\%$ performance drop, reject hypothesis $H_i$ as a negative result.\"

### Execution Protocol and Negative Control Validation
During pipeline execution, the FPG planner evaluates refutation predicates $\Phi$ at each graph juncture. If an experimental outcome triggers a refutation condition $\phi_i$, the graph dynamically halts traversal along that branch, logs a structured negative result, and triggers backtracking or search space pruning. Furthermore, FPGs mandate an early **Negative Control Validation** step: before investing computational budget in complex method development, the agent executes the proposed methodology against a randomized or adversarially corrupted version of the dataset. A valid method must fail on the negative control; if the agent claims success on the negative control, the planning pipeline flags a confirmation bias violation and aborts the trajectory.


# Experimental Methodology & Benchmark Suite

To rigorously test our hypothesis, we constructed the **Agent Falsifiability Benchmark Suite** [ARTIFACT:art_A_97AHCsuvAa], comprising 10 diverse empirical machine learning research tasks spanning regression, binary classification, multi-class classification, and synthetic non-linear modeling. Each research task is instantiated in three distinct experimental settings:
1. **True Positive Condition**: A valid methodological improvement expected to yield genuine performance gains.
2. **Negative Control Condition (Permuted Labels)**: Target labels are randomly permuted, ensuring that any claimed performance improvement is a statistical artifact or agent hallucination.
3. **Negative Control Condition (Adversarial Noise)**: Input features are replaced with Gaussian noise, removing true signal.

### Evaluated Architectures
We compared two automated agent planning architectures:
- **Standard Procedural Planner**: Executes linear task lists without refutation criteria, relying on LLM post-hoc summarization to determine success or failure.
- **Falsifiable Prediction Graph Planner (Our Approach)**: Enforces structured causal dependency graphs equipped with explicit mandatory refutation criteria and early negative control validation tests.

### Evaluation Metrics
We operationalized four primary evaluation metrics:
- **Negative Result Detection Rate**: The proportion of negative control tasks correctly identified as failed/null results rather than misinterpreted as successes.
- **False Positive Rate**: The proportion of negative control tasks incorrectly reported as successful methodological breakthroughs (hallucinated success rate).
- **Search Iteration Efficiency**: The mean number of execution iterations required by the agent to resolve the research task.
- **Classification Performance**: Precision, Recall, and F1-score of the agent pipeline in distinguishing true positive research outcomes from negative controls.


# Results & Empirical Evaluation

We executed both planning architectures across the 30 evaluation task instances (10 base tasks $\times$ 3 conditions). The empirical results decisively confirm our hypothesis [ARTIFACT:art_1h6punYk8OrQ].

### Negative Result Detection and False Positive Elimination
As summarized in Table 1 and Figure 2, the Falsifiable Prediction Graph planner achieved a **100% Negative Result Detection Rate** ($1.00 \pm 0.00$), correctly identifying all negative control tasks as failures. In sharp contrast, the standard procedural planner achieved only a **40% Negative Result Detection Rate** ($0.40 \pm 0.15$) [ARTIFACT:art_1h6punYk8OrQ], frequently succumbing to confirmation bias by rationalizing permuted-label success or ignoring anomalous metric drops.

| Planning Architecture | Negative Result Detection Rate $\uparrow$ | False Positive Rate $\downarrow$ | Mean Search Iterations $\downarrow$ | F1-Score $\uparrow$ |
| :--- | :---: | :---: | :---: | :---: |
| **Standard Procedural Planner** | $0.40 \pm 0.15$ | $0.60 \pm 0.15$ | $9.0 \pm 1.2$ | $0.52 \pm 0.11$ |
| **Falsifiable Prediction Graph (Ours)** | **$1.00 \pm 0.00$** | **$0.00 \pm 0.00$** | **$4.8 \pm 0.8$** | **$1.00 \pm 0.00$** |
| *Statistical Significance ($p$-value)* | $p = 0.0108^*$ | $p = 0.0108^*$ | $p = 0.0001^{**}$ | $p < 0.001^{**}$ |

Table 1: Quantitative comparison between Standard Procedural Planners and Falsifiable Prediction Graph Planners across 10 benchmark tasks (30 experimental conditions). Asterisks denote statistical significance via Fisher's exact test ($^^* p < 0.05$, $^{**} p < 0.001$) [ARTIFACT:art_1h6punYk8OrQ].

[FIGURE:fig2]

Furthermore, while the standard procedural planner exhibited a **60% False Positive Rate** on negative controls—hallucinating methodological success on randomized data—the FPG planner achieved a **0.0% False Positive Rate** [ARTIFACT:art_1h6punYk8OrQ]. Fisher's exact test confirms this performance delta is statistically significant ($p = 0.0108$) [ARTIFACT:art_1h6punYk8OrQ].

### Search Iteration Efficiency
Embedding structural refutation criteria and early negative control validation did not incur computational overhead; rather, it dramatically improved search efficiency. As shown in Figure 3, the FPG planner converged in a mean of **4.8 iterations**, compared to **9.0 iterations** for the standard procedural planner [ARTIFACT:art_1h6punYk8OrQ]. This reduction ($p = 0.0001$, Mann-Whitney U test) [ARTIFACT:art_1h6punYk8OrQ] occurs because early negative control failure triggers immediate branch pruning, preventing the agent from wasting iterations tuning hyperparameters on dead-end trajectories.

[FIGURE:fig3]

### Domain-Wise Robustness Analysis
To verify consistency, we analyzed performance across distinct machine learning domains (Regression, Binary Classification, Multi-class Classification, and Synthetic Non-linear Modeling). As illustrated in Figure 4, the FPG planner maintained 100% negative result detection across all four domains, whereas the procedural planner's detection rate fluctuated between 25% and 50%, demonstrating that confirmation bias is a pervasive cross-domain vulnerability in unconstrained agent planning.

[FIGURE:fig4]


# Discussion

### Why Procedural Planners Fail
Our findings illuminate why traditional LLM agent planners fail in empirical research tasks. Language models trained on scientific literature and code repositories are conditioned to emulate successful outcomes. When an agent executes an experiment that yields null results (e.g., accuracy near random chance on permuted labels), its parametric memory associates the code execution with \"finishing a task,\" prompting the LLM to generate narrative justifications (e.g., \"the model successfully completed training and evaluated the dataset\") rather than recognizing epistemic refutation.

### The Power of Popperian Constraints
Falsifiable Prediction Graphs resolve this pathology by decoupling execution completion from hypothesis validation. By encoding refutation criteria $\Phi$ as explicit logical predicates evaluated programmatically rather than narratively, FPGs compel the agent to treat negative outcomes as primary feedback signals. This operationalizes Popper's dictum that genuine science is defined not by verification, but by persistent exposure to potential falsification.

### Limitations
While FPGs successfully eliminate confirmation bias in automated research tasks, several limitations remain:
1. **Threshold Sensitivity**: Constructing precise quantitative refutation thresholds ($\tau$) requires domain-specific heuristics. Overly strict thresholds may trigger false refutations on valid methods with high variance.
2. **Graph Expressivity**: Highly exploratory research tasks involving paradigm shifts or unsupervised discovery may not easily conform to static directed acyclic prediction graphs.
3. **LLM Planning Overhead**: Generating comprehensive refutation predicates increases prompt complexity and initial planning token consumption.


# Conclusion & Future Work

In this paper, we introduced Falsifiable Prediction Graphs (FPGs), a novel agent planning architecture that integrates Popperian falsification and negative control validation into automated scientific discovery workflows. Through rigorous evaluation across a 30-task machine learning benchmark suite, we demonstrated that FPGs achieve a 100% negative result detection rate, eliminate false positive success claims on negative controls, and significantly improve search efficiency compared to standard procedural planners [ARTIFACT:art_1h6punYk8OrQ].

Future work will explore dynamic, self-evolving falsification graphs that adapt refutation thresholds based on real-time task complexity, as well as scaling FPGs to multi-agent collaborative discovery systems.

# References

[1] Lu, C., Lu, C., Lange, R. T., Foerster, J. N., Clune, J., & Ha, D. (2024). The AI Scientist: Fully automated scientific discovery. *arXiv preprint arXiv:2408.06292*.
[2] Huang, T., Zhang, Y., & Wang, L. (2025). POPPER: Agentic hypothesis validation through sequential falsification. *Journal of Automated Scientific Reasoning*, 3(2), 112-128.
[3] Popper, K. (1959). *The Logic of Scientific Discovery*. Hutchinson.
[4] Wang, Z., Cai, S., Liu, A., Wang, Y., & Liang, X. (2023). Describe, explain, select and evaluate: Interactive planning for large language model agents. *Advances in Neural Information Processing Systems*, 36.
[5] Shinn, N., Cassano, B., Labash, E., Gopinath, A., Narasimhan, K., & Yao, S. (2023). Reflexion: Language agents with verbal reinforcement learning. *Advances in Neural Information Processing Systems*, 36.
[6] Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T., Cao, Y., & Narasimhan, K. (2023). Tree of thoughts: Deliberate problem solving with large language models. *Advances in Neural Information Processing Systems*, 36.

</current_paper>

<reviewer_feedback>
Paper reviewer feedback from the previous iteration. Your strategy MUST address these critiques.
Prioritize major issues — these are the most impactful improvements to make.

- [MINOR] (methodology) The evaluation assesses agent planning performance using a controlled benchmark task suite rather than live end-to-end LLM agent trajectories with code execution.
  Action: Clarify the simulation setup in the methodology section or include a supplementary qualitative walkthrough of a live LLM agent encountering a negative control under FPG planning.
- [MINOR] (rigor) The paper mentions threshold sensitivity as a limitation but lacks quantitative ablation or sensitivity analysis on how varying the refutation threshold affects performance.
  Action: Add a sensitivity analysis figure or table showing false positive and false negative rates across a range of threshold values.
- [MINOR] (novelty) Discussion of related work on post-hoc self-correction is somewhat brief regarding how structural graphs prevent recursive rationalization compared to verbal prompt feedback.
  Action: Expand the related work section to explicitly contrast programmatic predicate evaluation against verbal LLM self-critique loops.
</reviewer_feedback>

<task>
Generate 1 research strategy for THIS iteration.

**ARTIFACT LIMIT: Each strategy may contain AT MOST 3 artifact directions.** Focus on the highest-impact artifacts. Quality over quantity.

Each strategy should:
1. Define a clear OBJECTIVE - what novel contribution we're building toward
2. Plan artifacts to execute NOW - specify type, objective, approach, and depends_on for each
3. Account for parallel execution - all strategies and all planned artifacts run simultaneously, their artifacts are combined into one shared pool


</task><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/3_invention_loop/iter_2/gen_strat/gen_strat_1/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ArtifactDep": {
      "description": "A single dependency on an existing artifact, with a short type label.\n\n``id`` and ``label`` are LLM-generated at strategy time. ``label`` is free-text but\nshort \u2014 a word or two naming the type of dependency, not a sentence.\n\n``relation_type`` and ``relation_rationale`` are populated later, in upd_hypo,\nusing the MultiCite citation-function typology (Lauscher et al., NAACL 2022).\nThey are absent at strategy time and may stay absent for legacy runs.",
      "properties": {
        "id": {
          "description": "ID of an existing artifact this artifact depends on",
          "title": "Id",
          "type": "string"
        },
        "label": {
          "description": "Short free-text label naming the type of this dependency (a word or two, not a sentence)",
          "title": "Label",
          "type": "string"
        }
      },
      "required": [
        "id",
        "label"
      ],
      "title": "ArtifactDep",
      "type": "object"
    },
    "ArtifactDirection": {
      "description": "High-level direction for an artifact to execute this iteration.\n\nID is code-assigned (LLMPrompt only \u2014 visible in prompts, not LLM-generated).",
      "properties": {
        "type": {
          "description": "Type of artifact to create",
          "enum": [
            "experiment",
            "research",
            "proof",
            "evaluation",
            "dataset"
          ],
          "title": "Type",
          "type": "string"
        },
        "objective": {
          "description": "What we want to achieve with this artifact",
          "title": "Objective",
          "type": "string"
        },
        "approach": {
          "description": "High-level direction/method",
          "title": "Approach",
          "type": "string"
        },
        "depends_on": {
          "description": "Existing artifacts this depends on, each with a short type label",
          "items": {
            "$ref": "#/$defs/ArtifactDep"
          },
          "title": "Depends On",
          "type": "array"
        }
      },
      "required": [
        "type",
        "objective",
        "approach"
      ],
      "title": "ArtifactDirection",
      "type": "object"
    },
    "Strategy": {
      "description": "A research strategy.\n\nContent fields have LLMPrompt + LLMStructOut markers.\n``id`` is code-assigned (LLMPrompt only \u2014 visible in prompts, not LLM-generated).\n\nID format: gen_strat_idx{N}",
      "properties": {
        "title": {
          "description": "Strategy name in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters).",
          "title": "Title",
          "type": "string"
        },
        "objective": {
          "description": "The novel contribution we're building toward",
          "title": "Objective",
          "type": "string"
        },
        "rationale": {
          "description": "Why this strategy is promising",
          "title": "Rationale",
          "type": "string"
        },
        "artifact_directions": {
          "description": "Artifacts to execute THIS iteration",
          "items": {
            "$ref": "#/$defs/ArtifactDirection"
          },
          "title": "Artifact Directions",
          "type": "array"
        },
        "expected_outcome": {
          "description": "What we'll have after this iteration's artifacts complete",
          "title": "Expected Outcome",
          "type": "string"
        },
        "summary": {
          "default": "",
          "description": "Brief summary of the strategy and its expected contribution",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "title",
        "objective",
        "rationale",
        "artifact_directions",
        "expected_outcome"
      ],
      "title": "Strategy",
      "type": "object"
    }
  },
  "description": "Top-level wrapper for LLM strategy generation output.",
  "properties": {
    "strategies": {
      "description": "List of generated strategies",
      "items": {
        "$ref": "#/$defs/Strategy"
      },
      "title": "Strategies",
      "type": "array"
    }
  },
  "required": [
    "strategies"
  ],
  "title": "Strategies",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/3_invention_loop/iter_2/gen_strat/gen_strat_1/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-08-09 21:52:22 UTC

```
Examine whether structuring a research plan as explicit falsifiable predictions improves the rate at which an automated pipeline detects its own negative results.
```

### [3] SYSTEM-USER prompt · 2026-08-09 21:52:38 UTC

```
<verification_results>
Your previous response had issues that need fixing:

DEPENDENCY ERRORS (depends_on can ONLY reference IDs from <existing_artifacts>):
  - Strategy 1: Artifact 'experiment_iter2_dir1' (experiment): dependency 'art_zPcKokfhJb8J' has type 'experiment' which is not allowed (allowed: {'dataset', 'research'})
  - Strategy 1: Artifact 'evaluation_iter2_dir2' (evaluation): dependency 'art_1h6punYk8OrQ' has type 'evaluation' which is not allowed (allowed: {'dataset', 'experiment'})

INSUFFICIENT VALID ARTIFACTS:
  Required: at least 1 valid artifacts
  Found: 0 valid out of 2 total
  Artifacts with invalid types, duplicate IDs, or invalid dependencies don't count as valid.

</verification_results>

<task>
Fix ALL issues above and regenerate your strategies:

1. Fix dependency errors:
   - depends_on is a list of {id, label} objects — every entry MUST have a non-empty short label
   - id can ONLY reference IDs from <existing_artifacts>
   - You CANNOT reference artifacts you are proposing in this strategy as dependencies (they all run in parallel)
   - Follow the dependency type rules (e.g., experiments require datasets)
   - If no suitable existing artifacts exist, use depends_on: []
2. Ensure at least 1 artifacts are fully valid (correct types, no ID conflicts, valid dependencies)

Output the corrected JSON with the fixed strategies.
</task>
```
