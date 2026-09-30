import logging

logging.basicConfig(
    filename="agent.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    encoding="utf-8",
)
logging.info("집계 시작")

cnt = 0

with open("sample_logs.csv", encoding="utf-8") as f:
    for line in f:
        cnt += 1

logging.info(f"집계 완료 {cnt}건")

!python count_logs.py
!cat agent.log
