# coding:utf-8
from ast import Delete
from tkinter import END
from tracemalloc import start
import time
import threading
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Sensors import TurnAngleSensor
from Walker import VirtualLineTrace
from Walker import VirtualLineTrace2
from Sensors import MotorMgmt
from section import SectionMgmt
from section import SectionRun
from Sensors import PositionMgmt

class Mgmt:

    UNDEFINED=0
    START=1
    INIT_SPEED=2
    SPEED=3
    END=4

    def __init__(self):


        self.mState=self.UNDEFINED
        #self.mSsm=SectionMgmt()
        
    def run(self):

        if self.mState == self.UNDEFINED:
            self.excecUndefined()
            
        elif self.mState == self.START:
            self.execStart()

        elif self.mState == self.INIT_SPEED:
            self.initSpeed()

        elif self.mState == self.SPEED:
            self.execSpeed()

        elif self.mState == self.END: 
            self.__del__()
        else:
            return True

        return False

    

    def excecUndefined(self):
        #キャリブレーション？
        self.mState=self.START

    def execStart(self):
        self.mstate=self.INIT_SPEED


    def initSpeed(self):
        self.mSsm.init()
        self.mState=self.SPEED

    def execSpeed(self):
        if self.mSsm.run():
            del self.mSsm
            self.mstate=self.END
        #finish()
    def __del__():
        #相談
        pass



    def main_task(self,mMotorMgmt):

            pass
        #mMotorMgmt.set_param(0,0)


    def Walker_task(self,mLinTracer,mLinTracer2):
        #パラメータ設定
        #self.param=[50,0,5,5,5]#タプル
        #{前進量,旋回量,P,I,D}

        #mLinTracer2.init(self.param)
        #mLinTracer2.run()

        #mLinTracer.init(self.param)
        #mLinTracer.run()
        pass

        
    def sensor_task(mTurnAngleSensor,mPositionMgmt):

        mTurnAngleSensor.update()
        mPositionMgmt.update()

    #センサーにタスク命令


        pass

    

def main():
    #スレッド実装
    mSsm=SectionMgmt()
    mgmt=Mgmt()
    mMotorMgmt=MotorMgmt()
    mLintracer=VirtualLineTrace()
    mLintracer2=VirtualLineTrace2()
    mTurnAngleSensor=TurnAngleSensor()
    mPositionMgmt=PositionMgmt()

    #mgmt.main_task(mMotorMgmt)

    #thread1=
    #thread2=
    #thread1.start()
    #thread2.start()



if __name__=="__main__":
    main()




    