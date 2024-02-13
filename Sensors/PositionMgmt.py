# coding: utf-8
#from multiprocessing import get_start_method
import sys
import pathlib,time,threading,csv

current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Sensors import Sensor,GPS2xy,LogMgmt,Lowpass,nmea2xy

class PositionMgmt(Sensor.Sensor):
    #gps = GPS2xy()
    position = 0.0,0.0
    logfile = None

    origin = None

    prev_position = 0.0,0.0
    x_moves = 0.0
    y_moves = 0.0
    last_pos = 0.0

    #インスタンス
    lowpass = Lowpass.Lowpass()
    nmea2xy = nmea2xy.nmea2xy()
    log_writer = LogMgmt.LogMgmt()
    log_header = None
    
    #pylon_position
    A_pylon_X = -3575.364588034064
    A_pylon_Y = -36836.31611362912
    
    B_pylon_X = -3560.656324873728
    B_pylon_Y = -36821.289400412934



    #A,B,C,D,E,C
    Point = [[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0]]

    #pos_total: float

    def __init__(self):
        
        
        # クラス変数
        self.logfile = 'PMgmt_log'
        self.log_header = ['pos_x','pos_y']
        self.log_writer.set_param(self.log_header,self.logfile)

        #GPSログの初期化
        #LogMgmt.clear(self.logfile)
        #LogMgmt.write(self.logfile,"GPS_loading...")

        """
        #初期値の登録
        
        
        #while self.origin == None:
        print("updating_origin...")
        self.Origin_update()
        self.origin = self.position
        #print(self.origin)
        #print("done")
        
        #self.thread1 = threading.Thread(target=self.update)
        #self.thread1.start()
        



        #print(self.origin)

        #x,yの増分 要検討
        self.x_moves = 5.0
        self.y_moves = 8.0
        
        """
        
    def PosMgmt_init(self):
        print("PosMgmt_init")

        #スレッド起動
        self.thread1 = threading.Thread(target=self.update)
        self.thread1.start()

        self.nmea2xy.nmea_init()

        #相対座標設定（庭用）

        #座標取得待ち
        while self.position[0] == 0:
            print(self.position)
        print("END")

        self.circuit_init()
        
        
        #print("origin_update")
        #self.Origin_update()
        
        #print(self.origin)
    
        #x,yの増分 要検討
        #self.x_moves = 4.0
        #self.y_moves = 6.0
        
        
        """
        #------for debug---------
        debug_X = 5.0
        debug_Y = 7.0
        self.position = debug_X,debug_Y
        self.origin = debug_X,debug_Y
        self.x_moves =  1.0
        self.y_moves =  1.0
        #------for debug -------
        """

    def Origin_update(self):
        temp = GPS2xy.GPS2xy.getvalue(self)
        
        if temp != None:
            i = 0
            while i < 1:
                self.last_pos = temp
                #temp = self.lowpass.filtering(temp)
                self.position = temp
                i += 1
                #print("updated position:")
            self.origin = self.position

    #Posparam_conf用GET関数
    def Conf_Param(self):
        conf_pos = GPS2xy.GPS2xy.getvalue(self)

        return conf_pos
    
    #中庭用相対座標の算出
    def circuit_init(self):

        origin = self.position

        diff_file = 'diff.csv'
        export_file =str(current_dir) +  '/../parameter/Circuit_Pos.prm'

        with open(diff_file) as f:
            reader = csv.reader(f)


            pos_diff = [row for row in reader]

        with open(export_file,'w',newline="") as exf:
            writer = csv.writer(exf)
            for diff in pos_diff:
               x = origin[0] + float(diff[0])
               y = origin[1] + float(diff[1])

               writer.writerow([x,y])






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
            #self.log_writer.write(self.logfile,self.position)

            #print("log_saved")
            #print("実行時間_GPSアリ")
            #print(time.perf_counter() - start_time)
            self.prev_position = self.position
            #print(self.position)
            return self.position

        #GPSが取得出来ていなかった時の処理
        else:

            #print("None_GPS")
            #print(self.position)
            #nonepos = [0,0]

            #ここで何かしら返さないとバグる
            #print("None_GPS")
            #print(self.position)

            #print(print("実行時間_GPSナシ"))
            #print(time.time() - start_time)
            #return self.prev_position
            return None


        #f.close()


    def PosInit(self):
        #左sita A
        self.Point[0][0] = self.origin[0] - self.x_moves
        self.Point[0][1] = self.origin[1] + self.y_moves
        
        #右ue D
        self.Point[1][0] = self.origin[0] + self.x_moves
        self.Point[1][1] = self.origin[1] + self.y_moves
        
        #真ん中 C
        self.Point[2][0] = self.origin[0]
        self.Point[2][1] = self.origin[1]

        #migi下 B
        self.Point[3][0] = self.origin[0] - self.x_moves
        self.Point[3][1] = self.origin[1] - self.y_moves

        #右下 E
        self.Point[4][0] = self.origin[0] + self.x_moves
        self.Point[4][1] = self.origin[1] - self.y_moves

        #真ん中 C
        self.Point[5][0] = self.origin[0]
        self.Point[5][1] = self.origin[1]
        
        """
        #---For Tokyo
        #左sita A
        self.Point[0][0] = -3563.9378317051733
        self.Point[0][1] = -36817.67859515735
        
        #右ue D
        self.Point[1][0] = -3557.3500873989533
        self.Point[1][1] = -36826.82967695915
        
        #真ん中 C
        self.Point[2][0] = self.origin[0]
        self.Point[2][1] = self.origin[1]

        #migi下 B
        self.Point[3][0] = -3575.7857532763014
        self.Point[3][1] = -36837.55368490133

        #右下 E
        self.Point[4][0] = -3563.4286332228694
        self.Point[4][1] = -36830.95649754655

        #真ん中 C
        self.Point[5][0] = self.origin[0]
        self.Point[5][1] = self.origin[1]
        """

        
        #print("GOAL_UPDATED!!")
        
        #LogMgmt.write(self.logfile,str(self.Point[0][0]) + ":" + str(self.Point[0][1]))
        return self.Point

    def REIWAInit(self):
        #self.update()

        #中点を返す C:[0] G:[1]
        #mid_point = self.set_mid()
        #print("中点")
        #print(mid_point)
        


        #左上 A
        self.Point[0][0] = -3563.9378317051733
        self.Point[0][1] = -36817.67859515735

        #左下 B
        self.Point[1][0] = -3557.3500873989533
        self.Point[1][1] = -36826.82967695915    #中点Cを通るため1m寄せる

        #中点 C 
        self.Point[2][0] = -3563.448034780053
        self.Point[2][1] = -36822.51344973406
        
        """
        #左上 D 
        self.Point[3][0] = mid_point[0]     #中点C後の直線 2mスタート地点に寄せる
        self.Point[3][1] = self.B_pylon_Y + self.y_moves
        """
        
        #右上 E aaa
        self.Point[3][0] = -3575.7857532763014
        self.Point[3][1] = -36837.55368490133
        
        """
        #右下 F
        self.Point[5][0] = self.origin[0] + self.x_moves - 1 #中点Gを通るため1m寄せる
        self.Point[5][1] = self.origin[1] - self.y_moves
        """
        
        #中点 G
        self.Point[4][0] = -3576.7161618403356
        self.Point[4][1] = -36835.05268294634

        #右上 H
        self.Point[5][0] = -3563.4286332228694   #中点G後の直線 2mスタート地点に寄せる
        self.Point[5][1] = -36830.95649754655

        #原点 S
        self.Point[6][0] = self.origin[0]
        self.Point[6][1] = self.origin[1]

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

                log_pos = [temp[0],temp[1]]
                
                #ログに書き込み
                self.log_writer.write(log_pos)

                #print("updated position:")
                #print(self.position)

            
            #else :
                #print("none_update")
            
            #print("UPDATE_実行時間")
            #print(time.perf_counter() - start_time)



def main():
    tesclass = PositionMgmt()
    tesclass.PosMgmt_init()
    #tesclass.update()
    #print(tesclass.position)
    
    #tesclass.thread1.start()

    # while True:
        
    #     #実行速度の計算
    #     start_time = time.perf_counter()
    #     pos = tesclass.getvalue()
        
    #     #print("now")
    #     print(pos)
        
    #     #print("実行時間")
    #     print(time.perf_counter() - start_time)
    
    
    #tesclass.update()
    #init = tesclass.PosInit()
    #print(init)

    #print(tesclass.origin[0])


if __name__ == '__main__':
    main()


