#from multiprocessing import get_start_method
import sys
import pathlib

current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Sensors import LogMgmt

class logtest():
    def __init__(self):
        # クラス変数
        self.logfile = 'LOG_TEST.txt'

        #GPSログの初期化
        LogMgmt.clear(self.logfile)
        LogMgmt.write(self.logfile,"LOG_testing...")

    def logtester(self,text):
        LogMgmt.write(self.logfile,text)




def main():
    testclass = logtest()
    i = 1
    while True:
        testclass.logtester(i)
        i += 1

if __name__ == '__main__':
    main()