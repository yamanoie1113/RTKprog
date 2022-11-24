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
from Judgement import TimeJudge
from Judgement import DistanceJudge
from Judgement import TurnAngleJudge



class SectionRun3:

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
    timejudge=TimeJudge.TimeJudge()
    state=True
    #mMotorMgmt=MotorMgmt()

    def init(self):
        self.deb=None
        pass

    def run(self,mjudge,mwalker,count,param):#判定２つ、走法２つ、秒数、パラメータ
        #早く仮想ラインつくってよおおおおおおおお
        while self.judgefirst:#trueかfalseか
            
            #ここで時間の判定を呼び出す
            #180秒経過したら強制的にbreakさせたい←それってステージ管理かな？
            #self.timejudge.run(self.state)
            #if self.state==true:
            #break

            if self.judgepoint==0:
                mjudge[self.judgepoint].run()#距離判定
            else:
                mjudge[self.judgepoint].run()#旋回角度判定
                self.judgepoint=0

            self.walkerfirst=True

        #走法
            while self.walkerfirst:
                if param[self.number1][self.N1]!=None:#walkerの配列がなくなったらおーわり★
                    self.state=self.timejudge.judge(count[self.cnt])#timejudgeにカウント数をぶち送る
                    mwalker[self.number1].run(param[self.number1][self.N1])#走法にGo(曲線)
                    self.cnt+=1
                    self.N1+=1
                    self.N2+=1
                    #stateの受け取り方がわからない　判定でstateを送る関数作ると思う
                    if self.state==False:
                        mwalker[self.number2].run(param[self.number2][self.N2],count[self.cnt])#走法にGo(直線)
                    #stateを戻す
                        self.state=True
                else:
                    self.walkerfirst=False
                    self.judgefirst=False#これでwhileを終わらせてしまう

        #self.mWalker.run()
            
    def request_Walker(self,walker):

    #走法の生成依頼

        if walker==self.CURVE:
            #オブジェクト生成
            self.mWalker=VirtualLineTrace()#今外すとエラーになりますわよ★
            #self.mWalker=0
            print("curve")

        if walker==self.STRAIGHT:
            #オブジェクト生成
            self.mWalker=curveLineTrace()
            #self.mWalker=2
            print("straight")
        
        return self.mWalker

    def request_judge(self,judge):

        #判定の生成依頼

        if judge==self.DISTANCE:
            #オブジェクト生成
            self.mJudge=DistanceJudge()
            self.mjudge-0
            print("judge")
        if judge==self.ANGLE:
            #オブジェクト生成
            self.mJudge=TurnAngleJudge()
            self.mjudge=1
            print("mjudghe")

        return self.mjudge

    def set_param(self,mnumber):#パラメータ設定
        #曲線
        if mnumber==0:
            self.prm=self.param.Curve_set_param()
            #[前進量、旋回量、P,I,D]
            print("cuevever",self.prm)
            #(ここで値を設定すると思っているs)
        elif mnumber==1:
        #直線
            self.prm=self.param.Straight_set_param()
            #[前進量、P,I,D]
            print("straight",self.deb)
        
        return self.prm

    def count_set_param(self):

        self.cnt=self.param.count_set_param()

        return self.cnt



def main():
    sec=SectionRun3()
    mnumber=1
    sec.set_param(mnumber)
    
    pass

if __name__=="__main__":
    main()