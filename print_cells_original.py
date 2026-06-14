import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('../financial_model_quantum.ipynb', encoding='utf-8') as f:
    nb = json.load(f)
print(f"Total cells: {len(nb['cells'])}")
for i, c in enumerate(nb['cells']):
    src = c['source'][0].strip() if c['source'] else 'EMPTY'
    src_safe = "".join(ch if ord(ch) < 128 else '?' for ch in src)
    print(f"{i:02d} [{c['cell_type'][:4]}]: {src_safe[:60]}")
