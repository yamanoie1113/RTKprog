import time
import sys
import pathlib
import Timer
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Sensors import Sensor 

class Timer(Sensor.Sensor):

    def update(self):
        #self.count=0
        self.count2=0

    def getvalue(self):

        print("perf_counter")
        for j in range(180):
            self.start = time.perf_counter()
            time.sleep(1)
            
            self.count2+=round(time.perf_counter() - self.start)
            
            if self.count2%10==0:
                print(self.count2,"秒経過")
                
            else:
                print(".")
            pass
        
        

def main():
    timer=Timer()
    timer.update()
    timer.getvalue()

    pass

    
if __name__=="__main__":
    main()


    


