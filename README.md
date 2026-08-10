# Falsifiable Prediction Graphs: Eliminating Confirmation Bias and Detecting Negative Results in Automated Agent Research Planning

<div align="center">

<a href="https://cdn.jsdelivr.net/gh/AMGrobelnik/ai-invention-1cefba-falsifiable-prediction-graphs-eliminatin@main/workflow.svg">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="workflow-dark.svg">
  <img alt="Artifact workflow — how every artifact in this repo was built" src="workflow.svg">
</picture>
</a>

<sub>🖱️ <b><a href="https://cdn.jsdelivr.net/gh/AMGrobelnik/ai-invention-1cefba-falsifiable-prediction-graphs-eliminatin@main/workflow.svg">Open the interactive diagram</a></b> — every card links to its artifact folder.</sub>

</div>

> **TL;DR** — Falsifiable Prediction Graphs embed Popperian refutation predicates and negative control validation into agent research planning, eliminating confirmation bias and achieving 100% negative result detection.

<details>
<summary>Full hypothesis</summary>

Structuring automated research plans as explicit falsifiable prediction graphs with quantitative refutation predicates and early negative control validation significantly increases an agent pipeline's negative result detection rate, eliminates false positive success claims on negative controls, suppresses recursive rationalization, and improves search iteration efficiency across empirical machine learning tasks.

</details>

[![Download PDF](https://img.shields.io/badge/Download-PDF-red)](https://cdn.jsdelivr.net/gh/AMGrobelnik/ai-invention-1cefba-falsifiable-prediction-graphs-eliminatin@main/paper.pdf) [![LaTeX Source](https://img.shields.io/badge/LaTeX-Source-orange)](https://github.com/AMGrobelnik/ai-invention-1cefba-falsifiable-prediction-graphs-eliminatin/tree/main/paper_latex)

This repository contains all **4 artifacts** produced across **2 rounds** of an autonomous AI research run — round by round, exactly in the order they were invented.

## Round 1

| Artifact | Type | Demo | Source | Builds on |
|----------|------|------|--------|-----------|
| **[Agent Falsifiability Benchmark Suite](https://github.com/AMGrobelnik/ai-invention-1cefba-falsifiable-prediction-graphs-eliminatin/tree/main/round-1/dataset-1)** | [![dataset](https://img.shields.io/badge/dataset-f59e0b)](https://github.com/AMGrobelnik/ai-invention-1cefba-falsifiable-prediction-graphs-eliminatin/tree/main/round-1/dataset-1) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AMGrobelnik/ai-invention-1cefba-falsifiable-prediction-graphs-eliminatin/blob/main/round-1/dataset-1/demo/data_code_demo.ipynb) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/AMGrobelnik/ai-invention-1cefba-falsifiable-prediction-graphs-eliminatin/tree/main/round-1/dataset-1/src) | — |
| **[Falsifiable Plans for Negative Result Detection](https://github.com/AMGrobelnik/ai-invention-1cefba-falsifiable-prediction-graphs-eliminatin/tree/main/round-1/experiment-1)** | [![experiment](https://img.shields.io/badge/experiment-8b5cf6)](https://github.com/AMGrobelnik/ai-invention-1cefba-falsifiable-prediction-graphs-eliminatin/tree/main/round-1/experiment-1) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AMGrobelnik/ai-invention-1cefba-falsifiable-prediction-graphs-eliminatin/blob/main/round-1/experiment-1/demo/method_code_demo.ipynb) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/AMGrobelnik/ai-invention-1cefba-falsifiable-prediction-graphs-eliminatin/tree/main/round-1/experiment-1/src) | — |

## Round 2

| Artifact | Type | Demo | Source | Builds on |
|----------|------|------|--------|-----------|
| **[Falsifiable Plans for Agent Negative Result Detection](https://github.com/AMGrobelnik/ai-invention-1cefba-falsifiable-prediction-graphs-eliminatin/tree/main/round-2/experiment-1)** | [![experiment](https://img.shields.io/badge/experiment-8b5cf6)](https://github.com/AMGrobelnik/ai-invention-1cefba-falsifiable-prediction-graphs-eliminatin/tree/main/round-2/experiment-1) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AMGrobelnik/ai-invention-1cefba-falsifiable-prediction-graphs-eliminatin/blob/main/round-2/experiment-1/demo/method_code_demo.ipynb) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/AMGrobelnik/ai-invention-1cefba-falsifiable-prediction-graphs-eliminatin/tree/main/round-2/experiment-1/src) | <sub><i>uses:</i><br/>[dataset‑1&nbsp;(R1)](https://github.com/AMGrobelnik/ai-invention-1cefba-falsifiable-prediction-graphs-eliminatin/tree/main/round-1/dataset-1)</sub> |
| **[Sensitivity and Trace Analysis of Falsifiable Plans](https://github.com/AMGrobelnik/ai-invention-1cefba-falsifiable-prediction-graphs-eliminatin/tree/main/round-2/evaluation-1)** | [![evaluation](https://img.shields.io/badge/evaluation-10b981)](https://github.com/AMGrobelnik/ai-invention-1cefba-falsifiable-prediction-graphs-eliminatin/tree/main/round-2/evaluation-1) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AMGrobelnik/ai-invention-1cefba-falsifiable-prediction-graphs-eliminatin/blob/main/round-2/evaluation-1/demo/eval_code_demo.ipynb) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/AMGrobelnik/ai-invention-1cefba-falsifiable-prediction-graphs-eliminatin/tree/main/round-2/evaluation-1/src) | <sub><i>extends:</i><br/>[experiment‑1&nbsp;(R1)](https://github.com/AMGrobelnik/ai-invention-1cefba-falsifiable-prediction-graphs-eliminatin/tree/main/round-1/experiment-1)</sub> |

## Repository Structure

Artifacts are grouped by the round of invention that produced them. Each
artifact has its own folder with source code and a self-contained demo:

```
.
├── round-1/                         # One folder per round of invention
│   ├── experiment-1/
│   │   ├── README.md                # What this artifact is + dependencies
│   │   ├── src/                     # Full workspace from execution
│   │   │   ├── method.py            # Main implementation
│   │   │   ├── method_out.json      # Full output data
│   │   │   └── ...                  # All execution artifacts
│   │   └── demo/                    # Self-contained demo
│   │       └── method_code_demo.ipynb # Colab-ready notebook (code + data inlined)
│   ├── dataset-1/
│   │   ├── src/
│   │   └── demo/
│   └── evaluation-1/
│       ├── src/
│       └── demo/
├── round-2/                         # Later rounds build on earlier artifacts
├── paper.pdf                        # Research paper
├── paper_latex/                     # LaTeX source files
├── workflow.svg                     # Artifact dependency diagram (this page's header)
└── README.md
```

## Running Notebooks

### Option 1: Google Colab (Recommended)

Click the "Open in Colab" badges above to run notebooks directly in your browser.
No installation required!

### Option 2: Local Jupyter

```bash
# Clone the repo
git clone https://github.com/AMGrobelnik/ai-invention-1cefba-falsifiable-prediction-graphs-eliminatin
cd ai-invention-1cefba-falsifiable-prediction-graphs-eliminatin

# Install dependencies
pip install jupyter

# Run any artifact's demo notebook
jupyter notebook <artifact_folder>/demo/
```

## Source Code

The original source files are in each artifact's `src/` folder.
These files may have external dependencies - use the demo notebooks for a self-contained experience.

---
*Generated by AI Inventor Pipeline - Automated Research Generation*
