from abc import abstractmethod


Anglespeed: float 
class AnglespeedSensor(Sensor):
    
    @abstractmethod 
    def getValue(self):
        pass #角速度取得
    
    def Update(self):
        pass

    def Reset(self):
        pass