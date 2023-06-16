from abc import abstractmethod
import Sensor

import requests
from bs4 import BeautifulSoup
import time


class GPS_Indoors(Sensor.Sensor):
    #緯度:crd.latitude
    #経度:crd.longitude

    url = 'https://testpage.jp/tool/gps_ido_keido.php'
    GPSpage = requests.get(url)
    soup = BeautifulSoup(GPSpage.content, "html.parser")

    GPS = soup.find('crd.latitude').text
    GPS = GPS.strip()

    print(soup)



def main():
    testcls = GPS_Indoors()


if __name__ == '__main__':
    main()
