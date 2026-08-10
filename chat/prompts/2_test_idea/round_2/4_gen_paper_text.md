# gen_paper_text — test_idea

> Phase: `invention_loop` · round 2 · `gen_paper_text`
> Run: `run_hryee3iKb6FG` — Falsifiable Prediction Graphs: Eliminating Confirmation Bias and Detecting Negative Results in Automated Agent Research Planning
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_paper_text` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-08-09 22:07:15 UTC

````
<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for related-work positioning and how this field frames a genuinely novel contribution.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>
<previous_paper>
STARTING POINT: This is your paper draft from the previous iteration.

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

</previous_paper>

<reviewer_feedback>
STEP 1 — REVIEW: A reviewer evaluated the previous paper draft above and produced this feedback.

- [MINOR] (methodology) The evaluation assesses agent planning performance using a controlled benchmark task suite rather than live end-to-end LLM agent trajectories with code execution.
  Action: Clarify the simulation setup in the methodology section or include a supplementary qualitative walkthrough of a live LLM agent encountering a negative control under FPG planning.
- [MINOR] (rigor) The paper mentions threshold sensitivity as a limitation but lacks quantitative ablation or sensitivity analysis on how varying the refutation threshold affects performance.
  Action: Add a sensitivity analysis figure or table showing false positive and false negative rates across a range of threshold values.
- [MINOR] (novelty) Discussion of related work on post-hoc self-correction is somewhat brief regarding how structural graphs prevent recursive rationalization compared to verbal prompt feedback.
  Action: Expand the related work section to explicitly contrast programmatic predicate evaluation against verbal LLM self-critique loops.
</reviewer_feedback>

<pipeline_steps>
STEP 2 — STRATEGY: The pipeline's strategy generator (gen_strat) read the reviewer feedback
and designed a new research strategy to address the critiques.

STEP 3 — PLANNING: The planner (gen_plan) turned the strategy into concrete artifact plans —
specific experiments, datasets, or research tasks to execute.

STEP 4 — EXECUTION: The executor (gen_art) ran those plans and produced the new artifacts
shown in <new_artifacts_this_iteration> below.
</pipeline_steps>

<hypothesis>
STEP 5 — HYPOTHESIS UPDATE: The hypothesis was revised based on evidence from previous iterations.

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

<all_artifacts>
FULL EVIDENCE BASE: All 5 research artifacts across all iterations.

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

--- Item 4 ---
id: art_HjQ6l6qOmCqb
type: experiment
title: Falsifiable Plans for Agent Negative Result Detection
summary: >-
  This experimental artifact evaluates the hypothesis that structuring agent research plans as explicit falsifiable predictions
  and programmatic refutation predicates significantly improves the detection of negative results and avoids confirmation
  bias compared to standard verbal self-correction loops. Using the 10-task Agent Falsifiability Benchmark Suite spanning
  classification and regression domains across true positive and negative control conditions (permuted labels), we performed
  rigorous threshold sweeps from tau = 0.00 to 0.20. The results demonstrate that our programmatic falsifiable graph planner
  achieves an overall negative result detection rate of 87.14% with a false positive rate of only 12.85%, whereas the procedural
  verbal self-correction baseline achieves a detection rate of only 38.57% (61.43% false positive rate), while maintaining
  100% true positive retention. The artifact provides the complete production implementation in method.py, detailed results
  and schema-validated outputs in method_out.json (and full/mini/preview variants), publication-quality vector and raster
  figures (figure_results.pdf/.png), and reproducibility metadata.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_hryee3iKb6FG/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 5 ---
id: art_QUgzY-dCbiIl
type: evaluation
title: Sensitivity and Trace Analysis of Falsifiable Plans
summary: >-
  This evaluation rigorously examines sensitivity curves across refutation thresholds (0.01 to 0.10 delta bounds), computes
  statistical significance and effect sizes (Fisher's exact tests, chi-squared tests, and Cohen's h) for Negative Result Detection
  Rate and False Positive Rate differences, and quantifies the Trajectory Rationalization Index measuring recursive rationalization
  and hallucinated success justifications in agent reasoning traces across domains. The results demonstrate the robust structural
  superiority of falsifiable prediction graphs over standard procedural planners.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_hryee3iKb6FG/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json
</all_artifacts>

<new_artifacts_this_iteration>
NEW THIS ITERATION: These 2 artifacts were created to address the reviewer
feedback. Their findings should be the primary basis for your revisions.

summary: >-
  This experimental artifact evaluates the hypothesis that structuring agent research plans as explicit falsifiable predictions
  and programmatic refutation predicates significantly improves the detection of negative results and avoids confirmation
  bias compared to standard verbal self-correction loops. Using the 10-task Agent Falsifiability Benchmark Suite spanning
  classification and regression domains across true positive and negative control conditions (permuted labels), we performed
  rigorous threshold sweeps from tau = 0.00 to 0.20. The results demonstrate that our programmatic falsifiable graph planner
  achieves an overall negative result detection rate of 87.14% with a false positive rate of only 12.85%, whereas the procedural
  verbal self-correction baseline achieves a detection rate of only 38.57% (61.43% false positive rate), while maintaining
  100% true positive retention. The artifact provides the complete production implementation in method.py, detailed results
  and schema-validated outputs in method_out.json (and full/mini/preview variants), publication-quality vector and raster
  figures (figure_results.pdf/.png), and reproducibility metadata.
id: art_HjQ6l6qOmCqb
title: Falsifiable Plans for Agent Negative Result Detection
type: experiment

summary: >-
  This evaluation rigorously examines sensitivity curves across refutation thresholds (0.01 to 0.10 delta bounds), computes
  statistical significance and effect sizes (Fisher's exact tests, chi-squared tests, and Cohen's h) for Negative Result Detection
  Rate and False Positive Rate differences, and quantifies the Trajectory Rationalization Index measuring recursive rationalization
  and hallucinated success justifications in agent reasoning traces across domains. The results demonstrate the robust structural
  superiority of falsifiable prediction graphs over standard procedural planners.
id: art_QUgzY-dCbiIl
title: Sensitivity and Trace Analysis of Falsifiable Plans
type: evaluation
</new_artifacts_this_iteration>

<data_files>
Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</data_files>

<task>
Write a research paper draft with LaTeX-ready text, BibTeX citations, and figure placeholders.

YOUR TURN (gen_paper_text): Revise the paper.

You are a researcher improving your paper after receiving a conference review.
Take the feedback seriously and make substantive changes, not cosmetic ones.

1. ADDRESS REVIEWER FEEDBACK: For each critique in <reviewer_feedback>, either fix the
   issue in the paper or argue convincingly why it doesn't apply. Major critiques MUST
   be resolved -- they would cause rejection if left unaddressed.
2. USE THE NEW EVIDENCE: The artifacts in <new_artifacts_this_iteration> were created
   specifically to address the reviewer's concerns. Reference their findings to
   strengthen the sections that were flagged as weak.
3. REWRITE, DON'T PATCH: Don't just append new paragraphs. Restructure and rewrite
   the sections the reviewer identified as problematic.
4. MAINTAIN CONSISTENCY: Ensure the paper aligns with the updated hypothesis.
</task>

<figure_instructions>
FIGURE FORMAT: Use [FIGURE:fig_id] markers in paper_text to indicate where each figure goes.
Then provide the full figure specs in the separate `figures` structured output array.
Each figure in the array must have an `id` matching a marker in the text. Set the `aspect_ratio`
field per figure: 21:9 for architecture / pipeline / flow-chart diagrams (the hero figure should
be one of these — place its marker near the END of the Introduction so it floats to the top of
page 2), 16:9 for comparisons / multi-panel results, 4:3 for dense charts, 1:1 for heatmaps /
confusion matrices / scatter plots.

FIGURE TYPE — set `figure_type` on every figure. One test decides it: does the figure plot numbers?
  "data"    — a DATA FIGURE: bars, curves, scatter, heatmaps, confusion matrices, scaling
              laws, distributions, Pareto fronts, ablation deltas. Rendered deterministically
              from the values you supply, so every bar is exactly the height of its number.
  "concept" — a CONCEPT FIGURE: conceptual artwork, architecture and flow diagrams, anything
              with no underlying dataset. Drawn by an image model.
If the figure has real numbers behind it, ALWAYS use "data". An image model only approximates
values: the bars come back close to, but not equal to, the numbers you asked for, and nothing
downstream detects it.

Example in paper_text:
  "...our method achieves state-of-the-art results as shown below.\n\n[FIGURE:fig3]\n\nThe results demonstrate..."

Example in figures array (results comparison — plots numbers, so a data figure):
  {"id": "fig3", "title": "Performance Comparison", "figure_type": "data", "caption": "Comparison of geometric mean query latency across optimizers.", "image_gen_detailed_description": "Grouped bar chart. Categories: PostgreSQL, Bao, RLQOpt. One series 'Latency'. Values: 4.6, 2.8, 2.0 seconds. Errors: 0.8, 0.5, 0.3. X-axis label 'Optimizer'. Y-axis label 'Latency (s)', range 0-5.", "aspect_ratio": "16:9", "summary": "Compares latency across optimizers"}

Example in figures array (architecture diagram, hero — no dataset, so a concept figure):
  {"id": "fig1", "title": "System Architecture", "figure_type": "concept", "caption": "End-to-end pipeline: encoder feeds latents into the planner, which queries the value head before emitting actions.", "image_gen_detailed_description": "Horizontal flow diagram, left to right. Five labeled boxes: 'Input' (gray), 'Encoder' (blue), 'Latent (z, 256-dim)' (light blue, narrow), 'Planner' (green), 'Action Head' (orange). Arrows labeled with shapes. Value head as separate green box below 'Planner', bidirectional arrow. Sans-serif font, clean white background, no 3D.", "aspect_ratio": "21:9", "summary": "Hero architecture diagram"}

CRITICAL: Before writing figure specs, look through artifact workspace output files (*_out.json)
and code to find ALL the exact values. The figure generator cannot read files — every exact number
and value MUST be in the image_gen_detailed_description. For a "data" figure, list the values per series
plus the axis labels and units; the renderer needs the numbers themselves, not a description of
what they look like.
</figure_instructions>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-writing, aii-semscholar-bib.
TODO 2. LITERATURE REVIEW: Use web search tools to research the landscape — search key terms from
<hypothesis> and <all_artifacts>. Then use aii_semscholar_bib__fetch to batch-fetch real
BibTeX entries. Build a comprehensive Related Work section. Do NOT fabricate entries.
TODO 3. READ ARTIFACTS: Before writing each section, READ the relevant artifact source code, output
files, and data in the workspace. Extract concrete implementation details, technical innovations,
algorithmic specifics, and quantitative results. Do NOT write surface-level descriptions.

ARTIFACT REFERENCES: When you reference results, methodology, or findings from a specific artifact,
place an [ARTIFACT:artifact_id] marker inline. These become footnotes linking to the artifact's code
in the GitHub repository (first mention gets a footnote with URL, subsequent mentions are omitted).
Use the exact artifact ID from <all_artifacts>. Place the marker right after the claim it supports.
Example:
  "Our evaluation showed a 15% improvement over baselines [ARTIFACT:art_4f9d2c81ab37]." 
TODO 4. WRITE PAPER: Write the full paper text with [FIGURE:fig_id] markers per <figure_instructions>,
and provide the figure specs in the figures array. Cite with numeric references [1], [2], etc.
At the end of the paper text, include a full bibliography section. Do NOT compile LaTeX or generate
actual image/figure files. Your ONLY output is the structured JSON.
</todos><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FigureSpec": {
      "description": "Figure specification \u2014 structured output from paper writing agent.\n\nThe LLM fills these as a list in PaperText.figures.\nLater converted to Figure objects for viz gen.",
      "properties": {
        "id": {
          "description": "Figure ID matching the [FIGURE:id] marker in paper_text (e.g., 'fig1')",
          "title": "Id",
          "type": "string"
        },
        "title": {
          "description": "Figure title in plain, everyday language \u2014 short and jargon-free. Aim for about 4-8 words (~40 characters).",
          "title": "Title",
          "type": "string"
        },
        "caption": {
          "description": "LaTeX figure caption \u2014 appears below the figure in the paper. Should describe what the figure shows and highlight key takeaways.",
          "title": "Caption",
          "type": "string"
        },
        "figure_type": {
          "description": "Which generator draws this figure. Decide by ONE test: does the figure plot numbers? 'data' \u2014 a DATA FIGURE: bars, curves, scatter, heatmaps, confusion matrices, scaling laws, distributions, Pareto fronts, ablation deltas. Rendered deterministically from the numbers, so every bar is exactly the height of its value. 'concept' \u2014 a CONCEPT FIGURE: conceptual artwork, architecture and flow diagrams, anything with no underlying dataset. When a figure has real numbers behind it, ALWAYS choose 'data': an image model only approximates values, producing bars that disagree with their own labels.",
          "enum": [
            "data",
            "concept"
          ],
          "title": "Figure Type",
          "type": "string"
        },
        "image_gen_detailed_description": {
          "description": "The generator's ONLY input \u2014 it cannot read files. For figure_type='data': every numeric value to plot, per series, with axis labels and units, category names, and what the figure has to make the reader see \u2014 the comparison, trend, trade-off or distribution that is the point. Name a chart type only if you actually want a specific one: the figure generator reads its own catalogue of chart types and picks the one that fits, so an enumeration here would only go stale as that catalogue grows. For figure_type='concept': the composition \u2014 what appears where, colours, labels, and what to leave out.",
          "title": "Image Gen Detailed Description",
          "type": "string"
        },
        "aspect_ratio": {
          "default": "21:9",
          "description": "Shape of the figure. '21:9' for architecture diagrams / pipelines / flow charts (the paper's hero diagram is usually one of these), '16:9' for side-by-side comparisons and multi-panel results, '4:3' for dense charts, '1:1' for heatmaps / confusion matrices / scatter plots, '3:4' or '9:16' for vertical layouts.",
          "enum": [
            "1:1",
            "4:3",
            "3:2",
            "16:9",
            "21:9",
            "3:4",
            "9:16"
          ],
          "title": "Aspect Ratio",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this figure communicates",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "id",
        "title",
        "caption",
        "figure_type",
        "image_gen_detailed_description",
        "summary"
      ],
      "title": "FigureSpec",
      "type": "object"
    }
  },
  "description": "Paper text \u2014 structured output from paper writing agent.\n\nStructured output fields (LLMPrompt + LLMStructOut):\n- title, abstract, paper_text, figures, summary\n\npaper_text contains [FIGURE:fig_id] markers for positioning.\nfigures contains the full specs as structured objects.\n\nMetadata fields (plain, set by pipeline code):\n- id",
  "properties": {
    "title": {
      "description": "Paper title \u2014 clear, plain-language, and short so a non-expert understands the main contribution at a glance. Aim for about 6-10 words; avoid jargon and acronyms.",
      "title": "Title",
      "type": "string"
    },
    "abstract": {
      "description": "Paper abstract",
      "title": "Abstract",
      "type": "string"
    },
    "paper_text": {
      "description": "Full paper body text with markdown section headers (# Introduction, # Methods, # Results, # Discussion, # Conclusion). Use [FIGURE:fig_id] markers (e.g. [FIGURE:fig1]) to indicate where each figure should appear.",
      "title": "Paper Text",
      "type": "string"
    },
    "figures": {
      "description": "List of figure specifications. Each must have an id matching a [FIGURE:id] marker in paper_text.",
      "items": {
        "$ref": "#/$defs/FigureSpec"
      },
      "title": "Figures",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the paper's main contribution and findings",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "abstract",
    "paper_text",
    "summary"
  ],
  "title": "PaperText",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-08-09 22:07:15 UTC

```
Examine whether structuring a research plan as explicit falsifiable predictions improves the rate at which an automated pipeline detects its own negative results.
```

### [3] SKILL-INPUT — aii-paper-writing · 2026-08-09 22:07:21 UTC

The agent loaded the **aii-paper-writing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-writing
description: Academic paper writing guidance for AI research. Covers paper structure, figure placeholders, bibliography building with Semantic Scholar, and citation rules. Does NOT cover LaTeX compilation or figure file generation — see aii-paper-to-latex for that.
---

## Technical Papers

Guidance for the standard "technical paper" format: propose a method/system/framework, evaluate it experimentally, report results. This is the main track at most CS venues (NeurIPS, ICML, ICLR, ACL, AAAI, etc.). Does NOT cover: pure theory/formal proofs, survey papers, position papers, or dataset/benchmark papers — those have different structures.

### Paper Structure

Target 6-8 pages. Use formal academic language, third person. Support claims with evidence from artifacts.

#### Rough Page Budget (8-page paper)

| Section | Pages | Notes |
|---|---|---|
| Abstract | 0.3 | Problem, approach, key result |
| Introduction | 1.0-1.5 | The most important section |
| Related Work | 0.5-1.0 | Beginning or end (see below) |
| Methods | 1.5-2.0 | Architecture fig on page 1 |
| Experiments | 1.5-2.0 | Setup + results + ablations |
| Discussion | 0.5-1.0 | Limitations go here |
| Conclusion | 0.3-0.5 | Do not repeat the abstract |
| References | 0.5-1.0 | Not counted in page limit |

**Critical rule**: A clear new technical contribution must be articulated by page 3 (quarter of the paper). If the reader doesn't know what you did by then, you've lost them.

#### Section Details

**Abstract** (150-250 words): State the problem, your approach, and the main results. Be factual and comprehensive. Do not repeat the abstract word-for-word later in the paper.

**Introduction** — Follow this 5-paragraph structure:

1. **What is the problem?** Define the task concretely.
2. **Why is it interesting and important?** Real-world impact, scale.
3. **Why is it hard?** Why do naive approaches fail?
4. **Why hasn't it been solved before?** What's wrong with prior solutions? How does yours differ?
5. **What are the key components of your approach and results?** Include specific limitations.

End with a "Summary of Contributions" subsection — bullet list of contributions with section references. This doubles as an outline, saving space.

**Related Work** — Placement decision:
- **Beginning** (Section 2): If it can be short yet detailed, or if you need a strong defensive stance against prior work early.
- **End** (before Conclusions): If comparisons require your technical content, or if it can be summarized briefly in the Introduction. Can be titled "Discussion and Related Work."

**Methods/Approach**: Every section tells a story — the story of the results, NOT the story of how you arrived at them. Use top-down description: readers should see where the material is going and be able to skip ahead. Move gory details to appendices.

**Experiments**: Setup (datasets, metrics, baselines) → main results → ablations → analysis. Every claim needs quantitative evidence.

**Discussion**: Interpret results, compare to prior work, state limitations honestly. Limitations should be specific and actionable, not vague disclaimers.

**Conclusion**: Short summarizing paragraph. Do NOT repeat material from the Abstract or Introduction. Make original claims more concrete (e.g., reference quantitative results). Include future work as bullet list — if actively pursuing follow-up, say so to mark territory.

#### Writing Quality Rules

- Define all notation/terminology before use, only once. Group global definitions in Preliminaries.
- Do NOT use nonreferential "this", "that", "these", "it". Always specify the referent. BAD: "This is important because..." GOOD: "This accuracy gap is important because..."
- Do NOT use "etc." unless remaining items are completely obvious. BAD: "We measure volatility, scalability, etc." GOOD: "We measure volatility and scalability."
- Do NOT write "for various reasons" — state the actual reasons.
- "That" is defining, "which" is nondefining. "The algorithms that are easy to implement" vs "The algorithms, which are easy to implement."
- Use italics for definitions and quotes, not for emphasis. Context alone should provide emphasis.

### Figure Format

Figures use a hybrid marker + structured array approach. ALL figures are generated by a separate pipeline step using an AI image model — your `image_gen_detailed_description` is the ONLY input that model sees. It cannot read files or access data. Do NOT generate actual image files yourself (no matplotlib, no PIL, no image generation scripts).

**In paper_text**: Place `[FIGURE:fig_id]` markers where figures should appear.

**In figures array**: Provide full specs as structured objects with these fields:
- `id` — matches the `[FIGURE:id]` marker in paper_text
- `title` — short descriptive title
- `caption` — LaTeX caption that appears below the figure in the paper
- `image_gen_detailed_description` — detailed prompt for the image generator (axes, ALL values, colors, layout)
- `summary` — brief summary of what the figure communicates

Example in paper_text:
```
...our method achieves state-of-the-art results as shown below.

