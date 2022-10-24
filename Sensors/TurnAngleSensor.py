# coding:utf-8
from abc import abstractmethod
from sense_hat import SenseHat
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')

from Sensors import Sensor0.2

sence = SenseHat()
yellow = (255,255,0)


class TurnAngleSensor(Sensor.Sensor):
    turnAngle: float

    def __init__(self):
        self.turnAngle = self.update()

    def getvalue(self):
            #event = sence.stick.wait_for_event()
            return gyro

    def update(self):
        gyro = sence.get_orientation_degrees()
        #print("p: {pitch}, r: {roll}, y: {yaw}".format(**gyro))
        sence.show_letter("G",yellow)
        self.turnAngle = gyro["yaw"]
        #print(self.turnAngle)

    def reset(self):
        self.turnAngle = None
        print("turnAngle reset")

#testrun

def main():
    testclass = TurnAngleSensor()
    testclass.update()

    print("before_reset")
    print(testclass.turnAngle)
    """
    testclass.reset()

    print(testclass.turnAngle)

    """

if __name__ == '__main__':
    main()