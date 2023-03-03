# coding:utf-8
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from section import Param
#from Sensors import MotorMgmt
#from Walker import Run
from Walker import VirtualLineTrace
from Walker import curveLineTrace
from Judgement import TimeJudge
from Judgement import DistanceJudge
from Judgement import TurnAngleJudge



class SectionRun:

    CURVE=0
    STRAIGHT=1
    DISTANCE=0
    ANGLE=1
    judgefirst=True
    mWalker=0
    mjudge=0
    deb=None
    param=Param.Param()
    number1=0
    number2=1
    countnum=0
    N1=0
    N2=0
    judgepoint=0
    timejudge=TimeJudge.TimeJudge()
    state=True
    counter=0
    #mMotorMgmt=MotorMgmt()

    def init(self):
        self.deb=None
        pass

    def run(self,mjudge,mwalker,counter,param):#判定２つ、走法２つ、秒数、パラメータ
        #早く仮想ラインつくってよおおおおおおおお
        while self.judgefirst:#trueかfalseか
            
                
            #ここで時間の判定を呼び出す
            
            if self.judgepoint==0:
                mjudge[self.judgepoint].judge()#距離判定
                self.judgepoint+=1
            else:
                mjudge[self.judgepoint].judge()#旋回角度判定
                self.judgepoint-=1
            

        #走法
            #while self.walkerfirst:
            if param[self.number1][self.N1]!=999:#walkerの配列がなくなったら終了
                self.state=self.timejudge.judge(counter[self.countnum])#timejudgeにカウント数を送る
                mwalker[self.number1].left_run(param[self.number1][self.N1])#走法にGo(曲線)
                self.countnum+=1
                self.N1+=1
                self.Statment=True
                
                while self.Statment:
                    print("待ち1")
                    pass

                    if self.state==False:
                        self.Statment==False
                        break

                    #if self.state==False:
                self.state=True
                self.Statment==True
                self.state=self.timejudge.judge(counter[self.countnum])
                #mwalker[self.number2].set_run(param[self.number2][self.N2])#走法にGo(直線)
                mwalker[self.number1].left_run(param[self.number2][self.N2])
                self.N2+=1
                self.countnum+=1

                if counter[self.countnum]==999:
                    print("秒数戻す")
                    self.judgefirst=False
                else:
                    while self.Statment:
                        print("待ち２")
                            

                        if self.state==False:
                            self.Statment==False
                            break

                    self.state=True
                    self.Statment=True
                    #stateを戻す

            else:
                self.judgefirst=False
            

            if self.judgefirst==False:
                print("終了")
                break

        mwalker[self.number1].stop()
        print("終了")
            
    def request_Walker(self,walker):

    #走法の生成依頼

        if walker==self.CURVE:
            #オブジェクト生成
            self.mWalker=curveLineTrace.cuvreLineTrace()
            #self.mWalker=0
            print("curve")

        if walker==self.STRAIGHT:
            #オブジェクト生成
            self.mWalker=VirtualLineTrace.VirtualLineTrace()
            #self.mWalker=2
            print("straight")
        
        return self.mWalker

    def request_judge(self,judge):

        #判定の生成依頼

        if judge==self.DISTANCE:
            #オブジェクト生成
            self.mJudge=DistanceJudge.DistanceJudge()
            #self.mjudge-0
            print("judge")
        if judge==self.ANGLE:
            #オブジェクト生成
            self.mJudge=TurnAngleJudge.TurnAngleJudge()
            #self.mjudge=1
            print("mjudghe")

        return self.mJudge

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
    sec=SectionRun()
    mnumber=1
    sec.set_param(mnumber)
    
    pass

if __name__=="__main__":
    main()