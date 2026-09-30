
import logging
from collections import Counter

logging.basicConfig(
    filename="agent.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    encoding="utf-8",
)
logging.info("파서 시작: sample_logs_broken.csv")

def parse_line(l):
    parts = l.strip().split(",")
    return {"time":parts[0], "user":parts[1], "event":parts[2], "ip": parts[3]}

rst = []
with open("sample_logs_broken.csv", encoding="utf-8") as f:
    for line in f:
        try:
            rst.append(parse_line(line))

        except IndexError:
            logging.warning(line)

logging.info(f"정상 로그 {len(rst)}건 처리 완료")

fail_users = []
for log in rst: 
    if log["event"] == "LOGIN_FAIL":
        fail_users.append(log["user"])

cnt = Counter(fail_users)

for user, c in cnt.items():
    if c >= 3:
        print(f"확인 필요: {user} - 실패 {c}")
        
