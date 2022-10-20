# coding:utf-8
import os
import sys
import pathlib
from cmath import cos, sin, sqrt
from math import fabs
from Walker.Run import Run
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Sensors import PositionMgmt
from section import SectionMgmt


class VirtualLineTrace(Run):

    
    startx = 0
    starty = 0
    goalx = 0
    goaly = 0


    def set_param(self,PositionMgmt):
        
        PositionMgmt.getvalue(para)

    def set_run(self,):

        SectionMgmt
        z = (d-b)/(c-a)
        x=(y+za-b)/z


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

    
