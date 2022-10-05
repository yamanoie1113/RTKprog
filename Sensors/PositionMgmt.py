from multiprocessing import get_start_method
import nmea_get
import time

class PositionMgmt():
    while True:
        aaa = nmea_get.nmea_Get()
        position = aaa.get()
        if position != None:
            print(position)



"""
while True:
    tmp = test2.get_str()
    print(tmp)
"""