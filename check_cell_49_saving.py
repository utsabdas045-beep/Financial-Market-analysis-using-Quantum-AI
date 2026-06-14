import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('model.ipynb', encoding='utf-8') as f:
    nb = json.load(f)

cell = nb['cells'][49]
src = "".join(cell.get('source', []))
for line in src.splitlines():
    if 'tables/' in line or 'to_latex' in line or 'to_csv' in line or 'open' in line:
        print(line)
