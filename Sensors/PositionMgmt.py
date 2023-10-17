#from multiprocessing import get_start_method
import sys
import pathlib,time,threading

current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Sensors import Sensor,GPS2xy,LogMgmt,Lowpass

class PositionMgmt(Sensor.Sensor):
    #gps = GPS2xy()
    position = 0.0,0.0
    logfile = None

    origin = None

    prev_position = 0.0,0.0
    x_moves = 0.0
    y_moves = 0.0
    last_pos = 0.0
    lowpass = Lowpass.Lowpass()



    #A,B,C,D,E,C
    Point = [[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0]]

    #pos_total: float

    def __init__(self):
        # クラス変数
        #self.logfile = 'GPS_log.txt'

        
        #初期値の登録
        while self.origin == None:
            print("updating_origin...")
            self.Origin_update()
            self.origin = self.position
            #print(self.origin)
        #print("done")
        


        self.thread1 = threading.Thread(target=self.update)
        self.thread1.start()
        

        #GPSログの初期化
        #LogMgmt.clear(self.logfile)
        #LogMgmt.write(self.logfile,"GPS_loading...")

        #print(self.origin)

        #x,yの増分 要検討
        self.x_moves = 7.0
        self.y_moves = 5.0

    def Origin_update(self):
        temp = GPS2xy.GPS2xy.getvalue(self)
        if temp != None:
            i = 0
            while i < 7:
                self.last_pos = temp
                #temp = self.lowpass.filtering(temp)
                self.position = temp
                i += 1
                #print("updated position:")
        
        

    #値の取得
    def getvalue(self):
        #実行速度の計算
        #start_time = time.perf_counter()

        #print("pos_get")
        #ログファイルオープン
        #f = open(self.logfile, 'a')

        #GPSの更新
        #self.update()

        #GPSが見つかったらその値を、それ以外はnoneを返す
        if self.position != None:
            #print(self.position)

            #logに書きこみ
            #LogMgmt.write(self.logfile,self.position)
            #print("log_saved")
            #print("実行時間_GPSアリ")
            #print(time.perf_counter() - start_time)
            self.prev_position = self.position

            return self.position

        #GPSが取得出来ていなかった時の処理
        else:

            #print("None_GPS")
            #print(self.position)
            nonepos = [0,0]

            #ここで何かしら返さないとバグる
            #print("None_GPS")
            #print(self.position)

            #print(print("実行時間_GPSナシ"))
            #print(time.time() - start_time)
            #return self.prev_position
            return None


        #f.close()


    def PosInit(self):        
        
        #左上 A
        self.Point[0][0] = self.origin[0] - self.x_moves
        self.Point[0][1] = self.origin[1] + self.y_moves

        #左下 B
        self.Point[1][0] = self.origin[0] + self.x_moves
        self.Point[1][1] = self.origin[1] + self.y_moves

        #真ん中 C
        self.Point[2][0] = self.origin[0]
        self.Point[2][1] = self.origin[1]

        #右上 D
        self.Point[3][0] = self.origin[0] + self.x_moves
        self.Point[3][1] = self.origin[1] - self.y_moves

        #右下 E
        self.Point[4][0] = self.origin[0] - self.x_moves
        self.Point[4][1] = self.origin[1] - self.y_moves

        #真ん中 C
        self.Point[5][0] = self.origin[0]
        self.Point[5][1] = self.origin[1]
        
        """

        #左上 A
        self.Point[0][0] = 70693.0
        self.Point[0][1] = -171683.0

        #左下 B
        self.Point[1][0] = 70688.0
        self.Point[1][1] = -171684.0

        #真ん中 C
        self.Point[2][0] = self.origin[0]
        self.Point[2][1] = self.origin[1]

        #右上 D
        self.Point[3][0] = 70702.0
        self.Point[3][1] = -171688.0

        #右下 E
        self.Point[4][0] = 70697.0
        self.Point[4][1] = -171689.0

        #真ん中 C
        self.Point[5][0] = self.origin[0]
        self.Point[5][1] = self.origin[1]
        """
        
        #print("GOAL_UPDATED!!")
        
        #LogMgmt.write(self.logfile,str(self.Point[0][0]) + ":" + str(self.Point[0][1]))
        return self.Point

    def REIWAInit(self):
        self.update()

        #中点を返す C:[0] G:[1]
        mid_point = self.set_mid()
        #print("中点")
        #print(mid_point)



        #左上 A
        self.Point[0][0] = self.origin[0] - self.x_moves
        self.Point[0][1] = self.origin[1] + self.y_moves

        #左下 B
        self.Point[1][0] = self.origin[0] - self.x_moves - 1    #中点Cを通るため1m寄せる
        self.Point[1][1] = self.origin[1] - self.y_moves

        #中点 C 
        self.Point[2][0] = mid_point[0]
        self.Point[2][1] = self.origin[1]

        #左上 D 
        self.Point[3][0] = mid_point[0] + 2     #中点C後の直線 2mスタート地点に寄せる
        self.Point[3][1] = self.origin[1] + self.y_moves

        #右上 E aaa
        self.Point[4][0] = self.origin[0] + self.x_moves
        self.Point[4][1] = self.origin[1] + self.y_moves

        #右下 F
        self.Point[5][0] = self.origin[0] + self.x_moves - 1 #中点Gを通るため1m寄せる
        self.Point[5][1] = self.origin[1] - self.y_moves

        #中点 G
        self.Point[6][0] = mid_point[1]
        self.Point[6][1] = self.origin[1]

        #右上 H
        self.Point[7][0] = mid_point[0] - 2    #中点G後の直線 2mスタート地点に寄せる
        self.Point[7][1] = self.origin[1] + self.y_moves

        #原点 S
        self.Point[8][0] = self.origin[0]
        self.Point[8][1] = self.origin[1]

        #print("REIWA_UPDATED!!")

        return self.Point


    def set_mid(self):

        #C付近のメインパイロンxポイント
        C_main = self.origin[0] - 10
        #C付近のサブパイロンxポイント
        C_sub = C_main + 1




        #G付近のメインパイロンxポイント
        G_main = self.origin[0] + 10
        #G付近のサブパイロンxポイント
        G_sub = G_main - 1


        C_mid = (C_main + C_sub)/2


        G_mid = (G_main + G_sub)/2

        #print("C_MAIN")
        #print(C_main)

        return C_mid,G_mid




    #値の更新
    def update(self):
        while True:
            #実行速度の計算
            #start_time = time.perf_counter()
            #debug
            #print("update position")
            
            
            temp = GPS2xy.GPS2xy.getvalue(self)
            if temp != None:
                self.last_pos = temp
                #---lowpass
                #temp = self.lowpass.filtering(temp)
                self.position = temp
                #print("updated position:")
                #print(self.position)

            
            #else :
                #print("none_update")
            
            #print("UPDATE_実行時間")
            #print(time.perf_counter() - start_time)



def main():
    tesclass = PositionMgmt()
    #tesclass.update()
    #print(tesclass.position)
    
    #tesclass.thread1.start()
    while True:
        
        #実行速度の計算
        #start_time = time.perf_counter()
        pos = tesclass.getvalue()
        
        #print("now")
        print(pos)
        
        #print("実行時間")
        #print(time.perf_counter() - start_time)

    #tesclass.update()
    init = tesclass.PosInit()
    #print(init)

    #print(tesclass.origin[0])


if __name__ == '__main__':
    main()


