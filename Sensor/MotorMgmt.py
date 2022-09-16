from time import sleep
import pigpio
import time

class MotorMgmt:
    def __init__(self):
        
        pi = pigpio.pi()
        pi.set_mode(17, pigpio.OUTPUT)
        pi.set_mode(22, pigpio.OUTPUT)
        #PWMパラメータ
        pwm_pin1 = 18 #PWM出力ピンを指
        duty = 0 #デューティー比を%で指定
        #freq = 100 #PWM周波数をHzで指定
        up_flag = True
        #IN1、IN2の制御信号
        pi.write(17, 0)
        pi.write(22, 1)





    def set_param(self):
        pi = pigpio.pi()
        pi.set_mode(17, pigpio.OUTPUT)
        pi.set_mode(22, pigpio.OUTPUT)
        #PWMパラメータ
        pwm_pin1 = 18 #PWM出力ピンを指
        duty = 0 #デューティー比を%で指定
        #freq = 100 #PWM周波数をHzで指定
        up_flag = True
        #IN1、IN2の制御信号
        pi.write(17, 0)
        pi.write(22, 1)
        while True:
    
        #デューティサイクル計算
            cnv_dutycycle = int((duty * 1000000 / 100))
        #PWMを出力
            #pi.hardware_PWM(pwm_pin1, freq, cnv_dutycycle)
        #dutyを変更
            if up_flag == True:
                if duty == 100:
                    up_flag = False
                else:
                    duty += 1
            else:
                if duty == 0:
                    up_flag = True
                else:
                    duty -=1
    
            time.sleep(0.05)

            pass


