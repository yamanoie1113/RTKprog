import datetime
import sys
import pathlib

dir = pathlib.Path(__file__).resolve().parent
dir = (str(dir) + '/../LOG/')

#ログの内容を消去する
def clear(filename):
    f = open(dir + filename,"w")
    f.close()

def write(filename,param):
    f = open(dir + filename,"a")
    f.write(str(datetime.datetime.now()) + ':')
    f.write(str(param) + ',\n')