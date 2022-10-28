# coding:utf-8
import os
import sys
import math
import pathlib
from cmath import cos, sin, sqrt
from math import fabs
from Walker.Run import Run
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Sensors import PositionMgmt
from section import SectionMgmt


class cuvreLineTrace2(Run):

     
    startx = 0
    starty = 0
    goalx = 0
    goaly = 0


    def set_param(PositionMgmt):
        
        PositionMgmt.getvalue(param)

    def set_run(self,):

        SectionMgmt
        z = (d-b)/(c-a)
        x=(y+z*a-b)/z
        startz = z
        position = True
        while position == False:
            VirtualLineTrace.set_param(param)
            gz = (d-parab)/(c-paraa)
            raz = (z - gz)/(1 + z*gz)
            math.degrees(math.atan(raz))