from time import sleep
import pigpio
import time

class MotorMgmt:

    def __init__(freq):
        
        pi = pigpio.pi()
        #PWMパラメータ
        pwm_pin1 = 19 #PWM出力ピンを指定
        pwm_pin2 = 18 #PWM出力ピンを指定
        duty1 = 9#デューティー比を%で指定　スピードモーター
        duty2 = 8#デューティー比を%で指定　サーボモーター
        freq = 0 #PWM周波数をHzで指定
        pwm = float(freq)
        up_flag = True
        #IN1、IN2の制御信号
        cnv_dutycycle1 = int((duty1 * 1000000 / 100))
        cnv_dutycycle2 = int((duty2 * 1000000 / 100))

        pi.hardware_PWM(pwm_pin1, pwm, cnv_dutycycle1)
        pi.hardware_PWM(pwm_pin2, pwm, cnv_dutycycle2)





    def set_param(freq,self):
        pi = pigpio.pi()
        #PWMパラメータ
        pwm_pin1 = 19 #PWM出力ピンを指定
        pwm_pin2 = 18 #PWM出力ピンを指定
        duty = 0 #デューティー比を%で指定
        pwm = float(freq)
        up_flag = True
        #IN1、IN2の制御信号
        pi.write(17, 0)
        pi.write(22, 1)
        while True:
    
        #デューティサイクル計算
            cnv_dutycycle = int((duty * 1000000 / 100))
        #PWMを出力
            pi.hardware_PWM(pwm_pin1, pwm, cnv_dutycycle)
            pi.hardware_PWM(pwm_pin2, pwm, cnv_dutycycle)
        #dutyを変更

            self.MAX_F=100
            self.MAX_T=100

          #限界値設定

            if self.mFoward > self.MAX_F:

               self.mFoward=100

            if self.mForward < -self.MAX_F:

               self.mForward=-100


            if self.mTurn > self.MAX_T:

               self.mTurn=100

            if self.mTurn < -self.MAX_T:

               self.mTurn=-100

            return self.mForward,self.mTurn
           

        


            




