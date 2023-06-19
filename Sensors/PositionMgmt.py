#from multiprocessing import get_start_method
import sys
import pathlib

current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Sensors import Sensor,GPS2xy,LogMgmt

class PositionMgmt(Sensor.Sensor):
    #gps = GPS2xy()
    position = None
    logfile = None
    #pos_total: float

    def __init__(self):
        # クラス変数
        self.logfile = 'GPS_log.txt'

        #GPSログの消去
        LogMgmt.clear(self.logfile)
        LogMgmt.write(self.logfile,"GPS_loading...")

        #チェックポイントの初期化



    #値の取得
    def getvalue(self):
        #print("pos_get")
        #ログファイルオープン
        f = open(self.logfile, 'a')

        #GPSの更新
        self.update()

        #GPSが見つかったらその値を、それ以外はnoneを返す
        if self.position != None:
            #print(self.position)

            #logに書きこみ
            LogMgmt.write(self.logfile,self.position)
            #print("log_saved")
            return self.position

        else:

            #print("None_GPS")
            #print(self.position)
            nonepos = [0,0]

            #ここで何かしら返さないとバグる
            print("None_GPS")
            print(self.position)
            return 0,0


        f.close()

    #値の更新
    def update(self):
        #debug
        #print("update position")
        temp = GPS2xy.GPS2xy.getvalue(self)
        if temp != None:
            self.position = temp
            #print("updated position:")

        """
        else :
            print("none_update")
        """




def main():
    tesclass = PositionMgmt()
    tesclass.update()
    tesclass.getvalue()

if __name__ == '__main__':
    main()


