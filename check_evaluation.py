import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('model.ipynb', encoding='utf-8') as f:
    nb = json.load(f)

# Let's search for the full_evaluation cell
found = False
for i, cell in enumerate(nb['cells']):
    src = "".join(cell.get('source', []))
    if 'def full_evaluation' in src or 'full_evaluation(' in src:
        print(f"Cell {i} source:")
        src_safe = "".join(ch if ord(ch) < 128 else '?' for ch in src)
        print(src_safe[:1500])
        print("="*40)
        found = True

if not found:
    print("Could not find full_evaluation cell.")
