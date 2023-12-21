import datetime
import sys
import pathlib
import csv



class LogMgmt():

    dir = pathlib.Path(__file__).resolve().parent
    dir = (str(dir) + '/../LOG/')
    log_file = None
    
    def _init__(self):
        pass
        
    def set_param(self,file):
        now = datetime.datetime.now()
        self.log_file = self.dir + file + "__" + now.strftime('%Y%m%d_%H%M%S')
    
    #ログの内容を消去する
    def clear(self):
        f = open(self.log_file,"w")
        f.close()

    def write(self,param):
        #now = datetime.datetime.now()
        with open(self.log_file,"a") as f:
            writer = csv.writer(f)
            writer.writerow(param)

    #ログファイルの読み込み
    def read(self):
        pass
        """
        now = datetime.datetime.now()
        with open(self.dir + filename + "__" + now.strftime('%Y%m%d_%H%M%S')) as f:
            print(f.read())
        """
    

def main():
    filename = "LogTest"
    i = 0
    tester = LogMgmt()
    
    param = [1,1]
    tester.set_param(filename)
    tester.write(param)
    tester.write(param)

if __name__ == '__main__':
    main()