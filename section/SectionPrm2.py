# coding:utf-8
import time
import os
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
#from Sensors import MotorMgmt
class SectionPrm2:
    #クラス変数
    curve=0
    straight=1

    def __init__(self):

        print("sectionprmです")


    def set_param(self,mnumber):#パラメータ設定
        #直線＝０
        if mnumber== 0:
            #カーブのパラメータ設定
            print("直線")

        #曲線＝１
        elif mnumber==1:
            print("曲線")


def main():
    msectionIdx=0
    dd=SectionPrm2()
    dd.set_param(msectionIdx)
    pass
    


if __name__=="__main__":
    main()

    #def set_Swalker():

        

        #pass


    #def set_Cwalker():


        #pass



    
        