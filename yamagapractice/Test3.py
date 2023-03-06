from multiprocessing import Process, Value
import time
import Test

class Test3:
    def __init__(self):
        self.count = Value('i', 0)

    def process(self):
        print('Run process')
        self.count.value = 100 #countを書き換え
        print(self.count.value)

    def process2(self):
        print('Run process')
        tes=Test.Test()
        self.count.value = tes.Re() #countを書き換え
        print(self.count.value)


    def main(self):
        print(self.count.value)
        p = Process(target=self.process)
        p2=Process(target=self.process2)

        p2.start()
        p.start()

        #time.sleep(1) #特に必要ないですが念の為。

        #print(self.count.value)

if __name__ == "__main__":
    t = Test3()
    t.main()
