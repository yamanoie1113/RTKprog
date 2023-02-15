import time
import sys
import pathlib
#import Timer4
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
#from Sensors import Sensor from Judgement import TimeJudge2
class Timerset():

    def __init__(self):

        pass

    def update():
        state=False

        return state
        


    def getvaluetest(self,count):

        for i in range(0, count, 1):
            time.sleep(1)
            print(i, "秒経過")

        return i

    def getvalue(self,count):
        state=0
        for i in range(0, count, 1):
            #self.update()
            time.sleep(1)
            print(i, "秒経過")

    def newtime(self):

        t1 = time.time() 
        # 計測したい処理
        for i in range(1000000):
            i ** 10

        # 処理後の時刻
        t2 = time.time()
        # 経過時間を表示
        elapsed_time = t2-t1
        print(f"経過時間：{elapsed_time}")  

def main():
    timer=Timerset()
    #timer.update()
    #timer.set_i()
    #timer.getvalue()
    #timer.getvalue(10)
    timer.newtime()

    
if __name__=="__main__":
    main()


    


