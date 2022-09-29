from msilib import MSIDBOPEN_DIRECT
import re
import sys
#from inspect import walktree
from Sensor.MotorMgmt import MotorMgmt
from Walker.PID import PID
#from Walker.Run import Run
from abc import ABCMeta,abstractmethod



class SimpleRun(metaclass=ABCMeta):
     @abstractmethod
     def __init__(self,mForward,mTurn):

          self.mForward=0 #前進
          self.mTurn=0   #ステアリング
          #self.mMotorMgmt=MotorMgmt(0,0)  

          # return self.mForward,self.mTurn
          


     @abstractmethod
     def set_param(self,param):
          
          #配列でパラメータを分けている
          self.mForward=param(0)#前進
          self.mTurn=param(1)#ステアリング

          
          

     @abstractmethod
     def run(self):
          #-100から100までのPWMを設定してMotorMgmtに送る
     
          #直接値をぶっこむと多分走る
          #モータ管理担当の大川君はモーター管理のset_paramに引数を入れて値を受け取れるようにする
          #↓モーター管理に値を渡している
          #self.mMotorMgmt.set_param(self.mFoward,self.mTurn)
          self.mMotorMgmt.set_param(self.mForward,self.mTurn)


     @abstractmethod
     def reset_param(self):
          self.mForward=0
          self.mTurn=0


def main(self):

     #mPID=PID()
     mrun=SimpleRun()
     self.mMOtorMgmt=MotorMgmt()
     #mvir=VirtualLineTrace()
     mrun.set_param()
     mrun.run()
     mrun.reset_param()

