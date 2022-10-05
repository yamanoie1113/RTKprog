from inspect import walktree
from turtle import speed
from Sensors.MotorMgmt import MotorMgmt
from Walker.SpeedCtl import SpeedCtl



class Run:
     def __init__(self):

          self.mForward=0 #前進
          self.mTurn=0   #ステアリング
          #self.mMotorMgmt=MotorMgmt(0,0)  

          # return self.mForward,self.mTurn
          
     def set_param(self,param):
          
          #配列でパラメータを分けている
          self.mForward=param(0)#前進
          self.mTurn=param(1)#ステアリング

     def run(self,mMotorMgmt):
          #-100から100までのPWMを設定してMotorMgmtに送る
          #self.mMotorMgmt.set_param(self.mFoward,self.mTurn)
          mMotorMgmt.set_param(self.mForward,self.mTurn)


     def reset_param(self):
          self.mForward=0
          self.mTurn=0

     #def set_comondV(self,mTargetSpeed,mTurn):
          #pass
'''
def main(self):

     mPID=PID()
     mrun=Run()
     mMotorMgmt=MotorMgmt()
     #mvir=VirtualLineTrace()
     mrun.set_param()
     mrun.run(mMotorMgmt)
     mrun.reset_param()
'''