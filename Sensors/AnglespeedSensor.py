# coding:utf-8

from abc import abstractmethod
from sense_hat import SenseHat
import math

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
        #print("x: {x}, y: {y}, z: {z}".format(**raw))

        # alternatives
        #print(sense.gyro_raw)
        #print(sense.gyroscope_raw)
        return raw

    def update(self):
        self.Anglespeed = self.getvalue()
        print(self.Anglespeed)

    def CalcAng(goal_x,goal_y):
        start_x = 0.0
        start_y = 0.0



        x = (goal_x - start_x)
        y = (goal_y - start_y)

        r = math.atan2(y,x)

        if r < 0 :
            r = r + 2 * math.pi

        angle = math.floor(r * 360 / (2 * math.pi))

        print(angle)


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
