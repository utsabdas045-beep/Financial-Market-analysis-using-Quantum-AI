import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('model.ipynb', encoding='utf-8') as f:
    nb = json.load(f)

# Find export cell
for i, cell in enumerate(nb['cells']):
    src = "".join(cell.get('source', []))
    if 'Export' in src or 'export_dict' in src:
        print(f"Cell {i} source:")
        src_safe = "".join(ch if ord(ch) < 128 else '?' for ch in src)
        print(src_safe)
        print("="*40)
