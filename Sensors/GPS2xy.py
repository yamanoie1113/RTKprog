from cgitb import lookup
import pyproj
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Sensors import nmea_get


class GPS2xy():
    latitude : float
    longitude : float


    def getvalue(self):
        print("gps2xy.getvalue")
        print("test")
        x,y = nmea_get.get()
        """
        #本番用コード
        self.latitude,self.longitude = nmea_get.get()
        print(self.latitude,self.longitude)
        
        
        latitude = nmea_get.list_GGA[2]
        longitude = nmea_get.list_GGA[4]
    
        
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
        print(latitude)

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
        print(longitude)

        # transform from grs80 to x-y
        #grs80 = pyproj.Proj(init='EPSG:6668')
        #rect6 = pyproj.Proj(init='EPSG:6680')

        #transformer = pyproj.Transformer.from_crs('EPSG:2453','EPSG:6680',always_xy=True)
        transformer = pyproj.Transformer.from_crs('EPSG:4612','EPSG:2453',always_xy=True)
        x,y = transformer.transform(longitude,latitude)
        """

        print("x:",end="")
        print(x)
        print("y:",end="")
        print(y)
        return x,y

def main():
    testclass = GPS2xy()
    testclass.getvalue()
    #testclass.return_position()

if __name__ == '__main__':
    main()

