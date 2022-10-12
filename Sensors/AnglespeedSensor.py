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
        try:
            while True:
                #event = sence.stick.wait_for_event()
                orientation = sence.get_orientation_degrees()
                print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))
                sence.show_letter("G",yellow)
                return orientation

        except KeyboardInterrupt:
            sence.clear()
            
    def update(self):
        self.Anglespeed = self.getvalue()
        print(self.Anglespeed)
         
    def reset(self):
        self.Anglespeed = None

#testrun
"""  
def main():
    testclass = AnglespeedSensor()
    testclass.update()
    testclass.reset()
    
    print(testclass.Anglespeed)
    sence.clear()
if __name__ == '__main__':
    main()
"""
