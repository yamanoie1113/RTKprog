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
    timelimit = 0
    time_master = 0
    startflag = True

    def __init__(self):
        #print("Timer_init")
        #タイマ初期化
        self.count2=0
        self.thread1 = threading.Thread(target=self.count)

        #タイマが機能停止する時間
        self.end_time = 50

        #self.thread2 = threading.Thread(target=self.getvalue)
        #print("end_Timer_init")

    def exec_thread(self):
        if self.startflag == True:
            print("thread_start")
            self.thread1.start()
            self.startflag = False

        else :
            self.update()
            

        



    def update(self):
        print("counter_reset")
        self.count2=0
        #time.sleep(1)


    def set_param(self,limit):
        self.timelimit = limit
        self.update()

    def count(self):

        #print("count")
        #カウントダウン
        try:
            print("count_loop")
            while True:#直接数字じゃなくて引数をいれるかも
                self.start = time.perf_counter()
                time.sleep(1)

                self.count2+=round(time.perf_counter() - self.start)
                self.time_master += 1
                print("limit=" + str(self.timelimit))
                print(self.time_master)
                
                """
                if self.count2 > self.timelimit:
                    #指定時間が終了したとき
                    #でもそれはジャッジでやるのでは？あれ？
                    return False
                """
                
                if self.time_master > self.end_time:
                    #制限時間経過後の終了処理
                    print("end")
                    return False
                

                    #print(self.count2)
                    #return self.count2


            #カウント終わり
            print("endcount")
            #タイマのリセットここでやってるけど変えるかも
        except KeyboardInterrupt:
            print("count_interrupt")


    def getvalue(self):

        #print("timer.getvalue")
        #print("return_value:",end="")
        #print(self.count2)
        return self.count2



def main():
    timer=Timer()
    #timer.update()
    #timer.set_i()
    timer.set_param(5)
    timer.thread1.start()
    timer.thread1.join()
    timer.set_param(10)



if __name__=="__main__":
    main()


