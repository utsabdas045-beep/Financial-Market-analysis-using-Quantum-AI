import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('model.ipynb', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    src = "".join(cell.get('source', []))
    if 'log_ret' in src:
        print(f"Cell {i} has 'log_ret':")
        src_safe = "".join(ch if ord(ch) < 128 else '?' for ch in src)
        lines = src_safe.split('\n')
        for line in lines:
            if 'log_ret' in line:
                print(f"  {line[:120]}")
        print("="*40)
