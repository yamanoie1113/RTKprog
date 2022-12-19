import sys
import pathlib
import time
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
import threading

from Sensors import Timer

class TimeJudge():
    #白井の班参考にして作成
    #タイマ値はちゃんと取得できてるっぽい
    #main関数でn秒経過後にタイマ値取得してる。取得しているのは"経過した"秒数？

    mtime=0.0
    timelimit = 0.0
    timer = Timer.Timer()
    def __init__(self):
        print("judge_init")
        #self.set_param()
        print("end_judge_init")

    def judge(self,limit):
        print("judge_enter￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥")
        #time.sleep(1)
        mtime = 0
        self.timelimit = limit
        print("timelimit:",end="")
        print(self.timelimit)
        self.timer.set_param(limit)
        print("tjudge_flag_reset")
        #print(mtime)
        print(self.timelimit)
        print(self.timer.getvalue())
        self.timer.exec_thread()
        
        flag =True
        #スレッドでカウントを開始する。

        while flag :
            print("--------------------------------------------------------------")
            
            mtime = self.timer.getvalue()

            print("gettime:",end="")
            print(mtime)

            if mtime >= self.timelimit :
                print("timejudge_return_False")
                #time.sleep(1)
                #flag = False
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
    test = TimeJudge()
        
    #タイマのカウント待ち
    #print("wait")        
    tm = 5
    hnt = True
    hnt=test.judge(int(tm))

    if hnt == False:
        hnt=test.judge(10)

    if hnt == False:
        hnt=test.judge(15)

    
    
    if hnt == False:
        print("end")



if __name__=="__main__":
     main()