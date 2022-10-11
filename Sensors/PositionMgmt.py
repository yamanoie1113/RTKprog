from multiprocessing import get_start_method
import GPS2xy
import Sensor

class PositionMgmt(Sensor.Sensor):
    position = 0.0

    def __init__(self):
        # クラス変数
        self.position


    #値の取得
    def getvalue(self):
        self.position = GPS2xy.getvalue()
        if self.position != None:
            print(self.position)

    #値の更新
    def update(self):
        return super().update()

def main():
    tesclass = PositionMgmt()
    tesclass.getvalue()

if __name__ == '__main__':
    main()


