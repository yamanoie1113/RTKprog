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
import threading
import time

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
    walker_thread=None
    judge_thread=None
    #pointer=None

    def __init__(self):
        print("aaaa")
        mwalker = None
        Walkeparam = None
        pointer = None
        #self.walker_thread=threading.Thread(target=self.exec_run, args=(mwalker,Walkeparam,pointer))
        #self.judge_thread=threading.Thread(target=self.exec_judge)
        
        

        #self.postitionI.update()
        


    def run(self,mwalker,mjudge,Walkeparam,pointer):#走法、判定、パラメータ、座標

        
        '''#中身確認
        print("mjudgeのオブジェクト",mjudge)
        print("mwalkerのオブジェクト",mwalker)
        print("walkeparam",Walkeparam)
        print("座標",pointer)
        '''
        walker_thread = threading.Thread(target=self.exec_run, args=(mwalker,Walkeparam,pointer))
        judge_thread = threading.Thread(target=self.exec_judge, args=(mjudge,pointer))
        walker_thread.start()
        judge_thread.start()
        
        #judge_thread.join()  
        #walker_thread.join()
        
    def exec_run(self,mwalker,Walkeparam,pointer):
        
        print("exec_run_start")
        mwalker.set_run(Walkeparam,pointer)
        print("exec_run_END")

    def exec_judge(self, mjudge,pointer):
        tes=mjudge.judge(pointer)#距離判定
        print("判定中です")
        t=True
        while t:
            if tes==False:
                t=False
                print("判定しました")
                break
        
    def test_straight(self,mwalker,mjudge,Walkeparam,pointer):
        
        t=True
        print("SECTION_RUN_TEST_straight")
        
        mwalker.set_run(Walkeparam,pointer)
        
        while t:
            tes=mjudge.judge(pointer)#距離判定
            print("判定中です")
            if tes==False:
                t=False
                print("STOP!!!!!!!!!!!!!!!")
                mwalker.set_run(self.STOP,pointer)
                print("判定しました")
                break

        
        
    def test_curve(self,mwalker,mjudge,Walkeparam,pointer):
        
        t=True
        print("SECTION_RUN_TEST_curve")
        
        mwalker.set_run(Walkeparam,pointer)
        #self.pointer=pointer
        #self.walker_thread.start()
        while t:
            tes=mjudge.judge(pointer)#距離判定
            print("判定中です")
            if tes==False:
                t=False
                print("STOP!!!!!!!!!!!!!!!")
                mwalker.set_run(self.STOP,pointer)
                print("判定しました")

        
        
        
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
            #後日コードを短く修正しておく
            self.mJudge=DistanceJudge.DistanceJudge()

            print("mjudghe")

        return self.mJudge

    def stop(self):
        mwalker.set_run(self.STOP,self.pointer)
        #while t:
        tes=mjudge.judge(self.pointer)#距離判定
        print("判定中です")
                

    
        if tes==False:
            #t=False
            print("STOP!!!!!!!!!!!!!!!")
        #self.Motor.stop()
            mwalker.set_run(self.STOP,self.pointer)
    
            print("判定しました")
            #break
        
        





def main():
    sec=SectionRun()
    mnumber=1
    sec.set_param(mnumber)
    
    pass

if __name__=="__main__":
    main()

