from abc import ABCMeta, abstractmethod

class Sensor(metaclass=ABCMeta):
    float measure_val
    @abstractmethod 

    def getValue(self):
        pass

    def update(self):
        pass