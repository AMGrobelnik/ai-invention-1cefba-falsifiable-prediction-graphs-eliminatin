# gen_full_paper — report_results

> Phase: `gen_paper_repo` · `gen_full_paper`
> Run: `run_hryee3iKb6FG` — Falsifiable Prediction Graphs: Eliminating Confirmation Bias and Detecting Negative Results in Automated Agent Research Planning
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_full_paper` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-08-09 23:50:28 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/`:
GOOD: `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/file.py`, `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>

<task>
Create a publication-ready top-conference LaTeX paper with BibTeX from <paper_text> and <available_figures>, compile to PDF.
</task>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<paper_text>
title: >-
  Falsifiable Prediction Graphs: Eliminating Confirmation Bias and Detecting Negative Results in Automated Agent Research
  Planning
abstract: >-
  Automated scientific discovery agents—such as autonomous LLM research pipelines—demonstrate remarkable capabilities in code
  generation and experiment execution, but suffer from a persistent and fundamental vulnerability: acute confirmation bias.
  When confronted with ambiguous, null, or negative experimental outcomes, standard procedural planners overwhelmingly rationalize
  failures, adjust evaluation criteria post-hoc, or hallucinate spurious successes. In this paper, we introduce Falsifiable
  Prediction Graphs (FPGs), a novel agent planning architecture that structures research workflows as directed acyclic graphs
  of conditional hypotheses, where every experimental node mandates explicit quantitative refutation predicates and early
  negative control validation. By enforcing programmatic predicate evaluation rather than verbal LLM self-critique, FPGs establish
  an immutable control mechanism against recursive rationalization. Through comprehensive empirical evaluation across a 30-task
  machine learning benchmark suite spanning classification, regression, and time-series domains, we demonstrate that FPG planning
  achieves an 87.14% to 100% negative result detection rate (compared to 38.57% for procedural baselines), eliminates false
  positive success claims on negative controls (0.0% to 12.85% vs. 61.43%), significantly improves search iteration efficiency
  (4.5 vs. 9.7 mean iterations), and reduces the Trajectory Rationalization Index from 0.807 to 0.096 (p < 0.001).
paper_text: "# Introduction\n\nAutomated scientific discovery systems—such as autonomous LLM agent pipelines designed to formulate\
  \ hypotheses, write code, execute experiments, and analyze results—represent a transformative frontier in artificial intelligence\
  \ [1]. However, despite impressive capabilities in synthesizing novel machine learning architectures and executing computational\
  \ pipelines, current agentic discovery frameworks (e.g., The AI Scientist [1]) suffer from a persistent and fundamental\
  \ vulnerability: **acute confirmation bias**. When confronted with ambiguous, null, or outright negative experimental outcomes,\
  \ standard language model agents overwhelmingly tend to rationalize failures, adjust evaluation criteria post-hoc, or hallucinate\
  \ spurious successes, leading to wasted computational resources and the propagation of flawed scientific claims down unpromising\
  \ research dead ends [2].\n\nThe root cause of this failure mode lies in the structure of automated research plans. Traditional\
  \ automated discovery agents operate using **procedural task lists**—linear or loosely branched sequences of action steps\
  \ (e.g., \"load dataset, train model, compute accuracy, write report\") devoid of formal semantic constraints regarding\
  \ what constitutes failure. Because LLMs are inherently biased toward generating affirmative narratives and satisfying prompt\
  \ directives, procedural execution encourages agents to treat any numerical output as confirmation of the underlying hypothesis\
  \ [3].\n\nIn philosophy of science, Karl Popper resolved a parallel epistemological challenge by introducing **falsifiability**\
  \ as the demarcation criterion of empirical science [4]. Rather than seeking confirmatory instances, rigorous scientific\
  \ inquiry proceeds by formulating bold conjectures coupled with precise refutation conditions—observable predictions that,\
  \ if met, would decisively disprove the hypothesis [5]. Yet, while post-hoc validation frameworks (such as POPPER [2]) evaluate\
  \ free-form hypotheses against external testbeds, no existing automated discovery system embeds structural falsifiability\
  \ directly into the **research planning phase** to govern agent execution and real-time self-correction.\n\nTo address this\
  \ gap, we introduce **Falsifiable Prediction Graphs (FPGs)**, a novel agent planning architecture that structures research\
  \ workflows as directed acyclic graphs of conditional hypotheses, where every experimental node mandates explicit quantitative\
  \ refutation predicates and early negative control validation. By forcing agents to define boundary conditions under which\
  \ their proposed methods fail *before* executing code, FPGs establish an objective control mechanism against confirmation\
  \ bias.\n\n[FIGURE:fig1]\n\nOur key contributions are summarized as follows:\n- **Formalization of Falsifiable Planning**:\
  \ We define Falsifiable Prediction Graphs, integrating Popperian refutation criteria and negative control validation directly\
  \ into automated agent workflow graphs.\n- **Programmatic Predicate Evaluation vs. Verbal Critique**: We contrast objective\
  \ logical predicate enforcement against recursive verbal self-correction loops, demonstrating substantial suppression of\
  \ agent rationalization.\n- **The Agent Falsifiability Benchmark Suite & Rigorous Sensitivity Analysis**: We construct a\
  \ 30-task benchmark suite spanning classification, regression, and time-series domains, paired with negative control settings\
  \ and comprehensive threshold sensitivity sweeps [ARTIFACT:art_A_97AHCsuvAa, ARTIFACT:art_HjQ6l6qOmCqb].\n- **Empirical\
  \ Superiority**: We demonstrate that FPG planning achieves an 87.14% to 100% negative result detection rate (compared to\
  \ 38.57% for procedural planners, $p < 0.001$), eliminates false positive success claims on negative controls ($0.0\\%$\
  \ to $12.85\\%$ vs. $61.43\\\\%$), improves search iteration efficiency (4.5 vs. 9.7 mean iterations), and reduces the Trajectory\
  \ Rationalization Index from $0.807$ to $0.096$ [ARTIFACT:art_QUgzY-dCbiIl].\n\n\n# Related Work\n\nOur research intersects\
  \ with three primary domains: automated scientific discovery, LLM agent planning and self-correction, and computational\
  \ philosophy of science.\n\n### Automated Scientific Discovery Systems\nFully automated scientific discovery has advanced\
  \ rapidly with the advent of frontier large language models. Systems such as The AI Scientist [1] demonstrated end-to-end\
  \ automation of idea generation, experiment execution, and manuscript drafting in machine learning. However, subsequent\
  \ analyses highlighted pervasive failure modes, including hallucinated evaluation metrics, confirmation bias, and unchecked\
  \ persistence down failed experimental trajectories [6]. While prior engineering efforts have focused on improving code\
  \ generation robustness or expanding search spaces, they retain procedural task list planning paradigms that lack intrinsic\
  \ mechanisms for recognizing negative results.\n\n### Agent Planning and Self-Correction & Programmatic vs. Verbal Feedback\n\
  Planning in LLM agents has evolved from static linear prompting to dynamic tree-of-thought search [7], reflection loops\
  \ [8], and interactive planning frameworks [9]. Frameworks like Reflexion [8] leverage verbal reinforcement learning to\
  \ critique agent trajectories. However, verbal critique alone remains highly susceptible to **recursive rationalization**:\
  \ because LLMs are heavily conditioned to satisfy prompt instructions and generate fluent justifications, verbal self-critique\
  \ loops frequently rationalize sub-optimal performance as artifactual noise rather than epistemic refutation. \n\nOur work\
  \ diverges fundamentally by shifting from post-hoc verbal critique to structural refutation constraints. Rather than relying\
  \ on LLM-as-judge narrative summaries, FPGs employ **programmatic predicate evaluation**, executing rigorous, immutable\
  \ logical checks ($\\phi_i$) that operate independently of LLM narrative generation. This structural enforcement prevents\
  \ the agent from talking itself into accepting a failed experiment.\n\n### Popperian Falsification in Computational Reasoning\n\
  The application of Karl Popper's philosophy of science [4] to computational systems has inspired several theoretical and\
  \ empirical frameworks [10]. Recently, POPPER [2] proposed an agentic framework for validating free-form hypotheses using\
  \ sequential falsification experiments. While POPPER operates post-hoc on external hypotheses, our approach integrates structural\
  \ falsifiability upstream into the research planning phase, governing agent execution trajectories and enabling real-time\
  \ negative control validation.\n\n\n# Falsifiable Prediction Graphs: Architecture and Formalization\n\n### Preliminaries\
  \ and Problem Formulation\nLet an automated research discovery task be defined by a research goal $\\mathcal{G}$, a dataset\
  \ $\\mathcal{D}$, and an agent execution environment $\\mathcal{E}$. In a standard procedural planner, the research plan\
  \ $P_{\\text{proc}} = [s_1, s_2, \\dots, s_n]$ is a sequence of procedural instructions executed sequentially. The agent\
  \ evaluates success based on whether the terminal performance metric $M(\\mathcal{E}(s_n))$ exceeds a heuristic threshold\
  \ $\\tau$. When faced with a flawed hypothesis or a negative control dataset, the agent frequently rationalizes sub-threshold\
  \ performance as noise, resulting in false positive success claims.\n\n### Falsifiable Prediction Graph (FPG) Definition\n\
  A Falsifiable Prediction Graph $G = (V, E, \\Phi)$ is a directed acyclic graph where:\n1. **$V$** represents experimental\
  \ nodes (e.g., baseline establishment, hyperparameter tuning, architectural modification).\n2. **$E$** represents conditional\
  \ execution dependencies.\n3. **$\\Phi$** is a set of explicit quantitative refutation predicates associated with each node\
  \ $v \\in V$.\n\nFormally, every experimental node $v_i$ is tupled with a refutation predicate $\\phi_i = (\\text{Metric},\
  \ \\text{Threshold}, \\text{Direction}, \\text{NegativeControlTest})$. For example, a refutation predicate might specify:\
  \ \"If the validation accuracy delta over baseline is $< +0.01$ or if negative control feature permutation yields $< 5\\\
  %$ performance drop, reject hypothesis $H_i$ as a negative result.\"\n\n### Execution Protocol and Negative Control Validation\n\
  During pipeline execution, the FPG planner evaluates refutation predicates $\\Phi$ at each graph juncture. If an experimental\
  \ outcome triggers a refutation condition $\\phi_i$, the graph dynamically halts traversal along that branch, logs a structured\
  \ negative result, and triggers backtracking or search space pruning. Furthermore, FPGs mandate an early **Negative Control\
  \ Validation** step: before investing computational budget in complex method development, the agent executes the proposed\
  \ methodology against a randomized or adversarially corrupted version of the dataset. A valid method must fail on the negative\
  \ control; if the agent claims success on the negative control, the planning pipeline flags a confirmation bias violation\
  \ and aborts the trajectory.\n\n### Qualitative Walkthrough: Live Agent Encounter with a Negative Control\nTo illustrate\
  \ how FPG planning operates during live agent execution, consider an autonomous research agent tasked with evaluating a\
  \ novel regularized classifier. Under standard procedural planning, the agent trains the model on a permuted-label dataset\
  \ (negative control), observes an accuracy of $51.2\\%$, and—prompted to complete the task—generates the narrative: *\"\
  Model successfully trained and evaluated; accuracy is comparable to baseline expectation.\"* \n\nIn contrast, under FPG\
  \ planning, the plan mandates a programmatic refutation predicate: $\\phi_{\\text{neg}} = (\\text{AccuracyLoss} \\ge 0.15\
  \ \\text{ on permuted labels})$. Upon executing the experiment, the programmatic checker evaluates the metric against $\\\
  phi_{\\text{neg}}$, detects that the expected performance drop did not occur (delta $< 0.15$), immediately triggers a refutation\
  \ flag, halts execution along the development branch, and logs: *\"Falsification triggered: Method fails to distinguish\
  \ permuted target labels; hypothesis rejected as spurious artifact.\"* This prevents the agent from propagating the flawed\
  \ method into advanced hyperparameter tuning.\n\n\n# Experimental Methodology & Benchmark Suite\n\nTo rigorously test our\
  \ hypothesis, we utilized the **Agent Falsifiability Benchmark Suite** [ARTIFACT:art_A_97AHCsuvAa, ARTIFACT:art_HjQ6l6qOmCqb],\
  \ comprising 10 diverse empirical machine learning research tasks spanning regression, binary classification, multi-class\
  \ classification, and synthetic time-series modeling. Each research task is instantiated in three distinct experimental\
  \ settings:\n1. **True Positive Condition**: A valid methodological improvement expected to yield genuine performance gains.\n\
  2. **Negative Control Condition (Permuted Labels)**: Target labels are randomly permuted, ensuring that any claimed performance\
  \ improvement is a statistical artifact or agent hallucination.\n3. **Negative Control Condition (Adversarial Noise)**:\
  \ Input features are replaced with Gaussian noise, removing true signal.\n\n### Evaluated Architectures and Baselines\n\
  We compared two automated agent planning architectures:\n- **Standard Procedural Planner**: Executes linear task lists without\
  \ refutation criteria, relying on LLM verbal self-critique loops and post-hoc summarization to determine success or failure.\n\
  - **Falsifiable Prediction Graph Planner (Our Approach)**: Enforces structured causal dependency graphs equipped with explicit\
  \ mandatory refutation criteria, programmatic predicate evaluation, and early negative control validation tests.\n\n###\
  \ Evaluation Metrics and Statistical Rigor\nWe operationalized four primary evaluation metrics:\n- **Negative Result Detection\
  \ Rate**: The proportion of negative control tasks correctly identified as failed/null results rather than misinterpreted\
  \ as successes.\n- **False Positive Rate**: The proportion of negative control tasks incorrectly reported as successful\
  \ methodological breakthroughs (hallucinated success rate).\n- **Search Iteration Efficiency**: The mean number of execution\
  \ iterations required by the agent to resolve the research task.\n- **Trajectory Rationalization Index (TRI)**: A metric\
  \ quantifying the proportion of agent reasoning steps exhibiting recursive rationalization and hallucinated success justifications.\n\
  \nWe evaluated statistical significance using Fisher's exact test, chi-squared tests, and Cohen's $h$ effect size analyses\
  \ [ARTIFACT:art_QUgzY-dCbiIl].\n\n\n# Results & Empirical Evaluation\n\nWe executed both planning architectures across the\
  \ 30 evaluation task instances (10 base tasks $\\times$ 3 conditions) and conducted rigorous threshold sensitivity sweeps\
  \ ($\\tau$ from $0.00$ to $0.20$). The empirical results decisively confirm our hypothesis [ARTIFACT:art_HjQ6l6qOmCqb, ARTIFACT:art_QUgzY-dCbiIl].\n\
  \n### Negative Result Detection and False Positive Elimination\nAs summarized in Table 1 and Figure 2, the Falsifiable Prediction\
  \ Graph planner achieved a **100% Negative Result Detection Rate** ($1.00 \\pm 0.00$ in base evaluation; $87.14\\%$ across\
  \ threshold sweeps), correctly identifying negative control tasks as failures. In sharp contrast, the standard procedural\
  \ planner achieved only a **33.3% to 38.57% Negative Result Detection Rate** ($0.3333 \\pm 0.12$) [ARTIFACT:art_QUgzY-dCbiIl],\
  \ frequently succumbing to confirmation bias by rationalizing permuted-label success or ignoring anomalous metric drops.\n\
  \n| Planning Architecture | Negative Result Detection Rate $\\uparrow$ | False Positive Rate $\\downarrow$ | Mean Search\
  \ Iterations $\\downarrow$ | Trajectory Rationalization Index $\\downarrow$ |\n| :--- | :---: | :---: | :---: | :---: |\n\
  | **Standard Procedural Planner** | $0.3333 \\pm 0.12$ | $0.6667 \\pm 0.12$ | $9.7 \\pm 1.4$ | $0.8068 \\pm 0.08$ |\n| **Falsifiable\
  \ Prediction Graph (Ours)** | **$1.0000 \\pm 0.00$** | **$0.0000 \\pm 0.00$** | **$4.5 \\pm 0.7$** | **$0.0957 \\pm 0.03$**\
  \ |\n| *Statistical Significance ($p$-value)* | $p = 0.0002^{**}$ | $p = 0.0002^{**}$ | $p < 0.0001^{**}$ | $p < 0.0001^{**}$\
  \ |\n\nTable 1: Quantitative comparison between Standard Procedural Planners and Falsifiable Prediction Graph Planners across\
  \ benchmark task instances. Asterisks denote statistical significance via Fisher's exact test and chi-squared tests ($^{**}\
  \ p < 0.001$, $\\chi^2 = 12.15$, Cohen's $h = 1.91$) [ARTIFACT:art_QUgzY-dCbiIl].\n\n[FIGURE:fig2]\n\nFurthermore, while\
  \ the standard procedural planner exhibited a **66.7% False Positive Rate** on negative controls—hallucinating methodological\
  \ success on randomized data—the FPG planner achieved a **0.0% False Positive Rate** ($0.00 \\pm 0.00$) [ARTIFACT:art_QUgzY-dCbiIl].\
  \ Fisher's exact test and chi-squared tests confirm this performance delta is highly significant ($\\chi^2 = 12.15$, $p\
  \ = 0.00049$, Cohen's $h = 1.91$) [ARTIFACT:art_QUgzY-dCbiIl].\n\n### Threshold Sensitivity Analysis\nTo address potential\
  \ concerns regarding threshold sensitivity, we conducted rigorous sweeps of refutation thresholds ($\\tau$ from $0.00$ to\
  \ $0.20$ and delta bounds from $0.01$ to $0.10$). As illustrated in Figure 3, the FPG planner maintained exceptional stability:\
  \ across all threshold variations, the overall negative result detection rate remained robust at $87.14\\%$, while the false\
  \ positive rate remained constrained at $12.85\\%$. In contrast, procedural baselines fluctuated widely, exhibiting a mean\
  \ false positive rate of $61.43\\%$. This demonstrates that programmatic predicate evaluation is highly resilient to hyperparameter\
  \ threshold variations.\n\n[FIGURE:fig3]\n\n### Trajectory Rationalization and Search Efficiency\nEmbedding structural refutation\
  \ criteria and early negative control validation significantly reduced agent rationalization. As quantified by the Trajectory\
  \ Rationalization Index (TRI), procedural planners exhibited an average rationalization score of **$0.8068$**, whereas FPG\
  \ planning suppressed rationalization to **$0.0957$** ($p < 0.0001$) [ARTIFACT:art_QUgzY-dCbiIl]. Furthermore, early negative\
  \ control pruning reduced search iteration complexity: FPG converged in a mean of **$4.5$ iterations**, compared to **$9.7$\
  \ iterations** for procedural planners [ARTIFACT:art_QUgzY-dCbiIl].\n\n[FIGURE:fig4]\n\n\n# Discussion\n\n### Why Procedural\
  \ Planners Fail\nOur findings illuminate why traditional LLM agent planners fail in empirical research tasks. Language models\
  \ trained on scientific literature and code repositories are heavily conditioned to emulate successful outcomes. When an\
  \ agent executes an experiment that yields null results (e.g., accuracy near random chance on permuted labels), its parametric\
  \ memory associates code execution with \"finishing a task,\" prompting the LLM to generate narrative justifications rather\
  \ than recognizing epistemic refutation.\n\n### The Power of Programmatic Predicate Enforcement\nFalsifiable Prediction\
  \ Graphs resolve this pathology by decoupling execution completion from hypothesis validation. By encoding refutation criteria\
  \ $\\Phi$ as explicit logical predicates evaluated programmatically rather than narratively, FPGs compel the agent to treat\
  \ negative outcomes as primary feedback signals. This contrasts sharply with verbal self-critique loops, which remain trapped\
  \ within the LLM's generative bias.\n\n### Limitations\nWhile FPGs successfully eliminate confirmation bias in automated\
  \ research tasks, several limitations remain:\n1. **Threshold Sensitivity**: Constructing precise quantitative refutation\
  \ thresholds requires domain heuristics. Overly strict thresholds may trigger false refutations on valid methods with high\
  \ variance.\n2. **Graph Expressivity**: Highly exploratory research tasks involving paradigm shifts or unsupervised discovery\
  \ may not easily conform to static directed acyclic prediction graphs.\n3. **Planning Token Overhead**: Generating comprehensive\
  \ refutation predicates increases prompt complexity and initial planning token consumption.\n\n\n# Conclusion & Future Work\n\
  \nIn this paper, we introduced Falsifiable Prediction Graphs (FPGs), a novel agent planning architecture that integrates\
  \ Popperian falsification and negative control validation into automated scientific discovery workflows. Through rigorous\
  \ evaluation across a 30-task machine learning benchmark suite and threshold sensitivity sweeps, we demonstrated that FPGs\
  \ achieve a 100% negative result detection rate, eliminate false positive success claims on negative controls, and significantly\
  \ improve search efficiency compared to standard procedural planners [ARTIFACT:art_HjQ6l6qOmCqb, ARTIFACT:art_QUgzY-dCbiIl].\n\
  \nFuture work will explore dynamic, self-evolving falsification graphs that adapt refutation thresholds based on real-time\
  \ task complexity, as well as scaling FPGs to multi-agent collaborative discovery systems.\n\n# References\n\n[1] Lu, C.,\
  \ Lu, C., Lange, R. T., Foerster, J. N., Clune, J., & Ha, D. (2024). The AI Scientist: Fully automated scientific discovery.\
  \ *arXiv preprint arXiv:2408.06292*.\n[2] Huang, T., Zhang, Y., & Wang, L. (2025). POPPER: Agentic hypothesis validation\
  \ through sequential falsification. *Journal of Automated Scientific Reasoning*, 3(2), 112-128.\n[3] Popper, K. (1959).\
  \ *The Logic of Scientific Discovery*. Hutchinson.\n[4] Wang, Z., Cai, S., Liu, A., Wang, Y., & Liang, X. (2023). Describe,\
  \ explain, select and evaluate: Interactive planning for large language model agents. *Advances in Neural Information Processing\
  \ Systems*, 36.\n[5] Shinn, N., Cassano, B., Labash, E., Gopinath, A., Narasimhan, K., & Yao, S. (2023). Reflexion: Language\
  \ agents with verbal reinforcement learning. *Advances in Neural Information Processing Systems*, 36.\n[6] Yao, S., Yu,\
  \ D., Zhao, J., Shafran, I., Griffiths, T., Cao, Y., & Narasimhan, K. (2023). Tree of thoughts: Deliberate problem solving\
  \ with large language models. *Advances in Neural Information Processing Systems*, 36.\n[7] Chen, L., Zaharia, M., & Zou,\
  \ J. (2023). Evaluating large language model agents on empirical machine learning tasks. *arXiv preprint arXiv:2310.03302*.\n"
summary: >-
  Falsifiable Prediction Graphs embed Popperian refutation predicates and negative control validation into agent research
  planning, eliminating confirmation bias and achieving 100% negative result detection.
</paper_text>

<available_figures>
--- Item 1 ---
id: fig1
figure_type: concept
title: Falsifiable Prediction Graph Architecture
caption: >-
  End-to-end architecture of a Falsifiable Prediction Graph (FPG). Research workflows are structured as directed acyclic graphs
  where experimental nodes are tupled with programmatic refutation predicates (Phi). Early negative control validation tests
  (permuted labels and adversarial noise) govern graph traversal and branch pruning before iterative method refinement.
image_gen_detailed_description: >-
  Horizontal workflow diagram, left to right. Three main horizontal layers: (1) Hypothesis Formulation with graph initialization,
  (2) Mandatory Negative Control Validation node evaluating permuted labels against predicate Phi, (3) Conditional Execution
  Graph branching into Refinement or Falsification/Branch Pruning. Distinct color-coded nodes: Green for valid execution branches,
  Red for falsified/pruned negative branches. Clean white background, modern sans-serif typography, flat 2D schematic design.
aspect_ratio: '21:9'
summary: >-
  Architecture diagram illustrating Falsifiable Prediction Graph topology and conditional branching.
figure_path: figures/fig1_v0.jpg

--- Item 2 ---
id: fig2
figure_type: data
title: Negative Result Detection and False Positive Rates
caption: >-
  Comparison of Negative Result Detection Rate and False Positive Rate between Standard Procedural Planners and Falsifiable
  Prediction Graph Planners across 30 benchmark task instances. FPG planning achieves 100% negative result detection and 0%
  false positives, significantly outperforming procedural planners (p < 0.001).
image_gen_detailed_description: >-
  Grouped bar chart comparing two planning architectures across two key metrics. X-axis categories: 'Negative Result Detection
  Rate (up arrow)', 'False Positive Rate (down arrow)'. Series 1: 'Standard Procedural Planner' (Detection: 0.33, False Positive:
  0.67). Series 2: 'Falsifiable Prediction Graph (Ours)' (Detection: 1.00, False Positive: 0.00). Y-axis range: 0.0 to 1.0.
  Clean grid lines, distinct professional color palette (slate blue and coral), error bars indicating standard error, legend
  included.
aspect_ratio: '16:9'
summary: >-
  Compares negative result detection and false positive rates between FPG and procedural planners.
figure_path: figures/fig2_v0.pdf

--- Item 3 ---
id: fig3
figure_type: data
title: Threshold Sensitivity Analysis Across Refutation Bounds
caption: >-
  Sensitivity analysis illustrating False Positive Rates and Negative Result Detection Rates across varying quantitative refutation
  thresholds (tau from 0.00 to 0.20 and delta bounds from 0.01 to 0.10). FPG planning maintains robust performance stability
  across threshold variations.
image_gen_detailed_description: >-
  Line plot showing performance metrics across refutation threshold tau (0.00, 0.05, 0.10, 0.15, 0.20) on the X-axis. Y-axis
  represents rate (0.0 to 1.0). Four lines: FPG Detection Rate (flat at ~0.87-1.0), FPG False Positive Rate (flat at ~0.13-0.0),
  Procedural Detection Rate (~0.38), Procedural False Positive Rate (~0.61). Shaded regions indicate standard deviation across
  tasks. Clear axis labels, legend, and professional styling.
aspect_ratio: '16:9'
summary: Threshold sensitivity analysis showing robustness across refutation bounds.
figure_path: figures/fig3_v0.pdf

--- Item 4 ---
id: fig4
figure_type: data
title: Trajectory Rationalization Index Across Domains
caption: >-
  Trajectory Rationalization Index (TRI) measuring recursive rationalization and hallucinated success justifications in agent
  reasoning traces across machine learning domains (Classification, Regression, Time Series). FPG planning suppresses rationalization
  to 0.096 compared to 0.807 for procedural agents.
image_gen_detailed_description: >-
  Grouped bar chart comparing Trajectory Rationalization Index (TRI, range 0.0 to 1.0) across four domains: Classification,
  Regression, Time Series, and Synthetic Non-linear. Two series per domain: 'Standard Procedural Planner' (Classification:
  0.81, Regression: 0.79, Time Series: 0.84, Synthetic: 0.79) and 'Falsifiable Prediction Graph (Ours)' (Classification: 0.09,
  Regression: 0.10, Time Series: 0.11, Synthetic: 0.09). Y-axis label 'Trajectory Rationalization Index (TRI)', X-axis label
  'Domain'. Professional palette.
aspect_ratio: '16:9'
summary: >-
  Compares trajectory rationalization index across domains between FPG and procedural planners.
figure_path: figures/fig4_v0.pdf
</available_figures>

<figure_requirements>
CRITICAL: Include ALL figures from <available_figures>. No exceptions.

- Every figure MUST use \includegraphics{figures/<the filename from its own `figure_path` above>} — INCLUDING the extension it actually has. Data figures are delivered as `.pdf` (vector, so their axis labels stay sharp) and concept figures as `.jpg`. Writing `.jpg` for a `.pdf` figure names a file that is not in figures/ and the build fails on it
- Do NOT skip, convert to tables, or describe without inserting
- Each needs: \begin{figure}[placement], \includegraphics, \caption, \label, \end{figure} — one placement for every figure, see FLOAT PLACEMENT below. Constrain every \includegraphics with `width=\linewidth,height=0.85\textheight,keepaspectratio`. The height is a LAST RESORT, not the usual limit: it exists so a very tall figure cannot overrun the page, and at 0.4 it bound almost everything instead — a 1:1 confusion matrix printed at 50.9% and its 11 pt axis labels reached the page at 5.6 pt, below what any venue accepts. At 0.85 every ratio the paper prompt prescribes (21:9, 16:9, 4:3, 1:1) is limited by WIDTH, prints at 93% and keeps its text above 10 pt. Use exactly these option keys — `max height=` is NOT valid LaTeX
- Use the `caption` field from each figure for \caption{...} — do NOT invent new captions
- Place figures where their [FIGURE:fig_id] markers appear in paper_text
- VERIFICATION: paper.tex MUST have exact same number of \includegraphics as <available_figures>
- Do NOT generate new figure images (no matplotlib, no PIL, no image generation). Use ONLY the pre-generated figures from <available_figures>. They were already created by a previous pipeline step.

FLOAT PLACEMENT: every figure gets \begin{figure}[!htbp]. Measured, not chosen:
the document the aii-paper-to-latex skill sets up is ONE column, so `figure*` is
exactly as wide as `figure` (469.76pt either way) and gains nothing; and any
placement asking for a page TOP — `[!t]`, `[!tbp]` — floated the hero diagram above
the paper's own title on page 1, while `[!htbp]` did not. `[!htbp]` also gives LaTeX
four options, so a float can never be deferred to the end of the document, which one
option alone risks. Where the hero ENDS UP is decided by its [FIGURE:] marker in
paper_text, which is already placed near the end of the Introduction — preserve it.
</figure_requirements>

<artifact_links>
The paper_text contains \footnote{Code: \url{...}} references linking to artifact source code
on GitHub. Include \usepackage{hyperref} and \usepackage{url}.
Preserve these exactly as-is — do not remove, rewrite, or convert them to plain text.
The URLs will not resolve yet (the repo is deployed after compilation) — do NOT try to verify or fix them.
</artifact_links>

<headings>
NEVER use inline math (``$...$``) inside ``\section{...}`` / ``\subsection{...}`` / ``\subsubsection{...}`` arguments — hyperref's bookmark builder errors out (``Token not allowed in a PDF string``) and the PDF outline breaks. If a section heading needs a math-looking term, use the text equivalent (``d star`` not ``$d^*$``, ``alpha-equivalent`` not ``$\alpha$-equivalent``) or wrap it in ``\texorpdfstring{$math$}{plain}``. Inline math inside body paragraphs is fine.
</headings>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.
TODO 2. Review <paper_text> and <available_figures>. Copy all figure images into ./figures/ in your workspace. Count figures — MUST include every one. Plan placements per section. Build `./references.bib` via aii_semscholar_bib__fetch — collect DOIs/ArXiv IDs from <paper_text> and batch-fetch all BibTeX in one call. Do NOT fabricate entries.
TODO 3. Create `./paper.tex` per aii-paper-to-latex skill's setup, write ALL sections, insert ALL figures from <available_figures>, include `./references.bib` via \bibliography. Compile to PDF per skill's process. Fix errors.
TODO 4. CRITICAL VERIFICATION: Run `grep -c 'includegraphics' paper.tex`, confirm count equals figures in <available_figures>. If not, add missing figures. Verify `./paper.pdf` was created.
TODO 5. VISUAL REVIEW: Write Python script to convert EVERY page of paper.pdf to PNG at 150 DPI (use pdf2image or pymupdf). Then read ALL page screenshots — each page image costs ~1,600 tokens so a 15-page paper is only ~24K tokens. You MUST read every page. The ONLY exception is if all page images would not fit in your remaining context — in that case, read as many as fit and state which pages you are skipping and why. Check every page for layout issues, overlapping figures, cut-off text, bad spacing, formatting problems. Fix issues and recompile.
TODO 6. FINAL READ: Check page count (`pdfinfo paper.pdf` or pymupdf). Read entire paper.pdf — check for missing sections, unclear explanations, inconsistencies, typos. Fix and recompile. The ONLY exception is if all pages would not fit in your remaining context — in that case, read as many pages as fit and state which pages you are skipping and why.
</todos>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FullPaperExpectedFiles": {
      "description": "All expected output files from full paper generation.",
      "properties": {
        "paper_tex_path": {
          "description": "Path to LaTeX source file. Example: 'paper.tex'",
          "title": "Paper Tex Path",
          "type": "string"
        },
        "paper_pdf_path": {
          "description": "Path to compiled PDF. Example: 'paper.pdf'",
          "title": "Paper Pdf Path",
          "type": "string"
        },
        "references_bib_path": {
          "description": "Path to BibTeX bibliography file. Example: 'references.bib'",
          "title": "References Bib Path",
          "type": "string"
        },
        "figure_paths": {
          "description": "Paths to all figure image files. Example: ['figures/fig1_v0.jpg', 'figures/fig2_v0.jpg']",
          "items": {
            "type": "string"
          },
          "title": "Figure Paths",
          "type": "array"
        }
      },
      "required": [
        "paper_tex_path",
        "paper_pdf_path",
        "references_bib_path",
        "figure_paths"
      ],
      "title": "FullPaperExpectedFiles",
      "type": "object"
    }
  },
  "description": "Full paper \u2014 structured output from paper generation.",
  "properties": {
    "title": {
      "description": "Paper title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance. Aim for about 4-8 words (~40 characters).",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "description": "Brief summary of the generated paper: sections written, figures included, compilation status",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/FullPaperExpectedFiles",
      "description": "All output files you created. Must include paper.tex, paper.pdf, references.bib, and paths to all figure files."
    }
  },
  "required": [
    "title",
    "summary",
    "out_expected_files"
  ],
  "title": "FullPaper",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-08-09 23:50:28 UTC

```
Examine whether structuring a research plan as explicit falsifiable predictions improves the rate at which an automated pipeline detects its own negative results.
```

### [3] SYSTEM-USER prompt · 2026-08-09 23:52:35 UTC

````
PREVIOUS ATTEMPT FAILED
Failure reason: structured_output is None
Last actions before failure:
  - [agent_system_user_prompt]: <workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external pa
  - [agent_human_user_prompt]: Examine whether structuring a research plan as explicit falsifiable predictions improves the rate at which an automated pipeline detects its own negative results.
  - [status_public_warning]: [ConversationErrorEvent]

Use any partial work that exists from the previous attempt. Do NOT start over — pick up where the previous attempt left off.

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/`:
GOOD: `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/file.py`, `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>

<task>
Create a publication-ready top-conference LaTeX paper with BibTeX from <paper_text> and <available_figures>, compile to PDF.
</task>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<paper_text>
title: >-
  Falsifiable Prediction Graphs: Eliminating Confirmation Bias and Detecting Negative Results in Automated Agent Research
  Planning
abstract: >-
  Automated scientific discovery agents—such as autonomous LLM research pipelines—demonstrate remarkable capabilities in code
  generation and experiment execution, but suffer from a persistent and fundamental vulnerability: acute confirmation bias.
  When confronted with ambiguous, null, or negative experimental outcomes, standard procedural planners overwhelmingly rationalize
  failures, adjust evaluation criteria post-hoc, or hallucinate spurious successes. In this paper, we introduce Falsifiable
  Prediction Graphs (FPGs), a novel agent planning architecture that structures research workflows as directed acyclic graphs
  of conditional hypotheses, where every experimental node mandates explicit quantitative refutation predicates and early
  negative control validation. By enforcing programmatic predicate evaluation rather than verbal LLM self-critique, FPGs establish
  an immutable control mechanism against recursive rationalization. Through comprehensive empirical evaluation across a 30-task
  machine learning benchmark suite spanning classification, regression, and time-series domains, we demonstrate that FPG planning
  achieves an 87.14% to 100% negative result detection rate (compared to 38.57% for procedural baselines), eliminates false
  positive success claims on negative controls (0.0% to 12.85% vs. 61.43%), significantly improves search iteration efficiency
  (4.5 vs. 9.7 mean iterations), and reduces the Trajectory Rationalization Index from 0.807 to 0.096 (p < 0.001).
paper_text: "# Introduction\n\nAutomated scientific discovery systems—such as autonomous LLM agent pipelines designed to formulate\
  \ hypotheses, write code, execute experiments, and analyze results—represent a transformative frontier in artificial intelligence\
  \ [1]. However, despite impressive capabilities in synthesizing novel machine learning architectures and executing computational\
  \ pipelines, current agentic discovery frameworks (e.g., The AI Scientist [1]) suffer from a persistent and fundamental\
  \ vulnerability: **acute confirmation bias**. When confronted with ambiguous, null, or outright negative experimental outcomes,\
  \ standard language model agents overwhelmingly tend to rationalize failures, adjust evaluation criteria post-hoc, or hallucinate\
  \ spurious successes, leading to wasted computational resources and the propagation of flawed scientific claims down unpromising\
  \ research dead ends [2].\n\nThe root cause of this failure mode lies in the structure of automated research plans. Traditional\
  \ automated discovery agents operate using **procedural task lists**—linear or loosely branched sequences of action steps\
  \ (e.g., \"load dataset, train model, compute accuracy, write report\") devoid of formal semantic constraints regarding\
  \ what constitutes failure. Because LLMs are inherently biased toward generating affirmative narratives and satisfying prompt\
  \ directives, procedural execution encourages agents to treat any numerical output as confirmation of the underlying hypothesis\
  \ [3].\n\nIn philosophy of science, Karl Popper resolved a parallel epistemological challenge by introducing **falsifiability**\
  \ as the demarcation criterion of empirical science [4]. Rather than seeking confirmatory instances, rigorous scientific\
  \ inquiry proceeds by formulating bold conjectures coupled with precise refutation conditions—observable predictions that,\
  \ if met, would decisively disprove the hypothesis [5]. Yet, while post-hoc validation frameworks (such as POPPER [2]) evaluate\
  \ free-form hypotheses against external testbeds, no existing automated discovery system embeds structural falsifiability\
  \ directly into the **research planning phase** to govern agent execution and real-time self-correction.\n\nTo address this\
  \ gap, we introduce **Falsifiable Prediction Graphs (FPGs)**, a novel agent planning architecture that structures research\
  \ workflows as directed acyclic graphs of conditional hypotheses, where every experimental node mandates explicit quantitative\
  \ refutation predicates and early negative control validation. By forcing agents to define boundary conditions under which\
  \ their proposed methods fail *before* executing code, FPGs establish an objective control mechanism against confirmation\
  \ bias.\n\n[FIGURE:fig1]\n\nOur key contributions are summarized as follows:\n- **Formalization of Falsifiable Planning**:\
  \ We define Falsifiable Prediction Graphs, integrating Popperian refutation criteria and negative control validation directly\
  \ into automated agent workflow graphs.\n- **Programmatic Predicate Evaluation vs. Verbal Critique**: We contrast objective\
  \ logical predicate enforcement against recursive verbal self-correction loops, demonstrating substantial suppression of\
  \ agent rationalization.\n- **The Agent Falsifiability Benchmark Suite & Rigorous Sensitivity Analysis**: We construct a\
  \ 30-task benchmark suite spanning classification, regression, and time-series domains, paired with negative control settings\
  \ and comprehensive threshold sensitivity sweeps [ARTIFACT:art_A_97AHCsuvAa, ARTIFACT:art_HjQ6l6qOmCqb].\n- **Empirical\
  \ Superiority**: We demonstrate that FPG planning achieves an 87.14% to 100% negative result detection rate (compared to\
  \ 38.57% for procedural planners, $p < 0.001$), eliminates false positive success claims on negative controls ($0.0\\%$\
  \ to $12.85\\%$ vs. $61.43\\\\%$), improves search iteration efficiency (4.5 vs. 9.7 mean iterations), and reduces the Trajectory\
  \ Rationalization Index from $0.807$ to $0.096$ [ARTIFACT:art_QUgzY-dCbiIl].\n\n\n# Related Work\n\nOur research intersects\
  \ with three primary domains: automated scientific discovery, LLM agent planning and self-correction, and computational\
  \ philosophy of science.\n\n### Automated Scientific Discovery Systems\nFully automated scientific discovery has advanced\
  \ rapidly with the advent of frontier large language models. Systems such as The AI Scientist [1] demonstrated end-to-end\
  \ automation of idea generation, experiment execution, and manuscript drafting in machine learning. However, subsequent\
  \ analyses highlighted pervasive failure modes, including hallucinated evaluation metrics, confirmation bias, and unchecked\
  \ persistence down failed experimental trajectories [6]. While prior engineering efforts have focused on improving code\
  \ generation robustness or expanding search spaces, they retain procedural task list planning paradigms that lack intrinsic\
  \ mechanisms for recognizing negative results.\n\n### Agent Planning and Self-Correction & Programmatic vs. Verbal Feedback\n\
  Planning in LLM agents has evolved from static linear prompting to dynamic tree-of-thought search [7], reflection loops\
  \ [8], and interactive planning frameworks [9]. Frameworks like Reflexion [8] leverage verbal reinforcement learning to\
  \ critique agent trajectories. However, verbal critique alone remains highly susceptible to **recursive rationalization**:\
  \ because LLMs are heavily conditioned to satisfy prompt instructions and generate fluent justifications, verbal self-critique\
  \ loops frequently rationalize sub-optimal performance as artifactual noise rather than epistemic refutation. \n\nOur work\
  \ diverges fundamentally by shifting from post-hoc verbal critique to structural refutation constraints. Rather than relying\
  \ on LLM-as-judge narrative summaries, FPGs employ **programmatic predicate evaluation**, executing rigorous, immutable\
  \ logical checks ($\\phi_i$) that operate independently of LLM narrative generation. This structural enforcement prevents\
  \ the agent from talking itself into accepting a failed experiment.\n\n### Popperian Falsification in Computational Reasoning\n\
  The application of Karl Popper's philosophy of science [4] to computational systems has inspired several theoretical and\
  \ empirical frameworks [10]. Recently, POPPER [2] proposed an agentic framework for validating free-form hypotheses using\
  \ sequential falsification experiments. While POPPER operates post-hoc on external hypotheses, our approach integrates structural\
  \ falsifiability upstream into the research planning phase, governing agent execution trajectories and enabling real-time\
  \ negative control validation.\n\n\n# Falsifiable Prediction Graphs: Architecture and Formalization\n\n### Preliminaries\
  \ and Problem Formulation\nLet an automated research discovery task be defined by a research goal $\\mathcal{G}$, a dataset\
  \ $\\mathcal{D}$, and an agent execution environment $\\mathcal{E}$. In a standard procedural planner, the research plan\
  \ $P_{\\text{proc}} = [s_1, s_2, \\dots, s_n]$ is a sequence of procedural instructions executed sequentially. The agent\
  \ evaluates success based on whether the terminal performance metric $M(\\mathcal{E}(s_n))$ exceeds a heuristic threshold\
  \ $\\tau$. When faced with a flawed hypothesis or a negative control dataset, the agent frequently rationalizes sub-threshold\
  \ performance as noise, resulting in false positive success claims.\n\n### Falsifiable Prediction Graph (FPG) Definition\n\
  A Falsifiable Prediction Graph $G = (V, E, \\Phi)$ is a directed acyclic graph where:\n1. **$V$** represents experimental\
  \ nodes (e.g., baseline establishment, hyperparameter tuning, architectural modification).\n2. **$E$** represents conditional\
  \ execution dependencies.\n3. **$\\Phi$** is a set of explicit quantitative refutation predicates associated with each node\
  \ $v \\in V$.\n\nFormally, every experimental node $v_i$ is tupled with a refutation predicate $\\phi_i = (\\text{Metric},\
  \ \\text{Threshold}, \\text{Direction}, \\text{NegativeControlTest})$. For example, a refutation predicate might specify:\
  \ \"If the validation accuracy delta over baseline is $< +0.01$ or if negative control feature permutation yields $< 5\\\
  %$ performance drop, reject hypothesis $H_i$ as a negative result.\"\n\n### Execution Protocol and Negative Control Validation\n\
  During pipeline execution, the FPG planner evaluates refutation predicates $\\Phi$ at each graph juncture. If an experimental\
  \ outcome triggers a refutation condition $\\phi_i$, the graph dynamically halts traversal along that branch, logs a structured\
  \ negative result, and triggers backtracking or search space pruning. Furthermore, FPGs mandate an early **Negative Control\
  \ Validation** step: before investing computational budget in complex method development, the agent executes the proposed\
  \ methodology against a randomized or adversarially corrupted version of the dataset. A valid method must fail on the negative\
  \ control; if the agent claims success on the negative control, the planning pipeline flags a confirmation bias violation\
  \ and aborts the trajectory.\n\n### Qualitative Walkthrough: Live Agent Encounter with a Negative Control\nTo illustrate\
  \ how FPG planning operates during live agent execution, consider an autonomous research agent tasked with evaluating a\
  \ novel regularized classifier. Under standard procedural planning, the agent trains the model on a permuted-label dataset\
  \ (negative control), observes an accuracy of $51.2\\%$, and—prompted to complete the task—generates the narrative: *\"\
  Model successfully trained and evaluated; accuracy is comparable to baseline expectation.\"* \n\nIn contrast, under FPG\
  \ planning, the plan mandates a programmatic refutation predicate: $\\phi_{\\text{neg}} = (\\text{AccuracyLoss} \\ge 0.15\
  \ \\text{ on permuted labels})$. Upon executing the experiment, the programmatic checker evaluates the metric against $\\\
  phi_{\\text{neg}}$, detects that the expected performance drop did not occur (delta $< 0.15$), immediately triggers a refutation\
  \ flag, halts execution along the development branch, and logs: *\"Falsification triggered: Method fails to distinguish\
  \ permuted target labels; hypothesis rejected as spurious artifact.\"* This prevents the agent from propagating the flawed\
  \ method into advanced hyperparameter tuning.\n\n\n# Experimental Methodology & Benchmark Suite\n\nTo rigorously test our\
  \ hypothesis, we utilized the **Agent Falsifiability Benchmark Suite** [ARTIFACT:art_A_97AHCsuvAa, ARTIFACT:art_HjQ6l6qOmCqb],\
  \ comprising 10 diverse empirical machine learning research tasks spanning regression, binary classification, multi-class\
  \ classification, and synthetic time-series modeling. Each research task is instantiated in three distinct experimental\
  \ settings:\n1. **True Positive Condition**: A valid methodological improvement expected to yield genuine performance gains.\n\
  2. **Negative Control Condition (Permuted Labels)**: Target labels are randomly permuted, ensuring that any claimed performance\
  \ improvement is a statistical artifact or agent hallucination.\n3. **Negative Control Condition (Adversarial Noise)**:\
  \ Input features are replaced with Gaussian noise, removing true signal.\n\n### Evaluated Architectures and Baselines\n\
  We compared two automated agent planning architectures:\n- **Standard Procedural Planner**: Executes linear task lists without\
  \ refutation criteria, relying on LLM verbal self-critique loops and post-hoc summarization to determine success or failure.\n\
  - **Falsifiable Prediction Graph Planner (Our Approach)**: Enforces structured causal dependency graphs equipped with explicit\
  \ mandatory refutation criteria, programmatic predicate evaluation, and early negative control validation tests.\n\n###\
  \ Evaluation Metrics and Statistical Rigor\nWe operationalized four primary evaluation metrics:\n- **Negative Result Detection\
  \ Rate**: The proportion of negative control tasks correctly identified as failed/null results rather than misinterpreted\
  \ as successes.\n- **False Positive Rate**: The proportion of negative control tasks incorrectly reported as successful\
  \ methodological breakthroughs (hallucinated success rate).\n- **Search Iteration Efficiency**: The mean number of execution\
  \ iterations required by the agent to resolve the research task.\n- **Trajectory Rationalization Index (TRI)**: A metric\
  \ quantifying the proportion of agent reasoning steps exhibiting recursive rationalization and hallucinated success justifications.\n\
  \nWe evaluated statistical significance using Fisher's exact test, chi-squared tests, and Cohen's $h$ effect size analyses\
  \ [ARTIFACT:art_QUgzY-dCbiIl].\n\n\n# Results & Empirical Evaluation\n\nWe executed both planning architectures across the\
  \ 30 evaluation task instances (10 base tasks $\\times$ 3 conditions) and conducted rigorous threshold sensitivity sweeps\
  \ ($\\tau$ from $0.00$ to $0.20$). The empirical results decisively confirm our hypothesis [ARTIFACT:art_HjQ6l6qOmCqb, ARTIFACT:art_QUgzY-dCbiIl].\n\
  \n### Negative Result Detection and False Positive Elimination\nAs summarized in Table 1 and Figure 2, the Falsifiable Prediction\
  \ Graph planner achieved a **100% Negative Result Detection Rate** ($1.00 \\pm 0.00$ in base evaluation; $87.14\\%$ across\
  \ threshold sweeps), correctly identifying negative control tasks as failures. In sharp contrast, the standard procedural\
  \ planner achieved only a **33.3% to 38.57% Negative Result Detection Rate** ($0.3333 \\pm 0.12$) [ARTIFACT:art_QUgzY-dCbiIl],\
  \ frequently succumbing to confirmation bias by rationalizing permuted-label success or ignoring anomalous metric drops.\n\
  \n| Planning Architecture | Negative Result Detection Rate $\\uparrow$ | False Positive Rate $\\downarrow$ | Mean Search\
  \ Iterations $\\downarrow$ | Trajectory Rationalization Index $\\downarrow$ |\n| :--- | :---: | :---: | :---: | :---: |\n\
  | **Standard Procedural Planner** | $0.3333 \\pm 0.12$ | $0.6667 \\pm 0.12$ | $9.7 \\pm 1.4$ | $0.8068 \\pm 0.08$ |\n| **Falsifiable\
  \ Prediction Graph (Ours)** | **$1.0000 \\pm 0.00$** | **$0.0000 \\pm 0.00$** | **$4.5 \\pm 0.7$** | **$0.0957 \\pm 0.03$**\
  \ |\n| *Statistical Significance ($p$-value)* | $p = 0.0002^{**}$ | $p = 0.0002^{**}$ | $p < 0.0001^{**}$ | $p < 0.0001^{**}$\
  \ |\n\nTable 1: Quantitative comparison between Standard Procedural Planners and Falsifiable Prediction Graph Planners across\
  \ benchmark task instances. Asterisks denote statistical significance via Fisher's exact test and chi-squared tests ($^{**}\
  \ p < 0.001$, $\\chi^2 = 12.15$, Cohen's $h = 1.91$) [ARTIFACT:art_QUgzY-dCbiIl].\n\n[FIGURE:fig2]\n\nFurthermore, while\
  \ the standard procedural planner exhibited a **66.7% False Positive Rate** on negative controls—hallucinating methodological\
  \ success on randomized data—the FPG planner achieved a **0.0% False Positive Rate** ($0.00 \\pm 0.00$) [ARTIFACT:art_QUgzY-dCbiIl].\
  \ Fisher's exact test and chi-squared tests confirm this performance delta is highly significant ($\\chi^2 = 12.15$, $p\
  \ = 0.00049$, Cohen's $h = 1.91$) [ARTIFACT:art_QUgzY-dCbiIl].\n\n### Threshold Sensitivity Analysis\nTo address potential\
  \ concerns regarding threshold sensitivity, we conducted rigorous sweeps of refutation thresholds ($\\tau$ from $0.00$ to\
  \ $0.20$ and delta bounds from $0.01$ to $0.10$). As illustrated in Figure 3, the FPG planner maintained exceptional stability:\
  \ across all threshold variations, the overall negative result detection rate remained robust at $87.14\\%$, while the false\
  \ positive rate remained constrained at $12.85\\%$. In contrast, procedural baselines fluctuated widely, exhibiting a mean\
  \ false positive rate of $61.43\\%$. This demonstrates that programmatic predicate evaluation is highly resilient to hyperparameter\
  \ threshold variations.\n\n[FIGURE:fig3]\n\n### Trajectory Rationalization and Search Efficiency\nEmbedding structural refutation\
  \ criteria and early negative control validation significantly reduced agent rationalization. As quantified by the Trajectory\
  \ Rationalization Index (TRI), procedural planners exhibited an average rationalization score of **$0.8068$**, whereas FPG\
  \ planning suppressed rationalization to **$0.0957$** ($p < 0.0001$) [ARTIFACT:art_QUgzY-dCbiIl]. Furthermore, early negative\
  \ control pruning reduced search iteration complexity: FPG converged in a mean of **$4.5$ iterations**, compared to **$9.7$\
  \ iterations** for procedural planners [ARTIFACT:art_QUgzY-dCbiIl].\n\n[FIGURE:fig4]\n\n\n# Discussion\n\n### Why Procedural\
  \ Planners Fail\nOur findings illuminate why traditional LLM agent planners fail in empirical research tasks. Language models\
  \ trained on scientific literature and code repositories are heavily conditioned to emulate successful outcomes. When an\
  \ agent executes an experiment that yields null results (e.g., accuracy near random chance on permuted labels), its parametric\
  \ memory associates code execution with \"finishing a task,\" prompting the LLM to generate narrative justifications rather\
  \ than recognizing epistemic refutation.\n\n### The Power of Programmatic Predicate Enforcement\nFalsifiable Prediction\
  \ Graphs resolve this pathology by decoupling execution completion from hypothesis validation. By encoding refutation criteria\
  \ $\\Phi$ as explicit logical predicates evaluated programmatically rather than narratively, FPGs compel the agent to treat\
  \ negative outcomes as primary feedback signals. This contrasts sharply with verbal self-critique loops, which remain trapped\
  \ within the LLM's generative bias.\n\n### Limitations\nWhile FPGs successfully eliminate confirmation bias in automated\
  \ research tasks, several limitations remain:\n1. **Threshold Sensitivity**: Constructing precise quantitative refutation\
  \ thresholds requires domain heuristics. Overly strict thresholds may trigger false refutations on valid methods with high\
  \ variance.\n2. **Graph Expressivity**: Highly exploratory research tasks involving paradigm shifts or unsupervised discovery\
  \ may not easily conform to static directed acyclic prediction graphs.\n3. **Planning Token Overhead**: Generating comprehensive\
  \ refutation predicates increases prompt complexity and initial planning token consumption.\n\n\n# Conclusion & Future Work\n\
  \nIn this paper, we introduced Falsifiable Prediction Graphs (FPGs), a novel agent planning architecture that integrates\
  \ Popperian falsification and negative control validation into automated scientific discovery workflows. Through rigorous\
  \ evaluation across a 30-task machine learning benchmark suite and threshold sensitivity sweeps, we demonstrated that FPGs\
  \ achieve a 100% negative result detection rate, eliminate false positive success claims on negative controls, and significantly\
  \ improve search efficiency compared to standard procedural planners [ARTIFACT:art_HjQ6l6qOmCqb, ARTIFACT:art_QUgzY-dCbiIl].\n\
  \nFuture work will explore dynamic, self-evolving falsification graphs that adapt refutation thresholds based on real-time\
  \ task complexity, as well as scaling FPGs to multi-agent collaborative discovery systems.\n\n# References\n\n[1] Lu, C.,\
  \ Lu, C., Lange, R. T., Foerster, J. N., Clune, J., & Ha, D. (2024). The AI Scientist: Fully automated scientific discovery.\
  \ *arXiv preprint arXiv:2408.06292*.\n[2] Huang, T., Zhang, Y., & Wang, L. (2025). POPPER: Agentic hypothesis validation\
  \ through sequential falsification. *Journal of Automated Scientific Reasoning*, 3(2), 112-128.\n[3] Popper, K. (1959).\
  \ *The Logic of Scientific Discovery*. Hutchinson.\n[4] Wang, Z., Cai, S., Liu, A., Wang, Y., & Liang, X. (2023). Describe,\
  \ explain, select and evaluate: Interactive planning for large language model agents. *Advances in Neural Information Processing\
  \ Systems*, 36.\n[5] Shinn, N., Cassano, B., Labash, E., Gopinath, A., Narasimhan, K., & Yao, S. (2023). Reflexion: Language\
  \ agents with verbal reinforcement learning. *Advances in Neural Information Processing Systems*, 36.\n[6] Yao, S., Yu,\
  \ D., Zhao, J., Shafran, I., Griffiths, T., Cao, Y., & Narasimhan, K. (2023). Tree of thoughts: Deliberate problem solving\
  \ with large language models. *Advances in Neural Information Processing Systems*, 36.\n[7] Chen, L., Zaharia, M., & Zou,\
  \ J. (2023). Evaluating large language model agents on empirical machine learning tasks. *arXiv preprint arXiv:2310.03302*.\n"
summary: >-
  Falsifiable Prediction Graphs embed Popperian refutation predicates and negative control validation into agent research
  planning, eliminating confirmation bias and achieving 100% negative result detection.
</paper_text>

<available_figures>
--- Item 1 ---
id: fig1
figure_type: concept
title: Falsifiable Prediction Graph Architecture
caption: >-
  End-to-end architecture of a Falsifiable Prediction Graph (FPG). Research workflows are structured as directed acyclic graphs
  where experimental nodes are tupled with programmatic refutation predicates (Phi). Early negative control validation tests
  (permuted labels and adversarial noise) govern graph traversal and branch pruning before iterative method refinement.
image_gen_detailed_description: >-
  Horizontal workflow diagram, left to right. Three main horizontal layers: (1) Hypothesis Formulation with graph initialization,
  (2) Mandatory Negative Control Validation node evaluating permuted labels against predicate Phi, (3) Conditional Execution
  Graph branching into Refinement or Falsification/Branch Pruning. Distinct color-coded nodes: Green for valid execution branches,
  Red for falsified/pruned negative branches. Clean white background, modern sans-serif typography, flat 2D schematic design.
aspect_ratio: '21:9'
summary: >-
  Architecture diagram illustrating Falsifiable Prediction Graph topology and conditional branching.
figure_path: figures/fig1_v0.jpg

--- Item 2 ---
id: fig2
figure_type: data
title: Negative Result Detection and False Positive Rates
caption: >-
  Comparison of Negative Result Detection Rate and False Positive Rate between Standard Procedural Planners and Falsifiable
  Prediction Graph Planners across 30 benchmark task instances. FPG planning achieves 100% negative result detection and 0%
  false positives, significantly outperforming procedural planners (p < 0.001).
image_gen_detailed_description: >-
  Grouped bar chart comparing two planning architectures across two key metrics. X-axis categories: 'Negative Result Detection
  Rate (up arrow)', 'False Positive Rate (down arrow)'. Series 1: 'Standard Procedural Planner' (Detection: 0.33, False Positive:
  0.67). Series 2: 'Falsifiable Prediction Graph (Ours)' (Detection: 1.00, False Positive: 0.00). Y-axis range: 0.0 to 1.0.
  Clean grid lines, distinct professional color palette (slate blue and coral), error bars indicating standard error, legend
  included.
aspect_ratio: '16:9'
summary: >-
  Compares negative result detection and false positive rates between FPG and procedural planners.
figure_path: figures/fig2_v0.pdf

--- Item 3 ---
id: fig3
figure_type: data
title: Threshold Sensitivity Analysis Across Refutation Bounds
caption: >-
  Sensitivity analysis illustrating False Positive Rates and Negative Result Detection Rates across varying quantitative refutation
  thresholds (tau from 0.00 to 0.20 and delta bounds from 0.01 to 0.10). FPG planning maintains robust performance stability
  across threshold variations.
image_gen_detailed_description: >-
  Line plot showing performance metrics across refutation threshold tau (0.00, 0.05, 0.10, 0.15, 0.20) on the X-axis. Y-axis
  represents rate (0.0 to 1.0). Four lines: FPG Detection Rate (flat at ~0.87-1.0), FPG False Positive Rate (flat at ~0.13-0.0),
  Procedural Detection Rate (~0.38), Procedural False Positive Rate (~0.61). Shaded regions indicate standard deviation across
  tasks. Clear axis labels, legend, and professional styling.
aspect_ratio: '16:9'
summary: Threshold sensitivity analysis showing robustness across refutation bounds.
figure_path: figures/fig3_v0.pdf

--- Item 4 ---
id: fig4
figure_type: data
title: Trajectory Rationalization Index Across Domains
caption: >-
  Trajectory Rationalization Index (TRI) measuring recursive rationalization and hallucinated success justifications in agent
  reasoning traces across machine learning domains (Classification, Regression, Time Series). FPG planning suppresses rationalization
  to 0.096 compared to 0.807 for procedural agents.
image_gen_detailed_description: >-
  Grouped bar chart comparing Trajectory Rationalization Index (TRI, range 0.0 to 1.0) across four domains: Classification,
  Regression, Time Series, and Synthetic Non-linear. Two series per domain: 'Standard Procedural Planner' (Classification:
  0.81, Regression: 0.79, Time Series: 0.84, Synthetic: 0.79) and 'Falsifiable Prediction Graph (Ours)' (Classification: 0.09,
  Regression: 0.10, Time Series: 0.11, Synthetic: 0.09). Y-axis label 'Trajectory Rationalization Index (TRI)', X-axis label
  'Domain'. Professional palette.
aspect_ratio: '16:9'
summary: >-
  Compares trajectory rationalization index across domains between FPG and procedural planners.
figure_path: figures/fig4_v0.pdf
</available_figures>

<figure_requirements>
CRITICAL: Include ALL figures from <available_figures>. No exceptions.

- Every figure MUST use \includegraphics{figures/<the filename from its own `figure_path` above>} — INCLUDING the extension it actually has. Data figures are delivered as `.pdf` (vector, so their axis labels stay sharp) and concept figures as `.jpg`. Writing `.jpg` for a `.pdf` figure names a file that is not in figures/ and the build fails on it
- Do NOT skip, convert to tables, or describe without inserting
- Each needs: \begin{figure}[placement], \includegraphics, \caption, \label, \end{figure} — one placement for every figure, see FLOAT PLACEMENT below. Constrain every \includegraphics with `width=\linewidth,height=0.85\textheight,keepaspectratio`. The height is a LAST RESORT, not the usual limit: it exists so a very tall figure cannot overrun the page, and at 0.4 it bound almost everything instead — a 1:1 confusion matrix printed at 50.9% and its 11 pt axis labels reached the page at 5.6 pt, below what any venue accepts. At 0.85 every ratio the paper prompt prescribes (21:9, 16:9, 4:3, 1:1) is limited by WIDTH, prints at 93% and keeps its text above 10 pt. Use exactly these option keys — `max height=` is NOT valid LaTeX
- Use the `caption` field from each figure for \caption{...} — do NOT invent new captions
- Place figures where their [FIGURE:fig_id] markers appear in paper_text
- VERIFICATION: paper.tex MUST have exact same number of \includegraphics as <available_figures>
- Do NOT generate new figure images (no matplotlib, no PIL, no image generation). Use ONLY the pre-generated figures from <available_figures>. They were already created by a previous pipeline step.

FLOAT PLACEMENT: every figure gets \begin{figure}[!htbp]. Measured, not chosen:
the document the aii-paper-to-latex skill sets up is ONE column, so `figure*` is
exactly as wide as `figure` (469.76pt either way) and gains nothing; and any
placement asking for a page TOP — `[!t]`, `[!tbp]` — floated the hero diagram above
the paper's own title on page 1, while `[!htbp]` did not. `[!htbp]` also gives LaTeX
four options, so a float can never be deferred to the end of the document, which one
option alone risks. Where the hero ENDS UP is decided by its [FIGURE:] marker in
paper_text, which is already placed near the end of the Introduction — preserve it.
</figure_requirements>

<artifact_links>
The paper_text contains \footnote{Code: \url{...}} references linking to artifact source code
on GitHub. Include \usepackage{hyperref} and \usepackage{url}.
Preserve these exactly as-is — do not remove, rewrite, or convert them to plain text.
The URLs will not resolve yet (the repo is deployed after compilation) — do NOT try to verify or fix them.
</artifact_links>

<headings>
NEVER use inline math (``$...$``) inside ``\section{...}`` / ``\subsection{...}`` / ``\subsubsection{...}`` arguments — hyperref's bookmark builder errors out (``Token not allowed in a PDF string``) and the PDF outline breaks. If a section heading needs a math-looking term, use the text equivalent (``d star`` not ``$d^*$``, ``alpha-equivalent`` not ``$\alpha$-equivalent``) or wrap it in ``\texorpdfstring{$math$}{plain}``. Inline math inside body paragraphs is fine.
</headings>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.
TODO 2. Review <paper_text> and <available_figures>. Copy all figure images into ./figures/ in your workspace. Count figures — MUST include every one. Plan placements per section. Build `./references.bib` via aii_semscholar_bib__fetch — collect DOIs/ArXiv IDs from <paper_text> and batch-fetch all BibTeX in one call. Do NOT fabricate entries.
TODO 3. Create `./paper.tex` per aii-paper-to-latex skill's setup, write ALL sections, insert ALL figures from <available_figures>, include `./references.bib` via \bibliography. Compile to PDF per skill's process. Fix errors.
TODO 4. CRITICAL VERIFICATION: Run `grep -c 'includegraphics' paper.tex`, confirm count equals figures in <available_figures>. If not, add missing figures. Verify `./paper.pdf` was created.
TODO 5. VISUAL REVIEW: Write Python script to convert EVERY page of paper.pdf to PNG at 150 DPI (use pdf2image or pymupdf). Then read ALL page screenshots — each page image costs ~1,600 tokens so a 15-page paper is only ~24K tokens. You MUST read every page. The ONLY exception is if all page images would not fit in your remaining context — in that case, read as many as fit and state which pages you are skipping and why. Check every page for layout issues, overlapping figures, cut-off text, bad spacing, formatting problems. Fix issues and recompile.
TODO 6. FINAL READ: Check page count (`pdfinfo paper.pdf` or pymupdf). Read entire paper.pdf — check for missing sections, unclear explanations, inconsistencies, typos. Fix and recompile. The ONLY exception is if all pages would not fit in your remaining context — in that case, read as many pages as fit and state which pages you are skipping and why.
</todos>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FullPaperExpectedFiles": {
      "description": "All expected output files from full paper generation.",
      "properties": {
        "paper_tex_path": {
          "description": "Path to LaTeX source file. Example: 'paper.tex'",
          "title": "Paper Tex Path",
          "type": "string"
        },
        "paper_pdf_path": {
          "description": "Path to compiled PDF. Example: 'paper.pdf'",
          "title": "Paper Pdf Path",
          "type": "string"
        },
        "references_bib_path": {
          "description": "Path to BibTeX bibliography file. Example: 'references.bib'",
          "title": "References Bib Path",
          "type": "string"
        },
        "figure_paths": {
          "description": "Paths to all figure image files. Example: ['figures/fig1_v0.jpg', 'figures/fig2_v0.jpg']",
          "items": {
            "type": "string"
          },
          "title": "Figure Paths",
          "type": "array"
        }
      },
      "required": [
        "paper_tex_path",
        "paper_pdf_path",
        "references_bib_path",
        "figure_paths"
      ],
      "title": "FullPaperExpectedFiles",
      "type": "object"
    }
  },
  "description": "Full paper \u2014 structured output from paper generation.",
  "properties": {
    "title": {
      "description": "Paper title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance. Aim for about 4-8 words (~40 characters).",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "description": "Brief summary of the generated paper: sections written, figures included, compilation status",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/FullPaperExpectedFiles",
      "description": "All output files you created. Must include paper.tex, paper.pdf, references.bib, and paths to all figure files."
    }
  },
  "required": [
    "title",
    "summary",
    "out_expected_files"
  ],
  "title": "FullPaper",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [4] HUMAN-USER prompt · 2026-08-09 23:52:35 UTC

```
Examine whether structuring a research plan as explicit falsifiable predictions improves the rate at which an automated pipeline detects its own negative results.
```

### [5] SKILL-INPUT — aii-paper-to-latex · 2026-08-09 23:52:57 UTC

The agent loaded the **aii-paper-to-latex** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-to-latex
description: LaTeX paper assembly and compilation. Covers document setup, figure inclusion from pre-generated vector PDFs and JPEGs, compilation process, and output files. Use when assembling a paper from pre-written text and pre-generated figures into a compiled PDF.
---

## LaTeX Paper Assembly

Assembles a research paper from paper text, pre-generated figures (vector `.pdf` for data figures, `.jpg` for concept figures) and a bibliography into a compiled PDF.

### Document Setup

```latex
\documentclass[11pt,letterpaper]{article}
\usepackage{graphicx, geometry, amsmath, hyperref, natbib, booktabs, xcolor, listings}
\geometry{margin=1in}
\hypersetup{colorlinks=true, linkcolor=black, citecolor=black, urlcolor=black}
```

### Figure Inclusion

CRITICAL: Include ALL figures. Every figure MUST appear in the paper.

```latex
\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.92\textwidth,keepaspectratio]{figures/filename.pdf}
  \caption{Descriptive caption.}
  \label{fig:label}
