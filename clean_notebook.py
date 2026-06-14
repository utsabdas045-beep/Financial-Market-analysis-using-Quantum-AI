import json

notebook_path = "model.ipynb"

# The unique markers for the inserted cells
removal_markers = [
    "PHASE 1 — STATISTICAL SIGNIFICANCE VALIDATION",
    "run_comprehensive_statistical_validation",
    "PHASE 2 — QUANTUM ATTRIBUTION ABLATION STUDY",
    "run_quantum_ablation_study",
    "PHASE 3 — MARKET REGIME ROBUSTNESS ANALYSIS",
    "run_market_regime_analysis",
    "PHASE 4 — FORECAST HORIZON ROBUSTNESS",
    "run_forecast_horizon_analysis",
    "PHASE 5 — COMPUTATIONAL SCALABILITY ANALYSIS",
    "run_computational_scalability_analysis",
    "PHASE 6 — QUANTUM NOISE ROBUSTNESS",
    "run_quantum_noise_robustness",
    "PHASE 7 — QUANTUM FEATURE SPACE ANALYSIS",
    "run_quantum_feature_space_analysis",
    "PHASE 8 — PUBLICATION-GRADE VISUALIZATIONS",
    "PHASE 9 — RESEARCH DISCUSSION",
    "PHASE 10 — FINAL PUBLICATION AUDIT"
]

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

original_cells = []
removed_count = 0

for cell in nb["cells"]:
    source_str = "".join(cell.get("source", []))
    should_remove = False
    for marker in removal_markers:
        if marker in source_str:
            should_remove = True
            break
    if should_remove:
        removed_count += 1
    else:
        original_cells.append(cell)

print(f"Removed {removed_count} enhancement cells. Remaining cells: {len(original_cells)}")

nb["cells"] = original_cells

with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=2, default=str)

print("Notebook cleaned successfully!")
