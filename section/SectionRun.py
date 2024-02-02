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
        
        pass
    

    def run(self,mwalker,mjudge,Walkeparam,pointer,PositionMgmt):#走法、判定、パラメータ、座標

        '''#中身確認
        print("mjudgeのオブジェクト",mjudge)
        print("mwalkerのオブジェクト",mwalker)
        print("walkeparam",Walkeparam)
        print("座標",pointer)
        '''
        
        walker_thread = threading.Thread(target=self.exec_run, args=(mwalker,Walkeparam,pointer,PositionMgmt))
        
        walker_thread.start()
        
        statement=False
        statement=self.exec_judge(mjudge,pointer,PositionMgmt)
        
        #print("return",statement)
        return statement
        
    def exec_run(self,mwalker,Walkeparam,pointer,PositionMgmt):
        
        mwalker.set_run(Walkeparam,pointer,PositionMgmt)
        
        

    def exec_judge(self, mjudge,pointer,PositionMgmt):
        
        #print("exec_judge_start")
        tes=True
        
        tes=mjudge.judge(pointer,PositionMgmt)#距離判定
            
        if tes==False:
        
            print("判定ました")
            #self.mWalker.stop()
                #break
            return True
                
        else:
            
            return False
        
        
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
            #print("判定中です")
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
            self.mJudge=DistanceJudge.DistanceJudge() #Turnanglejudgeを使用するときはここでインスタンス生成

            print("mjudghe")

        return self.mJudge

    def stop(self):
        
            print("STOP!!!!!!!!!!!!!!!")
            self.mWalker.stop()
            #mwalker.set_run(self.STOP,self.pointer)
    
            print("判定しました")
            #break
        
        





def main():
    sec=SectionRun()
    mnumber=1
    sec.set_param(mnumber)
    
    pass

if __name__=="__main__":
    main()

