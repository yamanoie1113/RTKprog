# coding:utf-8
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
import b
#from Sensors import MotorMgmt
#from Walker import Run
#from Walker import VirtualLineTrace
#from Walker import curveLineTrace
#from Judgement import DistanceJudge
#from Judgement import TimeJudge
#from Judgement import TurnAngleJudge



class SectionRun2:

    STRAIGHT=0
    CURVE=1
    DISTANCE=0
    ANGLE=1
    JudgeFarst=True

    def init(self):
        pass

    def run(self,mjudge,mwalker,Walkeparam):#判定２つ、走法２つ、パラメータ

        #中身確認
        print("mjudgeのオブジェクト",mjudge)
        print("mwalkerのオブジェクト",mwalker)
        print("walkeparam",Walkeparam)
        
        #point=0

        #while self.JudgeFarst:
            
        #mjudge[self.point].judge()#距離判定
        print("直進のジャッジ",mjudge[self.STRAIGHT])   #self.STRAIGHTは０
        #mwalker[pointr].run(Walkeparam[point])
        print("直線のウォーカーパラメータ",mwalker[self.STRAIGHT])

        #mjudge[self.point].judge()#旋回角度判定
        print("曲線のジャッジ",mjudge[self.CURVE])  #self.CURVEは１
        #mwalker[pointr].run(Walkeparam[point])
        print("曲線のウォーカーパラメータ",mwalker[self.CURVE])

        #self.JudgeFarst=False
        #break

            
    def request_Walker(self,number):

    #走法の生成依頼

        if number==self.CURVE:
            #オブジェクト生成
            #self.mWalker=curveLineTrace.cuvreLineTrace()

            #_________↓デバッグ__________
            self.mtest=b.b()    
            #______________________

            self.mWalker=0
            print("curve")

        if number==self.STRAIGHT:
            #オブジェクト生成
            #self.mWalker=VirtualLineTrace.VirtualLineTrace()

            #________↓デバッグ_________
            self.mtest=b.b()
            #______________________

            self.mWalker=2
            print("straight")
            
        #＿＿＿＿↓デバッグ＿＿＿
        return self.mtest
        #________＿＿＿＿＿＿＿＿

        #return self.mWalker

    def request_judge(self,judge):

        #判定の生成依頼

        if judge==self.DISTANCE:
            #オブジェクト生成
            #self.mJudge=DistanceJudge.DistanceJudge()
            #＿＿＿＿↓デバッグ＿＿＿
            self.mtest=b.b()
            #______________________

            self.mjudge=0
            print("judge")

        if judge==self.ANGLE:
            #オブジェクト生成
            #self.mJudge=TurnAngleJudge.TurnAngleJudge()

            #＿＿＿＿↓デバッグ＿＿＿
            self.mtest=b.b()
            #______________________

            self.mjudge=1
            print("mjudghe")

        #_______↓デバッグ_______
        return self.mtest
        #______________________

        #return self.mjudge

    



def main():
    sec=SectionRun2()
    mnumber=1
    sec.set_param(mnumber)
    
    pass

if __name__=="__main__":
    main()