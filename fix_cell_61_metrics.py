import json

notebook_path = "model.ipynb"

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

fixed = False
for cell in nb["cells"]:
    if cell["cell_type"] == "code":
        source_str = "".join(cell.get("source", []))
        if "def run_quantum_feature_space_analysis():" in source_str:
            print("Found Cell 61. Fixing missing metrics imports...")
            new_source = []
            for line in cell["source"]:
                new_source.append(line)
                if "def run_quantum_feature_space_analysis():" in line:
                    new_source.append("    from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score\n")
            cell["source"] = new_source
            fixed = True
            break

if fixed:
    with open(notebook_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=2, default=str)
    print("Cell 61 metrics fixed successfully!")
else:
    print("Failed to find or fix Cell 61.")
