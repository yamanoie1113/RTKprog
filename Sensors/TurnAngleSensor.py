# coding:utf-8

from abc import abstractmethod
from sense_hat import SenseHat
import Sensor

sence = SenseHat()
yellow = (255,255,0)

turnAngle: float 
class TurnAngleSensor(Sensor.Sensor):
    
    def __init__(self):
        pass
    
    def getvalue(self):
            #event = sence.stick.wait_for_event()
            orientation = sence.get_orientation_degrees()
            print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))
            sence.show_letter("G",yellow)
            
            return orientation

    def update(self):
        self.turnAngle = self.getvalue()
        print(self.turnAngle)
         
    def reset(self):
        self.turnAngle = None

#testrun
"""
def main():
    testclass = TurnAngleSensor()
    testclass.update()
    testclass.reset()
    
    print(testclass.turnAngle)
    sence.clear()
if __name__ == '__main__':
    main()
"""