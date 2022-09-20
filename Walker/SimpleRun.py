import sys
from inspect import walktree
from Sensor.MotorMgmt import MotorMgmt
from Walker.Run import Run




class SimpleRun(Run):
     def __init__(self):

          self.mForward=0
          self.mTurn=0

     def set_Param(self,param):
          #配列でパラメータを分けている
          self.mFoward=param(0)
          self.mTurn=param(1)

     
     def run(self):
          self.mMotorMgmt=MotorMgmt(self.mFoward,self.mTurn)

     def reset_Param(self,param):
          self.mForward=param(0)
          self.mTurn=param(1)

def main():
     mrun=SimpleRun()
     mrun.set_Param()
     mrun.run()
     mrun.reset_Param()

