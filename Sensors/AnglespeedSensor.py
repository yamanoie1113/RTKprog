from abc import abstractmethod
from sense_hat import SenseHat

sence = Sensehat()
yellow = (255,255,0)

Anglespeed: float 
class AnglespeedSensor(Sensor):
    
    @abstractmethod 
    def getvalue(self):
        try:
            while True:
                #event = sence.stick.wait_for_event()
                orientation = sence.get_orientation_degrees()
                print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))
                sence.show_letter("J",yellow)

        except KeyboardInterrupt:
            sence.clear()
    
    def update(self):
        pass

    def reset(self):
        pass