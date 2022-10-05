# coding:utf-8
from ast import Delete
from tkinter import END
from tracemalloc import start
from section.SectionMgmt import SectionMgmt

from section.SectionRun import SectionRun


class Mgmt:

    UNDEFINED=0
    START=1
    INIT_SPEED=2
    SPEED=3
    END=4

    def __init__(self):



        #
        self.mState=self.UNDEFINED
        self.mSsm=SectionMgmt()
        
    def run(self):

        if self.mState == self.UNDEFINED:
            self.execUndefined()
            
        elif self.mState == self.START:
            self.execStart()

        elif self.mState == self.INIT_SPEED:
            self.initSpeed()

        elif self.mState == self.SPEED:
            self.execSpeed()

        elif self.mState == self.END: 
            self.finish()
        else:
            return True

        return False

    

    def excecUndefined(self):
        #キャリブレーション？
        self.mState=self.START

    def execStart(self):
        self.mstate=self.INIT_SPEED


    def initSpeed(self):
        self.mSsm.init()
        self.mState=self.SPEED

    def execSpeed(self):
        if self.mSsm.run():
            del self.mSsm
            self.mstate=self.END

    def finish(self):
        #相談
        pass






    