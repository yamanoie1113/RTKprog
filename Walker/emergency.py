# coding:utf-8
from itertools import cycle
from time import sleep
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Sensors import MotorMgmt
import pigpio
import time
pi = pigpio.pi()

class emergency():

    def emergency():
        c= 0
        MM = MotorMgmt.MotorMgmt()
        while True:
            
            pi.set_mode(20,pigpio.INPUT)
    
            pi.set_pull_up_down(20, pigpio.PUD_UP)
            print(pi.read(20))
            p = pi.read(20)
            time.sleep(0.1)
            c += 1
            if p == 1:
                MM.set_param(0,0)
            if c ==20:
                print ('end')
                break
            
def main():
    #print (1)
    e = emergency()
    emergency.emergency()
        
if __name__ == '__main__':
    main()
            
        

            

