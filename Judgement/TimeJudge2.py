import sys
import pathlib
import time
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
import threading

from Sensors import Timer2

class TimeJudge2():
    #白井の班参考にして作成
    #タイマ値はちゃんと取得できてるっぽい
    #main関数でn秒経過後にタイマ値取得してる。取得しているのは"経過した"秒数？

    time=0.0
    timelimit = 0.0
    timer = Timer2.Timer2()
    def __init__(self):
        print("judge_init")
        #self.set_param()
        print("end_judge_init")

    def judge(self,limit):

        self.timelimit = limit
        print("timelimit:",end="")
        print(self.timelimit)
        self.timer.set_param(limit)
        self.timer.thread1.start()#スレッドでカウントを開始する。

        while True :
            print("_________________________________")
            time = self.timer.getvalue()

            print("gettime:",end="")
            print(time)

            if time > self.timelimit-1 :
                print("timejudge_return_False")
                return False
        """
            else :
                print("timejudge_return_FALSE")
                return False
        """


    def set_param(self,limit):
        #ここで時間を設定できるようにしなければならないけどまだ
        self.timelimit = limit
        print("limit:",end="")
        print(limit)


    #テスト用関数 10秒ごとにTrueとFalseを交互に返す
    def test(self):
        time = self.timer.getvalue()
        print("gettime:",end="")
        tmp = time /10
        testval = int(tmp % 2)
        print("testval:",end="")
        print(testval)

        if testval == 0 :
            print("timejudge_return_False")
            return False

        else :
            print("timejudge_return_True")
            return True




def main():
    test = TimeJudge2()
    #タイマのカウント待ち
    tm = input()
    test.set_param(int(tm))
    time.sleep(15)
    test.test()


if __name__=="__main__":
    main()