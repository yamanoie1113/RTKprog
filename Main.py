from Judgement.Judge import Judge
from Judgement.TurnAngleJudge import TurnAngleJudge
from Walker.Run import Run
from Walker.PID import PID
from Sensor.MotorMgmt import MotorMgmt
from Walker.VirtualLineTrace import VirtualLineTrace
from Walker.VirtualLineTrace2 import VirtulLineTrace2
from Judgement.DistanceJudge import DistenceJudge
from section.SectionMgmt import SectionMgmt
from section.SectionPrm import SectionPrm
from section.SectionRun import SectionRun


class Main:
    def user_system_create(self):
        mrun=Run()
        mPID=PID()
        mMotorMgmt=MotorMgmt()
        mvir=VirtualLineTrace()
        mvir2=VirtulLineTrace2()
        #計測器
        #座標計
        #旋回角度計
        #角速度計(必要？)
        mjudge=Judge()
        mdistance=DistenceJudge()
        mturnangle=TurnAngleJudge()
        msectionMgmt=SectionMgmt()
        msectionprm=SectionPrm()
        msectionrun=SectionRun()

    #破棄
    def __del__(self):
        pass


    def main_task(self):


