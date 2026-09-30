import re
import json

PATTERN = r"(?P<time>[\d:]+) (?P<level>\w+) \w+ login for (?P<user>[\w.]+) from (?P<ip>[\d.]+)"
rows = []
unmatched = []

def parse_raw_logs(line):
    # 여기를 채우세요
    m = re.search(PATTERN, line)
    if m: return m.groupdict()
    else: return None

with open("raw_logs.txt", encoding="utf-8") as f:
    for line in f:
        row = parse_raw_logs(line.strip())
        if row: rows.append(row)
        else: unmatched.append(line)

# rows와 unmatched를 만들고 파일 두 개로 저장하는 코드를 이어서 작성합니다.


with open("normalized_logs.json", "w", encoding="utf-8") as f:
    json.dump(rows,f,ensure_ascii=True,indent=2)

with open("unmatched_logs.txt", "w", encoding="utf-8") as f:
    for line in unmatched:
        f.write(line)

print(f"정규화 {len(rows)}건 / 안 맞음 {len(unmatched)}건")
