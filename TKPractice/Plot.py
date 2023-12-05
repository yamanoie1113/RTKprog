# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt


class Plot():
    array_X = np.array([0])
    array_Y = np.array([0])

    #プロット用の配列追加関数
    def add(self,x,y):
        self.array_X = np.append(self.array_X,[x])
        self.array_Y = np.append(self.array_Y,[y])

    
    def plot(self,filename):
        hmin = 0
        hmax = 10
        plt.plot(self.array_X, self.array_Y,label ="m",marker="o" )
        plt.hlines(0, hmin, hmax, colors='red',)
        print(self.array_X)
        print(self.array_Y)
        # 凡例の表示
        plt.legend()
        plt.savefig(filename)
        plt.show()


def main():
    i = 0
    filename = "test.png"
    testclass = Plot()

    while i <5:
        testclass.add(i,i)
        i+=1
    
    testclass.plot(filename)

if __name__ == "__main__":
    main()