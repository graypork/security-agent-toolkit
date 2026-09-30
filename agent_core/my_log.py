import logging
logging.basicConfig(
    filename="my.log",
    format="%(levelname)s %(message)s",
    encoding="utf-8",
    level=logging.INFO,
)

logging.info("시작")
logging.warning("주의")
logging.error("오류")
