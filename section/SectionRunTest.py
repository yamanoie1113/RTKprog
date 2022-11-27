# coding:utf-8
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from section import Param2
#from Sensors import MotorMgmt
#from Walker import Run
#from Walker import VirtualLineTrace
#from Walker import curveLineTrace
from Judgement import TimeJudge
#from Judgement import DistanceJudge
#from Judgement import TurnAngleJudge



class SectionRunTest:

    CURVE=1
    STRAIGHT=1
    DISTANCE=0
    ANGLE=1
    judgefirst=True
    walkerfirst=True
    mWalker=0
    mjudge=0
    deb=None
    param=Param2.Param2()
    number=0
    cnt=0
    N1=0
    judgepoint=0
    timejudge=TimeJudge.TimeJudge()
    state=True
    #mMotorMgmt=MotorMgmt()

    def init(self):
        self.deb=None

    def run(self,mjudge,mwalker,count,param):#判定２つ、走法２つ、秒数、パラメータ エラーになったらmWalkerを一回外して
        self.number=0
        self.N1=0
        self.judgepoint=0
        self.cnt=0
        #早く仮想ラインつくってよおおおおおおおお
        print("koraaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",count)
        print("いけええ",self.cnt)
        print("kokodesyo",count[1])
        while self.judgefirst:#trueかfalseか
            
            #ここで時間の判定を呼び出す
            #180秒経過はどこで実行判定すればいいかわからん
            #mjudge[self.judgepoint].__init__()
            print("judgeいけた")
            if self.judgepoint==0:
                #mjudge[self.judgepoint].judge()#距離判定
                #self.judgepoint+=1
                print("judge2いけた")
                
            else:
                #mjudge[self.judgepoint].judge()#旋回角度判定
                print("つかれた")

            self.walkerfirst=True

        #走法
            while self.walkerfirst:
                    print("ikuzwe!",count[self.cnt])
                #if param[self.N1]!=None or count[self.cnt] !=None:#別に２次元配列ではなくてもいいことに気が付いた
                    #param[self.number1][self.N1]!=None or count[self.cnt]!=None:#walkerかcpuntの配列がなくなったらおーわり★
                    #self.state=self.timejudge.judge(count[self.cnt])#timejudgeにカウント数をぶち送る
                    #mwalker[self.number].run(param[self.N1])#これをコメント外す
                    #mwalker[self.number].run(param[self.number1][self.N1])#走法にGo(曲線)　絶対にエラーになるのでコメントアウト
                    print("テスト１")
                    self.cnt+=1
                    self.N1+=1
                    self.number+=1
                    print("ikuzwe2!",count[self.cnt])
                    while self.state:
                        print("待ち1")
                        #デバック
                        self.state=False

                    
                        if self.state==False:
                            break
                        else:
                            pass

                    self.state=True
                    #if count[self.cnt]==None:
                        #self.walkerfirst=False
                    
                    print("テスト２")
                        #self.state=self.timejudge.judge(count[self.cnt])#timejudgeにカウントをぶち送る
                        #mwalker[self.number1].run(param[self.N1])#走法にGo(直線) 絶対にエラーになるのでコメントアウト
                        #stateを戻す

                    while self.state:
                        print("待ち2")
                        #デバック
                        self.state=False
                        

                        if self.state==False:
                            break
                        else:
                            pass
                    
                    
                    self.walkerfirst=False
                    self.judgefirst=False
                    break
                    
                

                    #irst=False
                    #self.judgefirst=False#これでwhileを終わらせてしまう
                    #sbreak
        
    def request_Walker(self,walker):

    #走法の生成依頼

        if walker==self.CURVE:
            #オブジェクト生成
            #self.mWalker=curveLineTrace.cuvreLineTrace()
            self.mWalker=0
            print("curve")

        if walker==self.STRAIGHT:
            #オブジェクト生成
            #self.mWalker=VirtualLineTrace.VirtualLineTrace()#今外すとエラーになりますわよ★
            self.mWalker=2
            print("straight")
        
        return self.mWalker

    def request_judge(self,judge):

        #判定の生成依頼

        if judge==self.ANGLE:
            #オブジェクト生成
            #self.mJudge=TurnAngleJudge.TurnAngleJudge()
            self.mjudge=0
            print("judge")
        if judge==self.DISTANCE:
            #オブジェクト生成
            #self.mjudge=DistanceJudge.DistenceJudge()
            self.mjudge=1
            print("mjudghe")

        return self.mjudge

    def set_param(self,mnumber,count):#パラメータ設定
        #曲線
        if mnumber==0:
            self.Count=count
            self.prm1=self.param.Curve_set_param(self.Count)
            #[前進量、旋回量、P,I,D]
            print("cuevever",self.prm1)
            #(ここで値を設定すると思っているs)
            return self.prm1
        
        if mnumber==1:
        #直線
            self.prm2=self.param.Straight_set_param(self.Count)
            #[前進量、P,I,D]
            print("straight",self.prm2)
        
        return self.prm2

    def count_set_param1(self,count):
        self.cnt=count

        self.cnt=self.param.count_set_param1(self.cnt)

        return self.cnt

    def count_set_param2(self,count):
        self.cnt=count

        self.cnt=self.param.count_set_param2(self.cnt)

        return self.cnt

def main():
    sec=SectionRunTest()
    mnumber=1
    sec.set_param(mnumber)
    
    pass

if __name__=="__main__":
    main()