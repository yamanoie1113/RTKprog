# coding:utf-8
from itertools import cycle
from time import sleep
import pigpio
import time
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Sensors import LogMgmt

pi = pigpio.pi()

class MotorTest():

    cycle = 0
    duty = 0
    log = LogMgmt.LogMgmt()


    def __init__(self):

        #self.mMotor = MotorMgmt()
        self.pi = pigpio.pi()
        #self.log.set_param("Motor_log")
        pass

        
    def set_param(self,sp,sv):

        
        if sv ==0:
            svduty = 6.825
        else:
            if sv > 0:
                svduty += sv*0.028
            else:
                svduty += sv*0.02375
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
        #value = ["sp", sp,"sv:",sv, "duty:",self.duty,"cycle:",self.cycle]
        #self.log.write(value)
                
                



    def run(self):
        
        #print('kiteruyo')
        self.pi.hardware_PWM(18, 50, self.cycle)
        up_flag = True
        self.pi.set_PWM_frequency(19,200)
        flog = 0
        self.duty = self.duty - 1
        #print(self.cycle,self.duty)
        try:

            while True:

                self.pi.set_PWM_dutycycle(19,self.duty)#36-76
        
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

        except KeyboardInterrupt:
                pass


    def stop(self):
        self.pi.set_mode(18, pigpio.INPUT)
        self.pi.set_mode(19, pigpio.INPUT)
        self.pi.stop()
        print('end')

def main():
    sp = input("スピード: ")
    sv = input("ステアリング: ")
    MotorTest.set_param(sp,sv)
    MotorTest.run
        
if __name__ == '__main__':
    main()

            

