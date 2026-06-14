# Quantum-Enhanced Financial Forecasting

> **IEEE Conference Paper + Reproducible Research Notebook**
> *A multi-market evaluation of quantum kernel methods and variational quantum regression for equity index return forecasting.*

---

## Overview

This repository contains the complete research artifacts for the paper:

**"Quantum-Enhanced Financial Forecasting: A Multi-Market Evaluation with Statistical Validation"**
*Utsab Das — School of Computer Engineering, KIIT Deemed to be University (KIIT-DU)*

The study evaluates whether Qiskit-based quantum machine learning models deliver statistically significant and practically meaningful improvements over strong classical baselines in financial time-series forecasting across **10 global equity indices** spanning **2010–2026**.

---

## Key Results

| Metric | Best Classical | Best Quantum | Improvement |
|--------|---------------|--------------|-------------|
| Mean RMSE | 0.0118 | 0.0072 | **−38.8%** |
| Mean R² | −0.054 | +0.440 | **+0.494** |
| Mean DirAcc | 52.9% | 73.0% | **+20.1 pp** |

All improvements are statistically significant at **p < 0.001** (Wilcoxon signed-rank, Holm–Bonferroni corrected) with large Cohen's d effect sizes (|d| > 3.8) across all 10 markets.

---

## Repository Structure

```
.
├── model.ipynb                          # Main research notebook (18 sections)
├── results/
│   ├── final_results.csv                # Per-market per-model metrics
│   ├── publication_report.md            # Auto-generated summary report
│   └── final_results.json               # Full structured results
├── figures/                             # All 21 publication figures (PNG)
│   ├── 06_cross_market_robustness.png
│   ├── 07_benchmark_comparison.png
│   ├── 09_quantum_circuits.png
│   ├── 10_shap_analysis.png
│   ├── 13_cd_diagram.png
│   ├── 15_ablation_study.png
│   └── ...
├── tables/                              # All result tables (CSV + LaTeX)
│   ├── benchmark_results.csv
│   ├── dataset_statistics.csv
│   ├── statistical_tests.csv
│   ├── ablation_study.csv
│   ├── quantum_contribution.csv
│   ├── pairwise_wilcoxon.tex
│   └── publication_tables.tex
├── paper/
│   ├── main.tex                         # IEEE LaTeX manuscript
│   └── references.bib                   # BibTeX bibliography (23 entries)
└── README.md
```

---

## Markets Evaluated

| Market | Index | Region | Trading Days |
|--------|-------|--------|-------------|
| SSE | Shanghai Composite (000001.SS) | China | 3,915 |
| CSI300 | CSI 300 (000300.SS) | China | 1,202 |
| SP500 | S&P 500 (^GSPC) | USA | 4,064 |
| NASDAQ | NASDAQ Composite (^IXIC) | USA | 4,064 |
| DJIA | Dow Jones Industrial (^DJI) | USA | 4,064 |
| FTSE100 | FTSE 100 (^FTSE) | UK | 4,079 |
| DAX | DAX 40 (^GDAXI) | Germany | 4,100 |
| CAC40 | CAC 40 (^FCHI) | France | 4,132 |
| NIFTY50 | Nifty 50 (^NSEI) | India | 3,965 |
| BOVESPA | Ibovespa (^BVSP) | Brazil | 4,003 |

---

## Models

### Quantum Models
| Model | Description |
|-------|-------------|
| **QKernel-Ridge** | ZZFeatureMap quantum kernel + Ridge regression |
| **QKernel-XGBoost** | ZZFeatureMap quantum kernel + XGBoost |
| **VQR** | 4-qubit Variational Quantum Regressor (RealAmplitudes ansatz, 3 reps) |

### Classical Baselines
| Model | Description |
|-------|-------------|
| Ridge | L2-regularized linear regression |
| RandomForest | 500-tree ensemble, Optuna-tuned |
| XGBoost | Gradient boosting, Optuna-tuned |
| LightGBM | Gradient boosting (LGBM), Optuna-tuned |
| CatBoost | Gradient boosting (CatBoost), Optuna-tuned |

---

## Quantum Architecture

```
Input (4 features)
       │
       ▼
┌─────────────────────────┐
│  ZZFeatureMap           │  ← Data re-uploading encoding
│  n_qubits=4, reps=2     │    φ_j(x) = x_j
│  ZZ cross-terms         │    φ_jk(x) = (π−x_j)(π−x_k)
└─────────────────────────┘
       │
       ▼
┌─────────────────────────┐
│  RealAmplitudes Ansatz  │  ← Variational circuit (VQR only)
│  n_qubits=4, reps=3     │    24 trainable parameters
│  Linear entanglement    │    Optimizer: L-BFGS-B, 150 epochs
└─────────────────────────┘
       │
       ▼
  ⟨Z₀⟩ → predicted return   (VQR)
  K(x,x') → kernel matrix   (QKernel)
```

**Kernel definition:**
$$k_Q(\mathbf{x}, \mathbf{x}') = |\langle 0^{\otimes n}|U^\dagger(\mathbf{x}')U(\mathbf{x})|0^{\otimes n}\rangle|^2$$

---

## Notebook Structure (`model.ipynb`)

The notebook is organized into 18 self-contained sections:

