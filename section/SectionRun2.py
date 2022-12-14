# coding:utf-8
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from section import Param2
#from Sensors import MotorMgmt
#from Walker import Run
from Walker import VirtualLineTrace
from Walker import curveLineTrace
from Judgement import TimeJudge
from Judgement import DistanceJudge
from Judgement import TurnAngleJudge



class SectionRun2:

    CURVE=0
    STRAIGHT=1
    DISTANCE=0
    ANGLE=1
    #mWalker=0
    #mjudge=0
    deb=None
    param=Param2.Param2()
    timejudge=TimeJudge.TimeJudge()
    
    #mMotorMgmt=MotorMgmt()

    def __init__(self):
        self.deb=None
        self.number=0
        self.N1=0
        self.cnt=0   
        self.judgepoint=0
        self.judgefirst=True
        self.walkerfirst=True
        self.state=True

    def run(self,mjudge,mwalker,count,param):#判定２つ、走法２つ、秒数、パラメータ エラーになったらmWalkerを一回外して
        #早く仮想ラインつくってよおおおおおおおお
        while self.judgefirst:#trueかfalseか
            
            mjudge[self.judgepoint].__init__()

            if self.judgepoint==0:
                mjudge[self.judgepoint].judge()#距離判定
                self.judgepoint+=1
            else:
                mjudge[self.judgepoint].judge()#旋回角度判定


            self.walkerfirst=True

            #走法
            while self.walkerfirst:
                if  (param[0]!=None) or (count[0] !=None):#配列無しならおわり
                    self.state=self.timejudge.judge(count[0])#timejudgeにカウント数をぶち送る
                    #mwalker[self.number].run(param[self.N1])#これをコメント外す
                    print("テスト１")
                    self.cnt+=1
                    self.N1+=1
                    self.number+=1

                    while self.state:
                        print("待ち1")

                        if self.state==False:
                            break
                        else:
                            pass

                    self.state=True
                    print("テスト２")
                    if (param[1]!=None) or (count[1] !=None):#配列無しならおわり
                        self.state=self.timejudge.judge(count[1])#timejudgeにカウントをぶち送る
                        #mwalker[self.number1].run(param[self.N1])#走法にGo(直線) 絶対にエラーになるのでコメントアウト

                        while self.state:
                            print("待ち2")
                        
                            if self.state==False:
                                break
                            else:
                                pass
                
                        self.walkerfirst=False

                        if self.walkerfirst==False:
                            break
                    else:
                        self.walkerfirst==False

                        if self.walkerfirst==False:
                            break
                        

                else:
                    self.walkerfirst==False

                    if self.walkerfirst==False:
                        break

            
            self.judgefirst=False
                    
            #↓ここで終わりたい
            if self.judgefirst==False:
                break
        
        
    def request_Walker(self,walker):

    #走法の生成依頼

        if walker==self.CURVE:
            #オブジェクト生成
            self.mWalker=curveLineTrace.cuvreLineTrace()
            #self.mWalker=0
            print("curve")

        if walker==self.STRAIGHT:
            #オブジェクト生成
            self.mWalker=VirtualLineTrace.VirtualLineTrace()#今外すとエラーになりますわよ★
            #self.mWalker=2
            print("straight")
        
        return self.mWalker

    def request_judge(self,judge):

        #判定の生成依頼

        if judge==self.ANGLE:
            #オブジェクト生成
            self.mJudge=TurnAngleJudge.TurnAngleJudge()
            #self.mjudge=0
            print("judge")
        if judge==self.DISTANCE:
            #オブジェクト生成
            self.mjudge=DistanceJudge.DistanceJudge()
            #self.mjudge=1
            print("mjudghe")

        return self.mJudge

    def set_param(self,mnumber,count):#パラメータ設定
        #曲線
        if mnumber==0:
            self.Count=count
            self.prm=self.param.Curve_set_param(self.Count)
            #[前進量、旋回量、P,I,D]
            print("cuevever",self.prm)
            #(ここで値を設定すると思っているs)
        elif mnumber==1:
        #直線
            self.prm=self.param.Straight_set_param(self.Count)
            #[前進量、P,I,D]
            print("straight",self.deb)
        
        return self.prm

    def count_set_param1(self,count):#これが曲線
        self.cnt=count

        self.cnt=self.param.count_set_param1(self.cnt)

        return self.cnt

    def count_set_param2(self,count):#これが直線
        self.cnt=count

        self.cnt=self.param.count_set_param2(self.cnt)

        return self.cnt


def main():
    sec=SectionRun2()
    mnumber=1
    sec.set_param(mnumber)
    
    pass

if __name__=="__main__":
    main()