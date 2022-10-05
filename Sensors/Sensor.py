from abc import ABCMeta, abstractmethod

class Sensor(metaclass=ABCMeta):
    measure_val: float
    
    @abstractmethod 
    def getvalue(self):
        pass

    @abstractmethod
    def update(self):
        pass