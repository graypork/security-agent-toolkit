import logging

logging.basicConfig(
    filename="agent.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    encoding="utf-8",
)

logging.info("기록을 시작합니다")
logging.warning("주의할 일이 있었습니다")
print("화면에는 이 줄만 보입니다")
