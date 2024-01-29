import numpy as np
import math,csv

import sys
import pathlib,time,threading
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Judgement import Judge


from Sensors import LogMgmt,PositionMgmt as PMgmt

class DisTester():

    distance = None
    PosClass = PMgmt.PositionMgmt()
    goal_pos = None
    pos = None
    param_file = '/Users/takak/OneDrive/ドキュメント/GitHub/RTKplog2/parameter/Test_Straight_Pos.prm'

    def __init__(self):
        self.PosClass.PosMgmt_init()
        

    def set_target(self):
        with open(self.param_file, mode='r') as f:
        # parameterファイルreaderの生成
            reader = csv.reader(f)
            #reader_header=next(f)


            for prm in reader:
                self.goal_pos= prm

        #print(self.goal_pos)

    def judge(self,goal_pos):
        while True:
            cur_pos = self.get_pos()
            if cur_pos != None:
                

                break
        mdistance = self.calc_dist(cur_pos,goal_pos)

        print(mdistance)
        #print(cur_pos)

        
        if mdistance < 2.0 :
           return True

        else :
           return False

    def calc_dist(self,cur_pos,goal_pos):
        #2点間の距離計算
        distance = math.sqrt(( float(goal_pos[0]) - cur_pos[0])**2 + ( float(goal_pos[1]) - cur_pos[1])**2)

        return distance

    def get_pos(self):
        pos = self.PosClass.getvalue()
        return pos


def main():
    test = DisTester()
    test.set_target()
    tmp = False

    while True:
        tmp = test.judge(test.goal_pos)
        #print(tmp)
        if tmp == True:
            break


if __name__ == '__main__':
    main()