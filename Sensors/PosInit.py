import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')

import numpy as np

from Sensors import PositionMgmt

class PosInit():
    #A,B,C,D,E,C
    Point = [[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0]]
    #start_point = [1.0,1.0] #ダミー
    x_moves = 0.0
    y_moves = 0.0

    def __init__(self):
        #初期値の取得


        #x,yの増分

        self.x_moves = 1.0
        self.y_moves = 3.0


    def update(self):
        self.PMgmt.getvalue()

        #左上 A
        self.Point[0][0] = self.start_point[0] - self.x_moves
        self.Point[0][1] = self.start_point[1] + self.y_moves

        #左下 B
        self.Point[1][0] = self.start_point[0] - self.x_moves
        self.Point[1][1] = self.start_point[1] - self.y_moves

        #真ん中 C
        self.Point[2][0] = self.start_point[0]
        self.Point[2][1] = self.start_point[1]

        #右上 D
        self.Point[3][0] = self.start_point[0] + self.x_moves
        self.Point[3][1] = self.start_point[1] + self.y_moves

        #右下 E
        self.Point[4][0] = self.start_point[0] + self.x_moves
        self.Point[4][1] = self.start_point[1] - self.y_moves

        #真ん中 C
        self.Point[5][0] = self.start_point[0]
        self.Point[5][1] = self.start_point[1]

        return self.Point


def main():
    test = PosInit()
    a = test.update()
    print(a)


if __name__=="__main__":
    main()