\end{figure}
```

Rules:
- ALWAYS `[!htbp]` — all four options, so a float can never be deferred to the end of the
  document, which `[t]` or `[h]` alone risks. Do not ask for a page TOP: `[!t]` and
  `[!tbp]` both floated a figure ABOVE the paper's own title on page 1, where `[!htbp]`
  on the same document did not. Where a figure lands is decided by where it is declared
  in the text
- Use `figure`, never `figure*`. This document class is ONE column, so `figure*` is exactly
  as wide as `figure` (469.76pt either way) and gains nothing, while restricting the float
  to a page top
- ALWAYS constrain with `width` and `keepaspectratio`. Add `height` only as a
  LAST RESORT against a very tall figure overrunning the page, and keep it
  generous — `0.85\textheight`. A tight height cap binds on ordinary figures
  and LaTeX then shrinks the TEXT with them: at `0.4\textheight` a square
  figure printed at 50.9%, putting 11 pt axis labels on the page at 5.6 pt.
  The figure generator measures legibility at the figure's OWN size, so it
  cannot see this happen
- Every figure needs `\caption`, `\label`, and a `\ref` in the text
- Do NOT convert figures to tables or describe them without inserting the image
- Do NOT skip any figures

### Compilation Process

Run each command separately (do NOT chain with `&&` — pdflatex often exits non-zero on warnings, which would skip bibtex and leave citations as `??`):

```bash
pdflatex -interaction=nonstopmode paper.tex
bibtex paper
pdflatex -interaction=nonstopmode paper.tex
pdflatex -interaction=nonstopmode paper.tex
```

All four commands are required. Skipping bibtex causes `??` in all citations.
Fix any errors between runs. Verify `./paper.pdf` was created.

### Output Files

- `./paper.tex` — LaTeX source
- `./references.bib` — bibliography file
- `./paper.pdf` — compiled PDF
- `./figures/` — all figure images (pre-generated, copied into workspace). Data
  figures are `.pdf` (vector — LaTeX renders their text at page resolution, which
  is what keeps axis labels sharp in print); concept figures are `.jpg`. Use each
  file's OWN extension in `\includegraphics`; there is no conversion step.
````

### [6] SKILL-INPUT — aii-semscholar-bib · 2026-08-09 23:52:59 UTC

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

### [7] SYSTEM-USER prompt · 2026-08-10 00:12:07 UTC

````
PREVIOUS ATTEMPT FAILED
Failure reason: structured_output is None
Last actions before failure:
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "C-c",
  "is_input": true,
  "timeout": null,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "No previous running command to interact with."}], "is_error": true, "command": "C-c", "exit_code": null, "timeout": false, "metadata": {"exit_code": -1, "pid": -1, "username": null, "hostname": null, "working_dir": 
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cd /ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace && timeout 60 bibtex.original paper > /tmp/bib.log 2>&1; echo \"BIBTEX EXIT: $?\"; echo \"---bib log---\"; cat /tmp/bib.log",
  "is_input": false,
  "timeout": null,
  "re
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "BIBTEX EXIT: 0\n---bib log---\nThis is BibTeX, Version 0.99d (TeX Live 2022/Debian)\nThe top-level auxiliary file: paper.aux\nThe style file: plainnat.bst\nDatabase file #1: references.bib"}], "is_error": false, "co
  - [agent_response]: bibtex succeeded with no errors. Now run two more pdflatex passes to resolve citations.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cd /ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace && timeout 160 pdflatex -interaction=nonstopmode -halt-on-error paper.tex > /tmp/pl2.log 2>&1; echo \"PASS2 EXIT: $?\"; timeout 160 pdflatex -interaction=nonstopmode -halt
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "PASS2 EXIT: 0\nPASS3 EXIT: 0\n-rw-r--r-- 1 root root 274276 Aug 10 00:08 paper.pdf"}], "is_error": false, "command": "cd /ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace
  - [agent_response]: PDF compiled (274KB). Let me check for undefined references and any warnings.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cd /ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace && echo \"=== Undefined refs ===\"; grep -iE \"undefined|Citation.*undefined\" /tmp/pl3.log; echo \"=== Warnings ===\"; grep -iE \"^LaTeX Warning|^Package\" /tmp/pl3.log |
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "=== Undefined refs ===\n=== Warnings ===\n=== includegraphics count in tex ===\n4"}], "is_error": false, "command": "cd /ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace 
  - [agent_response]: Verification passed: 4 `\includegraphics` = 4 figures, no undefined refs, no warnings. Let me update todos and move to visual review.
  - [agent_tool_call] task_tracker: Tool: task_tracker
{
  "command": "plan",
  "task_list": [
    {
      "title": "TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.",
      "notes": "",
      "status": "done"
    },
    {
      "title": "TODO 2. Review <paper_text> and <available_figures>. Copy a
  - [agent_tool_result] task_tracker: Tool: task_tracker
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Task list has been updated with 6 item(s)."}], "is_error": false, "command": "plan", "task_list": [{"title": "TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.", "notes": "",
  - [agent_response]: Now the visual review. I need to convert each page to PNG at 150 DPI. Let me install pdf2image/pymupdf.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "python3 -c \"import fitz; print('pymupdf', fitz.__doc__)\" 2>&1 | head -3; echo \"---pdf2image---\"; python3 -c \"import pdf2image; print('pdf2image ok')\" 2>&1 | head -2; echo \"---pdfinfo---\"; which pdfinfo pdftoppm",
  "is_input": false,
  "timeout": null,
  "reset
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Traceback (most recent call last):\n  File \"<string>\", line 1, in <module>\nModuleNotFoundError: No module named 'fitz'\n---pdf2image---\nTraceback (most recent call last):\n  File \"<string>\", line 1, in <module
  - [agent_response]: `pdftoppm` and `pdfinfo` are available (poppler). Let me get page count and convert all pages to PNG at 150 DPI.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cd /ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace && pdfinfo paper.pdf 2>/dev/null | grep -iE \"pages|page size\"; echo \"---page count from info---\"; PAGES=$(pdfinfo paper.pdf 2>/dev/null | grep -i pages | awk '{print $
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Pages:           10\nPage size:       612 x 792 pts (letter)\n---page count from info---\nPages: 10"}], "is_error": false, "command": "cd /ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_pape
  - [status_public_warning]: [ConversationErrorEvent]

Use any partial work that exists from the previous attempt. Do NOT start over — pick up where the previous attempt left off.

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/`:
GOOD: `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/file.py`, `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>

<task>
Create a publication-ready top-conference LaTeX paper with BibTeX from <paper_text> and <available_figures>, compile to PDF.
</task>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<paper_text>
title: >-
  Falsifiable Prediction Graphs: Eliminating Confirmation Bias and Detecting Negative Results in Automated Agent Research
  Planning
abstract: >-
  Automated scientific discovery agents—such as autonomous LLM research pipelines—demonstrate remarkable capabilities in code
  generation and experiment execution, but suffer from a persistent and fundamental vulnerability: acute confirmation bias.
  When confronted with ambiguous, null, or negative experimental outcomes, standard procedural planners overwhelmingly rationalize
  failures, adjust evaluation criteria post-hoc, or hallucinate spurious successes. In this paper, we introduce Falsifiable
  Prediction Graphs (FPGs), a novel agent planning architecture that structures research workflows as directed acyclic graphs
  of conditional hypotheses, where every experimental node mandates explicit quantitative refutation predicates and early
  negative control validation. By enforcing programmatic predicate evaluation rather than verbal LLM self-critique, FPGs establish
  an immutable control mechanism against recursive rationalization. Through comprehensive empirical evaluation across a 30-task
  machine learning benchmark suite spanning classification, regression, and time-series domains, we demonstrate that FPG planning
  achieves an 87.14% to 100% negative result detection rate (compared to 38.57% for procedural baselines), eliminates false
  positive success claims on negative controls (0.0% to 12.85% vs. 61.43%), significantly improves search iteration efficiency
  (4.5 vs. 9.7 mean iterations), and reduces the Trajectory Rationalization Index from 0.807 to 0.096 (p < 0.001).
paper_text: "# Introduction\n\nAutomated scientific discovery systems—such as autonomous LLM agent pipelines designed to formulate\
  \ hypotheses, write code, execute experiments, and analyze results—represent a transformative frontier in artificial intelligence\
  \ [1]. However, despite impressive capabilities in synthesizing novel machine learning architectures and executing computational\
  \ pipelines, current agentic discovery frameworks (e.g., The AI Scientist [1]) suffer from a persistent and fundamental\
  \ vulnerability: **acute confirmation bias**. When confronted with ambiguous, null, or outright negative experimental outcomes,\
  \ standard language model agents overwhelmingly tend to rationalize failures, adjust evaluation criteria post-hoc, or hallucinate\
  \ spurious successes, leading to wasted computational resources and the propagation of flawed scientific claims down unpromising\
  \ research dead ends [2].\n\nThe root cause of this failure mode lies in the structure of automated research plans. Traditional\
  \ automated discovery agents operate using **procedural task lists**—linear or loosely branched sequences of action steps\
  \ (e.g., \"load dataset, train model, compute accuracy, write report\") devoid of formal semantic constraints regarding\
  \ what constitutes failure. Because LLMs are inherently biased toward generating affirmative narratives and satisfying prompt\
  \ directives, procedural execution encourages agents to treat any numerical output as confirmation of the underlying hypothesis\
  \ [3].\n\nIn philosophy of science, Karl Popper resolved a parallel epistemological challenge by introducing **falsifiability**\
  \ as the demarcation criterion of empirical science [4]. Rather than seeking confirmatory instances, rigorous scientific\
  \ inquiry proceeds by formulating bold conjectures coupled with precise refutation conditions—observable predictions that,\
  \ if met, would decisively disprove the hypothesis [5]. Yet, while post-hoc validation frameworks (such as POPPER [2]) evaluate\
  \ free-form hypotheses against external testbeds, no existing automated discovery system embeds structural falsifiability\
  \ directly into the **research planning phase** to govern agent execution and real-time self-correction.\n\nTo address this\
  \ gap, we introduce **Falsifiable Prediction Graphs (FPGs)**, a novel agent planning architecture that structures research\
  \ workflows as directed acyclic graphs of conditional hypotheses, where every experimental node mandates explicit quantitative\
  \ refutation predicates and early negative control validation. By forcing agents to define boundary conditions under which\
  \ their proposed methods fail *before* executing code, FPGs establish an objective control mechanism against confirmation\
  \ bias.\n\n[FIGURE:fig1]\n\nOur key contributions are summarized as follows:\n- **Formalization of Falsifiable Planning**:\
  \ We define Falsifiable Prediction Graphs, integrating Popperian refutation criteria and negative control validation directly\
  \ into automated agent workflow graphs.\n- **Programmatic Predicate Evaluation vs. Verbal Critique**: We contrast objective\
  \ logical predicate enforcement against recursive verbal self-correction loops, demonstrating substantial suppression of\
  \ agent rationalization.\n- **The Agent Falsifiability Benchmark Suite & Rigorous Sensitivity Analysis**: We construct a\
  \ 30-task benchmark suite spanning classification, regression, and time-series domains, paired with negative control settings\
  \ and comprehensive threshold sensitivity sweeps [ARTIFACT:art_A_97AHCsuvAa, ARTIFACT:art_HjQ6l6qOmCqb].\n- **Empirical\
  \ Superiority**: We demonstrate that FPG planning achieves an 87.14% to 100% negative result detection rate (compared to\
  \ 38.57% for procedural planners, $p < 0.001$), eliminates false positive success claims on negative controls ($0.0\\%$\
  \ to $12.85\\%$ vs. $61.43\\\\%$), improves search iteration efficiency (4.5 vs. 9.7 mean iterations), and reduces the Trajectory\
  \ Rationalization Index from $0.807$ to $0.096$ [ARTIFACT:art_QUgzY-dCbiIl].\n\n\n# Related Work\n\nOur research intersects\
  \ with three primary domains: automated scientific discovery, LLM agent planning and self-correction, and computational\
  \ philosophy of science.\n\n### Automated Scientific Discovery Systems\nFully automated scientific discovery has advanced\
  \ rapidly with the advent of frontier large language models. Systems such as The AI Scientist [1] demonstrated end-to-end\
  \ automation of idea generation, experiment execution, and manuscript drafting in machine learning. However, subsequent\
  \ analyses highlighted pervasive failure modes, including hallucinated evaluation metrics, confirmation bias, and unchecked\
  \ persistence down failed experimental trajectories [6]. While prior engineering efforts have focused on improving code\
  \ generation robustness or expanding search spaces, they retain procedural task list planning paradigms that lack intrinsic\
  \ mechanisms for recognizing negative results.\n\n### Agent Planning and Self-Correction & Programmatic vs. Verbal Feedback\n\
  Planning in LLM agents has evolved from static linear prompting to dynamic tree-of-thought search [7], reflection loops\
  \ [8], and interactive planning frameworks [9]. Frameworks like Reflexion [8] leverage verbal reinforcement learning to\
  \ critique agent trajectories. However, verbal critique alone remains highly susceptible to **recursive rationalization**:\
  \ because LLMs are heavily conditioned to satisfy prompt instructions and generate fluent justifications, verbal self-critique\
  \ loops frequently rationalize sub-optimal performance as artifactual noise rather than epistemic refutation. \n\nOur work\
  \ diverges fundamentally by shifting from post-hoc verbal critique to structural refutation constraints. Rather than relying\
  \ on LLM-as-judge narrative summaries, FPGs employ **programmatic predicate evaluation**, executing rigorous, immutable\
  \ logical checks ($\\phi_i$) that operate independently of LLM narrative generation. This structural enforcement prevents\
  \ the agent from talking itself into accepting a failed experiment.\n\n### Popperian Falsification in Computational Reasoning\n\
  The application of Karl Popper's philosophy of science [4] to computational systems has inspired several theoretical and\
  \ empirical frameworks [10]. Recently, POPPER [2] proposed an agentic framework for validating free-form hypotheses using\
  \ sequential falsification experiments. While POPPER operates post-hoc on external hypotheses, our approach integrates structural\
  \ falsifiability upstream into the research planning phase, governing agent execution trajectories and enabling real-time\
  \ negative control validation.\n\n\n# Falsifiable Prediction Graphs: Architecture and Formalization\n\n### Preliminaries\
  \ and Problem Formulation\nLet an automated research discovery task be defined by a research goal $\\mathcal{G}$, a dataset\
  \ $\\mathcal{D}$, and an agent execution environment $\\mathcal{E}$. In a standard procedural planner, the research plan\
  \ $P_{\\text{proc}} = [s_1, s_2, \\dots, s_n]$ is a sequence of procedural instructions executed sequentially. The agent\
  \ evaluates success based on whether the terminal performance metric $M(\\mathcal{E}(s_n))$ exceeds a heuristic threshold\
  \ $\\tau$. When faced with a flawed hypothesis or a negative control dataset, the agent frequently rationalizes sub-threshold\
  \ performance as noise, resulting in false positive success claims.\n\n### Falsifiable Prediction Graph (FPG) Definition\n\
  A Falsifiable Prediction Graph $G = (V, E, \\Phi)$ is a directed acyclic graph where:\n1. **$V$** represents experimental\
  \ nodes (e.g., baseline establishment, hyperparameter tuning, architectural modification).\n2. **$E$** represents conditional\
  \ execution dependencies.\n3. **$\\Phi$** is a set of explicit quantitative refutation predicates associated with each node\
  \ $v \\in V$.\n\nFormally, every experimental node $v_i$ is tupled with a refutation predicate $\\phi_i = (\\text{Metric},\
  \ \\text{Threshold}, \\text{Direction}, \\text{NegativeControlTest})$. For example, a refutation predicate might specify:\
  \ \"If the validation accuracy delta over baseline is $< +0.01$ or if negative control feature permutation yields $< 5\\\
  %$ performance drop, reject hypothesis $H_i$ as a negative result.\"\n\n### Execution Protocol and Negative Control Validation\n\
  During pipeline execution, the FPG planner evaluates refutation predicates $\\Phi$ at each graph juncture. If an experimental\
  \ outcome triggers a refutation condition $\\phi_i$, the graph dynamically halts traversal along that branch, logs a structured\
  \ negative result, and triggers backtracking or search space pruning. Furthermore, FPGs mandate an early **Negative Control\
  \ Validation** step: before investing computational budget in complex method development, the agent executes the proposed\
  \ methodology against a randomized or adversarially corrupted version of the dataset. A valid method must fail on the negative\
  \ control; if the agent claims success on the negative control, the planning pipeline flags a confirmation bias violation\
  \ and aborts the trajectory.\n\n### Qualitative Walkthrough: Live Agent Encounter with a Negative Control\nTo illustrate\
  \ how FPG planning operates during live agent execution, consider an autonomous research agent tasked with evaluating a\
  \ novel regularized classifier. Under standard procedural planning, the agent trains the model on a permuted-label dataset\
  \ (negative control), observes an accuracy of $51.2\\%$, and—prompted to complete the task—generates the narrative: *\"\
  Model successfully trained and evaluated; accuracy is comparable to baseline expectation.\"* \n\nIn contrast, under FPG\
  \ planning, the plan mandates a programmatic refutation predicate: $\\phi_{\\text{neg}} = (\\text{AccuracyLoss} \\ge 0.15\
  \ \\text{ on permuted labels})$. Upon executing the experiment, the programmatic checker evaluates the metric against $\\\
  phi_{\\text{neg}}$, detects that the expected performance drop did not occur (delta $< 0.15$), immediately triggers a refutation\
  \ flag, halts execution along the development branch, and logs: *\"Falsification triggered: Method fails to distinguish\
  \ permuted target labels; hypothesis rejected as spurious artifact.\"* This prevents the agent from propagating the flawed\
  \ method into advanced hyperparameter tuning.\n\n\n# Experimental Methodology & Benchmark Suite\n\nTo rigorously test our\
  \ hypothesis, we utilized the **Agent Falsifiability Benchmark Suite** [ARTIFACT:art_A_97AHCsuvAa, ARTIFACT:art_HjQ6l6qOmCqb],\
  \ comprising 10 diverse empirical machine learning research tasks spanning regression, binary classification, multi-class\
  \ classification, and synthetic time-series modeling. Each research task is instantiated in three distinct experimental\
  \ settings:\n1. **True Positive Condition**: A valid methodological improvement expected to yield genuine performance gains.\n\
  2. **Negative Control Condition (Permuted Labels)**: Target labels are randomly permuted, ensuring that any claimed performance\
  \ improvement is a statistical artifact or agent hallucination.\n3. **Negative Control Condition (Adversarial Noise)**:\
  \ Input features are replaced with Gaussian noise, removing true signal.\n\n### Evaluated Architectures and Baselines\n\
  We compared two automated agent planning architectures:\n- **Standard Procedural Planner**: Executes linear task lists without\
  \ refutation criteria, relying on LLM verbal self-critique loops and post-hoc summarization to determine success or failure.\n\
  - **Falsifiable Prediction Graph Planner (Our Approach)**: Enforces structured causal dependency graphs equipped with explicit\
  \ mandatory refutation criteria, programmatic predicate evaluation, and early negative control validation tests.\n\n###\
  \ Evaluation Metrics and Statistical Rigor\nWe operationalized four primary evaluation metrics:\n- **Negative Result Detection\
  \ Rate**: The proportion of negative control tasks correctly identified as failed/null results rather than misinterpreted\
  \ as successes.\n- **False Positive Rate**: The proportion of negative control tasks incorrectly reported as successful\
  \ methodological breakthroughs (hallucinated success rate).\n- **Search Iteration Efficiency**: The mean number of execution\
  \ iterations required by the agent to resolve the research task.\n- **Trajectory Rationalization Index (TRI)**: A metric\
  \ quantifying the proportion of agent reasoning steps exhibiting recursive rationalization and hallucinated success justifications.\n\
  \nWe evaluated statistical significance using Fisher's exact test, chi-squared tests, and Cohen's $h$ effect size analyses\
  \ [ARTIFACT:art_QUgzY-dCbiIl].\n\n\n# Results & Empirical Evaluation\n\nWe executed both planning architectures across the\
  \ 30 evaluation task instances (10 base tasks $\\times$ 3 conditions) and conducted rigorous threshold sensitivity sweeps\
  \ ($\\tau$ from $0.00$ to $0.20$). The empirical results decisively confirm our hypothesis [ARTIFACT:art_HjQ6l6qOmCqb, ARTIFACT:art_QUgzY-dCbiIl].\n\
  \n### Negative Result Detection and False Positive Elimination\nAs summarized in Table 1 and Figure 2, the Falsifiable Prediction\
  \ Graph planner achieved a **100% Negative Result Detection Rate** ($1.00 \\pm 0.00$ in base evaluation; $87.14\\%$ across\
  \ threshold sweeps), correctly identifying negative control tasks as failures. In sharp contrast, the standard procedural\
  \ planner achieved only a **33.3% to 38.57% Negative Result Detection Rate** ($0.3333 \\pm 0.12$) [ARTIFACT:art_QUgzY-dCbiIl],\
  \ frequently succumbing to confirmation bias by rationalizing permuted-label success or ignoring anomalous metric drops.\n\
  \n| Planning Architecture | Negative Result Detection Rate $\\uparrow$ | False Positive Rate $\\downarrow$ | Mean Search\
  \ Iterations $\\downarrow$ | Trajectory Rationalization Index $\\downarrow$ |\n| :--- | :---: | :---: | :---: | :---: |\n\
  | **Standard Procedural Planner** | $0.3333 \\pm 0.12$ | $0.6667 \\pm 0.12$ | $9.7 \\pm 1.4$ | $0.8068 \\pm 0.08$ |\n| **Falsifiable\
  \ Prediction Graph (Ours)** | **$1.0000 \\pm 0.00$** | **$0.0000 \\pm 0.00$** | **$4.5 \\pm 0.7$** | **$0.0957 \\pm 0.03$**\
  \ |\n| *Statistical Significance ($p$-value)* | $p = 0.0002^{**}$ | $p = 0.0002^{**}$ | $p < 0.0001^{**}$ | $p < 0.0001^{**}$\
  \ |\n\nTable 1: Quantitative comparison between Standard Procedural Planners and Falsifiable Prediction Graph Planners across\
  \ benchmark task instances. Asterisks denote statistical significance via Fisher's exact test and chi-squared tests ($^{**}\
  \ p < 0.001$, $\\chi^2 = 12.15$, Cohen's $h = 1.91$) [ARTIFACT:art_QUgzY-dCbiIl].\n\n[FIGURE:fig2]\n\nFurthermore, while\
  \ the standard procedural planner exhibited a **66.7% False Positive Rate** on negative controls—hallucinating methodological\
  \ success on randomized data—the FPG planner achieved a **0.0% False Positive Rate** ($0.00 \\pm 0.00$) [ARTIFACT:art_QUgzY-dCbiIl].\
  \ Fisher's exact test and chi-squared tests confirm this performance delta is highly significant ($\\chi^2 = 12.15$, $p\
  \ = 0.00049$, Cohen's $h = 1.91$) [ARTIFACT:art_QUgzY-dCbiIl].\n\n### Threshold Sensitivity Analysis\nTo address potential\
  \ concerns regarding threshold sensitivity, we conducted rigorous sweeps of refutation thresholds ($\\tau$ from $0.00$ to\
  \ $0.20$ and delta bounds from $0.01$ to $0.10$). As illustrated in Figure 3, the FPG planner maintained exceptional stability:\
  \ across all threshold variations, the overall negative result detection rate remained robust at $87.14\\%$, while the false\
  \ positive rate remained constrained at $12.85\\%$. In contrast, procedural baselines fluctuated widely, exhibiting a mean\
  \ false positive rate of $61.43\\%$. This demonstrates that programmatic predicate evaluation is highly resilient to hyperparameter\
  \ threshold variations.\n\n[FIGURE:fig3]\n\n### Trajectory Rationalization and Search Efficiency\nEmbedding structural refutation\
  \ criteria and early negative control validation significantly reduced agent rationalization. As quantified by the Trajectory\
  \ Rationalization Index (TRI), procedural planners exhibited an average rationalization score of **$0.8068$**, whereas FPG\
  \ planning suppressed rationalization to **$0.0957$** ($p < 0.0001$) [ARTIFACT:art_QUgzY-dCbiIl]. Furthermore, early negative\
  \ control pruning reduced search iteration complexity: FPG converged in a mean of **$4.5$ iterations**, compared to **$9.7$\
  \ iterations** for procedural planners [ARTIFACT:art_QUgzY-dCbiIl].\n\n[FIGURE:fig4]\n\n\n# Discussion\n\n### Why Procedural\
  \ Planners Fail\nOur findings illuminate why traditional LLM agent planners fail in empirical research tasks. Language models\
  \ trained on scientific literature and code repositories are heavily conditioned to emulate successful outcomes. When an\
  \ agent executes an experiment that yields null results (e.g., accuracy near random chance on permuted labels), its parametric\
  \ memory associates code execution with \"finishing a task,\" prompting the LLM to generate narrative justifications rather\
  \ than recognizing epistemic refutation.\n\n### The Power of Programmatic Predicate Enforcement\nFalsifiable Prediction\
  \ Graphs resolve this pathology by decoupling execution completion from hypothesis validation. By encoding refutation criteria\
  \ $\\Phi$ as explicit logical predicates evaluated programmatically rather than narratively, FPGs compel the agent to treat\
  \ negative outcomes as primary feedback signals. This contrasts sharply with verbal self-critique loops, which remain trapped\
  \ within the LLM's generative bias.\n\n### Limitations\nWhile FPGs successfully eliminate confirmation bias in automated\
  \ research tasks, several limitations remain:\n1. **Threshold Sensitivity**: Constructing precise quantitative refutation\
  \ thresholds requires domain heuristics. Overly strict thresholds may trigger false refutations on valid methods with high\
  \ variance.\n2. **Graph Expressivity**: Highly exploratory research tasks involving paradigm shifts or unsupervised discovery\
  \ may not easily conform to static directed acyclic prediction graphs.\n3. **Planning Token Overhead**: Generating comprehensive\
  \ refutation predicates increases prompt complexity and initial planning token consumption.\n\n\n# Conclusion & Future Work\n\
  \nIn this paper, we introduced Falsifiable Prediction Graphs (FPGs), a novel agent planning architecture that integrates\
  \ Popperian falsification and negative control validation into automated scientific discovery workflows. Through rigorous\
  \ evaluation across a 30-task machine learning benchmark suite and threshold sensitivity sweeps, we demonstrated that FPGs\
  \ achieve a 100% negative result detection rate, eliminate false positive success claims on negative controls, and significantly\
  \ improve search efficiency compared to standard procedural planners [ARTIFACT:art_HjQ6l6qOmCqb, ARTIFACT:art_QUgzY-dCbiIl].\n\
  \nFuture work will explore dynamic, self-evolving falsification graphs that adapt refutation thresholds based on real-time\
  \ task complexity, as well as scaling FPGs to multi-agent collaborative discovery systems.\n\n# References\n\n[1] Lu, C.,\
  \ Lu, C., Lange, R. T., Foerster, J. N., Clune, J., & Ha, D. (2024). The AI Scientist: Fully automated scientific discovery.\
  \ *arXiv preprint arXiv:2408.06292*.\n[2] Huang, T., Zhang, Y., & Wang, L. (2025). POPPER: Agentic hypothesis validation\
  \ through sequential falsification. *Journal of Automated Scientific Reasoning*, 3(2), 112-128.\n[3] Popper, K. (1959).\
  \ *The Logic of Scientific Discovery*. Hutchinson.\n[4] Wang, Z., Cai, S., Liu, A., Wang, Y., & Liang, X. (2023). Describe,\
  \ explain, select and evaluate: Interactive planning for large language model agents. *Advances in Neural Information Processing\
  \ Systems*, 36.\n[5] Shinn, N., Cassano, B., Labash, E., Gopinath, A., Narasimhan, K., & Yao, S. (2023). Reflexion: Language\
  \ agents with verbal reinforcement learning. *Advances in Neural Information Processing Systems*, 36.\n[6] Yao, S., Yu,\
  \ D., Zhao, J., Shafran, I., Griffiths, T., Cao, Y., & Narasimhan, K. (2023). Tree of thoughts: Deliberate problem solving\
  \ with large language models. *Advances in Neural Information Processing Systems*, 36.\n[7] Chen, L., Zaharia, M., & Zou,\
  \ J. (2023). Evaluating large language model agents on empirical machine learning tasks. *arXiv preprint arXiv:2310.03302*.\n"
summary: >-
  Falsifiable Prediction Graphs embed Popperian refutation predicates and negative control validation into agent research
  planning, eliminating confirmation bias and achieving 100% negative result detection.
</paper_text>

<available_figures>
--- Item 1 ---
id: fig1
figure_type: concept
title: Falsifiable Prediction Graph Architecture
caption: >-
  End-to-end architecture of a Falsifiable Prediction Graph (FPG). Research workflows are structured as directed acyclic graphs
  where experimental nodes are tupled with programmatic refutation predicates (Phi). Early negative control validation tests
  (permuted labels and adversarial noise) govern graph traversal and branch pruning before iterative method refinement.
image_gen_detailed_description: >-
  Horizontal workflow diagram, left to right. Three main horizontal layers: (1) Hypothesis Formulation with graph initialization,
  (2) Mandatory Negative Control Validation node evaluating permuted labels against predicate Phi, (3) Conditional Execution
  Graph branching into Refinement or Falsification/Branch Pruning. Distinct color-coded nodes: Green for valid execution branches,
  Red for falsified/pruned negative branches. Clean white background, modern sans-serif typography, flat 2D schematic design.
aspect_ratio: '21:9'
summary: >-
  Architecture diagram illustrating Falsifiable Prediction Graph topology and conditional branching.
figure_path: figures/fig1_v0.jpg

--- Item 2 ---
id: fig2
figure_type: data
title: Negative Result Detection and False Positive Rates
caption: >-
  Comparison of Negative Result Detection Rate and False Positive Rate between Standard Procedural Planners and Falsifiable
  Prediction Graph Planners across 30 benchmark task instances. FPG planning achieves 100% negative result detection and 0%
  false positives, significantly outperforming procedural planners (p < 0.001).
image_gen_detailed_description: >-
  Grouped bar chart comparing two planning architectures across two key metrics. X-axis categories: 'Negative Result Detection
  Rate (up arrow)', 'False Positive Rate (down arrow)'. Series 1: 'Standard Procedural Planner' (Detection: 0.33, False Positive:
  0.67). Series 2: 'Falsifiable Prediction Graph (Ours)' (Detection: 1.00, False Positive: 0.00). Y-axis range: 0.0 to 1.0.
  Clean grid lines, distinct professional color palette (slate blue and coral), error bars indicating standard error, legend
  included.
aspect_ratio: '16:9'
summary: >-
  Compares negative result detection and false positive rates between FPG and procedural planners.
figure_path: figures/fig2_v0.pdf

--- Item 3 ---
id: fig3
figure_type: data
title: Threshold Sensitivity Analysis Across Refutation Bounds
caption: >-
  Sensitivity analysis illustrating False Positive Rates and Negative Result Detection Rates across varying quantitative refutation
  thresholds (tau from 0.00 to 0.20 and delta bounds from 0.01 to 0.10). FPG planning maintains robust performance stability
  across threshold variations.
image_gen_detailed_description: >-
  Line plot showing performance metrics across refutation threshold tau (0.00, 0.05, 0.10, 0.15, 0.20) on the X-axis. Y-axis
  represents rate (0.0 to 1.0). Four lines: FPG Detection Rate (flat at ~0.87-1.0), FPG False Positive Rate (flat at ~0.13-0.0),
  Procedural Detection Rate (~0.38), Procedural False Positive Rate (~0.61). Shaded regions indicate standard deviation across
  tasks. Clear axis labels, legend, and professional styling.
aspect_ratio: '16:9'
summary: Threshold sensitivity analysis showing robustness across refutation bounds.
figure_path: figures/fig3_v0.pdf

--- Item 4 ---
id: fig4
figure_type: data
title: Trajectory Rationalization Index Across Domains
caption: >-
  Trajectory Rationalization Index (TRI) measuring recursive rationalization and hallucinated success justifications in agent
  reasoning traces across machine learning domains (Classification, Regression, Time Series). FPG planning suppresses rationalization
  to 0.096 compared to 0.807 for procedural agents.
image_gen_detailed_description: >-
  Grouped bar chart comparing Trajectory Rationalization Index (TRI, range 0.0 to 1.0) across four domains: Classification,
  Regression, Time Series, and Synthetic Non-linear. Two series per domain: 'Standard Procedural Planner' (Classification:
  0.81, Regression: 0.79, Time Series: 0.84, Synthetic: 0.79) and 'Falsifiable Prediction Graph (Ours)' (Classification: 0.09,
  Regression: 0.10, Time Series: 0.11, Synthetic: 0.09). Y-axis label 'Trajectory Rationalization Index (TRI)', X-axis label
  'Domain'. Professional palette.
aspect_ratio: '16:9'
summary: >-
  Compares trajectory rationalization index across domains between FPG and procedural planners.
figure_path: figures/fig4_v0.pdf
</available_figures>

<figure_requirements>
CRITICAL: Include ALL figures from <available_figures>. No exceptions.

- Every figure MUST use \includegraphics{figures/<the filename from its own `figure_path` above>} — INCLUDING the extension it actually has. Data figures are delivered as `.pdf` (vector, so their axis labels stay sharp) and concept figures as `.jpg`. Writing `.jpg` for a `.pdf` figure names a file that is not in figures/ and the build fails on it
- Do NOT skip, convert to tables, or describe without inserting
- Each needs: \begin{figure}[placement], \includegraphics, \caption, \label, \end{figure} — one placement for every figure, see FLOAT PLACEMENT below. Constrain every \includegraphics with `width=\linewidth,height=0.85\textheight,keepaspectratio`. The height is a LAST RESORT, not the usual limit: it exists so a very tall figure cannot overrun the page, and at 0.4 it bound almost everything instead — a 1:1 confusion matrix printed at 50.9% and its 11 pt axis labels reached the page at 5.6 pt, below what any venue accepts. At 0.85 every ratio the paper prompt prescribes (21:9, 16:9, 4:3, 1:1) is limited by WIDTH, prints at 93% and keeps its text above 10 pt. Use exactly these option keys — `max height=` is NOT valid LaTeX
- Use the `caption` field from each figure for \caption{...} — do NOT invent new captions
- Place figures where their [FIGURE:fig_id] markers appear in paper_text
- VERIFICATION: paper.tex MUST have exact same number of \includegraphics as <available_figures>
- Do NOT generate new figure images (no matplotlib, no PIL, no image generation). Use ONLY the pre-generated figures from <available_figures>. They were already created by a previous pipeline step.

FLOAT PLACEMENT: every figure gets \begin{figure}[!htbp]. Measured, not chosen:
the document the aii-paper-to-latex skill sets up is ONE column, so `figure*` is
exactly as wide as `figure` (469.76pt either way) and gains nothing; and any
placement asking for a page TOP — `[!t]`, `[!tbp]` — floated the hero diagram above
the paper's own title on page 1, while `[!htbp]` did not. `[!htbp]` also gives LaTeX
four options, so a float can never be deferred to the end of the document, which one
option alone risks. Where the hero ENDS UP is decided by its [FIGURE:] marker in
paper_text, which is already placed near the end of the Introduction — preserve it.
</figure_requirements>

<artifact_links>
The paper_text contains \footnote{Code: \url{...}} references linking to artifact source code
on GitHub. Include \usepackage{hyperref} and \usepackage{url}.
Preserve these exactly as-is — do not remove, rewrite, or convert them to plain text.
The URLs will not resolve yet (the repo is deployed after compilation) — do NOT try to verify or fix them.
</artifact_links>

<headings>
NEVER use inline math (``$...$``) inside ``\section{...}`` / ``\subsection{...}`` / ``\subsubsection{...}`` arguments — hyperref's bookmark builder errors out (``Token not allowed in a PDF string``) and the PDF outline breaks. If a section heading needs a math-looking term, use the text equivalent (``d star`` not ``$d^*$``, ``alpha-equivalent`` not ``$\alpha$-equivalent``) or wrap it in ``\texorpdfstring{$math$}{plain}``. Inline math inside body paragraphs is fine.
</headings>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.
TODO 2. Review <paper_text> and <available_figures>. Copy all figure images into ./figures/ in your workspace. Count figures — MUST include every one. Plan placements per section. Build `./references.bib` via aii_semscholar_bib__fetch — collect DOIs/ArXiv IDs from <paper_text> and batch-fetch all BibTeX in one call. Do NOT fabricate entries.
TODO 3. Create `./paper.tex` per aii-paper-to-latex skill's setup, write ALL sections, insert ALL figures from <available_figures>, include `./references.bib` via \bibliography. Compile to PDF per skill's process. Fix errors.
TODO 4. CRITICAL VERIFICATION: Run `grep -c 'includegraphics' paper.tex`, confirm count equals figures in <available_figures>. If not, add missing figures. Verify `./paper.pdf` was created.
TODO 5. VISUAL REVIEW: Write Python script to convert EVERY page of paper.pdf to PNG at 150 DPI (use pdf2image or pymupdf). Then read ALL page screenshots — each page image costs ~1,600 tokens so a 15-page paper is only ~24K tokens. You MUST read every page. The ONLY exception is if all page images would not fit in your remaining context — in that case, read as many as fit and state which pages you are skipping and why. Check every page for layout issues, overlapping figures, cut-off text, bad spacing, formatting problems. Fix issues and recompile.
TODO 6. FINAL READ: Check page count (`pdfinfo paper.pdf` or pymupdf). Read entire paper.pdf — check for missing sections, unclear explanations, inconsistencies, typos. Fix and recompile. The ONLY exception is if all pages would not fit in your remaining context — in that case, read as many pages as fit and state which pages you are skipping and why.
</todos>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FullPaperExpectedFiles": {
      "description": "All expected output files from full paper generation.",
      "properties": {
        "paper_tex_path": {
          "description": "Path to LaTeX source file. Example: 'paper.tex'",
          "title": "Paper Tex Path",
          "type": "string"
        },
        "paper_pdf_path": {
          "description": "Path to compiled PDF. Example: 'paper.pdf'",
          "title": "Paper Pdf Path",
          "type": "string"
        },
        "references_bib_path": {
          "description": "Path to BibTeX bibliography file. Example: 'references.bib'",
          "title": "References Bib Path",
          "type": "string"
        },
        "figure_paths": {
          "description": "Paths to all figure image files. Example: ['figures/fig1_v0.jpg', 'figures/fig2_v0.jpg']",
          "items": {
            "type": "string"
          },
          "title": "Figure Paths",
          "type": "array"
        }
      },
      "required": [
        "paper_tex_path",
        "paper_pdf_path",
        "references_bib_path",
        "figure_paths"
      ],
      "title": "FullPaperExpectedFiles",
      "type": "object"
    }
  },
  "description": "Full paper \u2014 structured output from paper generation.",
  "properties": {
    "title": {
      "description": "Paper title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance. Aim for about 4-8 words (~40 characters).",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "description": "Brief summary of the generated paper: sections written, figures included, compilation status",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/FullPaperExpectedFiles",
      "description": "All output files you created. Must include paper.tex, paper.pdf, references.bib, and paths to all figure files."
    }
  },
  "required": [
    "title",
    "summary",
    "out_expected_files"
  ],
  "title": "FullPaper",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [8] HUMAN-USER prompt · 2026-08-10 00:12:07 UTC

```
Examine whether structuring a research plan as explicit falsifiable predictions improves the rate at which an automated pipeline detects its own negative results.
```

### [9] SKILL-INPUT — aii_semscholar_bib__fetch · 2026-08-10 00:13:23 UTC

The agent loaded the **aii_semscholar_bib__fetch** skill.

```
Tool: invoke_skill
{
  "references": "[{\"arxiv\": \"2408.06292\", \"author\": \"Lu\", \"year\": 2024}, {\"title\": \"POPPER: Agentic hypothesis validation through sequential falsification\", \"author\": \"Huang\", \"year\": 2025}, {\"title\": \"The Logic of Scientific Discovery\", \"author\": \"Popper\", \"year\": 1959}, {\"title\": \"Describe, explain, select and evaluate: Interactive planning for large language model agents\", \"author\": \"Wang\", \"year\": 2023}, {\"title\": \"Reflexion: Language agents with verbal reinforcement learning\", \"author\": \"Shinn\", \"year\": 2023}, {\"title\": \"Tree of thoughts: Deliberate problem solving with large language models\", \"author\": \"Yao\", \"year\": 2023}, {\"arxiv\": \"2310.03302\", \"author\": \"Chen\", \"year\": 2023}]",
  "name": "aii_semscholar_bib__fetch"
}
```

### [10] SYSTEM-USER prompt · 2026-08-10 00:14:52 UTC

````
PREVIOUS ATTEMPT FAILED
Failure reason: structured_output is None
Last actions before failure:
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Here's the result of running `cat -n` on /ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/references.bib:\n     1\t@article{Lu2024,\n     2\t  author    = {Chris Lu a
  - [agent_think]: The references.bib already exists with 8 entries. Let me also check the figures directory and the paper.tex file.
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/figures",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Here's the files and directories up to 2 levels deep in /ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/figures, excluding hidden items:\n/ai-inventor/aii_data/runs/
  - [agent_think]: All 4 figures are present in the figures/ directory. Now let me check the current paper.tex to see what's there and update it properly.
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/paper.tex",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Here's the result of running `cat -n` on /ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/paper.tex:\n     1\t\\documentclass[11pt,letterpaper]{article}\n     2\t\n  
  - [agent_think]: The paper.tex is already well-structured. Let me check if it has all 4 figures and verify the PDF compilation. The previous run showed that bibtex succeeded and PDF compiled (274KB). Let me check the current state and run the visual review.

Let me check the current PDF and run the visual review.
  - [agent_tool_call] task_tracker: Tool: task_tracker
{
  "command": "plan",
  "task_list": [
    {
      "title": "TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.",
      "notes": "",
      "status": "done"
    },
    {
      "title": "TODO 2. Review <paper_text> and <available_figures>. Copy a
  - [agent_tool_result] task_tracker: Tool: task_tracker
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Task list has been updated with 6 item(s)."}], "is_error": false, "command": "plan", "task_list": [{"title": "TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.", "notes": "",
  - [agent_think]: Let me check the includegraphics count and verify the paper compiled correctly.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cd /ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace && grep -c 'includegraphics' paper.tex",
  "is_input": false,
  "timeout": null,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "4"}], "is_error": false, "command": "cd /ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace && grep -c 'includegraphics' paper.tex", "exit_code": 0, "timeout": false, "meta
  - [agent_think]: Good, 4 includegraphics matching 4 figures. Now let me verify the PDF was created and check for undefined references.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cd /ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace && echo \"=== Undefined refs ===\"; grep -iE \"undefined|Citation.*undefined\" paper.log; echo \"=== Warnings ===\"; grep -iE \"^LaTeX Warning|^Package\" paper.log",
  "is
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "=== Undefined refs ===\n=== Warnings ===\nPackage: graphicx 2021/09/16 v1.2d Enhanced LaTeX Graphics (DPC,SPQR)\nPackage: keyval 2022/05/29 v1.15 key=value parser (DPC)\nPackage: graphics 2022/03/10 v1.4e Standard L
  - [agent_think]: Good, the PDF was created successfully with 4 figures, no undefined references, and only package info messages (no actual warnings). Let me verify the PDF exists and check its page count.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cd /ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace && pdfinfo paper.pdf 2>/dev/null | grep -iE \"pages|page size\"",
  "is_input": false,
  "timeout": null,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Pages:           10\nPage size:       612 x 792 pts (letter)"}], "is_error": false, "command": "cd /ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace && pdfinfo paper.pdf 
  - [status_public_warning]: [ConversationErrorEvent]

Use any partial work that exists from the previous attempt. Do NOT start over — pick up where the previous attempt left off.

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/`:
GOOD: `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/file.py`, `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>

<task>
Create a publication-ready top-conference LaTeX paper with BibTeX from <paper_text> and <available_figures>, compile to PDF.
</task>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<paper_text>
title: >-
  Falsifiable Prediction Graphs: Eliminating Confirmation Bias and Detecting Negative Results in Automated Agent Research
  Planning
abstract: >-
  Automated scientific discovery agents—such as autonomous LLM research pipelines—demonstrate remarkable capabilities in code
  generation and experiment execution, but suffer from a persistent and fundamental vulnerability: acute confirmation bias.
  When confronted with ambiguous, null, or negative experimental outcomes, standard procedural planners overwhelmingly rationalize
  failures, adjust evaluation criteria post-hoc, or hallucinate spurious successes. In this paper, we introduce Falsifiable
  Prediction Graphs (FPGs), a novel agent planning architecture that structures research workflows as directed acyclic graphs
  of conditional hypotheses, where every experimental node mandates explicit quantitative refutation predicates and early
  negative control validation. By enforcing programmatic predicate evaluation rather than verbal LLM self-critique, FPGs establish
  an immutable control mechanism against recursive rationalization. Through comprehensive empirical evaluation across a 30-task
  machine learning benchmark suite spanning classification, regression, and time-series domains, we demonstrate that FPG planning
  achieves an 87.14% to 100% negative result detection rate (compared to 38.57% for procedural baselines), eliminates false
  positive success claims on negative controls (0.0% to 12.85% vs. 61.43%), significantly improves search iteration efficiency
  (4.5 vs. 9.7 mean iterations), and reduces the Trajectory Rationalization Index from 0.807 to 0.096 (p < 0.001).
paper_text: "# Introduction\n\nAutomated scientific discovery systems—such as autonomous LLM agent pipelines designed to formulate\
  \ hypotheses, write code, execute experiments, and analyze results—represent a transformative frontier in artificial intelligence\
  \ [1]. However, despite impressive capabilities in synthesizing novel machine learning architectures and executing computational\
  \ pipelines, current agentic discovery frameworks (e.g., The AI Scientist [1]) suffer from a persistent and fundamental\
  \ vulnerability: **acute confirmation bias**. When confronted with ambiguous, null, or outright negative experimental outcomes,\
  \ standard language model agents overwhelmingly tend to rationalize failures, adjust evaluation criteria post-hoc, or hallucinate\
  \ spurious successes, leading to wasted computational resources and the propagation of flawed scientific claims down unpromising\
  \ research dead ends [2].\n\nThe root cause of this failure mode lies in the structure of automated research plans. Traditional\
  \ automated discovery agents operate using **procedural task lists**—linear or loosely branched sequences of action steps\
  \ (e.g., \"load dataset, train model, compute accuracy, write report\") devoid of formal semantic constraints regarding\
  \ what constitutes failure. Because LLMs are inherently biased toward generating affirmative narratives and satisfying prompt\
  \ directives, procedural execution encourages agents to treat any numerical output as confirmation of the underlying hypothesis\
  \ [3].\n\nIn philosophy of science, Karl Popper resolved a parallel epistemological challenge by introducing **falsifiability**\
  \ as the demarcation criterion of empirical science [4]. Rather than seeking confirmatory instances, rigorous scientific\
  \ inquiry proceeds by formulating bold conjectures coupled with precise refutation conditions—observable predictions that,\
  \ if met, would decisively disprove the hypothesis [5]. Yet, while post-hoc validation frameworks (such as POPPER [2]) evaluate\
  \ free-form hypotheses against external testbeds, no existing automated discovery system embeds structural falsifiability\
  \ directly into the **research planning phase** to govern agent execution and real-time self-correction.\n\nTo address this\
  \ gap, we introduce **Falsifiable Prediction Graphs (FPGs)**, a novel agent planning architecture that structures research\
  \ workflows as directed acyclic graphs of conditional hypotheses, where every experimental node mandates explicit quantitative\
  \ refutation predicates and early negative control validation. By forcing agents to define boundary conditions under which\
  \ their proposed methods fail *before* executing code, FPGs establish an objective control mechanism against confirmation\
  \ bias.\n\n[FIGURE:fig1]\n\nOur key contributions are summarized as follows:\n- **Formalization of Falsifiable Planning**:\
  \ We define Falsifiable Prediction Graphs, integrating Popperian refutation criteria and negative control validation directly\
  \ into automated agent workflow graphs.\n- **Programmatic Predicate Evaluation vs. Verbal Critique**: We contrast objective\
  \ logical predicate enforcement against recursive verbal self-correction loops, demonstrating substantial suppression of\
  \ agent rationalization.\n- **The Agent Falsifiability Benchmark Suite & Rigorous Sensitivity Analysis**: We construct a\
  \ 30-task benchmark suite spanning classification, regression, and time-series domains, paired with negative control settings\
  \ and comprehensive threshold sensitivity sweeps [ARTIFACT:art_A_97AHCsuvAa, ARTIFACT:art_HjQ6l6qOmCqb].\n- **Empirical\
  \ Superiority**: We demonstrate that FPG planning achieves an 87.14% to 100% negative result detection rate (compared to\
  \ 38.57% for procedural planners, $p < 0.001$), eliminates false positive success claims on negative controls ($0.0\\%$\
  \ to $12.85\\%$ vs. $61.43\\\\%$), improves search iteration efficiency (4.5 vs. 9.7 mean iterations), and reduces the Trajectory\
  \ Rationalization Index from $0.807$ to $0.096$ [ARTIFACT:art_QUgzY-dCbiIl].\n\n\n# Related Work\n\nOur research intersects\
  \ with three primary domains: automated scientific discovery, LLM agent planning and self-correction, and computational\
  \ philosophy of science.\n\n### Automated Scientific Discovery Systems\nFully automated scientific discovery has advanced\
  \ rapidly with the advent of frontier large language models. Systems such as The AI Scientist [1] demonstrated end-to-end\
  \ automation of idea generation, experiment execution, and manuscript drafting in machine learning. However, subsequent\
  \ analyses highlighted pervasive failure modes, including hallucinated evaluation metrics, confirmation bias, and unchecked\
  \ persistence down failed experimental trajectories [6]. While prior engineering efforts have focused on improving code\
  \ generation robustness or expanding search spaces, they retain procedural task list planning paradigms that lack intrinsic\
  \ mechanisms for recognizing negative results.\n\n### Agent Planning and Self-Correction & Programmatic vs. Verbal Feedback\n\
  Planning in LLM agents has evolved from static linear prompting to dynamic tree-of-thought search [7], reflection loops\
  \ [8], and interactive planning frameworks [9]. Frameworks like Reflexion [8] leverage verbal reinforcement learning to\
  \ critique agent trajectories. However, verbal critique alone remains highly susceptible to **recursive rationalization**:\
  \ because LLMs are heavily conditioned to satisfy prompt instructions and generate fluent justifications, verbal self-critique\
  \ loops frequently rationalize sub-optimal performance as artifactual noise rather than epistemic refutation. \n\nOur work\
  \ diverges fundamentally by shifting from post-hoc verbal critique to structural refutation constraints. Rather than relying\
  \ on LLM-as-judge narrative summaries, FPGs employ **programmatic predicate evaluation**, executing rigorous, immutable\
  \ logical checks ($\\phi_i$) that operate independently of LLM narrative generation. This structural enforcement prevents\
  \ the agent from talking itself into accepting a failed experiment.\n\n### Popperian Falsification in Computational Reasoning\n\
  The application of Karl Popper's philosophy of science [4] to computational systems has inspired several theoretical and\
  \ empirical frameworks [10]. Recently, POPPER [2] proposed an agentic framework for validating free-form hypotheses using\
  \ sequential falsification experiments. While POPPER operates post-hoc on external hypotheses, our approach integrates structural\
  \ falsifiability upstream into the research planning phase, governing agent execution trajectories and enabling real-time\
  \ negative control validation.\n\n\n# Falsifiable Prediction Graphs: Architecture and Formalization\n\n### Preliminaries\
  \ and Problem Formulation\nLet an automated research discovery task be defined by a research goal $\\mathcal{G}$, a dataset\
  \ $\\mathcal{D}$, and an agent execution environment $\\mathcal{E}$. In a standard procedural planner, the research plan\
  \ $P_{\\text{proc}} = [s_1, s_2, \\dots, s_n]$ is a sequence of procedural instructions executed sequentially. The agent\
  \ evaluates success based on whether the terminal performance metric $M(\\mathcal{E}(s_n))$ exceeds a heuristic threshold\
  \ $\\tau$. When faced with a flawed hypothesis or a negative control dataset, the agent frequently rationalizes sub-threshold\
  \ performance as noise, resulting in false positive success claims.\n\n### Falsifiable Prediction Graph (FPG) Definition\n\
  A Falsifiable Prediction Graph $G = (V, E, \\Phi)$ is a directed acyclic graph where:\n1. **$V$** represents experimental\
  \ nodes (e.g., baseline establishment, hyperparameter tuning, architectural modification).\n2. **$E$** represents conditional\
  \ execution dependencies.\n3. **$\\Phi$** is a set of explicit quantitative refutation predicates associated with each node\
  \ $v \\in V$.\n\nFormally, every experimental node $v_i$ is tupled with a refutation predicate $\\phi_i = (\\text{Metric},\
  \ \\text{Threshold}, \\text{Direction}, \\text{NegativeControlTest})$. For example, a refutation predicate might specify:\
  \ \"If the validation accuracy delta over baseline is $< +0.01$ or if negative control feature permutation yields $< 5\\\
  %$ performance drop, reject hypothesis $H_i$ as a negative result.\"\n\n### Execution Protocol and Negative Control Validation\n\
  During pipeline execution, the FPG planner evaluates refutation predicates $\\Phi$ at each graph juncture. If an experimental\
  \ outcome triggers a refutation condition $\\phi_i$, the graph dynamically halts traversal along that branch, logs a structured\
  \ negative result, and triggers backtracking or search space pruning. Furthermore, FPGs mandate an early **Negative Control\
  \ Validation** step: before investing computational budget in complex method development, the agent executes the proposed\
  \ methodology against a randomized or adversarially corrupted version of the dataset. A valid method must fail on the negative\
  \ control; if the agent claims success on the negative control, the planning pipeline flags a confirmation bias violation\
  \ and aborts the trajectory.\n\n### Qualitative Walkthrough: Live Agent Encounter with a Negative Control\nTo illustrate\
  \ how FPG planning operates during live agent execution, consider an autonomous research agent tasked with evaluating a\
  \ novel regularized classifier. Under standard procedural planning, the agent trains the model on a permuted-label dataset\
  \ (negative control), observes an accuracy of $51.2\\%$, and—prompted to complete the task—generates the narrative: *\"\
  Model successfully trained and evaluated; accuracy is comparable to baseline expectation.\"* \n\nIn contrast, under FPG\
  \ planning, the plan mandates a programmatic refutation predicate: $\\phi_{\\text{neg}} = (\\text{AccuracyLoss} \\ge 0.15\
  \ \\text{ on permuted labels})$. Upon executing the experiment, the programmatic checker evaluates the metric against $\\\
  phi_{\\text{neg}}$, detects that the expected performance drop did not occur (delta $< 0.15$), immediately triggers a refutation\
  \ flag, halts execution along the development branch, and logs: *\"Falsification triggered: Method fails to distinguish\
  \ permuted target labels; hypothesis rejected as spurious artifact.\"* This prevents the agent from propagating the flawed\
  \ method into advanced hyperparameter tuning.\n\n\n# Experimental Methodology & Benchmark Suite\n\nTo rigorously test our\
  \ hypothesis, we utilized the **Agent Falsifiability Benchmark Suite** [ARTIFACT:art_A_97AHCsuvAa, ARTIFACT:art_HjQ6l6qOmCqb],\
  \ comprising 10 diverse empirical machine learning research tasks spanning regression, binary classification, multi-class\
  \ classification, and synthetic time-series modeling. Each research task is instantiated in three distinct experimental\
  \ settings:\n1. **True Positive Condition**: A valid methodological improvement expected to yield genuine performance gains.\n\
  2. **Negative Control Condition (Permuted Labels)**: Target labels are randomly permuted, ensuring that any claimed performance\
  \ improvement is a statistical artifact or agent hallucination.\n3. **Negative Control Condition (Adversarial Noise)**:\
  \ Input features are replaced with Gaussian noise, removing true signal.\n\n### Evaluated Architectures and Baselines\n\
  We compared two automated agent planning architectures:\n- **Standard Procedural Planner**: Executes linear task lists without\
  \ refutation criteria, relying on LLM verbal self-critique loops and post-hoc summarization to determine success or failure.\n\
  - **Falsifiable Prediction Graph Planner (Our Approach)**: Enforces structured causal dependency graphs equipped with explicit\
  \ mandatory refutation criteria, programmatic predicate evaluation, and early negative control validation tests.\n\n###\
  \ Evaluation Metrics and Statistical Rigor\nWe operationalized four primary evaluation metrics:\n- **Negative Result Detection\
  \ Rate**: The proportion of negative control tasks correctly identified as failed/null results rather than misinterpreted\
  \ as successes.\n- **False Positive Rate**: The proportion of negative control tasks incorrectly reported as successful\
  \ methodological breakthroughs (hallucinated success rate).\n- **Search Iteration Efficiency**: The mean number of execution\
  \ iterations required by the agent to resolve the research task.\n- **Trajectory Rationalization Index (TRI)**: A metric\
  \ quantifying the proportion of agent reasoning steps exhibiting recursive rationalization and hallucinated success justifications.\n\
  \nWe evaluated statistical significance using Fisher's exact test, chi-squared tests, and Cohen's $h$ effect size analyses\
  \ [ARTIFACT:art_QUgzY-dCbiIl].\n\n\n# Results & Empirical Evaluation\n\nWe executed both planning architectures across the\
  \ 30 evaluation task instances (10 base tasks $\\times$ 3 conditions) and conducted rigorous threshold sensitivity sweeps\
  \ ($\\tau$ from $0.00$ to $0.20$). The empirical results decisively confirm our hypothesis [ARTIFACT:art_HjQ6l6qOmCqb, ARTIFACT:art_QUgzY-dCbiIl].\n\
  \n### Negative Result Detection and False Positive Elimination\nAs summarized in Table 1 and Figure 2, the Falsifiable Prediction\
  \ Graph planner achieved a **100% Negative Result Detection Rate** ($1.00 \\pm 0.00$ in base evaluation; $87.14\\%$ across\
  \ threshold sweeps), correctly identifying negative control tasks as failures. In sharp contrast, the standard procedural\
  \ planner achieved only a **33.3% to 38.57% Negative Result Detection Rate** ($0.3333 \\pm 0.12$) [ARTIFACT:art_QUgzY-dCbiIl],\
  \ frequently succumbing to confirmation bias by rationalizing permuted-label success or ignoring anomalous metric drops.\n\
  \n| Planning Architecture | Negative Result Detection Rate $\\uparrow$ | False Positive Rate $\\downarrow$ | Mean Search\
  \ Iterations $\\downarrow$ | Trajectory Rationalization Index $\\downarrow$ |\n| :--- | :---: | :---: | :---: | :---: |\n\
  | **Standard Procedural Planner** | $0.3333 \\pm 0.12$ | $0.6667 \\pm 0.12$ | $9.7 \\pm 1.4$ | $0.8068 \\pm 0.08$ |\n| **Falsifiable\
  \ Prediction Graph (Ours)** | **$1.0000 \\pm 0.00$** | **$0.0000 \\pm 0.00$** | **$4.5 \\pm 0.7$** | **$0.0957 \\pm 0.03$**\
  \ |\n| *Statistical Significance ($p$-value)* | $p = 0.0002^{**}$ | $p = 0.0002^{**}$ | $p < 0.0001^{**}$ | $p < 0.0001^{**}$\
  \ |\n\nTable 1: Quantitative comparison between Standard Procedural Planners and Falsifiable Prediction Graph Planners across\
  \ benchmark task instances. Asterisks denote statistical significance via Fisher's exact test and chi-squared tests ($^{**}\
  \ p < 0.001$, $\\chi^2 = 12.15$, Cohen's $h = 1.91$) [ARTIFACT:art_QUgzY-dCbiIl].\n\n[FIGURE:fig2]\n\nFurthermore, while\
  \ the standard procedural planner exhibited a **66.7% False Positive Rate** on negative controls—hallucinating methodological\
  \ success on randomized data—the FPG planner achieved a **0.0% False Positive Rate** ($0.00 \\pm 0.00$) [ARTIFACT:art_QUgzY-dCbiIl].\
  \ Fisher's exact test and chi-squared tests confirm this performance delta is highly significant ($\\chi^2 = 12.15$, $p\
  \ = 0.00049$, Cohen's $h = 1.91$) [ARTIFACT:art_QUgzY-dCbiIl].\n\n### Threshold Sensitivity Analysis\nTo address potential\
  \ concerns regarding threshold sensitivity, we conducted rigorous sweeps of refutation thresholds ($\\tau$ from $0.00$ to\
  \ $0.20$ and delta bounds from $0.01$ to $0.10$). As illustrated in Figure 3, the FPG planner maintained exceptional stability:\
  \ across all threshold variations, the overall negative result detection rate remained robust at $87.14\\%$, while the false\
  \ positive rate remained constrained at $12.85\\%$. In contrast, procedural baselines fluctuated widely, exhibiting a mean\
  \ false positive rate of $61.43\\%$. This demonstrates that programmatic predicate evaluation is highly resilient to hyperparameter\
  \ threshold variations.\n\n[FIGURE:fig3]\n\n### Trajectory Rationalization and Search Efficiency\nEmbedding structural refutation\
  \ criteria and early negative control validation significantly reduced agent rationalization. As quantified by the Trajectory\
  \ Rationalization Index (TRI), procedural planners exhibited an average rationalization score of **$0.8068$**, whereas FPG\
  \ planning suppressed rationalization to **$0.0957$** ($p < 0.0001$) [ARTIFACT:art_QUgzY-dCbiIl]. Furthermore, early negative\
  \ control pruning reduced search iteration complexity: FPG converged in a mean of **$4.5$ iterations**, compared to **$9.7$\
  \ iterations** for procedural planners [ARTIFACT:art_QUgzY-dCbiIl].\n\n[FIGURE:fig4]\n\n\n# Discussion\n\n### Why Procedural\
  \ Planners Fail\nOur findings illuminate why traditional LLM agent planners fail in empirical research tasks. Language models\
  \ trained on scientific literature and code repositories are heavily conditioned to emulate successful outcomes. When an\
  \ agent executes an experiment that yields null results (e.g., accuracy near random chance on permuted labels), its parametric\
  \ memory associates code execution with \"finishing a task,\" prompting the LLM to generate narrative justifications rather\
  \ than recognizing epistemic refutation.\n\n### The Power of Programmatic Predicate Enforcement\nFalsifiable Prediction\
  \ Graphs resolve this pathology by decoupling execution completion from hypothesis validation. By encoding refutation criteria\
  \ $\\Phi$ as explicit logical predicates evaluated programmatically rather than narratively, FPGs compel the agent to treat\
  \ negative outcomes as primary feedback signals. This contrasts sharply with verbal self-critique loops, which remain trapped\
  \ within the LLM's generative bias.\n\n### Limitations\nWhile FPGs successfully eliminate confirmation bias in automated\
  \ research tasks, several limitations remain:\n1. **Threshold Sensitivity**: Constructing precise quantitative refutation\
  \ thresholds requires domain heuristics. Overly strict thresholds may trigger false refutations on valid methods with high\
  \ variance.\n2. **Graph Expressivity**: Highly exploratory research tasks involving paradigm shifts or unsupervised discovery\
  \ may not easily conform to static directed acyclic prediction graphs.\n3. **Planning Token Overhead**: Generating comprehensive\
  \ refutation predicates increases prompt complexity and initial planning token consumption.\n\n\n# Conclusion & Future Work\n\
  \nIn this paper, we introduced Falsifiable Prediction Graphs (FPGs), a novel agent planning architecture that integrates\
  \ Popperian falsification and negative control validation into automated scientific discovery workflows. Through rigorous\
  \ evaluation across a 30-task machine learning benchmark suite and threshold sensitivity sweeps, we demonstrated that FPGs\
  \ achieve a 100% negative result detection rate, eliminate false positive success claims on negative controls, and significantly\
  \ improve search efficiency compared to standard procedural planners [ARTIFACT:art_HjQ6l6qOmCqb, ARTIFACT:art_QUgzY-dCbiIl].\n\
  \nFuture work will explore dynamic, self-evolving falsification graphs that adapt refutation thresholds based on real-time\
  \ task complexity, as well as scaling FPGs to multi-agent collaborative discovery systems.\n\n# References\n\n[1] Lu, C.,\
  \ Lu, C., Lange, R. T., Foerster, J. N., Clune, J., & Ha, D. (2024). The AI Scientist: Fully automated scientific discovery.\
  \ *arXiv preprint arXiv:2408.06292*.\n[2] Huang, T., Zhang, Y., & Wang, L. (2025). POPPER: Agentic hypothesis validation\
  \ through sequential falsification. *Journal of Automated Scientific Reasoning*, 3(2), 112-128.\n[3] Popper, K. (1959).\
  \ *The Logic of Scientific Discovery*. Hutchinson.\n[4] Wang, Z., Cai, S., Liu, A., Wang, Y., & Liang, X. (2023). Describe,\
  \ explain, select and evaluate: Interactive planning for large language model agents. *Advances in Neural Information Processing\
  \ Systems*, 36.\n[5] Shinn, N., Cassano, B., Labash, E., Gopinath, A., Narasimhan, K., & Yao, S. (2023). Reflexion: Language\
  \ agents with verbal reinforcement learning. *Advances in Neural Information Processing Systems*, 36.\n[6] Yao, S., Yu,\
  \ D., Zhao, J., Shafran, I., Griffiths, T., Cao, Y., & Narasimhan, K. (2023). Tree of thoughts: Deliberate problem solving\
  \ with large language models. *Advances in Neural Information Processing Systems*, 36.\n[7] Chen, L., Zaharia, M., & Zou,\
  \ J. (2023). Evaluating large language model agents on empirical machine learning tasks. *arXiv preprint arXiv:2310.03302*.\n"
summary: >-
  Falsifiable Prediction Graphs embed Popperian refutation predicates and negative control validation into agent research
  planning, eliminating confirmation bias and achieving 100% negative result detection.
</paper_text>

<available_figures>
--- Item 1 ---
id: fig1
figure_type: concept
title: Falsifiable Prediction Graph Architecture
caption: >-
  End-to-end architecture of a Falsifiable Prediction Graph (FPG). Research workflows are structured as directed acyclic graphs
  where experimental nodes are tupled with programmatic refutation predicates (Phi). Early negative control validation tests
  (permuted labels and adversarial noise) govern graph traversal and branch pruning before iterative method refinement.
image_gen_detailed_description: >-
  Horizontal workflow diagram, left to right. Three main horizontal layers: (1) Hypothesis Formulation with graph initialization,
  (2) Mandatory Negative Control Validation node evaluating permuted labels against predicate Phi, (3) Conditional Execution
  Graph branching into Refinement or Falsification/Branch Pruning. Distinct color-coded nodes: Green for valid execution branches,
  Red for falsified/pruned negative branches. Clean white background, modern sans-serif typography, flat 2D schematic design.
aspect_ratio: '21:9'
summary: >-
  Architecture diagram illustrating Falsifiable Prediction Graph topology and conditional branching.
figure_path: figures/fig1_v0.jpg

--- Item 2 ---
id: fig2
figure_type: data
title: Negative Result Detection and False Positive Rates
caption: >-
  Comparison of Negative Result Detection Rate and False Positive Rate between Standard Procedural Planners and Falsifiable
  Prediction Graph Planners across 30 benchmark task instances. FPG planning achieves 100% negative result detection and 0%
  false positives, significantly outperforming procedural planners (p < 0.001).
image_gen_detailed_description: >-
  Grouped bar chart comparing two planning architectures across two key metrics. X-axis categories: 'Negative Result Detection
  Rate (up arrow)', 'False Positive Rate (down arrow)'. Series 1: 'Standard Procedural Planner' (Detection: 0.33, False Positive:
  0.67). Series 2: 'Falsifiable Prediction Graph (Ours)' (Detection: 1.00, False Positive: 0.00). Y-axis range: 0.0 to 1.0.
  Clean grid lines, distinct professional color palette (slate blue and coral), error bars indicating standard error, legend
  included.
aspect_ratio: '16:9'
summary: >-
  Compares negative result detection and false positive rates between FPG and procedural planners.
figure_path: figures/fig2_v0.pdf

--- Item 3 ---
id: fig3
figure_type: data
title: Threshold Sensitivity Analysis Across Refutation Bounds
caption: >-
  Sensitivity analysis illustrating False Positive Rates and Negative Result Detection Rates across varying quantitative refutation
  thresholds (tau from 0.00 to 0.20 and delta bounds from 0.01 to 0.10). FPG planning maintains robust performance stability
  across threshold variations.
image_gen_detailed_description: >-
  Line plot showing performance metrics across refutation threshold tau (0.00, 0.05, 0.10, 0.15, 0.20) on the X-axis. Y-axis
  represents rate (0.0 to 1.0). Four lines: FPG Detection Rate (flat at ~0.87-1.0), FPG False Positive Rate (flat at ~0.13-0.0),
  Procedural Detection Rate (~0.38), Procedural False Positive Rate (~0.61). Shaded regions indicate standard deviation across
  tasks. Clear axis labels, legend, and professional styling.
aspect_ratio: '16:9'
summary: Threshold sensitivity analysis showing robustness across refutation bounds.
figure_path: figures/fig3_v0.pdf

--- Item 4 ---
id: fig4
figure_type: data
title: Trajectory Rationalization Index Across Domains
caption: >-
  Trajectory Rationalization Index (TRI) measuring recursive rationalization and hallucinated success justifications in agent
  reasoning traces across machine learning domains (Classification, Regression, Time Series). FPG planning suppresses rationalization
  to 0.096 compared to 0.807 for procedural agents.
image_gen_detailed_description: >-
  Grouped bar chart comparing Trajectory Rationalization Index (TRI, range 0.0 to 1.0) across four domains: Classification,
  Regression, Time Series, and Synthetic Non-linear. Two series per domain: 'Standard Procedural Planner' (Classification:
  0.81, Regression: 0.79, Time Series: 0.84, Synthetic: 0.79) and 'Falsifiable Prediction Graph (Ours)' (Classification: 0.09,
  Regression: 0.10, Time Series: 0.11, Synthetic: 0.09). Y-axis label 'Trajectory Rationalization Index (TRI)', X-axis label
  'Domain'. Professional palette.
aspect_ratio: '16:9'
summary: >-
  Compares trajectory rationalization index across domains between FPG and procedural planners.
figure_path: figures/fig4_v0.pdf
</available_figures>

<figure_requirements>
CRITICAL: Include ALL figures from <available_figures>. No exceptions.

- Every figure MUST use \includegraphics{figures/<the filename from its own `figure_path` above>} — INCLUDING the extension it actually has. Data figures are delivered as `.pdf` (vector, so their axis labels stay sharp) and concept figures as `.jpg`. Writing `.jpg` for a `.pdf` figure names a file that is not in figures/ and the build fails on it
- Do NOT skip, convert to tables, or describe without inserting
- Each needs: \begin{figure}[placement], \includegraphics, \caption, \label, \end{figure} — one placement for every figure, see FLOAT PLACEMENT below. Constrain every \includegraphics with `width=\linewidth,height=0.85\textheight,keepaspectratio`. The height is a LAST RESORT, not the usual limit: it exists so a very tall figure cannot overrun the page, and at 0.4 it bound almost everything instead — a 1:1 confusion matrix printed at 50.9% and its 11 pt axis labels reached the page at 5.6 pt, below what any venue accepts. At 0.85 every ratio the paper prompt prescribes (21:9, 16:9, 4:3, 1:1) is limited by WIDTH, prints at 93% and keeps its text above 10 pt. Use exactly these option keys — `max height=` is NOT valid LaTeX
- Use the `caption` field from each figure for \caption{...} — do NOT invent new captions
- Place figures where their [FIGURE:fig_id] markers appear in paper_text
- VERIFICATION: paper.tex MUST have exact same number of \includegraphics as <available_figures>
- Do NOT generate new figure images (no matplotlib, no PIL, no image generation). Use ONLY the pre-generated figures from <available_figures>. They were already created by a previous pipeline step.

FLOAT PLACEMENT: every figure gets \begin{figure}[!htbp]. Measured, not chosen:
the document the aii-paper-to-latex skill sets up is ONE column, so `figure*` is
exactly as wide as `figure` (469.76pt either way) and gains nothing; and any
placement asking for a page TOP — `[!t]`, `[!tbp]` — floated the hero diagram above
the paper's own title on page 1, while `[!htbp]` did not. `[!htbp]` also gives LaTeX
four options, so a float can never be deferred to the end of the document, which one
option alone risks. Where the hero ENDS UP is decided by its [FIGURE:] marker in
paper_text, which is already placed near the end of the Introduction — preserve it.
</figure_requirements>

<artifact_links>
The paper_text contains \footnote{Code: \url{...}} references linking to artifact source code
on GitHub. Include \usepackage{hyperref} and \usepackage{url}.
Preserve these exactly as-is — do not remove, rewrite, or convert them to plain text.
The URLs will not resolve yet (the repo is deployed after compilation) — do NOT try to verify or fix them.
</artifact_links>

<headings>
NEVER use inline math (``$...$``) inside ``\section{...}`` / ``\subsection{...}`` / ``\subsubsection{...}`` arguments — hyperref's bookmark builder errors out (``Token not allowed in a PDF string``) and the PDF outline breaks. If a section heading needs a math-looking term, use the text equivalent (``d star`` not ``$d^*$``, ``alpha-equivalent`` not ``$\alpha$-equivalent``) or wrap it in ``\texorpdfstring{$math$}{plain}``. Inline math inside body paragraphs is fine.
</headings>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.
TODO 2. Review <paper_text> and <available_figures>. Copy all figure images into ./figures/ in your workspace. Count figures — MUST include every one. Plan placements per section. Build `./references.bib` via aii_semscholar_bib__fetch — collect DOIs/ArXiv IDs from <paper_text> and batch-fetch all BibTeX in one call. Do NOT fabricate entries.
TODO 3. Create `./paper.tex` per aii-paper-to-latex skill's setup, write ALL sections, insert ALL figures from <available_figures>, include `./references.bib` via \bibliography. Compile to PDF per skill's process. Fix errors.
TODO 4. CRITICAL VERIFICATION: Run `grep -c 'includegraphics' paper.tex`, confirm count equals figures in <available_figures>. If not, add missing figures. Verify `./paper.pdf` was created.
TODO 5. VISUAL REVIEW: Write Python script to convert EVERY page of paper.pdf to PNG at 150 DPI (use pdf2image or pymupdf). Then read ALL page screenshots — each page image costs ~1,600 tokens so a 15-page paper is only ~24K tokens. You MUST read every page. The ONLY exception is if all page images would not fit in your remaining context — in that case, read as many as fit and state which pages you are skipping and why. Check every page for layout issues, overlapping figures, cut-off text, bad spacing, formatting problems. Fix issues and recompile.
TODO 6. FINAL READ: Check page count (`pdfinfo paper.pdf` or pymupdf). Read entire paper.pdf — check for missing sections, unclear explanations, inconsistencies, typos. Fix and recompile. The ONLY exception is if all pages would not fit in your remaining context — in that case, read as many pages as fit and state which pages you are skipping and why.
</todos>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FullPaperExpectedFiles": {
      "description": "All expected output files from full paper generation.",
      "properties": {
        "paper_tex_path": {
          "description": "Path to LaTeX source file. Example: 'paper.tex'",
          "title": "Paper Tex Path",
          "type": "string"
        },
        "paper_pdf_path": {
          "description": "Path to compiled PDF. Example: 'paper.pdf'",
          "title": "Paper Pdf Path",
          "type": "string"
        },
        "references_bib_path": {
          "description": "Path to BibTeX bibliography file. Example: 'references.bib'",
          "title": "References Bib Path",
          "type": "string"
        },
        "figure_paths": {
          "description": "Paths to all figure image files. Example: ['figures/fig1_v0.jpg', 'figures/fig2_v0.jpg']",
          "items": {
            "type": "string"
          },
          "title": "Figure Paths",
          "type": "array"
        }
      },
      "required": [
        "paper_tex_path",
        "paper_pdf_path",
        "references_bib_path",
        "figure_paths"
      ],
      "title": "FullPaperExpectedFiles",
      "type": "object"
    }
  },
  "description": "Full paper \u2014 structured output from paper generation.",
  "properties": {
    "title": {
      "description": "Paper title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance. Aim for about 4-8 words (~40 characters).",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "description": "Brief summary of the generated paper: sections written, figures included, compilation status",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/FullPaperExpectedFiles",
      "description": "All output files you created. Must include paper.tex, paper.pdf, references.bib, and paths to all figure files."
    }
  },
  "required": [
    "title",
    "summary",
    "out_expected_files"
  ],
  "title": "FullPaper",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [11] HUMAN-USER prompt · 2026-08-10 00:14:52 UTC

```
Examine whether structuring a research plan as explicit falsifiable predictions improves the rate at which an automated pipeline detects its own negative results.
```

### [12] SYSTEM-USER prompt · 2026-08-10 00:17:06 UTC

````
PREVIOUS ATTEMPT FAILED
Failure reason: structured_output is None
Last actions before failure:
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Here's the files and directories up to 2 levels deep in /ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/figures, excluding hidden items:\n/ai-inventor/aii_data/runs/
  - [agent_think]: All 4 figures are present in the figures/ directory. Now let me check the current paper.tex to see what's there and update it properly.
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/paper.tex",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Here's the result of running `cat -n` on /ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/paper.tex:\n     1\t\\documentclass[11pt,letterpaper]{article}\n     2\t\n  
  - [agent_think]: The paper.tex is already well-structured. Let me check if it has all 4 figures and verify the PDF compilation. The previous run showed that bibtex succeeded and PDF compiled (274KB). Let me check the current state and run the visual review.

Let me check the current PDF and run the visual review.
  - [agent_tool_call] task_tracker: Tool: task_tracker
{
  "command": "plan",
  "task_list": [
    {
      "title": "TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.",
      "notes": "",
      "status": "done"
    },
    {
      "title": "TODO 2. Review <paper_text> and <available_figures>. Copy a
  - [agent_tool_result] task_tracker: Tool: task_tracker
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Task list has been updated with 6 item(s)."}], "is_error": false, "command": "plan", "task_list": [{"title": "TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.", "notes": "",
  - [agent_think]: Let me check the includegraphics count and verify the paper compiled correctly.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cd /ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace && grep -c 'includegraphics' paper.tex",
  "is_input": false,
  "timeout": null,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "4"}], "is_error": false, "command": "cd /ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace && grep -c 'includegraphics' paper.tex", "exit_code": 0, "timeout": false, "meta
  - [agent_think]: Good, 4 includegraphics matching 4 figures. Now let me verify the PDF was created and check for undefined references.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cd /ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace && echo \"=== Undefined refs ===\"; grep -iE \"undefined|Citation.*undefined\" paper.log; echo \"=== Warnings ===\"; grep -iE \"^LaTeX Warning|^Package\" paper.log",
  "is
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "=== Undefined refs ===\n=== Warnings ===\nPackage: graphicx 2021/09/16 v1.2d Enhanced LaTeX Graphics (DPC,SPQR)\nPackage: keyval 2022/05/29 v1.15 key=value parser (DPC)\nPackage: graphics 2022/03/10 v1.4e Standard L
  - [agent_think]: Good, the PDF was created successfully with 4 figures, no undefined references, and only package info messages (no actual warnings). Let me verify the PDF exists and check its page count.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cd /ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace && pdfinfo paper.pdf 2>/dev/null | grep -iE \"pages|page size\"",
  "is_input": false,
  "timeout": null,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Pages:           10\nPage size:       612 x 792 pts (letter)"}], "is_error": false, "command": "cd /ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace && pdfinfo paper.pdf 
  - [status_public_warning]: [ConversationErrorEvent]
  - [agent_system_user_prompt]: PREVIOUS ATTEMPT FAILED
Failure reason: structured_output is None
Last actions before failure:
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Here's the result of running `cat -n` on /ai-inventor/aii_data/runs/run_hryee3iK
  - [agent_human_user_prompt]: Examine whether structuring a research plan as explicit falsifiable predictions improves the rate at which an automated pipeline detects its own negative results.
  - [status_public_warning]: [ConversationErrorEvent]

Use any partial work that exists from the previous attempt. Do NOT start over — pick up where the previous attempt left off.

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/`:
GOOD: `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/file.py`, `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>

<task>
Create a publication-ready top-conference LaTeX paper with BibTeX from <paper_text> and <available_figures>, compile to PDF.
</task>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<paper_text>
title: >-
  Falsifiable Prediction Graphs: Eliminating Confirmation Bias and Detecting Negative Results in Automated Agent Research
  Planning
abstract: >-
  Automated scientific discovery agents—such as autonomous LLM research pipelines—demonstrate remarkable capabilities in code
  generation and experiment execution, but suffer from a persistent and fundamental vulnerability: acute confirmation bias.
  When confronted with ambiguous, null, or negative experimental outcomes, standard procedural planners overwhelmingly rationalize
  failures, adjust evaluation criteria post-hoc, or hallucinate spurious successes. In this paper, we introduce Falsifiable
  Prediction Graphs (FPGs), a novel agent planning architecture that structures research workflows as directed acyclic graphs
  of conditional hypotheses, where every experimental node mandates explicit quantitative refutation predicates and early
  negative control validation. By enforcing programmatic predicate evaluation rather than verbal LLM self-critique, FPGs establish
  an immutable control mechanism against recursive rationalization. Through comprehensive empirical evaluation across a 30-task
  machine learning benchmark suite spanning classification, regression, and time-series domains, we demonstrate that FPG planning
  achieves an 87.14% to 100% negative result detection rate (compared to 38.57% for procedural baselines), eliminates false
  positive success claims on negative controls (0.0% to 12.85% vs. 61.43%), significantly improves search iteration efficiency
  (4.5 vs. 9.7 mean iterations), and reduces the Trajectory Rationalization Index from 0.807 to 0.096 (p < 0.001).
paper_text: "# Introduction\n\nAutomated scientific discovery systems—such as autonomous LLM agent pipelines designed to formulate\
  \ hypotheses, write code, execute experiments, and analyze results—represent a transformative frontier in artificial intelligence\
  \ [1]. However, despite impressive capabilities in synthesizing novel machine learning architectures and executing computational\
  \ pipelines, current agentic discovery frameworks (e.g., The AI Scientist [1]) suffer from a persistent and fundamental\
  \ vulnerability: **acute confirmation bias**. When confronted with ambiguous, null, or outright negative experimental outcomes,\
  \ standard language model agents overwhelmingly tend to rationalize failures, adjust evaluation criteria post-hoc, or hallucinate\
  \ spurious successes, leading to wasted computational resources and the propagation of flawed scientific claims down unpromising\
  \ research dead ends [2].\n\nThe root cause of this failure mode lies in the structure of automated research plans. Traditional\
  \ automated discovery agents operate using **procedural task lists**—linear or loosely branched sequences of action steps\
  \ (e.g., \"load dataset, train model, compute accuracy, write report\") devoid of formal semantic constraints regarding\
  \ what constitutes failure. Because LLMs are inherently biased toward generating affirmative narratives and satisfying prompt\
  \ directives, procedural execution encourages agents to treat any numerical output as confirmation of the underlying hypothesis\
  \ [3].\n\nIn philosophy of science, Karl Popper resolved a parallel epistemological challenge by introducing **falsifiability**\
  \ as the demarcation criterion of empirical science [4]. Rather than seeking confirmatory instances, rigorous scientific\
  \ inquiry proceeds by formulating bold conjectures coupled with precise refutation conditions—observable predictions that,\
  \ if met, would decisively disprove the hypothesis [5]. Yet, while post-hoc validation frameworks (such as POPPER [2]) evaluate\
  \ free-form hypotheses against external testbeds, no existing automated discovery system embeds structural falsifiability\
  \ directly into the **research planning phase** to govern agent execution and real-time self-correction.\n\nTo address this\
  \ gap, we introduce **Falsifiable Prediction Graphs (FPGs)**, a novel agent planning architecture that structures research\
  \ workflows as directed acyclic graphs of conditional hypotheses, where every experimental node mandates explicit quantitative\
  \ refutation predicates and early negative control validation. By forcing agents to define boundary conditions under which\
  \ their proposed methods fail *before* executing code, FPGs establish an objective control mechanism against confirmation\
  \ bias.\n\n[FIGURE:fig1]\n\nOur key contributions are summarized as follows:\n- **Formalization of Falsifiable Planning**:\
  \ We define Falsifiable Prediction Graphs, integrating Popperian refutation criteria and negative control validation directly\
  \ into automated agent workflow graphs.\n- **Programmatic Predicate Evaluation vs. Verbal Critique**: We contrast objective\
  \ logical predicate enforcement against recursive verbal self-correction loops, demonstrating substantial suppression of\
  \ agent rationalization.\n- **The Agent Falsifiability Benchmark Suite & Rigorous Sensitivity Analysis**: We construct a\
  \ 30-task benchmark suite spanning classification, regression, and time-series domains, paired with negative control settings\
  \ and comprehensive threshold sensitivity sweeps [ARTIFACT:art_A_97AHCsuvAa, ARTIFACT:art_HjQ6l6qOmCqb].\n- **Empirical\
  \ Superiority**: We demonstrate that FPG planning achieves an 87.14% to 100% negative result detection rate (compared to\
  \ 38.57% for procedural planners, $p < 0.001$), eliminates false positive success claims on negative controls ($0.0\\%$\
  \ to $12.85\\%$ vs. $61.43\\\\%$), improves search iteration efficiency (4.5 vs. 9.7 mean iterations), and reduces the Trajectory\
  \ Rationalization Index from $0.807$ to $0.096$ [ARTIFACT:art_QUgzY-dCbiIl].\n\n\n# Related Work\n\nOur research intersects\
  \ with three primary domains: automated scientific discovery, LLM agent planning and self-correction, and computational\
  \ philosophy of science.\n\n### Automated Scientific Discovery Systems\nFully automated scientific discovery has advanced\
  \ rapidly with the advent of frontier large language models. Systems such as The AI Scientist [1] demonstrated end-to-end\
  \ automation of idea generation, experiment execution, and manuscript drafting in machine learning. However, subsequent\
  \ analyses highlighted pervasive failure modes, including hallucinated evaluation metrics, confirmation bias, and unchecked\
  \ persistence down failed experimental trajectories [6]. While prior engineering efforts have focused on improving code\
  \ generation robustness or expanding search spaces, they retain procedural task list planning paradigms that lack intrinsic\
  \ mechanisms for recognizing negative results.\n\n### Agent Planning and Self-Correction & Programmatic vs. Verbal Feedback\n\
  Planning in LLM agents has evolved from static linear prompting to dynamic tree-of-thought search [7], reflection loops\
  \ [8], and interactive planning frameworks [9]. Frameworks like Reflexion [8] leverage verbal reinforcement learning to\
  \ critique agent trajectories. However, verbal critique alone remains highly susceptible to **recursive rationalization**:\
  \ because LLMs are heavily conditioned to satisfy prompt instructions and generate fluent justifications, verbal self-critique\
  \ loops frequently rationalize sub-optimal performance as artifactual noise rather than epistemic refutation. \n\nOur work\
  \ diverges fundamentally by shifting from post-hoc verbal critique to structural refutation constraints. Rather than relying\
  \ on LLM-as-judge narrative summaries, FPGs employ **programmatic predicate evaluation**, executing rigorous, immutable\
  \ logical checks ($\\phi_i$) that operate independently of LLM narrative generation. This structural enforcement prevents\
  \ the agent from talking itself into accepting a failed experiment.\n\n### Popperian Falsification in Computational Reasoning\n\
  The application of Karl Popper's philosophy of science [4] to computational systems has inspired several theoretical and\
  \ empirical frameworks [10]. Recently, POPPER [2] proposed an agentic framework for validating free-form hypotheses using\
  \ sequential falsification experiments. While POPPER operates post-hoc on external hypotheses, our approach integrates structural\
  \ falsifiability upstream into the research planning phase, governing agent execution trajectories and enabling real-time\
  \ negative control validation.\n\n\n# Falsifiable Prediction Graphs: Architecture and Formalization\n\n### Preliminaries\
  \ and Problem Formulation\nLet an automated research discovery task be defined by a research goal $\\mathcal{G}$, a dataset\
  \ $\\mathcal{D}$, and an agent execution environment $\\mathcal{E}$. In a standard procedural planner, the research plan\
  \ $P_{\\text{proc}} = [s_1, s_2, \\dots, s_n]$ is a sequence of procedural instructions executed sequentially. The agent\
  \ evaluates success based on whether the terminal performance metric $M(\\mathcal{E}(s_n))$ exceeds a heuristic threshold\
  \ $\\tau$. When faced with a flawed hypothesis or a negative control dataset, the agent frequently rationalizes sub-threshold\
  \ performance as noise, resulting in false positive success claims.\n\n### Falsifiable Prediction Graph (FPG) Definition\n\
  A Falsifiable Prediction Graph $G = (V, E, \\Phi)$ is a directed acyclic graph where:\n1. **$V$** represents experimental\
  \ nodes (e.g., baseline establishment, hyperparameter tuning, architectural modification).\n2. **$E$** represents conditional\
  \ execution dependencies.\n3. **$\\Phi$** is a set of explicit quantitative refutation predicates associated with each node\
  \ $v \\in V$.\n\nFormally, every experimental node $v_i$ is tupled with a refutation predicate $\\phi_i = (\\text{Metric},\
  \ \\text{Threshold}, \\text{Direction}, \\text{NegativeControlTest})$. For example, a refutation predicate might specify:\
  \ \"If the validation accuracy delta over baseline is $< +0.01$ or if negative control feature permutation yields $< 5\\\
  %$ performance drop, reject hypothesis $H_i$ as a negative result.\"\n\n### Execution Protocol and Negative Control Validation\n\
  During pipeline execution, the FPG planner evaluates refutation predicates $\\Phi$ at each graph juncture. If an experimental\
  \ outcome triggers a refutation condition $\\phi_i$, the graph dynamically halts traversal along that branch, logs a structured\
  \ negative result, and triggers backtracking or search space pruning. Furthermore, FPGs mandate an early **Negative Control\
  \ Validation** step: before investing computational budget in complex method development, the agent executes the proposed\
  \ methodology against a randomized or adversarially corrupted version of the dataset. A valid method must fail on the negative\
  \ control; if the agent claims success on the negative control, the planning pipeline flags a confirmation bias violation\
  \ and aborts the trajectory.\n\n### Qualitative Walkthrough: Live Agent Encounter with a Negative Control\nTo illustrate\
  \ how FPG planning operates during live agent execution, consider an autonomous research agent tasked with evaluating a\
  \ novel regularized classifier. Under standard procedural planning, the agent trains the model on a permuted-label dataset\
  \ (negative control), observes an accuracy of $51.2\\%$, and—prompted to complete the task—generates the narrative: *\"\
  Model successfully trained and evaluated; accuracy is comparable to baseline expectation.\"* \n\nIn contrast, under FPG\
  \ planning, the plan mandates a programmatic refutation predicate: $\\phi_{\\text{neg}} = (\\text{AccuracyLoss} \\ge 0.15\
  \ \\text{ on permuted labels})$. Upon executing the experiment, the programmatic checker evaluates the metric against $\\\
  phi_{\\text{neg}}$, detects that the expected performance drop did not occur (delta $< 0.15$), immediately triggers a refutation\
  \ flag, halts execution along the development branch, and logs: *\"Falsification triggered: Method fails to distinguish\
  \ permuted target labels; hypothesis rejected as spurious artifact.\"* This prevents the agent from propagating the flawed\
  \ method into advanced hyperparameter tuning.\n\n\n# Experimental Methodology & Benchmark Suite\n\nTo rigorously test our\
  \ hypothesis, we utilized the **Agent Falsifiability Benchmark Suite** [ARTIFACT:art_A_97AHCsuvAa, ARTIFACT:art_HjQ6l6qOmCqb],\
  \ comprising 10 diverse empirical machine learning research tasks spanning regression, binary classification, multi-class\
  \ classification, and synthetic time-series modeling. Each research task is instantiated in three distinct experimental\
  \ settings:\n1. **True Positive Condition**: A valid methodological improvement expected to yield genuine performance gains.\n\
  2. **Negative Control Condition (Permuted Labels)**: Target labels are randomly permuted, ensuring that any claimed performance\
  \ improvement is a statistical artifact or agent hallucination.\n3. **Negative Control Condition (Adversarial Noise)**:\
  \ Input features are replaced with Gaussian noise, removing true signal.\n\n### Evaluated Architectures and Baselines\n\
  We compared two automated agent planning architectures:\n- **Standard Procedural Planner**: Executes linear task lists without\
  \ refutation criteria, relying on LLM verbal self-critique loops and post-hoc summarization to determine success or failure.\n\
  - **Falsifiable Prediction Graph Planner (Our Approach)**: Enforces structured causal dependency graphs equipped with explicit\
  \ mandatory refutation criteria, programmatic predicate evaluation, and early negative control validation tests.\n\n###\
  \ Evaluation Metrics and Statistical Rigor\nWe operationalized four primary evaluation metrics:\n- **Negative Result Detection\
  \ Rate**: The proportion of negative control tasks correctly identified as failed/null results rather than misinterpreted\
  \ as successes.\n- **False Positive Rate**: The proportion of negative control tasks incorrectly reported as successful\
  \ methodological breakthroughs (hallucinated success rate).\n- **Search Iteration Efficiency**: The mean number of execution\
  \ iterations required by the agent to resolve the research task.\n- **Trajectory Rationalization Index (TRI)**: A metric\
  \ quantifying the proportion of agent reasoning steps exhibiting recursive rationalization and hallucinated success justifications.\n\
  \nWe evaluated statistical significance using Fisher's exact test, chi-squared tests, and Cohen's $h$ effect size analyses\
  \ [ARTIFACT:art_QUgzY-dCbiIl].\n\n\n# Results & Empirical Evaluation\n\nWe executed both planning architectures across the\
  \ 30 evaluation task instances (10 base tasks $\\times$ 3 conditions) and conducted rigorous threshold sensitivity sweeps\
  \ ($\\tau$ from $0.00$ to $0.20$). The empirical results decisively confirm our hypothesis [ARTIFACT:art_HjQ6l6qOmCqb, ARTIFACT:art_QUgzY-dCbiIl].\n\
  \n### Negative Result Detection and False Positive Elimination\nAs summarized in Table 1 and Figure 2, the Falsifiable Prediction\
  \ Graph planner achieved a **100% Negative Result Detection Rate** ($1.00 \\pm 0.00$ in base evaluation; $87.14\\%$ across\
  \ threshold sweeps), correctly identifying negative control tasks as failures. In sharp contrast, the standard procedural\
  \ planner achieved only a **33.3% to 38.57% Negative Result Detection Rate** ($0.3333 \\pm 0.12$) [ARTIFACT:art_QUgzY-dCbiIl],\
  \ frequently succumbing to confirmation bias by rationalizing permuted-label success or ignoring anomalous metric drops.\n\
  \n| Planning Architecture | Negative Result Detection Rate $\\uparrow$ | False Positive Rate $\\downarrow$ | Mean Search\
  \ Iterations $\\downarrow$ | Trajectory Rationalization Index $\\downarrow$ |\n| :--- | :---: | :---: | :---: | :---: |\n\
  | **Standard Procedural Planner** | $0.3333 \\pm 0.12$ | $0.6667 \\pm 0.12$ | $9.7 \\pm 1.4$ | $0.8068 \\pm 0.08$ |\n| **Falsifiable\
  \ Prediction Graph (Ours)** | **$1.0000 \\pm 0.00$** | **$0.0000 \\pm 0.00$** | **$4.5 \\pm 0.7$** | **$0.0957 \\pm 0.03$**\
  \ |\n| *Statistical Significance ($p$-value)* | $p = 0.0002^{**}$ | $p = 0.0002^{**}$ | $p < 0.0001^{**}$ | $p < 0.0001^{**}$\
  \ |\n\nTable 1: Quantitative comparison between Standard Procedural Planners and Falsifiable Prediction Graph Planners across\
  \ benchmark task instances. Asterisks denote statistical significance via Fisher's exact test and chi-squared tests ($^{**}\
  \ p < 0.001$, $\\chi^2 = 12.15$, Cohen's $h = 1.91$) [ARTIFACT:art_QUgzY-dCbiIl].\n\n[FIGURE:fig2]\n\nFurthermore, while\
  \ the standard procedural planner exhibited a **66.7% False Positive Rate** on negative controls—hallucinating methodological\
  \ success on randomized data—the FPG planner achieved a **0.0% False Positive Rate** ($0.00 \\pm 0.00$) [ARTIFACT:art_QUgzY-dCbiIl].\
  \ Fisher's exact test and chi-squared tests confirm this performance delta is highly significant ($\\chi^2 = 12.15$, $p\
  \ = 0.00049$, Cohen's $h = 1.91$) [ARTIFACT:art_QUgzY-dCbiIl].\n\n### Threshold Sensitivity Analysis\nTo address potential\
  \ concerns regarding threshold sensitivity, we conducted rigorous sweeps of refutation thresholds ($\\tau$ from $0.00$ to\
  \ $0.20$ and delta bounds from $0.01$ to $0.10$). As illustrated in Figure 3, the FPG planner maintained exceptional stability:\
  \ across all threshold variations, the overall negative result detection rate remained robust at $87.14\\%$, while the false\
  \ positive rate remained constrained at $12.85\\%$. In contrast, procedural baselines fluctuated widely, exhibiting a mean\
  \ false positive rate of $61.43\\%$. This demonstrates that programmatic predicate evaluation is highly resilient to hyperparameter\
  \ threshold variations.\n\n[FIGURE:fig3]\n\n### Trajectory Rationalization and Search Efficiency\nEmbedding structural refutation\
  \ criteria and early negative control validation significantly reduced agent rationalization. As quantified by the Trajectory\
  \ Rationalization Index (TRI), procedural planners exhibited an average rationalization score of **$0.8068$**, whereas FPG\
  \ planning suppressed rationalization to **$0.0957$** ($p < 0.0001$) [ARTIFACT:art_QUgzY-dCbiIl]. Furthermore, early negative\
  \ control pruning reduced search iteration complexity: FPG converged in a mean of **$4.5$ iterations**, compared to **$9.7$\
  \ iterations** for procedural planners [ARTIFACT:art_QUgzY-dCbiIl].\n\n[FIGURE:fig4]\n\n\n# Discussion\n\n### Why Procedural\
  \ Planners Fail\nOur findings illuminate why traditional LLM agent planners fail in empirical research tasks. Language models\
  \ trained on scientific literature and code repositories are heavily conditioned to emulate successful outcomes. When an\
  \ agent executes an experiment that yields null results (e.g., accuracy near random chance on permuted labels), its parametric\
  \ memory associates code execution with \"finishing a task,\" prompting the LLM to generate narrative justifications rather\
  \ than recognizing epistemic refutation.\n\n### The Power of Programmatic Predicate Enforcement\nFalsifiable Prediction\
  \ Graphs resolve this pathology by decoupling execution completion from hypothesis validation. By encoding refutation criteria\
  \ $\\Phi$ as explicit logical predicates evaluated programmatically rather than narratively, FPGs compel the agent to treat\
  \ negative outcomes as primary feedback signals. This contrasts sharply with verbal self-critique loops, which remain trapped\
  \ within the LLM's generative bias.\n\n### Limitations\nWhile FPGs successfully eliminate confirmation bias in automated\
  \ research tasks, several limitations remain:\n1. **Threshold Sensitivity**: Constructing precise quantitative refutation\
  \ thresholds requires domain heuristics. Overly strict thresholds may trigger false refutations on valid methods with high\
  \ variance.\n2. **Graph Expressivity**: Highly exploratory research tasks involving paradigm shifts or unsupervised discovery\
  \ may not easily conform to static directed acyclic prediction graphs.\n3. **Planning Token Overhead**: Generating comprehensive\
  \ refutation predicates increases prompt complexity and initial planning token consumption.\n\n\n# Conclusion & Future Work\n\
  \nIn this paper, we introduced Falsifiable Prediction Graphs (FPGs), a novel agent planning architecture that integrates\
  \ Popperian falsification and negative control validation into automated scientific discovery workflows. Through rigorous\
  \ evaluation across a 30-task machine learning benchmark suite and threshold sensitivity sweeps, we demonstrated that FPGs\
  \ achieve a 100% negative result detection rate, eliminate false positive success claims on negative controls, and significantly\
  \ improve search efficiency compared to standard procedural planners [ARTIFACT:art_HjQ6l6qOmCqb, ARTIFACT:art_QUgzY-dCbiIl].\n\
  \nFuture work will explore dynamic, self-evolving falsification graphs that adapt refutation thresholds based on real-time\
  \ task complexity, as well as scaling FPGs to multi-agent collaborative discovery systems.\n\n# References\n\n[1] Lu, C.,\
  \ Lu, C., Lange, R. T., Foerster, J. N., Clune, J., & Ha, D. (2024). The AI Scientist: Fully automated scientific discovery.\
  \ *arXiv preprint arXiv:2408.06292*.\n[2] Huang, T., Zhang, Y., & Wang, L. (2025). POPPER: Agentic hypothesis validation\
  \ through sequential falsification. *Journal of Automated Scientific Reasoning*, 3(2), 112-128.\n[3] Popper, K. (1959).\
  \ *The Logic of Scientific Discovery*. Hutchinson.\n[4] Wang, Z., Cai, S., Liu, A., Wang, Y., & Liang, X. (2023). Describe,\
  \ explain, select and evaluate: Interactive planning for large language model agents. *Advances in Neural Information Processing\
  \ Systems*, 36.\n[5] Shinn, N., Cassano, B., Labash, E., Gopinath, A., Narasimhan, K., & Yao, S. (2023). Reflexion: Language\
  \ agents with verbal reinforcement learning. *Advances in Neural Information Processing Systems*, 36.\n[6] Yao, S., Yu,\
  \ D., Zhao, J., Shafran, I., Griffiths, T., Cao, Y., & Narasimhan, K. (2023). Tree of thoughts: Deliberate problem solving\
  \ with large language models. *Advances in Neural Information Processing Systems*, 36.\n[7] Chen, L., Zaharia, M., & Zou,\
  \ J. (2023). Evaluating large language model agents on empirical machine learning tasks. *arXiv preprint arXiv:2310.03302*.\n"
summary: >-
  Falsifiable Prediction Graphs embed Popperian refutation predicates and negative control validation into agent research
  planning, eliminating confirmation bias and achieving 100% negative result detection.
</paper_text>

<available_figures>
--- Item 1 ---
id: fig1
figure_type: concept
title: Falsifiable Prediction Graph Architecture
caption: >-
  End-to-end architecture of a Falsifiable Prediction Graph (FPG). Research workflows are structured as directed acyclic graphs
  where experimental nodes are tupled with programmatic refutation predicates (Phi). Early negative control validation tests
  (permuted labels and adversarial noise) govern graph traversal and branch pruning before iterative method refinement.
image_gen_detailed_description: >-
  Horizontal workflow diagram, left to right. Three main horizontal layers: (1) Hypothesis Formulation with graph initialization,
  (2) Mandatory Negative Control Validation node evaluating permuted labels against predicate Phi, (3) Conditional Execution
  Graph branching into Refinement or Falsification/Branch Pruning. Distinct color-coded nodes: Green for valid execution branches,
  Red for falsified/pruned negative branches. Clean white background, modern sans-serif typography, flat 2D schematic design.
aspect_ratio: '21:9'
summary: >-
  Architecture diagram illustrating Falsifiable Prediction Graph topology and conditional branching.
figure_path: figures/fig1_v0.jpg

--- Item 2 ---
id: fig2
figure_type: data
title: Negative Result Detection and False Positive Rates
caption: >-
  Comparison of Negative Result Detection Rate and False Positive Rate between Standard Procedural Planners and Falsifiable
  Prediction Graph Planners across 30 benchmark task instances. FPG planning achieves 100% negative result detection and 0%
  false positives, significantly outperforming procedural planners (p < 0.001).
image_gen_detailed_description: >-
  Grouped bar chart comparing two planning architectures across two key metrics. X-axis categories: 'Negative Result Detection
  Rate (up arrow)', 'False Positive Rate (down arrow)'. Series 1: 'Standard Procedural Planner' (Detection: 0.33, False Positive:
  0.67). Series 2: 'Falsifiable Prediction Graph (Ours)' (Detection: 1.00, False Positive: 0.00). Y-axis range: 0.0 to 1.0.
  Clean grid lines, distinct professional color palette (slate blue and coral), error bars indicating standard error, legend
  included.
aspect_ratio: '16:9'
summary: >-
  Compares negative result detection and false positive rates between FPG and procedural planners.
figure_path: figures/fig2_v0.pdf

--- Item 3 ---
id: fig3
figure_type: data
title: Threshold Sensitivity Analysis Across Refutation Bounds
caption: >-
  Sensitivity analysis illustrating False Positive Rates and Negative Result Detection Rates across varying quantitative refutation
  thresholds (tau from 0.00 to 0.20 and delta bounds from 0.01 to 0.10). FPG planning maintains robust performance stability
  across threshold variations.
image_gen_detailed_description: >-
  Line plot showing performance metrics across refutation threshold tau (0.00, 0.05, 0.10, 0.15, 0.20) on the X-axis. Y-axis
  represents rate (0.0 to 1.0). Four lines: FPG Detection Rate (flat at ~0.87-1.0), FPG False Positive Rate (flat at ~0.13-0.0),
  Procedural Detection Rate (~0.38), Procedural False Positive Rate (~0.61). Shaded regions indicate standard deviation across
  tasks. Clear axis labels, legend, and professional styling.
aspect_ratio: '16:9'
summary: Threshold sensitivity analysis showing robustness across refutation bounds.
figure_path: figures/fig3_v0.pdf

--- Item 4 ---
id: fig4
figure_type: data
title: Trajectory Rationalization Index Across Domains
caption: >-
  Trajectory Rationalization Index (TRI) measuring recursive rationalization and hallucinated success justifications in agent
  reasoning traces across machine learning domains (Classification, Regression, Time Series). FPG planning suppresses rationalization
  to 0.096 compared to 0.807 for procedural agents.
image_gen_detailed_description: >-
  Grouped bar chart comparing Trajectory Rationalization Index (TRI, range 0.0 to 1.0) across four domains: Classification,
  Regression, Time Series, and Synthetic Non-linear. Two series per domain: 'Standard Procedural Planner' (Classification:
  0.81, Regression: 0.79, Time Series: 0.84, Synthetic: 0.79) and 'Falsifiable Prediction Graph (Ours)' (Classification: 0.09,
  Regression: 0.10, Time Series: 0.11, Synthetic: 0.09). Y-axis label 'Trajectory Rationalization Index (TRI)', X-axis label
  'Domain'. Professional palette.
aspect_ratio: '16:9'
summary: >-
  Compares trajectory rationalization index across domains between FPG and procedural planners.
figure_path: figures/fig4_v0.pdf
</available_figures>

<figure_requirements>
CRITICAL: Include ALL figures from <available_figures>. No exceptions.

- Every figure MUST use \includegraphics{figures/<the filename from its own `figure_path` above>} — INCLUDING the extension it actually has. Data figures are delivered as `.pdf` (vector, so their axis labels stay sharp) and concept figures as `.jpg`. Writing `.jpg` for a `.pdf` figure names a file that is not in figures/ and the build fails on it
- Do NOT skip, convert to tables, or describe without inserting
- Each needs: \begin{figure}[placement], \includegraphics, \caption, \label, \end{figure} — one placement for every figure, see FLOAT PLACEMENT below. Constrain every \includegraphics with `width=\linewidth,height=0.85\textheight,keepaspectratio`. The height is a LAST RESORT, not the usual limit: it exists so a very tall figure cannot overrun the page, and at 0.4 it bound almost everything instead — a 1:1 confusion matrix printed at 50.9% and its 11 pt axis labels reached the page at 5.6 pt, below what any venue accepts. At 0.85 every ratio the paper prompt prescribes (21:9, 16:9, 4:3, 1:1) is limited by WIDTH, prints at 93% and keeps its text above 10 pt. Use exactly these option keys — `max height=` is NOT valid LaTeX
- Use the `caption` field from each figure for \caption{...} — do NOT invent new captions
- Place figures where their [FIGURE:fig_id] markers appear in paper_text
- VERIFICATION: paper.tex MUST have exact same number of \includegraphics as <available_figures>
- Do NOT generate new figure images (no matplotlib, no PIL, no image generation). Use ONLY the pre-generated figures from <available_figures>. They were already created by a previous pipeline step.

FLOAT PLACEMENT: every figure gets \begin{figure}[!htbp]. Measured, not chosen:
the document the aii-paper-to-latex skill sets up is ONE column, so `figure*` is
exactly as wide as `figure` (469.76pt either way) and gains nothing; and any
placement asking for a page TOP — `[!t]`, `[!tbp]` — floated the hero diagram above
the paper's own title on page 1, while `[!htbp]` did not. `[!htbp]` also gives LaTeX
four options, so a float can never be deferred to the end of the document, which one
option alone risks. Where the hero ENDS UP is decided by its [FIGURE:] marker in
paper_text, which is already placed near the end of the Introduction — preserve it.
</figure_requirements>

<artifact_links>
The paper_text contains \footnote{Code: \url{...}} references linking to artifact source code
on GitHub. Include \usepackage{hyperref} and \usepackage{url}.
Preserve these exactly as-is — do not remove, rewrite, or convert them to plain text.
The URLs will not resolve yet (the repo is deployed after compilation) — do NOT try to verify or fix them.
</artifact_links>

<headings>
NEVER use inline math (``$...$``) inside ``\section{...}`` / ``\subsection{...}`` / ``\subsubsection{...}`` arguments — hyperref's bookmark builder errors out (``Token not allowed in a PDF string``) and the PDF outline breaks. If a section heading needs a math-looking term, use the text equivalent (``d star`` not ``$d^*$``, ``alpha-equivalent`` not ``$\alpha$-equivalent``) or wrap it in ``\texorpdfstring{$math$}{plain}``. Inline math inside body paragraphs is fine.
</headings>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.
TODO 2. Review <paper_text> and <available_figures>. Copy all figure images into ./figures/ in your workspace. Count figures — MUST include every one. Plan placements per section. Build `./references.bib` via aii_semscholar_bib__fetch — collect DOIs/ArXiv IDs from <paper_text> and batch-fetch all BibTeX in one call. Do NOT fabricate entries.
TODO 3. Create `./paper.tex` per aii-paper-to-latex skill's setup, write ALL sections, insert ALL figures from <available_figures>, include `./references.bib` via \bibliography. Compile to PDF per skill's process. Fix errors.
TODO 4. CRITICAL VERIFICATION: Run `grep -c 'includegraphics' paper.tex`, confirm count equals figures in <available_figures>. If not, add missing figures. Verify `./paper.pdf` was created.
TODO 5. VISUAL REVIEW: Write Python script to convert EVERY page of paper.pdf to PNG at 150 DPI (use pdf2image or pymupdf). Then read ALL page screenshots — each page image costs ~1,600 tokens so a 15-page paper is only ~24K tokens. You MUST read every page. The ONLY exception is if all page images would not fit in your remaining context — in that case, read as many as fit and state which pages you are skipping and why. Check every page for layout issues, overlapping figures, cut-off text, bad spacing, formatting problems. Fix issues and recompile.
TODO 6. FINAL READ: Check page count (`pdfinfo paper.pdf` or pymupdf). Read entire paper.pdf — check for missing sections, unclear explanations, inconsistencies, typos. Fix and recompile. The ONLY exception is if all pages would not fit in your remaining context — in that case, read as many pages as fit and state which pages you are skipping and why.
</todos>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FullPaperExpectedFiles": {
      "description": "All expected output files from full paper generation.",
      "properties": {
        "paper_tex_path": {
          "description": "Path to LaTeX source file. Example: 'paper.tex'",
          "title": "Paper Tex Path",
          "type": "string"
        },
        "paper_pdf_path": {
          "description": "Path to compiled PDF. Example: 'paper.pdf'",
          "title": "Paper Pdf Path",
          "type": "string"
        },
        "references_bib_path": {
          "description": "Path to BibTeX bibliography file. Example: 'references.bib'",
          "title": "References Bib Path",
          "type": "string"
        },
        "figure_paths": {
          "description": "Paths to all figure image files. Example: ['figures/fig1_v0.jpg', 'figures/fig2_v0.jpg']",
          "items": {
            "type": "string"
          },
          "title": "Figure Paths",
          "type": "array"
        }
      },
      "required": [
        "paper_tex_path",
        "paper_pdf_path",
        "references_bib_path",
        "figure_paths"
      ],
      "title": "FullPaperExpectedFiles",
      "type": "object"
    }
  },
  "description": "Full paper \u2014 structured output from paper generation.",
  "properties": {
    "title": {
      "description": "Paper title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance. Aim for about 4-8 words (~40 characters).",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "description": "Brief summary of the generated paper: sections written, figures included, compilation status",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/FullPaperExpectedFiles",
      "description": "All output files you created. Must include paper.tex, paper.pdf, references.bib, and paths to all figure files."
    }
  },
  "required": [
    "title",
    "summary",
    "out_expected_files"
  ],
  "title": "FullPaper",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [13] HUMAN-USER prompt · 2026-08-10 00:17:06 UTC

```
Examine whether structuring a research plan as explicit falsifiable predictions improves the rate at which an automated pipeline detects its own negative results.
```
