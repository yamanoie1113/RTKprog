from multiprocessing import get_start_method
import sys
import pathlib

current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Sensors import Sensor,GPS2xy

class PositionMgmt(Sensor.Sensor):
   # gps = GPS2xy()
    position: float
    #pos_total: float
    def __init__(self):
        # クラス変数
        pass

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
        print("update position")
        self.position = GPS2xy.GPS2xy.getvalue(self)
        print("updated position:")



def main():
    tesclass = PositionMgmt(0.0)
    tesclass.update()
    tesclass.getvalue()

if __name__ == '__main__':
    main()


