#coding:utf-8
import socket
import time
import threading

from cgitb import lookup
import pyproj
import sys
import pathlib

current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')

class nmea2xy():

    position = None
    nmea = None
    latitude = None
    longitude = None
    start_time = None
    

    def __init__(self) -> None:
        pass
    
    def nmea_init(self):
        self.thread1 = threading.Thread(target=self.nmea_update)
        self.thread1.start()



    #threadで動かしてもいいかも
    def nmea_update(self):

        # サーバーIPとポート番号

        IPADDR = "localhost"
        PORT = 2101
        
        # AF_INET：IPv4形式でソケット作成(省略可)

        sock_sv = socket.socket(socket.AF_INET)

        # IPアドレスとポート番号でバインド、タプルで指定
        sock_sv.connect((IPADDR, PORT))
        # 接続・受信の無限ループ

        #本番用
        #print("GPS_loading....")
        while True:
            #実行速度の計算
            #self.start_time = time.perf_counter()

            while True:
                # ソケットから byte 形式でデータ受信
                data = sock_sv.recv(1)
                #print(data)

                if data==b"$":
                    #print("break1")
                    break


            data = sock_sv.recv(5)
            #print(data)
            if data==b'GNGGA':
                #debug
                #print("getGGA")
                GGA=data.decode('utf-8')
                while True:
                    tmp = sock_sv.recv(1)
                    GGA += tmp.decode('utf-8')
                    if tmp==b'\n':
                        #print(tmp)
                        break

                    #GNGGAをカンマ区切りでリスト化
                    list_GGA = GGA.split(",")

                if list_GGA[2] != '' and list_GGA[4] !='':
                    #print(list_GGA[2],list_GGA[4])
                    #print("NMEA_実行時間")
                    #print(time.perf_counter() - start_time)
                    self.nmea = list_GGA[2],list_GGA[4]
                    self.GPS2xy()



    #nmeaデータを緯度/経度からx/yに加工する 経度がx,緯度がy
    def GPS2xy(self):
        #実行速度の計算
        #start_time = time.perf_counter()
        """
        #テスト用コード
        print("gps2xy.getvalue")
        print("test")
        x,y = nmea_get.get()
        #----------------------------test
        """

        #------本番用コード

        #latitude:緯度,longitude:経度
        self.latitude,self.longitude = self.nmea
        
        #debug
        #print(self.latitude,self.longitude)
        

        #latitude = nmea_get.list_GGA[2]
        #longitude = nmea_get.list_GGA[4]
        
        #緯度 ddmm.mmmmmmm
        #latitude = "3539.3146239"

        #緯度のdを抽出
        latitude_d = self.latitude[0:2]
        #print("latitude_d:" + latitude_d)

        #緯度のdをfloatに変換
        latitude_d = float(latitude_d)
        #print(latitude_d)

        #緯度のmを抽出
        latitude_m = self.latitude[2:]
        #print("latitude_m:" + latitude_m)

        #緯度のmをfloatに変換
        latitude_m =float(latitude_m)
        #print(latitude_m)

        #mを度に変換し足し合わせる
        latitude_m = latitude_m / 60
        latitude = latitude_d+ latitude_m
        #print(latitude)

        #経度 dddmm.mmmmmmm
        #longitude = "13945.6411751"

        #経度のdを抽出
        longitude_d = self.longitude[0:3]
        #print("longitude_d:" + longitude_d)

        #経度のdをfloatに変換
        longitude_d = float(longitude_d)
        #print(longitude_d)

        #経度のmを抽出
        longitude_m = self.longitude[3:]
        #print("longitude_m:" + longitude_m)

        #経度のmをfloatに変換
        longitude_m = float(longitude_m)
        #print(longitude_m)

        #mを度に変換し足し合わせる
        longitude_m = longitude_m / 60
        longitude = longitude_d + longitude_m
        #print(longitude)

        # transform from grs80 to x-y
        #grs80 = pyproj.Proj(init='EPSG:6668')
        #rect6 = pyproj.Proj(init='EPSG:6680')

        #---------のぼりべつ用変換


        #日本測地系における地理座標系から平面直角座標系の11系(北海道の登別等)に変換
        transformer = pyproj.Transformer.from_crs('EPSG:4612','EPSG:2453',always_xy=True)

        #---------のぼりべつ用変換


        #---------東京用変換

        #日本測地系における地理座標系から平面直角座標系の9系(東京)に変換
        #transformer = pyproj.Transformer.from_crs('EPSG:4612','EPSG:2451',always_xy=True)


        #---------東京用変換

        x,y = transformer.transform(longitude,latitude)
    
        #debug
        """
        print("x:",end="")
        print(x)
        print("y:",end="")
        print(y)
        """
        self.position = x,y
        
        #print(time.perf_counter() - self.start_time)



    #他クラスがGPSを取得するときに実行する関数
    def getvalue(self):
        return self.position
    

def main():
    test = nmea2xy()
    test.nmea_init()

    while True:
        #実行速度の計算
        #start_time = time.perf_counter()
        pos = test.getvalue()
        #print(time.perf_counter() - start_time)
        #print(pos)


if __name__ == '__main__' :
    main()