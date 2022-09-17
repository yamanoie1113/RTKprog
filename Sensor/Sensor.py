from abc import ABCMeta, abstractmethod

class Sensor(metaclass=ABCMeta):
    measure_val: float
    @abstractmethod 
    def getValue(self):
        pass

    def Update(self):
        pass