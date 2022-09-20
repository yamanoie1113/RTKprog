from inspect import walktree
from Sensor.MotorMgmt import MotorMgmt
from Walker.Run import Run


class SimpleRuntest(Run):
     def __init__(self):

          self.mFoward=0
          self.mTurn=0

     def set_Param(self,param):
          #配列でパラメータを分けている
          self.mFoward=param[0]
          self.mTurn=param[1]

     
     def run(self,MotorMgmt):

          self.frontPWM=0
          self.rearPWM=0
          self.advance=self.mFoward
          self.turning=self.mTurn
          self.frontPWM=(self.advance + self.turning)
          self.rearPWM=(self.advance - self.turning)
          self.mMotorMgmt=MotorMgmt(self.frontPWM,self.rearPWM)

     def main():

          mrun=SimpleRuntest()
          mrun.set_Param()
          mrun.run()
          mrun.reset_Param()

     if __name__ == "__main__":main()
     
        
     def reset_Param(self,param):

          self.mForward=param[0]
          self.mTurn=param[1]
