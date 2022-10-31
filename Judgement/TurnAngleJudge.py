import Judge
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Sensors import TurnAngleSensor as TASensor,PositionMgmt as PMgmt

class TurnAngleJudge(Judge.Judge):

    startangle=0.0
    finishangle=0.03


    last_angle = 0.0
    mx=0.0
    my=0.0

    def __init__(self):
        #旋回角度取得
        #sensehatからジャイロ取得
        angget = TASensor.TurnAngleSensor()

        #ジャイロから旋回角度抽出
        tmp = angget.getvalue()
        self.startangle = tmp['yaw'] + self.startangle
        #XYから値取得

        """
        pget = PMgmt.PositionMgmt(0.0)
        positionXY = pget.getvalue()
        #mx,myに座標をセット
        self.mx = positionXY[0]
        self.my = positionXY[1]
        """


    def judge(self):
        #X,Y座標を取得し、その値が基準値をこえていたらTrueを返す。それ以外はFalse
        #ここジャイロでやるからXY関係ない説ある?

        if self.finishangle >= self.startangle :

            if PMgmt.getvalue() >= self.finishangle :
                return True

            else :
                return False

        else :

            if PMgmt.getvalue() <= self.finishangle :
                return True

            else :
                return False

    def set_param(self,judgevalue):
            self.finishangle = self.startangle + judgevalue




    def Test(self):
        print(self.mx,self.my)

#testrun
def main():
    testclass = TurnAngleJudge()
    testclass.Test()
    print(testclass.startangle)

if __name__ == '__main__':
    main()