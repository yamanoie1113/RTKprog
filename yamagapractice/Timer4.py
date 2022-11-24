import time
import sys
import pathlib
import Timer4
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
#from Sensors import Sensor 

class Timer4():

    def __init__(self):

        self.count2=0

    def update(self):
        #self.count=0
        pass
        

    def getvalue(self):

        print("実行")
            
        for j in range(100):#直接数字じゃなくて引数をいれるかも
            self.start = time.perf_counter()
            time.sleep(1)
            
            self.count2+=round(time.perf_counter() - self.start)
            print("Timer3",self.count2)
            #return self.count2

            return self.count2


def main():
    timer=Timer4()
    #timer.update()
    #timer.set_i()
    timer.getvalue()

    pass

    
if __name__=="__main__":
    main()


    


