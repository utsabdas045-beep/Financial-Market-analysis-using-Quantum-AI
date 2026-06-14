import json

notebook_path = "model.ipynb"

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

fixed = False
for cell in nb["cells"]:
    if cell["cell_type"] == "code":
        source_str = "".join(cell.get("source", []))
        if "def run_forecast_horizon_analysis():" in source_str:
            print("Found Cell 55. Fixing forecast horizon analysis...")
            # We replace the target_col assignment line
            old_line = 'target_col = f"target_ret_{h}d" if h in [1, 5, 10] else "target_ret_20d"'
            new_lines = """        target_col = f"target_ret_{h}d"
        if target_col not in sp_df.columns:
            sp_df = sp_df.copy()
            sp_df[target_col] = sp_df["Close"].pct_change(h).shift(-h)"""
            
            new_source = []
            for line in cell["source"]:
                if "target_col = f\"target_ret_{h}d\"" in line:
                    new_source.append(new_lines + "\n")
                else:
                    new_source.append(line)
            cell["source"] = new_source
            fixed = True
            break

if fixed:
    with open(notebook_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=2, default=str)
    print("Cell 55 fixed successfully!")
else:
    print("Failed to find or fix Cell 55.")
