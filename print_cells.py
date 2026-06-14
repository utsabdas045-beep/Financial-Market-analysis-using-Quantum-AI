import json
import sys

# Reconfigure stdout to use utf-8 to avoid encoding crashes on Windows
sys.stdout.reconfigure(encoding='utf-8')

with open('model.ipynb', encoding='utf-8') as f:
    nb = json.load(f)
for i, c in enumerate(nb['cells']):
    src = c['source'][0].strip() if c['source'] else 'EMPTY'
    # Clean up non-ascii to print safely in console just in case
    src_safe = "".join(ch if ord(ch) < 128 else '?' for ch in src)
    print(f"{i:02d} [{c['cell_type'][:4]}]: {src_safe[:60]}")
