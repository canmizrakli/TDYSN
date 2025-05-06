import json

NB = "/Users/canmizrakli/Desktop/8th semester/CMPE 490/TDSP.Net/TDSP_YOLO_v2.ipynb"

# 1) Load the raw JSON
with open(NB, "r", encoding="utf-8") as f:
    data = json.load(f)

# 2) Remove any top-level widgets key
data.get("metadata", {}).pop("widgets", None)

# 3) Remove cell-level widgets metadata
for cell in data.get("cells", []):
    cell.get("metadata", {}).pop("widgets", None)

# 4) Write back a clean, indented JSON
with open(NB, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

print("✅ Stripped out all widget metadata (top-level and per-cell).")