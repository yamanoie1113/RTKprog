from inspect import walktree
from Sensor.MotorMgmt import WheelMotorMgmt
from Walker.Run import Run


class SimpleRun(Run):
    def __init__():

         mForward=0
         mTurn=0 


    def main():

     mrun=SimpleRun()
     set_Param()
     run()
     reset_Param()


    def set_Param(param[]):

          mFoward=param[0]
          mTurn=param[1]

     
    def Run(self,frontPWM,rearPWM,advance,turning):

         self.frontPWM=0
         self.rearPWM=0
         self.advance=mForward
         self.turning=mTurn
         frontPWM=(advance + turning)
         rearPWM=(advance - turning)
         mWheelMotorMgmt=WheelMotorMgmt()


     
        
    #def reset_Param(param[]):

        #self.mset_param=MotorMgmt()
        #mForward=param[0]
        #mTurn=param[1]
