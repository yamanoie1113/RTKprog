from cmath import cos, sin, sqrt
from math import fabs
from Walker.Run import Run


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
        self.M_PI=3.14159265358979323846

        #生成
        #mXPosition=
        #mYPosition=
        #mTurnAngle=
        self.cx=mXPosition.get_value()-self.mround*sin((mTurnAngle.get_value()/180)*self.M_PI)
        self.cy=mYPosition.get_value()+self.mround*cos((mTurnAngle.get_value()/180)*self.M_PI)
        self.buf[100]

    def set_param(self,speed,kp,ki,kd,angleTarget,angleKp):
        self.mTargetSpeed=speed

        self.mPFactor=kp
        self.mIFactor=ki
        self.mDFactor=kd

        mPID.set_target(fabs(self.mround))

        mPID.set_Kpid(self.mPFactor,self.mIFactor,self.mDFactor)

        self.mCurve=angleTarget
        self.mAngleKp=angleKp

        self.currentdistance=calc_distance()

        mPID.reset_param()

    def set_round(self,round):
        self.mround=round


    def set_center_position(self,centerx,centery):
        self.cx=centerx
        self.cy=centery

    def set_base_distance(self):
        self.ax=mXPosition.get_value()
        self.ay=mYPosition.get_value()

        self.basedistance=calc_distance()

    def calc_distance(self):
        self.buf[100]
        if self.mTargetSpeed<0:
            return sqrt((self.ax-self.co-self.cx)*(self.ax+self.co-self.cx)+(self.ay-self.si-self.cy)*(self.ay-self.si-self.cy))
        else:
            return sqrt((self.ax+self.co-self.cx)*(self.ax+self.co-self.cx)+(self.ay+self.si-self.cy)*(self.ay+self.si-self.cy))
    

    def calc_turn(self):
        self.val1_turn=mPID.get_operation(self.basedistance)
        self.set_bias(-self.mForward*(1-self.mCurve)/(1+self.mCurve)*self.mAngleKp)
        self.turn=self.val1_turn+self.mBias
        return self.turn

    def set_limit(self,limit):
        self.mLimit=limit
        mPID.set_Limit(limit)


    def run(self):
        self.co=7*cos((mTurnAngle.get_value()/180)*self.M_PI)
        self.si=7*sin((mTurnAngle.get_value()/180)*self.M_PI)

        set_base_distance()

        if self.mTargetSpeed>0:
            if self.mround<0:
                self.mTurn=-(self.calc_turn())
            else:
                self.mTurn=(self.calc_turn())
        else:
            if self.mround<0:
                self.mTurn=(self.calc_turn())
            else:
                self.mTurn=-(self.calc_turn())

        Run.set_comondV(self.mForward,self.mTurn)
        Run.run()

    


    def set_bias(self,curve):
        self.mBias=curve

    
