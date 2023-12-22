import datetime
import os
import sys
import pathlib
import csv



class LogMgmt():
    now = datetime.datetime.now()
    dir = pathlib.Path(__file__).resolve().parent
    dir = (str(dir) + '/../LOG/') + now.strftime('%Y%m%d_%H%M%S') + '/'
    os.mkdir(dir)
    log_file = None
    
    def _init__(self):
        pass
    
    #ディレクトリとヘッダーの作成(list[]:str,str)
    def set_param(self,header,file):

        self.log_file = self.dir + file

        with open(self.log_file,"a") as f:

            writer = csv.writer(f)
            writer.writerow(['timestamp',header])
    
    #ログの内容を消去する
    def clear(self):
        f = open(self.log_file,"w")
        f.close()

    def write(self,param):
        #now = datetime.datetime.now()
        with open(self.log_file,"a") as f:
            writer = csv.writer(f)
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            writer.writerow([now,param])

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
    header = ['test_val1','test_val2']
    i = 0
    tester = LogMgmt()

    
    param = [1,1]
    tester.set_param(header,filename)
    tester.write(param)
    tester.write(param)

if __name__ == '__main__':
    main()