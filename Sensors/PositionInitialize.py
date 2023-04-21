import numpy as np

import PositionMgmt

class PositionInitialize():
    Point = np.array([0.0,0.0,0.0,0.0][0.0,0.0])
    start_point = 0.0
    x_moves = 0.0
    y_moves = 0.0

    PMgmt = PositionMgmt.PositionMgmt()

    def __init__(self):
        self.start_point=self.PMgmt.getvalue()
        self.x_moves = 1.0
        self.y_moves = 3.0


    def update(self):

        #左上
        self.Point[0][0] = self.start_point[0] - self.x_moves
        self.Point[0][1] = self.start_point[1] + self.y_moves

        #左下
        self.Point[1][0] = self.start_point[0] - self.x_moves
        self.Point[1][1] = self.start_point[1] - self.y_moves

        #右上
        self.Point[2][0] = self.start_point[0] + self.x_moves
        self.Point[2][1] = self.start_point[1] + self.y_moves

        #右下
        self.Point[3][0] = self.start_point[0] + self.x_moves
        self.Point[3][1] = self.start_point[1] - self.y_moves


def main():
    test = PositionInitialize()
    test.update()
    

if __name__=="__main__":
    main()
