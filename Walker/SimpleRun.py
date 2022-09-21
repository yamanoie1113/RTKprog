import sys
from inspect import walktree
from Sensor.MotorMgmt import MotorMgmt
from Walker.Run import Run




class SimpleRun(Run):
     def __init__(self):

          self.mForward=0
          self.mTurn=0
          self.mMotorMgmt=MotorMgmt(0,0)

     def set_Param(self,param):
          #おそらく速度制御からパラメータを持って来る
          #配列でパラメータを分けている
          self.mFoward=param(0)
          self.mTurn=param(1)

     
     def run(self):
          #-100から100までのPWMを設定してMotorMgmtに送る
          self.frontPWM=0
          self.rearPWM=0
          self.frontPWM=self.mFoward
          self.rearPWM=self.mTurn
          #直接値をぶっこむと走る
          self.mMotorMgmt.set_param(self.frontPWM,self.rearPWM)

     def reset_Param(self):
          self.mForward=0
          self.mTurn=0


def main():
     mrun=SimpleRun()
     mrun.set_Param()
     mrun.run()
     mrun.reset_Param()

