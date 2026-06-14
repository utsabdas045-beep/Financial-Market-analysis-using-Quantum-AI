import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('model.ipynb', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    src = "".join(cell.get('source', []))
    if 'all_results' in src:
        print(f"Cell {i} has 'all_results':")
        src_safe = "".join(ch if ord(ch) < 128 else '?' for ch in src)
        # Print the lines containing 'all_results'
        lines = src_safe.split('\n')
        for line in lines:
            if 'all_results' in line:
                print(f"  {line[:120]}")
        print("="*40)
