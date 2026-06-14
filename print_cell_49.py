import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('model.ipynb', encoding='utf-8') as f:
    nb = json.load(f)

cell = nb['cells'][49]
print("=== CELL 49 SOURCE ===")
print("".join(cell.get('source', [])))
