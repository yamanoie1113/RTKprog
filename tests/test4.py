import logging
import time
from concurrent.futures import ThreadPoolExecutor
logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")
def myworker(x: int, y: int):
    logging.debug("start")
    result = x + y
    time.sleep(5)
    logging.debug(f"end: {result}")
    return result
def main():
    logging.debug("start")
    # max_workersでスレッド数を指定
    with ThreadPoolExecutor(max_workers=5) as executor:
        f1 = executor.submit(myworker, 2, 3)
        f2 = executor.submit(myworker, 5, 10)
        logging.debug(f1.result())
        logging.debug(f2.result())
    logging.debug("end")
if __name__ == "__main__":
    main()