| # | Section | Description |
|---|---------|-------------|
| 1 | Environment Setup | Package installation (Qiskit, Aer, ML libs) |
| 2 | Global Config | CFG dictionary, market tickers, seeds |
| 3 | Data Acquisition | yfinance download with retry logic |
| 4 | EDA | Market overview, return distributions, correlations |
| 5 | Feature Engineering | 40+ technical, statistical, and regime features |
| 6 | Leakage Prevention | Temporal integrity audit, purging gap verification |
| 7 | Walk-Forward Validation | Purged 5-fold CV framework |
| 8 | Classical Benchmarks | Ridge, RF, XGBoost, LightGBM, CatBoost |
| 9 | Quantum Architecture | ZZFeatureMap, ansatz builder, Optuna search |
| 10 | Hybrid Systems | QKernel-Ridge, QKernel-XGBoost, VQR |
| 11 | Ablation Study | Component contribution analysis |
| 12 | Cross-Market Robustness | All 10 markets evaluated |
| 13 | Statistical Testing | Wilcoxon, Friedman, Nemenyi tests |
| 14 | Explainability | SHAP, permutation importance |
| 15 | Metric Robustness | SMAPE vs MAPE stability analysis |
| 16 | Publication Figures | All 21 figures generated |
| 17 | Evidence Dashboard | IEEE audit KPI gauges |
| 18 | Export | CSV, JSON, LaTeX tables |

---

## Installation

### Requirements

- Python 3.9+
- CUDA optional (CPU simulation sufficient for 4-qubit circuits)

### Install dependencies

```bash
pip install qiskit==1.1.2 \
            qiskit-aer==0.14.2 \
            qiskit-machine-learning==0.7.2 \
            qiskit-algorithms==0.3.1 \
            yfinance>=0.2.40 \
            pandas>=2.0 \
            numpy>=1.24 \
            scikit-learn>=1.3 \
            xgboost>=2.0 \
            lightgbm>=4.0 \
            catboost>=1.2 \
            optuna>=3.4 \
            shap>=0.44 \
            statsmodels>=0.14 \
            hmmlearn>=0.3 \
            matplotlib>=3.7 \
            seaborn>=0.13 \
            scipy>=1.11
```

Or install all at once:

```bash
pip install -r requirements.txt
```

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/<your-username>/quantum-financial-forecasting.git
cd quantum-financial-forecasting

# Install dependencies
pip install -r requirements.txt

# Launch the notebook
jupyter notebook model.ipynb
```

Run all cells in order. Data is downloaded automatically via `yfinance`. Total runtime on CPU: approximately 2–4 hours for all 10 markets (quantum kernel computation dominates).

---

## Reproducing Paper Results

All figures and tables in the paper are generated directly by the notebook:

```bash
# Results are saved to:
results/final_results.csv       # main performance table
tables/statistical_tests.csv    # Wilcoxon test results
tables/quantum_contribution.csv # per-market quantum gain
figures/*.png                   # all 21 publication figures
tables/publication_tables.tex   # ready-to-paste LaTeX tables
```

To compile the paper:

```bash
cd paper/
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

Or upload `main.tex`, `references.bib`, and the `figures/` folder directly to [Overleaf](https://overleaf.com).

---

## Validation Framework

The study uses a **purged walk-forward validation** protocol to eliminate temporal data leakage:

```
Timeline ──────────────────────────────────────────────►

  Fold 1: [████████████ Train ████████████] [gap] [Test]
  Fold 2:    [████████████ Train ████████████] [gap] [Test]
  Fold 3:       [████████████ Train ████████████] [gap] [Test]
  Fold 4:          [████████████ Train ████████████] [gap] [Test]
  Fold 5:             [████████████ Train ████████████] [gap] [Test]

  gap = 10 trading days (purge window)
```

An independent leakage audit confirms **zero train-test overlap** across all markets and folds.

---

## Statistical Validation Summary

| Test | Result |
|------|--------|
| Wilcoxon signed-rank (QKernel-XGB vs XGBoost) | p = 0.001, W = 0, d = −4.53 |
| Wilcoxon signed-rank (QKernel-XGB vs LightGBM) | p = 0.001, W = 0, d = −5.16 |
| Wilcoxon signed-rank (QKernel-XGB vs CatBoost) | p = 0.001, W = 0, d = −4.49 |
| Friedman test (all 8 models × 10 markets) | p < 0.001 |
| Nemenyi post-hoc | Quantum models form distinct superior cluster |

`W = 0` means the quantum model outperforms the classical model on **every single one** of the 10 markets.

---

## Citation

If you use this code or paper in your research, please cite:

```bibtex
@inproceedings{das2026quantum,
  author    = {Das, Utsab},
  title     = {Quantum-Enhanced Financial Forecasting: A Multi-Market
               Evaluation with Statistical Validation},
  booktitle = {Proceedings of the IEEE Conference},
  year      = {2026},
  institution = {School of Computer Engineering,
                 Kalinga Institute of Industrial Technology
                 Deemed to be University (KIIT-DU)}
}
```

---

## Author

**Utsab Das**
School of Computer Engineering
Kalinga Institute of Industrial Technology Deemed to be University (KIIT-DU)
📧 [2505647@kiit.ac.in](mailto:2505647@kiit.ac.in)

---

## License

This project is released for academic research purposes. Please contact the author for commercial use inquiries.

---

*Built with [Qiskit](https://qiskit.org/) · [Qiskit Machine Learning](https://qiskit-community.github.io/qiskit-machine-learning/) · [Qiskit Aer](https://qiskit.github.io/qiskit-aer/)*
