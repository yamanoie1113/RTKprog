# coding:utf-8
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Sensors import Timer

class timedebuge:

    def init(self):
        self.time=0
        pass

    def request(self,ob):

        self.time=170
        ob.getValue(self.time)
        


    def main():

        ti=timedebuge()
        ob=Timer()
        ti.request(ob)