[FIGURE:fig_1]

The results in Figure 1 demonstrate...
```

Example figure spec in figures array:
```json
{"id": "fig_1", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers on JOB benchmark. RLQOpt achieves 2.3x speedup over PostgreSQL.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: ModelA=0.847, ModelB=0.762, Baseline=0.531. Error bars with std: 0.02, 0.03, 0.05. Sans-serif font, white background.", "summary": "Compares accuracy of proposed methods vs baseline."}
```

Every marker in text MUST have a matching figure in the array, and vice versa.

#### Data Precision Requirement

`image_gen_detailed_description` MUST include exact numbers from artifact output files. Read the actual output files before writing figure specs.

- BAD: "Compare accuracy metrics across configurations"
- GOOD: "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: K=3: 0.765, K=5: 0.729, Baseline: 0.121."

#### Figure vs Table Decision

Do NOT create figures for tabular data (rows/columns of text or numbers). Use `\begin{table}` in LaTeX instead. Figures are for actual visualizations only (charts, plots, diagrams).

#### Figure Placement Strategy

Be intentional with figure ordering. The architectural/method overview figure explaining the proposed approach MUST appear early — in the Introduction or at the start of Methods — so readers can immediately orient themselves. Readers skim papers top-down; if the first figure they see is a results bar chart, they have no mental model for interpreting it.

Recommended ordering:
1. **Architecture/method diagram** — Introduction or early Methods (so readers understand the approach before diving into details)
2. **Conceptual/analogy figures** — Introduction or Methods (to build intuition)
3. **Results figures** (bar charts, line plots, scatter plots) — Results section
4. **Analysis/ablation figures** — Discussion or later Results

#### Guidelines

- Plan 3-6 figures total across the paper
- Place [FIGURE:fig_id] markers INLINE where referenced in text
- Include axes, labels, ALL numeric values in figure descriptions
- Both data-driven figures (bar charts, line plots) and conceptual diagrams (architecture, flowcharts)
- Be as detailed as possible in descriptions: specify aspect ratio, preferred colors, all data values, axis labels, ranges, legend entries, and any other visual details. The more specific the description, the better the generated figure

### Bibliography with Semantic Scholar

Build `./references.bib` using the aii-semscholar-bib skill (real BibTeX from Semantic Scholar):

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in one batch
3. Write the returned .bib text into `./references.bib`

Rules:
- Do NOT fabricate BibTeX entries — always fetch from Semantic Scholar
- If a paper isn't found (very recent preprint), write the entry manually as fallback
- Use `\bibliography{references}` and `\bibliographystyle{plainnat}`
- Do NOT use inline `thebibliography` environment

### Citation Format (for Research Artifacts)

When writing research with numbered citations:

1. Every factual claim MUST have a numbered citation: `[1]`, `[2]`, `[1, 3]`, etc.
2. Each source in the "sources" array MUST have an "index" field
3. The index MUST EXACTLY MATCH citation numbers in the text
4. NEVER cite a number without a matching source index
5. Example: "LLMs show 40% improvement with multi-agent collaboration [1]."
````

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-08-09 22:07:21 UTC

The agent loaded the **aii-semscholar-bib** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-semscholar-bib
description: Build bibliographies using Semantic Scholar. Batch-fetch BibTeX for papers by DOI, ArXiv ID, or title. Use when writing papers, generating reference lists, or building .bib files.
---

## Tool: `aii_semscholar_bib__fetch`

Batch-fetch BibTeX entries from Semantic Scholar. Pass all references in a single call — the tool handles batching internally.

### How it works

1. **DOI/ArXiv refs** → batched into POST /paper/batch calls (up to 500 per API call, auto-chunked)
2. **Title-only refs** → individual GET /paper/search/match (1s delay between)
3. **Post-process** → fix entry type, fix citation key (AuthorYYYY), inject DOI

The ability server runs a single worker (`max_threads: 1`). Multiple concurrent tool calls are queued — each runs independently (no cross-request aggregation). Batching happens within each request.

### Input format

```json
{
  "references": [
    {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
    {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
    {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
  ]
}
```

Each reference object can have:
- `doi` — DOI string (ArXiv DOIs like `10.48550/arXiv.XXXX.XXXXX` auto-convert to ArXiv IDs)
- `arxiv` — ArXiv ID (e.g. `"2305.14325"`)
- `title` — Paper title (used for search/match when no DOI/ArXiv)
- `author` — First author last name (for cleaner citation key)
- `year` — Publication year (int, for citation key)

At least one of `doi`, `arxiv`, or `title` is required per reference.

### Output format

```json
{
  "success": true,
  "bib_text": "@inproceedings{Vaswani2017, ...}\n\n@article{Wei2022, ...}",
  "total": 3,
  "found": 3,
  "failed_count": 0,
  "entries": [{"citation_key": "Vaswani2017", "bibtex": "...", "title": "...", "doi": "...", "arxiv": ""}],
  "failed": []
}
```

### Workflow

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in **one call**
3. Save `bib_text` from the response to your `references.bib` file
4. Check `failed` — for any missed papers, follow the **fallback procedure** below

### Fallback for failed references (MANDATORY)

NEVER fabricate BibTeX. For each failed reference:
1. **WebSearch** for `"Title" author year` (try `site:arxiv.org` too)
2. **WebFetch** the paper page → extract title, authors, year, venue, DOI/ArXiv ID
3. If DOI/ArXiv found → retry `aii_semscholar_bib__fetch` with it
4. Last resort: write BibTeX by hand using **only verified info from the actual paper page**

---

### CLI (for manual use / debugging)

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-semscholar-bib" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_semscholar_bib__fetch.py --refs '[
  {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
  {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
  {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
]'
```

`--json, -j` — output raw JSON instead of .bib text

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````
