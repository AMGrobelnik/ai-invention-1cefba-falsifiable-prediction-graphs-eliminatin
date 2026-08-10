# gen_plan_experiment_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_plan`
> Run: `run_hryee3iKb6FG` — Falsifiable Prediction Graphs: Eliminating Confirmation Bias and Detecting Negative Results in Automated Agent Research Planning
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_plan_experiment_1` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-08-09 21:53:00 UTC

````
<hypothesis>
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
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the methods, proper baselines, and evaluation this field demands.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: experiment_iter2_dir1
type: experiment
objective: >-
  Execute threshold sensitivity sweeps and live LLM agent trajectory simulations comparing programmatic refutation predicates
  against verbal self-correction loops on negative controls.
approach: >-
  Run simulation experiments across refutation thresholds tau in {0.00, 0.01, 0.02, 0.05, 0.10} and execute live LLM agent
  planning loops (via OpenRouter) on benchmark tasks with negative controls, logging rationalization vs refutation events.
depends_on:
- id: art_A_97AHCsuvAa
  label: dataset
  relation_type:
  relation_rationale:
</artifact_direction>

<dependencies>
Completed artifacts this artifact can use during execution.

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
</dependencies>

<instructions>
YOUR ROLE: Write a detailed PLAN for the artifact. A separate executor agent runs the actual artifact later.

You are a PLANNER, not an executor. Your output is a plan that tells the executor what to do and how.
Do NOT execute the artifact itself — a separate agent handles that. Your job is to plan it so well that the executor can follow your plan step by step.

You CAN and SHOULD: search the web, read papers, and explore library docs to make your plan concrete.
You CANNOT run shell commands or scripts — code execution is disabled. Research via web tools only.

Do NOT do the executor's job: don't download datasets, don't implement code, don't run experiments, don't write proofs, don't compute evaluations.

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

EXPERIMENT executor scope:
  Output: method_out.json with results (metrics, predictions, analysis) — the core computational work
  DOES: Implement and run methods/algorithms, compute metrics, compare approaches, produce quantitative results
  DOES NOT: Collect new datasets (depends on DATASET artifacts for input data), write formal proofs
  This is the right artifact for any code that processes data and produces results
</artifact_executor_scope>

<artifact_planning_rules>
EXPERIMENT: Must depend on at least one DATASET. Define clear metrics and baselines before running. Consider trying multiple method variations rather than a single approach.
</artifact_planning_rules>


GOOD PLANS: specific, actionable, consider failure scenarios, build on the suggested approach.
BAD PLANS: vague hand-waving, ignoring the suggested approach, missing critical executor details.
</instructions><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_1/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "description": "Plan for an EXPERIMENT artifact.",
  "properties": {
    "title": {
      "description": "Plan title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters).",
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Brief summary",
      "title": "Summary",
      "type": "string"
    },
    "runpod_compute_profile": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "cpu_light",
      "description": "Compute tier for execution \u2014 pick from the available profiles list (e.g., 'gpu', 'cpu_heavy', 'cpu_light'). Only used in RunPod mode.",
      "title": "Runpod Compute Profile"
    },
    "implementation_pseudocode": {
      "description": "High-level pseudocode for the experiment implementation",
      "title": "Implementation Pseudocode",
      "type": "string"
    },
    "fallback_plan": {
      "description": "What to do if the primary approach fails - alternative methods, simplified versions",
      "title": "Fallback Plan",
      "type": "string"
    },
    "testing_plan": {
      "description": "How to validate the experiment works: start with small/fast tests, look for confirmation signals before running full-scale experiments",
      "title": "Testing Plan",
      "type": "string"
    }
  },
  "required": [
    "title",
    "implementation_pseudocode",
    "fallback_plan",
    "testing_plan"
  ],
  "title": "ExperimentPlan",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_1/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-08-09 21:53:00 UTC

```
Examine whether structuring a research plan as explicit falsifiable predictions improves the rate at which an automated pipeline detects its own negative results.
```
