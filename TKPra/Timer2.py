import time
import sys
import pathlib
import threading

current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Sensors import Sensor

class Timer2(Sensor.Sensor):
    #timer2ｗちょこっと変更
    #countをスレッドで動かしてみてる

    #count2 = 0
    thread1 = None
    thread2 = None

    def __init__(self):
        print("init")
        self.count2=0
        self.thread1 = threading.Thread(target=self.count)
        self.thread1.start()
        self.thread2 = threading.Thread(target=self.getvalue)
        print("end_init")



    def update(self):
        #self.count=0
        pass

    def count(self):
        print("count")
        for j in range(50):#直接数字じゃなくて引数をいれるかも
            self.start = time.perf_counter()
            time.sleep(1)

            self.count2+=round(time.perf_counter() - self.start)
            print(self.count2)
            #sprint(self.count2)
            #return self.count2

        print("endcount")




    def getvalue(self):

        print("timer.getvalue")
        print("return_value:",end="")
        print(self.count2)
        return self.count2


"""
def main():
    timer=Timer2()
    #timer.update()
    #timer.set_i()
    rand = random.randint(0,10)
    time.sleep(rand)
    print("rand:",end="")
    print(rand)
    timer.thread2.start()

    pass


if __name__=="__main__":
    main()
"""

