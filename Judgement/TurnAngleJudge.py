import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')

import math
from Judgement import Judge
from Sensors import TurnAngleSensor as TASensor,PositionMgmt as PMgmt
from section import SectionMgmt2

class TurnAngleJudge(Judge.Judge):

    start_angle=0.0
    finish_angle=0.0
    baseline = 0.0


    last_angle = 0.0
    mx=0.0
    my=0.0

    angget = TASensor.TurnAngleSensor()


    def __init__(self):
        #旋回角度取得
        #sensehatからジャイロ取得


        #sectionからstatusを渡す位置を考える initかsetparamか
        #とりあえずダミーを設置する
        status = 0.0

        self.set_param(status)

        #tmp = angget.getvalue()
        #self.startangle = tmp['yaw'] + self.startangle
        #XYから値取得

        
        pget = PMgmt.PositionMgmt(0.0)
        positionXY = pget.getvalue()
        #mx,myに座標をセット
        self.mx = positionXY[0]
        self.my = positionXY[1]
        

    def judge(self):
        pass
    """

        if self.finish_angle >= self.start_angle :

            if self.pget.getvalue() >= self.finish_angle :
                return True

            else :
                return False

        else :

            if self.pget.getvalue() <= self.finish_angle :
                return True

            else :
                return False

    """

    """

    def judge(self):
        #X,Y座標を取得し、その値が基準値をこえていたらTrueを返す。それ以外はFalse
        #ここジャイロでやるからXY関係ない説ある?

        if self.finish_angle >= self.start_angle :

            if PMgmt.getvalue() >= self.finish_angle :
                return True

            else :
                return False

        else :

            if PMgmt.getvalue() <= self.finish_angle :
                return True

            else :
                return False
    """

    def set_param(self,status):
        self.start_angle = self.angget.getvalue()
        self.finish_angle = status

        self.finish_angle = self.start_angle + status

    def Test(self):
        print(self.mx,self.my)

#testrun
def main():
    testclass = TurnAngleJudge()
    testclass.Test()
    print(testclass.start_angle)

if __name__ == '__main__':
    main()