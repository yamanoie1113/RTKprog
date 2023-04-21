import numpy as np

import PositionMgmt

class PositionInitialize():
    Point = [[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0]]
    start_point = [1.0,1.0] #ダミー
    x_moves = 0.0
    y_moves = 0.0

    PMgmt = PositionMgmt.PositionMgmt()

    def __init__(self):
        #self.start_point=self.PMgmt.getvalue()

        #x,yの増分
        self.x_moves = 1.0
        self.y_moves = 3.0


    def update(self):

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


def main():
    test = PositionInitialize()
    test.update()
    print(test.Point)


if __name__=="__main__":
    main()