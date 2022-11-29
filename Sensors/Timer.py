import time
import sys
import pathlib
import threading

current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Sensors import Sensor

class Timer(Sensor.Sensor):
    #timer2ｗちょこっと変更
    #countをスレッドで動かしてみてる

    #count2 = 0
    thread1 = None
    thread2 = None
    timelimit = 0
    sumtime = 0
    startflag = True

    def __init__(self):
        print("Timer_init")
        #タイマ初期化
        self.count2=0
        self.thread1 = threading.Thread(target=self.count)


        #self.thread2 = threading.Thread(target=self.getvalue)
        print("end_Timer_init")

    def exec_thread(self):
        if self.startflag == True:
            print("thread_start")
            self.thread1.start()
            self.startflag = False

        else :
            print("thread_run")
            self.thread1.run()



    def update(self):
        self.count=0
        pass

    def set_param(self,limit):
        self.timelimit = limit

    def count(self):

        print("count")
        self.update()
        #カウントダウン

        for j in range(self.timelimit):#直接数字じゃなくて引数をいれるかも
            self.start = time.perf_counter()
            time.sleep(1)

            self.count2+=round(time.perf_counter() - self.start)
            self.sumtime += 1
            print(self.count2)
            #sprint(self.count2)
            #return self.count2

        #カウント終わり
        print("endcount")
        self.count2 = 0
        return
        #タイマのリセットここでやってるけど変えるかも

            




    def getvalue(self):

        print("timer.getvalue")
        print("return_value:",end="")
        print(self.count2)
        return self.count2


"""
def main():
    timer=Timer()
    #timer.update()
    #timer.set_i()
    timer.set_param(5)
    timer.thread1.start()
    timer.thread1.join()
    timer.set_param(10)   
    timer.thread3.start() 

    pass


if __name__=="__main__":
    main()
"""

