from inspect import walktree
from Sensor.MotorMgmt import WheelMotorMgmt
from Walker.Run import Run


class SimpleRun(Run):
     def __init__():

         mForward=0
         mTurn=0 


     def set_Param(param):
          #配列でパラメータを分けている
          mFoward=param[0]
          mTurn=param[1]

     
     def run(self,frontPWM,rearPWM,advance,turning):

         self.frontPWM=0
         self.rearPWM=0
         self.advance=mForward
         self.turning=mTurn
         frontPWM=(self.advance + self.turning)
         rearPWM=(self.advance - self.turning)
         mWheelMotorMgmt=WheelMotorMgmt(self.frontPWM,self.rearPWM)

     def main():

          mrun=SimpleRun()
          mrun.set_Param()
          mrun.run()
     #reset_Param()

     if __name__ == "__main__":main()
     
        
    #def reset_Param(param[]):

        #self.mset_param=MotorMgmt()
        #mForward=param[0]
        #mTurn=param[1]
