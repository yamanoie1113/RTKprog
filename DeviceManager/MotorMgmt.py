from itertools import cycle
from time import sleep
import pigpio
import time
pi = pigpio.pi()

class MotorMgmt:

        
    def set_param(a,b,c : float):

        duty = a
        freq = b
        if freq == 100:
            pin = 19
        else:
            pin = 18
        cycle = int((duty * 1000000 / 100))

        return pin,freq,cycle



    def run(self):
        pin,freq,cycle = MotorMgmt.set_param()

        while True:

            pi.hardware_PWM(pin, freq, cycle)