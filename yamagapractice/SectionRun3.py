# coding:utf-8
from asyncio.windows_events import NULL
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
import Param
#from Sensors import MotorMgmt
#from Walker import Run
#from Walker import VirtualLineTrace
#from Walker import curveLineTrace
#from Judgement import DistanceJudge
#from Judgement import TurnAngleJudge



class SectionRun3:

    CURVE=0
    STRAIGHT=1
    DISTANCE=0
    ANGLE=1
    judgefirst=True
    walkerfirst=True
    mWalker=0
    mjudge=0
    deb=None
    param=Param.Param()
    #mMotorMgmt=MotorMgmt()

    def init(self):
        self.deb=None
        pass

    def run(self):#作成中
        
        #判定
        if self.judgefirst:#truekafalseか
            #self.mjudge.init()
            #if self.ajudge !=None: #ajudgeはどうすれば？
                #self.aJudge.init()
            #self.judgefirst= False
        #if self.mjudge.run():
            pass
            #return  True
        #走法
        if self.walkerfirst:
            #self.mWalker.init()
            self.walkerfirst=False
        #self.mWalker.run()
            
    def request_Walker(self,walker):

    #走法の生成依頼

        if walker==self.CURVE:
            #オブジェクト生成
            #self.mWalker=VirtualLineTrace()#今外すとエラーになりますわよ★
            print("curve")
        elif walker==self.STRAIGHT:
            #オブジェクト生成
            #self.mWalker=curveLineTrace()
            print("straight")
        
        #return self.mWalker

    def request_judge(self,judge):

        #判定の生成依頼

        if judge==self.DISTANCE:
            #オブジェクト生成
            #self.mJudge=DistanceJudge()
            print("judge")
        elif judge==self.ANGLE:
            #オブジェクト生成
            #self.mJudge=TurnAngleJudge()
            print("mjudghe")

        #return self.mJudge

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




def main():
    sec=SectionRun3()
    mnumber=1
    sec.set_param(mnumber)
    
    pass

if __name__=="__main__":
    main()