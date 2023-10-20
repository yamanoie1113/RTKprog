# coding:utf-8
from abc import abstractmethod
from sense_hat import SenseHat
import sys
import pathlib
import threading
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')

from Sensors import Sensor

sence = SenseHat()
yellow = (255,255,0)



class TurnAngleSensor(Sensor.Sensor):
    turnAngle = 0.0
    #合計
    ang_total = 0.0

    #前回旋回後の角度
    last_ang = 0.0

    #走行体が最終的に向きたい角度（finishang?）
    base_ang = 0.0

    def __init__(self):
        #self.turnAngle = self.update()
        pass

    def ang_init(self):
        self.thread1 = threading.Thread(target=self.update)
        self.thread1.start()

    def getvalue(self):
            return self.turnAngle  #ここ返すのangtotalかも
            #return self.ang_total

    def update(self):
        
        #print("p: {pitch}, r: {roll}, y: {yaw}".format(**gyro))
        while True:
            gyro = sence.get_orientation_degrees()
            self.turnAngle = gyro["yaw"]
            

            #360をまたいだか判定
            if abs(self.turnAngle - self.last_ang) < 180:
                self.ang_total += self.turnAngle

            else :
                self.ang_total += (360 - self.last_ang) + self.turnAngle

            self.last_ang = self.turnAngle


            #print(self.turnAngle)

    def reset(self):
        self.turnAngle = None
        print("turnAngle reset")
  
#testrun

def main():
    testclass = TurnAngleSensor()
    testclass.ang_init()
    
    while True:
        angle = testclass.getvalue()
        print(angle)

if __name__ == '__main__':
    main()