from itertools import cycle
from time import sleep
import pigpio
import time
pi = pigpio.pi()

class MotorMgmt:

        
    def set_param(a,b,c : float):

        duty = a
        freq = b
        cycle = c


        return duty,freq,cycle



    def run():
        duty,freq,cycle = MotorMgmt.set_param()
        pin1 = 19 #スピード
        pin2 = 18 #サーボ

        while True:
            pi.hardware_PWM(pin1, freq, cycle)
            pi.hardware_PWM(pin2, freq, cycle)




            




