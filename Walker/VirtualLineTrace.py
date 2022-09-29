from msilib import MSIDBOPEN_DIRECT
from Walker.SimpleRun import SimpleRun
from Walker.PID import PID


class VirtualLineTrace(SimpleRun):
    def __init__(self):
        
        self.cx=0
        self.cy=0
        self.ax=0
        self.ay=0
        self.basedistance=0
        self.currentdistance=0
        self.mPFactor=0
        self.mIFactor=0
        self.mDFactor=0
        self.mLimit=100
        self.co=0
        self.si=0


    def set_param(self,speed,kp,ki,kd,angleTarget,angleKp):
        self.mTargetSpeed=speed
        self.mPFactor=kp
        self.mIFactor=ki
        self.mDFactor=kd
        self.mPID.set_Kp(self.mPFactor)
        self.mPID.set_ki(self.mIFactor)
        self.mPID.set_kd(self.mDFactor)

        self.mCurve=angleTarget
        self.mAnglekp=angleKp

        


        

    def reset_param(self):
        
        pass

    def run(self):

        pass
    

        
