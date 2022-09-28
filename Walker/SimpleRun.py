import sys
from inspect import walktree
from Sensor.MotorMgmt import MotorMgmt
from Walker.Run import Run




class SimpleRun(Run):
     def __init__(self):

          self.mForward=0 #前進
          self.mTurn=0   #ステアリング
          self.mMotorMgmt=MotorMgmt(0,0)

     def set_Param(self,param):

          #配列でパラメータを分けている
          self.mFoward=param(0)
          self.mTurn=param(1)
          self.MAX_F=100
          self.MAX_T=100

          #限界値設定
          if self.mFoward > self.MAX_F:

               self.mFoward=100

          if self.mForward < -self.MAX_F:

               self.mForward=-100


          if self.mTurn > self.MAX_T:

               self.mTurn=100

          if self.mTurn < -self.MAX_T:

               self.mTurn=-100

          return self.mForward,self.mTurn

          
          
     
     def run(self):
          #-100から100までのPWMを設定してMotorMgmtに送る
     
          #直接値をぶっこむと多分走る
          #モータ管理担当の大川君はモーター管理のset_paramに引数を入れて値を受け取れるようにする
          #↓モーター管理に値を渡している
          self.mMotorMgmt.set_param(self.mFoward,self.mTurn)

     def reset_param(self):
          self.mForward=0
          self.mTurn=0


def main(self):
     #self.mMotorMgmt=MotorMgmt(0,0)
     mrun=SimpleRun()
     mrun.set_Param()
     mrun.run()
     mrun.reset_param()

