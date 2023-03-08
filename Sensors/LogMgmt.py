import datetime
#ログの内容を消去する
def clear(path):
    f = open(path,"w")
    f.close()

def write(path,position):
    f = open(path,"a")
    f.write(str(datetime.datetime.now()) + ':')
    f.write(str(position) + ',\n')