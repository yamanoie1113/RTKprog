from inspect import walktree
from turtle import speed
from Sensor.MotorMgmt import MotorMgmt
from Walker.Run import Run
from Walker.SpeedCtl import SpeedCtl


class SimpleRuntest(Run):
     def __init__(self):

          self.mForward(0)
          self.mTurn(0)
          self.mBreale_flag(False)
          self.mMode_flag(False)
          self.buf[256]
          self.sprintf(self.buf,"SimpleWalker init %f,%d",self.mForward,self.mTurn)
          self.msg_log(self.buf)          
          self.mMotorMgmt=MotorMgmt(0,0)
          self.mSpeedCtl=SpeedCtl(0)
     #def set_Param(self,param):
          #配列でパラメータを分けている
          #self.mFoward=param[0]
          #self.mTurn=param[1]
          #yamaie = self.yuki
          if self.mMode_flag:
               self.set_commandV(self.mForward,self.mTurn)
          else :
               self.set_command(self.mForward,self.mTurn)
     
     def run(self,MotorMgmt):
          
          #float(speed)=0
          self.speed=0
          self.Forward=self.mSpeedCtl.get_pwm()
          self.pwm_f=self.mForward + self.mTurn #front
          #self.pwm_b=self.mForward - self.mTurn #back

          self.MAXPWM=100

          self.diff=0

          if self.pwm_f > self.MAXPWM:
               #わからん
               # self.pwm_b=(int)((float)self.MAXPWM*pwm_b/pwm_f)
               self.pwm_f=self.MAXPWM

          if self.pwm_f<-self.MAXPWM:

               self.pwm_f=-self.MAXPWM

          if self.pwm_f>100:
               self.pwm_f=100

          if self.pwm_f<-100:
               self.pwm_f=-100

          
          self.mMotorMgmt.set_pwm(self.pwm_f)


     def set_command(self,forward,turn):

          self.mForward=forward
          self.mSpeedCtl.reset_param()
          self.mSpeedCtl.set_target_speed(forward)
          self.mTurn=turn
          self.mSpeedCtl.set_mode(False)


     def  set_commandV(self,forward,turn):

          self.mSpeedCtl.set_target_speed(forward)
          self.speedCtl.setBreak(False)

          if forward==0:

               self.mSpeedCtl.set_mode(True)


     def reset_param(self):

          self.mSpeedCtl.reset_param()



     def main():

          mrun=SimpleRuntest()
          mrun.set_param()
          mrun.run()
          mrun.reset_param()

     if __name__ == "__main__":main()
     