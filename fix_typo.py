import json

notebook_path = "model.ipynb"

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

fixed_count = 0
for cell in nb["cells"]:
    if "source" in cell:
        for idx, line in enumerate(cell["source"]):
            if "fill_space_df" in line:
                cell["source"][idx] = line.replace("fill_space_df", "feat_space_df")
                fixed_count += 1

print(f"Fixed {fixed_count} occurrence(s) of fill_space_df -> feat_space_df")

with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=2, default=str)

print("Notebook updated and saved.")
