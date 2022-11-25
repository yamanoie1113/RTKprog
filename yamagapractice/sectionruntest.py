# coding:utf-8
from asyncio.windows_events import NULL
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
import Param
#from Sensors import MotorMgmt
#from Walker import Run
from Walker import VirtualLineTrace
from Walker import curveLineTrace
import Timer2
import Timer3
import Timer4
import Timer_judge
from Judgement import DistanceJudge
from Judgement import TurnAngleJudge



class sectionruntest:

    CURVE=1
    STRAIGHT=1
    DISTANCE=0
    ANGLE=1
    judgefirst=True
    walkerfirst=True
    mWalker=0
    mjudge=0
    deb=None
    param=Param.Param()
    number1=0
    number2=0
    cnt=0
    N1=0
    N2=0
    judgepoint=0
    timejudge2=Timer2.Timer2()
    timejudge3=Timer3.Timer3()
    timejudge4=Timer4.Timer4()
    count=Timer_judge.Timer_Judge()
    state=True
    walkerfirst=True
    
    #mMotorMgmt=MotorMgmt()

    def init(self):
        self.param[self.timejudge3,self.timejudge4]
        self.count[10,10]

    def run(self):#判定２つ、走法２つ、秒数、パラメータ
        #早く仮想ラインつくってよおおおおおおおお
            while self.walkerfirst:
                if self.param!=None:#walkerの配列がなくなったらおーわり★
                    self.state=self.count(10)#timejudgeにカウント数をぶち送る
                    self.param[self.timejudge3].getvalue()
                    
                    #stateの受け取り方がわからない　判定でstateを送る関数作ると思う
                    if self.state==False:
                        self.param[self.timejudge4].getvalue()
                    #stateを戻す
                        self.state=True
                else:
                    self.walkerfirst=False

        #self.mWalker.run()
            
    


def main():
    sec=sectionruntest()
    mnumber=1
    sec.set_param(mnumber)
    
    pass

if __name__=="__main__":
    main()