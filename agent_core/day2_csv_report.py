import csv
from collections import Counter

THRESHOLD = 2

failed_users = []
with open("logs_with_header.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # ← 여기에 두 줄: 결과가 FAIL 이면 failed_users 에 계정을 append
        if row["result"] == "FAIL": 
            failed_users.append(row["user"])

counts = Counter(failed_users)
for user, count in counts.items():
    # ← 여기에 두 줄: 횟수가 THRESHOLD 이상이면
    if count >= THRESHOLD : 
        print(f"확인 필요: {user} · {count}회")
    #                print(f"확인 필요: {user} · {count}회")
