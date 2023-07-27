# coding:utf-8
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Sensors import MotorMgmt
from Walker import VirtualLineTrace
from Walker import curveLineTrace
from Judgement import DistanceJudge
from Judgement import TimeJudge
from Judgement import TurnAngleJudge
from Sensors import PosInit


class SectionRun:

    STRAIGHT=0
    CURVE=1
    DISTANCE=0
    ANGLE=1
    STOP=[0,0,0,0]
    JudgeFarst=True
    timejudge=TimeJudge.TimeJudge()
    Motor=MotorMgmt.MotorMgmt()
    postitionI=PosInit.PosInit()

    def __init__(self):
        
        #self.postitionI.update()
        pass


    def run(self,mwalker,mjudge,Walkeparam,pointer,state):#走法、判定、パラメータ、座標

        #中身確認
        print("mjudgeのオブジェクト",mjudge)
        print("mwalkerのオブジェクト",mwalker)
        print("walkeparam",Walkeparam)
        print("座標",pointer)
        print("state",state)
        
        
        if state==0:
            
            mwalker.set_run(Walkeparam,pointer)
            
            tes=mjudge.judge(pointer)#距離判定
            print("判定中です")
            
            t=True
            
            while t:

                if tes==False:
                    t=False
                    print("判定しました")
                    break
            
        else:  

            mwalker.set_run(Walkeparam,pointer)
            
            tes=mjudge.judge(pointer)#旋回角度判定
            
            print("判定中です")
        
            t=True

            while t:

                if tes==False:
                    t=False
                    print("判定しました")
                    break

                
    def test(self,mwalker,mjudge,Walkeparam,pointer):
        list_num=([0,0,0,0,0])
        T=True
        print(Walkeparam)
        print("debug",mwalker)
        print("mjugedebug",mjudge)
        
        print(pointer)
        
        tes=mjudge.judge(pointer)
        mwalker.set_run(Walkeparam)
        #mwalker.run()
        
        while t:

            if tes==False:
                t=False
                break
                print("まだ2")
        
        #syuuryou
        mwalker.set_run(list_num)
        #mwalker.run()
        
    def test2(self,mwalker,mjudge,Walkeparam,pointer,state):
        
        mwalker.set_run(Walkeparam,pointer)
            
        tes=mjudge.judge(pointer)#旋回角度判定
            
        print("判定中です")
        
        t=True

        while t:

            if tes==False:
                t=False
                print("判定しました")
                break
        
        print("STOP!!!!!!!!!!!!!!!")
        self.Motor.stop()
        
        
    def request_Walker(self,number):

    #走法の生成依頼

        if number==self.CURVE:
            #オブジェクト生成
            self.mWalker=curveLineTrace.cuvreLineTrace()

            print("curve")

        if number==self.STRAIGHT:
            #オブジェクト生成
            self.mWalker=VirtualLineTrace.VirtualLineTrace()

            
            print("straight")
        
        return self.mWalker

    def request_judge(self,judge):

        #判定の生成依頼

        if judge==self.DISTANCE:
            
            #オブジェクト生成
            self.mJudge=DistanceJudge.DistanceJudge()
            
            print("judge")

        if judge==self.ANGLE:
            #オブジェクト生成
            self.mJudge=TurnAngleJudge.TurnAngleJudge()

            print("mjudghe")

        return self.mJudge

    



def main():
    sec=SectionRun()
    mnumber=1
    sec.set_param(mnumber)
    
    pass

if __name__=="__main__":
    main()

