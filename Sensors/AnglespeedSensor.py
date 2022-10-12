# coding:utf-8

from abc import abstractmethod
from sense_hat import SenseHat
import Sensor

sence = SenseHat()
yellow = (255,255,0)

Anglespeed: float 
class AnglespeedSensor(Sensor.Sensor):
    
    def __init__(self):
        pass
    
    def getvalue(self):
        sense = SenseHat()
        raw = sense.get_gyroscope_raw()
        print("x: {x}, y: {y}, z: {z}".format(**raw))

        # alternatives
        print(sense.gyro_raw)
        print(sense.gyroscope_raw)
        return raw

    def update(self):
        self.Anglespeed = self.getvalue()
        print(self.Anglespeed)
         
    def reset(self):
        self.Anglespeed = None

#testrun
def main():
    testclass = AnglespeedSensor()
    testclass.update()
    testclass.reset()
    
    print(testclass.Anglespeed)
    sence.clear()
if __name__ == '__main__':
    main()
