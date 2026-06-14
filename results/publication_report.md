# Quantum-Enhanced Financial Forecasting — Publication Report

Generated: 2026-06-14 16:11

## Summary
- Markets evaluated: 10
- Models evaluated : 8
- Best avg R²      : 0.4305
- Best DirAcc      : 0.7533

## Quantum Architecture
- n_qubits: 4
- reps: 3
- encoding: reuploading
- use_kernel: False

## Quantum Contribution
| Market   |   RMSE Impr (%) |   R² Gain | Quantum Helps   |
|:---------|----------------:|----------:|:----------------|
| SSE      |           51.91 |    0.519  | True            |
| CSI300   |           20.71 |    0.4495 | True            |
| SP500    |           43.39 |    0.4575 | True            |
| NASDAQ   |           42.47 |    0.4878 | True            |
| DJIA     |           41.29 |    0.5091 | True            |
| FTSE100  |           34.92 |    0.5635 | True            |
| DAX      |           41.67 |    0.5401 | True            |
| CAC40    |           36.84 |    0.4696 | True            |
| NIFTY50  |           38    |    0.4542 | True            |
| BOVESPA  |           36.18 |    0.4883 | True            |

## Statistical Tests
| Quantum Model   | Classical Model   |   n_markets |   Mean Qu RMSE |   Mean Cl RMSE |   W-statistic |   p-value | Significant   |   Effect Size (d) |
|:----------------|:------------------|------------:|---------------:|---------------:|--------------:|----------:|:--------------|------------------:|
| QKernel_XGBoost | XGBoost           |          10 |       0.007274 |       0.012721 |             0 |     0.001 | True          |           -4.5298 |
| QKernel_XGBoost | LightGBM          |          10 |       0.007274 |       0.012633 |             0 |     0.001 | True          |           -5.1617 |
| QKernel_XGBoost | CatBoost          |          10 |       0.007274 |       0.011812 |             0 |     0.001 | True          |           -4.4851 |
| QKernel_Ridge   | XGBoost           |          10 |       0.007741 |       0.012721 |             0 |     0.001 | True          |           -4.0504 |
| QKernel_Ridge   | LightGBM          |          10 |       0.007741 |       0.012633 |             0 |     0.001 | True          |           -4.5755 |
| QKernel_Ridge   | CatBoost          |          10 |       0.007741 |       0.011812 |             0 |     0.001 | True          |           -3.8436 |

## Figures Generated
- figures/01_market_overview.png
- figures/02_return_distributions.png
- figures/03_correlation_matrix.png
- figures/04_feature_importance_mi.png
- figures/05_walk_forward_splits.png
- figures/06_cross_market_robustness.png
- figures/07_benchmark_comparison.png
- figures/08_actual_vs_predicted.png
- figures/09_quantum_circuits.png
- figures/09a_feature_map.png
- figures/09b_ansatz.png
- figures/10_shap_analysis.png
- figures/11_metric_robustness.png
- figures/12_evidence_dashboard.png
- figures/13_cd_diagram.png
- figures/14_pairwise_wilcoxon_heatmap.png
- figures/15_ablation_study.png
- figures/16_regime_heatmap.png
- figures/17_regime_diracc.png
- figures/18_horizon_decay.png
- figures/19_computational_scalability.png
- figures/20_noise_robustness.png
- figures/21_feature_space_projections.png

## Tables Generated
- tables/ablation_study.csv
- tables/benchmark_results.csv
- tables/computational_scalability.csv
- tables/dataset_statistics.csv
- tables/failure_correction_log.csv
- tables/feature_space_analysis.csv
- tables/forecast_horizon_robustness.csv
- tables/leakage_audit.csv
- tables/market_regime_analysis.csv
- tables/noise_robustness.csv
- tables/pairwise_wilcoxon.tex
- tables/pairwise_wilcoxon_tests.csv
- tables/pivot_r2.csv
- tables/publication_tables.tex
- tables/quantum_contribution.csv
- tables/statistical_tests.csv