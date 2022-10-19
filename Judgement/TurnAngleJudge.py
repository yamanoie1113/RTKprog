from pdb import pm
from re import X
from turtle import position
import Judge
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Sensors import PositionMgmt as PMgmt

class TurnAngleJudge(Judge.Judge):

    startangle=0.0
    finishangle=0.0
    mx=0.0
    my=0.0
    
    def __init__(self):
        #XYから値取得 selfを渡しているが、そこは要検証
        pget = PMgmt.PositionMgmt(0.0)
        positionXY = pget.getvalue()
        #mx,myに座標をセット
        self.mx = positionXY[0]
        self.my = positionXY[1]


    def judge(self):
        #X,Y座標を取得し、その値が基準値をこえていたらTrueを返す。それ以外はFalse
        
        if self.finishangle >= self.startangle :
            if PMgmt.getvalue() >= self.finishangle :
                return True
            else :
                return False

        else : 
            if PMgmt.getvalue() >= self.finishangle :
                return True
            
            else :
                return False

    def set_param(self,judgevalue):
        self.finishangle =judgevalue

    def Test(self):
        print(self.mx,self.my)


#testrun

def main():
    testclass = TurnAngleJudge()
    testclass.Test()

if __name__ == '__main__':
    main()