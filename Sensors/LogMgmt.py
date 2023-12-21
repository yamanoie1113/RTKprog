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
        f = open(self.dir + filename + "__" + now.strftime('%Y%m%d_%H%M%S'),"a")
        f.write(str(datetime.datetime.now()) + ':::')
        f.write(str(param) + ',\n')


def main():
    filename = "LogTest"
    test_val = "testtttt"
    i = 0

    tester = LogMgmt()

    while i<5:
        tester.write(filename,i)
        i+=1

if __name__ == '__main__':
    main()