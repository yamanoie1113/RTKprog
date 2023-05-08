import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')

import math
from Judgement import Judge
from Sensors import TurnAngleSensor as TASensor,PositionMgmt as PMgmt

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
        #status = float(input("input_finish_angle?"))

        #self.set_param(status)

        self.start_angle = self.angget.getvalue()
        
        #XYから値取得

        
        self.pget = PMgmt.PositionMgmt()
        #positionXY = pget.getvalue()
        
        #mx,myに座標をセット
        #self.mx = positionXY[0]
        #self.my = positionXY[1]
        
        #test_position
        self.mx = 1
        self.my = 0
        

    def judge(self,XYpos):
        print("ANGLE_judge")
        x = XYpos[0]
        y = XYpos[1]
        if self.finish_angle >= self.start_angle :

            if self.angget.getvalue() >= self.finish_angle :
                return True

            else :
                return False

        else :

            if self.angget.getvalue() <= self.finish_angle :
                return False

            else :
                return True
    """
    def judge(self):
        #X,Y座標を取得し、その値が基準値をこえていたらTrueを返す。それ以外はFalse
        #ここジャイロでやるからXY関係ない説ある?


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

    #目標地点との角度の計算 return float
    def CalcAng(goal_x,goal_y):
        #現在地取得
        start_x = 0.0
        start_y = 0.0



        x = (goal_x - start_x)
        y = (goal_y - start_y)

        r = math.atan2(y,x)

        if r < 0 :
            r = r + 2 * math.pi

        angle = math.floor(r * 360 / (2 * math.pi))
        return angle


    def set_param(self,status):
        self.start_angle = self.angget.getvalue()
        print(self.start_angle)
        #終了角度をセクションから受け取る場合
        self.finish_angle = status

        #旋回したい角度をセクションから受け取る場合
        #self.finish_angle = self.start_angle + status


#testrun
def main():
    testclass = TurnAngleJudge()
    judge_val = False
    
    while judge_val == False:
        judge_val = testclass.judge()
        print(testclass.angget.getvalue(),":",testclass.finish_angle)

    print("-------------------------END-------------------------------")

if __name__ == '__main__':
    main()