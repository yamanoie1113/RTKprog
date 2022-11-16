import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')

from TKPra import Timer2

class TKTimejudge():
    #白井の班参考にして作成
    #まだちゃんと動作してないっぽい

    time=0.0
    timelimit = 0.0
    timer = Timer2.Timer2()
    def __init__(self):
        self.set_param(10)

    def judge(self):
        time = self.timer.getvalue()
        print("gettime:",end="")
        print(time)

        if(time >= self.timelimit):
            return True

        else :
            return False


    def set_param(self,limit):
        self.timelimit = limit
        print("limit:",end="")
        print(limit)


def main():
    test = TKTimejudge()
    test.judge()


if __name__=="__main__":
     main()
