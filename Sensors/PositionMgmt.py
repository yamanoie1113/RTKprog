from multiprocessing import get_start_method
from GPS2xy import *
import Sensor

class PositionMgmt(Sensor.Sensor):
    position = 0.0
    gps = GPS2xy()
    def __init__(self,posiion):
        # クラス変数
        self.position = posiion
        
    #値の取得
    def getvalue(self):
        if self.position != None:
            print(self.position)
            print("return_end")
            return self.position
            
        else:
            print("None GPS")
            print(self.position)

    #値の更新
    def update(self):
        print("position")
        self.position = self.gps.getvalue()
"""
def main():
    tesclass = PositionMgmt(0.0)
    tesclass.update()
    tesclass.getvalue()

if __name__ == '__main__':
    main()
"""

