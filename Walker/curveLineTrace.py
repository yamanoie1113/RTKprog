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


class VirtulLineTrace2(Run):

    sx=0
    sy=0
    fx=0
    fy=0
    nx=0
    ny=0
    basedistance=0
    mTarget=0
    mTargetSpeed=0
    mPFactor=0
    mIFactor=0
    mDFactor=0
    mLimit=100
    #?
    mPID.resetParam()

    def init(self):
        #?
        self.sx=mXPosition.getvalue()
        self.sy=mYPosition.getvalue()
