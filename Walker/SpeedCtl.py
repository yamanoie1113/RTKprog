from audioop import findmax
from math import fabs
from re import M
import syslog
from statistics import mode
from Walker.PID import PID



class SpeedCtl():

    def __init__(self):
        self.mMode_flag(True)
        self.mBreake_flag
        self.mPID=PID()
        #self.debug(false)
        pass



    def set_target_speed(self,speed): #目標スピードを設定

        self.prev_speed=0   #予測スピード？
        self.bai=1.0


        self.spd=findmax(fabs(self.mTargetSpeed),fabs(speed))

        if self.mTargetSpeed!=speed:
                self.mPID.reset_param()

                if self.mTargetSpeed*speed<0:
                    self.bai=0.6

                if fabs(self.mTargetSpeed)>fabs(speed):
                    self.bai=1.2
                    
        self.mTargetSpeed=speed
        self.mPID.set_target(speed)
        self.mPID.set_Kp(1.1*self.bai)
        self.mPID.set_limit(15*self.bai+1)


    def get_pwm(self): #pwm取得

        #直接制御
        #if(!mMotde_flag)
        if not self.mMode_flag:
            self.mForward=self.mTargetSpeed

            return self.mTargetSpeed

        #停止モード
        if self.mBreake_flag:
            self.mForward=0
            return 0


        #if mBreake_flag

        #self.mForward=0

        self.maxFwd=100
        
        #最大値を超えたときの処理
        if self.mForward>self.maxFwd:
            syslog.syslog(syslog.LOG_NOTICE,"over speed")
            self.mForward=self.maxFwd

        #最小値を超えたときの処理
        if self.mForward<-self.maxFwd:
            syslog.syslog(syslog.LOG_NOTICE,"over speed")
            self.mForward=self.maxFwd

        self.mCnt=0      

        return self.mForward

    def reset_param(self):#パラメーターをリセット

        self.mForward=0
        self.mCnt=0
        self.mPID.reset_param()
        


    def set_mode(self,mode):#???

        self.mMode_flag=mode
        

        

    def set_break(self,brk):#ブレイク

        self.mBreake_flag=brk

        


    def get_current_fwd(self):#現在の前進量を取得

        return self.mForward


    def get_current_speed(self):#現在のスピードを取得

        return self.mCurrentSpeed

