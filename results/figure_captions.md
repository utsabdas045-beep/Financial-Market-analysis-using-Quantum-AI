# Figure Captions for Manuscript Submission

## 01_market_overview.png
**Path:** `figures/01_market_overview.png`  
**Caption:** Fig. 1. Historical adjusted closing prices and trading volumes for all ten evaluated global indices from 2018 to 2024, providing a diverse cross-market baseline.

## 02_return_distributions.png
**Path:** `figures/02_return_distributions.png`  
**Caption:** Fig. 2. Empirical return distributions of the ten markets, overlaid with Gaussian fit curves, demonstrating non-normal fat-tail characteristics typical of financial time series.

## 03_correlation_matrix.png
**Path:** `figures/03_correlation_matrix.png`  
**Caption:** Fig. 3. Heatmap of daily return correlations across the ten global markets, highlighting systemic linkages and cross-market dependencies.

## 04_feature_importance_mi.png
**Path:** `figures/04_feature_importance_mi.png`  
**Caption:** Fig. 4. Mutual Information scores of the engineered feature set against the target next-day return, sorting features by information gain.

## 05_walk_forward_splits.png
**Path:** `figures/05_walk_forward_splits.png`  
**Caption:** Fig. 5. Schema of the purged walk-forward validation splits showing training and test partitions with a 10-day purging window to prevent overlap and look-ahead bias.

## 06_cross_market_robustness.png
**Path:** `figures/06_cross_market_robustness.png`  
**Caption:** Fig. 6. Cross-market R2, RMSE, and Directional Accuracy comparison for all models, highlighting consistent quantum improvement.

## 07_benchmark_comparison.png
**Path:** `figures/07_benchmark_comparison.png`  
**Caption:** Fig. 7. Comparison of predictions across the evaluated models highlighting variance and directional consensus on S&P 500 test set.

## 08_actual_vs_predicted.png
**Path:** `figures/08_actual_vs_predicted.png`  
**Caption:** Fig. 8. Actual vs. predicted returns for the best-performing model on the S&P 500 index, illustrating forecasting quality.

## 09_quantum_circuits.png
**Path:** `figures/09_quantum_circuits.png`  
**Caption:** Fig. 9. High-level architecture schematic of the parameterized quantum circuits (PQC) used in VQR and QKernel configurations.

## 09a_feature_map.png
**Path:** `figures/09a_feature_map.png`  
**Caption:** Fig. 9a. Parameterized circuit diagram of the ZZFeatureMap used to encode the classical features into quantum states.

## 09b_ansatz.png
**Path:** `figures/09b_ansatz.png`  
**Caption:** Fig. 9b. Parameterized ansatz (RealAmplitudes) circuit with entanglement structure for model training.

## 10_shap_analysis.png
**Path:** `figures/10_shap_analysis.png`  
**Caption:** Fig. 10. SHAP (SHapley Additive exPlanations) summary plot for feature attribution in the hybrid quantum-classical pipeline, comparing feature impacts.

## 11_metric_robustness.png
**Path:** `figures/11_metric_robustness.png`  
**Caption:** Fig. 11. Comparison of SMAPE and MAPE behavior under near-zero targets, proving the stability of SMAPE as a robust evaluation metric.

## 12_evidence_dashboard.png
**Path:** `figures/12_evidence_dashboard.png`  
**Caption:** Fig. 12. Final Evidence Dashboard displaying KPI gauges against pre-specified publication readiness success criteria.

## 13_cd_diagram.png
**Path:** `figures/13_cd_diagram.png`  
**Caption:** Fig. 13. Critical Difference (CD) diagram generated from the Nemenyi post-hoc test, grouping models by statistical similarity (at alpha = 0.05).

## 14_pairwise_wilcoxon_heatmap.png
**Path:** `figures/14_pairwise_wilcoxon_heatmap.png`  
**Caption:** Fig. 14. Pairwise Wilcoxon signed-rank test p-value heatmap with Holm-Bonferroni correction, evaluating significance of quantum R2 gains.

## 15_ablation_study.png
**Path:** `figures/15_ablation_study.png`  
**Caption:** Fig. 15. Component ablation study results comparing the full quantum pipeline to classical, hybrid, and lower-qubit configurations.

## 16_regime_heatmap.png
**Path:** `figures/16_regime_heatmap.png`  
**Caption:** Fig. 16. Heatmap of model R2 scores under partitioned market regimes (Bull, Bear, Sideways, High Volatility, Low Volatility) on S&P 500.

## 17_regime_diracc.png
**Path:** `figures/17_regime_diracc.png`  
**Caption:** Fig. 17. Directional Accuracy of all models across identified market regimes, illustrating regime-dependent model performance.

## 18_horizon_decay.png
**Path:** `figures/18_horizon_decay.png`  
**Caption:** Fig. 18. Performance decay of model forecasts as a function of the horizon (1, 5, 10, and 20 days) for classical and quantum models.

## 19_computational_scalability.png
**Path:** `figures/19_computational_scalability.png`  
**Caption:** Fig. 19. Computational runtime and memory scaling logs as functions of sample size N and qubit dimension, detailing scaling bottlenecks.

## 20_noise_robustness.png
**Path:** `figures/20_noise_robustness.png`  
**Caption:** Fig. 20. Predictive degradation curves of quantum models under simulated depolarizing noise models of NISQ hardware.

## 21_feature_space_projections.png
**Path:** `figures/21_feature_space_projections.png`  
**Caption:** Fig. 21. 2D t-SNE projections of features in the original space, classical PCA space, and quantum kernel space, colored by positive/negative return class.
