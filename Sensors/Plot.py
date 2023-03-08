import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

class Plot():
    x = []
    y = []
    fig = plt.figure(figsize=(500000,500000))

    def __init__(self):
        plt.title('Title',fontsize=15)
        plt.xlabel('X',fontsize=10)
        plt.ylabel('Y',fontsize=10)

    def plotting(self,x,y):
        #座標（x,y）にplot
        plt.plot(x,y,marker='.')


    def update(self,x, y):
        #グラフの更新
        # 現在のグラフを消去する
        plt.cla()
        # データを更新 (追加) する
        self.x.append()
        self.y.append()
        # 折れ線グラフを再描画する
        plt.plot(x, y)

    def animePlot(self,x,y):
        params = {
        'fig': self.fig,
        'func': self.update,  # グラフを更新する関数
        'fargs': (x, y),  # 関数の引数 (フレーム番号を除く)
        'interval': 10,  # 更新間隔 (ミリ秒)
        'frames': np.arange(0, 10, 0.1),  # フレーム番号を生成するイテレータ
        'repeat': False,  # 繰り返さない
        }
        anime = animation.FuncAnimation(**params)



def main():
    test = Plot()
    test.animePlot(1,1)
    test.animePlot(2,2)
    test.animePlot(3,3)


if __name__ == '__main__':
    main()