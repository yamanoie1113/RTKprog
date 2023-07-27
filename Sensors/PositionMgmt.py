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

    origin = None

    x_moves = 0.0
    y_moves = 0.0



    #A,B,C,D,E,C
    Point = [[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0]]

    #pos_total: float

    def __init__(self):
        # クラス変数
        self.logfile = 'GPS_log.txt'

        #GPSログの初期化
        LogMgmt.clear(self.logfile)
        LogMgmt.write(self.logfile,"GPS_loading...")

        while self.origin == None:
            print("updating_origin...")
            self.update()
            self.origin = self.position
            print("done")
            
        print(self.origin)
        

        #x,yの増分
        self.x_moves = 1.0
        self.y_moves = 3.0


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
            return None


        f.close()


    def PosInit(self):
        self.update()

        #左上 A
        self.Point[0][0] = self.origin[0] - self.x_moves
        self.Point[0][1] = self.origin[1] + self.y_moves

        #左下 B
        self.Point[1][0] = self.origin[0] - self.x_moves
        self.Point[1][1] = self.origin[1] - self.y_moves

        #真ん中 C
        self.Point[2][0] = self.origin[0]
        self.Point[2][1] = self.origin[1]

        #右上 D
        self.Point[3][0] = self.origin[0] + self.x_moves
        self.Point[3][1] = self.origin[1] + self.y_moves

        #右下 E
        self.Point[4][0] = self.origin[0] + self.x_moves
        self.Point[4][1] = self.origin[1] - self.y_moves

        #真ん中 C
        self.Point[5][0] = self.origin[0]
        self.Point[5][1] = self.origin[1]
        
        print("GOAL_UPDATED!!")

        return self.Point


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


