from math import fabs
from msilib import MSIDBOPEN_DIRECT
from Walker.Run import Run
from Walker.PID import PID



class VirtualLineTrace(Run):
    def __init__(self):

        self.cx=0
        self.cy=0
        self.ax=0
        self.ay=0
        self.basedistance=0
        self.currentdistance=0
        self.mTarget=0
        self.mTargetSpeed=0
        self.mPFactor=0
        self.mIFactor=0
        self.mDFactor=0
        self.mCurve
        self.mAngleKp
        self.mLimit=100
        self.round
        self.mround
        self.uflag
        self.mBias
        self.co=0
        self.si=0
        
        




    def set_param(self,speed,kp,ki,kd,anglrTarget,angleKp):
        self.mTargetSpeed=speed

        self.mPFactor=kp
        self.mIFactor=ki
        self.mDFactor=kd

        self.mPID.setTarget(fabs(self.mround))
        self.mPID.set_Kpi(self.mPFactor,self.mIFactor,self.mDFactor)

        self.mCurve=anglrTarget
        self.mAngleKp=angleKp

        self.currentdistance=calc_distance()
        self.mPID.reset_param()
    #パラメータの設定
        


    def run(self):
        

        #走らせる
        pass
    
    def reset_param(self):
        
        #パラメータの初期化

        pass

    def calc_distance(self):

        self.buf[100]

        
