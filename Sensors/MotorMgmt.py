from itertools import cycle
from time import sleep
import pigpio
import time
pi = pigpio.pi()

class MotorMgmt:

        
    def set_param(pin,pwm,freq,duty : float):

        if pin == 18:
            freq = 50
            if pwm ==0:
                duty = 7.25
            else:
                if pwm > 0:
                    duty = 7.25 + pwm*0.0475
                else:
                    duty = 7.25 - pwm*0.0475        
        else:
            freq = 200
            if pwm == 0:
                duty == 78
            else:
                if pwm >= 0:
                    a2 = 76
                    duty = a2 - pwm*0.4
                else:
                    pwm = pwm *-1
                    a2 = 80
                    duty = a2 + pwm*0.38
                
        cycle = int((duty * 1000000 / 100))

        return pin,duty,freq,cycle



    def run(self):
        pin,duty,freq,cycle = MotorMgmt.set_param()
        
        if pin == 18:
            pi.hardware_PWM(pin, freq, cycle)
        else:
            up_flag = True
            pi.set_PWM_frequency(pin,freq)
            flog = 0
            duty = duty - 1
            try:

                while True:

                    pi.set_PWM_dutycycle(pin,duty)#36-76
        
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

            except KeybordInterrupt:
                pass

            pi.set_mode(PIN, pigpio.INPUT)
            pi.stop()

            




