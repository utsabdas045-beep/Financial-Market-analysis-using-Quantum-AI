import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('model.ipynb', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    src = "".join(cell.get('source', []))
    if 'feat_data' in src or 'download_market' in src:
        print(f"Cell {i} source:")
        src_safe = "".join(ch if ord(ch) < 128 else '?' for ch in src)
        lines = src_safe.split('\n')
        for line in lines:
            if 'feat_data' in line or 'download_market' in line:
                print(f"  {line[:120]}")
        print("="*40)
