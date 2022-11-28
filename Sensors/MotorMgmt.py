# coding:utf-8
from itertools import cycle
from time import sleep
#import pigpio
import time
#pi = pigpio.pi()

class MotorMgmt():

    cycle = 0
    duty = 0


    def __init__(self):

        self.mMotor = MotorMgmt()
        #self.pi = pigpio.pi()
        pass

        
    def set_param(self,sp,sv):

        
        if sv ==0:
            svduty = 7.25
        else:
            if sv > 0:
                svduty = 7.25 + sv*0.0475
            else:
                svduty = 7.25 - sv*0.0475
        self.cycle = int((svduty * 1000000 / 100))        
        
        if sp == 0:
            self.duty = 78
        else:
            if sp >= 0:
                a2 = 76
                self.duty = a2 - sp*0.4
            else:
                sp = sp *-1
                a2 = 80
                self.duty = a2 + sp*0.38
                



    def run(self):
        
        #self.pi.hardware_PWM(18, 50, self.cycle)
        up_flag = True
        #self.pi.set_PWM_frequency(19,200)
        flog = 0
        self.duty = self.duty - 1
        print(self.cycle,self.duty)
        try:

            while True:

                #self.pi.set_PWM_dutycycle(19,duty)#36-76
        
                if up_flag == True:
                    if self.duty >= self.duty:
                        self.up_flag = False
                    else:
                        self.duty += 1
                else:
                    if self.duty <= self.duty:
                        up_flag = True
                    else:
                        self.duty -=1
                    if flog == 0:
                        self.duty = self.duty + 1
                        flog = 1
                    time.sleep(0.1)
                    break

        except KeybordInterrupt:
                pass

        #self.pi.set_mode(PIN, pigpio.INPUT)
        #self.pi.stop()

def main():
    MotorMgmt.set_param(10,100)
        
if __name__ == '__main__':
    main()

            




