#from Judgement.Judge import Judge
#from Judgement.TurnAngleJudge import TurnAngleJudge
from Walker.Run import Run
from Walker.PID import PID
from Sensors.MotorMgmt import MotorMgmt
from Walker.VirtualLineTrace import VirtualLineTrace
from Walker.VirtualLineTrace2 import VirtulLineTrace2
from Judgement.DistanceJudge import DistenceJudge
from section.SectionMgmt import SectionMgmt
from section.SectionPrm import SectionPrm
from section.SectionRun import SectionRun

class Main:
    mrun=Run()
    mPID=PID()
    mMotorMgmt=MotorMgmt()
    mvir=VirtualLineTrace()
    mvir2=VirtulLineTrace2()
        #計測器
        #座標計
        #旋回角度計
        #角速度計(必要？)
    #mjudge=Judge()
    mdistance=DistenceJudge()
    #mturnangle=TurnAngleJudge()
    msectionMgmt=SectionMgmt()
    msectionprm=SectionPrm()
    msectionrun=SectionRun()
    print("a")

    def init(self):
        
        self.mPID.run(self.mMotorMgmt)
        
    #破棄
    #def __del__(self):
        #pass


    def main_task(self):

        pass

    def main():
        pass

    #if __name__=="__main__":
        #main()

a=Main()

