import logging

logging.basicConfig(
    filename="nolevel.log",
    format="%(levelname)s %(message)s",
    encoding="utf-8",
)

logging.info("info 로 남긴 줄")
logging.warning("이 줄은 남을까요")
