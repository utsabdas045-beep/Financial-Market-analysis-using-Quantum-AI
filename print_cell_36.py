import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('model.ipynb', encoding='utf-8') as f:
    nb = json.load(f)

cell = nb['cells'][36]
print("=== CELL 36 SOURCE ===")
print("".join(cell.get('source', [])))
