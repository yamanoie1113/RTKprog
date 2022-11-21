# coding:utf-8
from itertools import cycle
from time import sleep
#import pigpio
import time
#pi = pigpio.pi()

class MotorMgmt():


    def set_param(self,sp,sv):


        if sv ==0:
            svduty = 7.25
        else:
            if sv > 0:
                svduty = 7.25 + sv*0.0475
            else:
                svduty = 7.25 - sv*0.0475
        cycle = int((svduty * 1000000 / 100))

        if sp == 0:
            spduty = 78
        else:
            if sp >= 1:
                a2 = 76
                spduty = a2 - sp*0.4
            else:
                sp = sp *-1
                a2 = 80
                spduty = a2 + sp*0.38


        MotorMgmt.run(cycle,spduty)



    def run(cycle,duty):

        pi.hardware_PWM(18, 50, cycle)
        up_flag = True
        pi.set_PWM_frequency(19,200)
        flog = 0
        duty = duty - 1
        print(cycle,duty)
        try:

            while True:

                pi.set_PWM_dutycycle(19,duty)#36-76

                if up_flag == True:
                    if duty >= duty:
                        up_flag = False
                    else:
                        duty += 1
                else:
                    if duty <= duty:
                        up_flag = True
                    else:
                        duty -=1
                    if flog == 0:
                        duty = duty + 1
                        flog = 1
                    time.sleep(0.1)
                    break

        except KeyboardInterrupt:
                pass

        #pi.set_mode(PIN, pigpio.INPUT)
        #pi.stop()





