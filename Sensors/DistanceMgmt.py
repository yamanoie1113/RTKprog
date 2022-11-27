import Sensor
#いや、距離計なんてなくね？
class DistanceSensor(Sensor.Sensor):
    distotal = 0.0
    startx  = 0.0
    starty = 0.0
    goalx = 0.0
    goaly = 0.0
    
    def __init__(self,distance_val):
        #self.distance_val = distance_val
        pass

    def getValue(self):
        #getval
        pass

    def Update(self):
        pass
        #distance_val = 0#updated val