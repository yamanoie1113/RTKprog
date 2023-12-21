import datetime
import sys
import pathlib
import csv



class LogMgmt():

    dir = pathlib.Path(__file__).resolve().parent
    dir = (str(dir) + '/../LOG/')


    #ログの内容を消去する
    def clear(self,filename):
        f = open(self.dir + filename,"w")
        f.close()

    def write(self,filename,param):
        now = datetime.datetime.now()
        
        with open(self.dir + filename + "__" + now.strftime('%Y%m%d_%H%M%S'),"a") as f:
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
    param = [1,1]
    tester = LogMgmt()
    tester.write(filename,param)
    tester.write(filename,param)

if __name__ == '__main__':
    main()