# coding:utf-8
import os
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Sensors import MotorMgmt
from Walker import Run2
class Run(Run2):
     def __init__(self):

          self.mForward=0 #前進
          self.mTurn=0   #ステアリング
          print(self.mForward,self.mTurn)
          
     def set_param(self):
          #とりあえずここで設定
          #本番はおそらくステージ管理
          self.mForward=50#前進
          self.mTurn=50#ステ
          print(self.mForward,self.mTurn)

     def run(self,mMotorMgmt):
          #-100から100までのPWMを設定してMotorMgmtに送る
          #self.mMotorMgmt.set_param(self.mFoward,self.mTurn)
          mMotorMgmt.set_param(self.mForward,self.mTurn)
          #set_param(self.mForward,self.mTurn)
          
     def reset_param(self):
          self.mForward=0
          self.mTurn=0

     #def set_comondV(self,mTargetSpeed,mTurn):
          #pass

def main():
     #mPID=PID()
     mrun=Run()
     mMotorMgmt=MotorMgmt.MotorMgmt()
     #mvir=VirtualLineTrace()
     mrun.set_param()
     mrun.run(mMotorMgmt)
     #mMotorMgmt.set_param()
     #mrun.reset_param()
     pass


if __name__=="__main__":
     main()


