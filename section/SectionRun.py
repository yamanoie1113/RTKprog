from Walker.Run import Run
from Walker.VirtualLineTrace import VirtualLineTrace
from Walker.VirtualLineTrace2 import VirtualLineTrace2
from Judgement.DistanceJudge import DistenceJudge
from Judgement.TurnAngleJudge import TurnAngleJudge

class SectionRun:

    CURVE=0
    STRAIGHT=1
    DISTANCE=0
    ANGLE=1
    judgefirst=True
    walkerfirst=True
    mWalker=0
    mjudge=0

    def run(self):
        
        #if self.judgefast:

        pass

    def request_Walker(self,walker):

    #走法の生成依頼

        if walker==self.CURVE:
            self.mWalker=VirtualLineTrace()
            #self.mWalker=Run()
        elif walker==self.STRAIGHT:
            self.mWalker=VirtualLineTrace2()
        
        return self.mWalker

    def request_judge(self,judge):

        #判定の生成依頼

        if judge==self.DISTANCE:
            self.mJudge=DistenceJudge()
        elif judge==self.ANGLE:
            self.mJudge=TurnAngleJudge()

        return self.mJudge

def main():
    pass

if __name__=="__main__":
    main()