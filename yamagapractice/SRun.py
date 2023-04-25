# coding:utf-8
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
#import b
from Sensors import MotorMgmt
#from Walker import Run
#from Walker import VirtualLineTrace
#from Walker import curveLineTrace
#from Judgement import DistanceJudge
#from Judgement import TimeJudge
#from Judgement import TurnAngleJudge



class SRun:

    def test(self,mwalker,mjudge,Walkeparam,pointer):
        print("mwalker:",mwalker,"mjudge",mjudge,"Walkeparam:",Walkeparam,"pointer",pointer)



def main():
    sec=SRun()
    mnumber=1
    sec.set_param(mnumber)
    
    pass

if __name__=="__main__":
    main()

