import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')

import numpy as np

from Sensors import PositionMgmt

class Test():
    #A,B,C,D,E,C
    Point = (None)
    start_point = [1.0,1.0] #ダミー
    x_moves = 0.0
    y_moves = 0.0

    PMgmt = PositionMgmt.PositionMgmt()

    def __init__(self):
        #初期値の取得
        #self.start_point=self.PMgmt.getvalue()

        #x,yの増分
        self.x_moves = 1.0
        self.y_moves = 3.0


    def update(self):

        self.Point= ([self.start_point[0] - self.x_moves, self.start_point[1] + self.y_moves], #左上A
                    [self.start_point[0] - self.x_moves,  self.start_point[1] - self.y_moves], #左下B
                    [self.start_point[0],self.start_point[1]], #真ん中C
                    [self.start_point[0] + self.x_moves,self.start_point[1] + self.y_moves], #右上D
                    [self.start_point[0] + self.x_moves,self.start_point[1] - self.y_moves], #右下E
                    [self.start_point[0],self.start_point[1]]  #真ん中C
                    )

        return self.Point


def main():
    test = Test()
    test.update()
    


if __name__=="__main__":
    main()
