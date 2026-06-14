import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('model.ipynb', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    src = "".join(cell.get('source', []))
    if 'pairwise_wilcoxon.tex' in src or 'pairwise_wilcoxon' in src:
        print(f"Cell {i} contains 'pairwise_wilcoxon':")
        for line in src.splitlines():
            if 'pairwise_wilcoxon' in line:
                print("  ", line)
        print("="*40)
