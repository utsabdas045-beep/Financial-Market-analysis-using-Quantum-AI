import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('model.ipynb', encoding='utf-8') as f:
    nb = json.load(f)

src = "".join(nb['cells'][45].get('source', []))
src_safe = "".join(ch if ord(ch) < 128 else '?' for ch in src)
print(src_safe)
