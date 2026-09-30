import json

data = {"city": "seoul", "count": 3}

with open("demo.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("저장 완료")
