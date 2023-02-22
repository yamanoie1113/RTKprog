import numpy as np
import math

import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Judgement import Judge

from Sensors import PositionMgmt as PMgmt,TurnAngleSensor as TASensor

class PointJudge(Judge.Judge):

    start_x=0.0    #X座標系　オブジェクト
    start_y=0.0   #Y座標系　オブジェクト

    def __init__(self):
        self.pget = PMgmt.PositionMgmt()

    def judge():
        if True:
            return True

        else :
            return False

    def set_param():

        pass

    def getPosition(self):
        positionXY = self.pget.getvalue()

        #mx ,myに座標をセット
        self.start_x = positionXY[0]
        self.start_y = positionXY[1]