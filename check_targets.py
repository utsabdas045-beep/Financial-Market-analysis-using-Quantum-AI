import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('model.ipynb', encoding='utf-8') as f:
    nb = json.load(f)

# Find feature engineering cell (Cell 10)
src = "".join(nb['cells'][10].get('source', []))
src_safe = "".join(ch if ord(ch) < 128 else '?' for ch in src)
print("Cell 10 return column definitions:")
for line in src_safe.split('\n'):
    if 'target' in line or 'ret' in line or 'Close' in line:
        print(f"  {line[:120]}")
