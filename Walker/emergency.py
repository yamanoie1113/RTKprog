# coding:utf-8
from itertools import cycle
from time import sleep
import pigpio
import time
pi = pigpio.pi()

class emergency():

    def emergency():
        c= 0
        while True:
            
            pi.set_mode(20,pigpio.INPUT)
    
            pi.set_pull_up_down(20, pigpio.PUD_UP)
            print(pi.read(20))
            time.sleep(0.1)
            c += 1
            if c ==20:
                print ('end')
                break
            
def main():
    #print (1)
    e = emergency()
    emergency.emergency()
        
if __name__ == '__main__':
    main()
            
        

            

