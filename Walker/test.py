import sys
from abc import ABCMeta,abstractmethod

class Run(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def set_param(self):
        pass

    @abstractmethod
    def reset_param(self):
        pass



