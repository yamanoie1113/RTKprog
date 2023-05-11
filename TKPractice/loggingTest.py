import logging

# format="%(asctime)s - %(levelname)s:%(name)s - %(message)s"を　追加
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s:%(name)s - %(message)s",filename="test.log")


logging.debug("This is DEBUG message.")     #デバッグ
logging.info("This is INFO message.")       #情報
logging.warning("This is WARNING message.") #警告
logging.error("This is ERROR message.")     #エラー
logging.critical("This is CRITICAL message.") #致命的エラー
