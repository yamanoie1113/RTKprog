import pandas as pd

class LowpassTest():
    sampling = 240  #サンプリング周波数
    time_constant = 0.5 #時定数

    lastLPF_X = 0.0   #LPF_Xの前回値
    lastLPF_Y = 0.0   #LPF_Yの前回値


    X_rate = 0.04  #X減衰率
    Y_rate = 0.48  #Y減衰率

    dummy_file = '/Users/takak/OneDrive/ドキュメント/GitHub/RTKplog2/LOG/GPS_Dummy'
    gps_df = None



    def __init__(self):
        pass

    def filtering(self,input_val):
        LPF_X = (1 - self.X_rate)* input_val[0] + self.X_rate *self.lastLPF_X
        LPF_Y = (1 - self.Y_rate)* input_val[1] + self.Y_rate *self.lastLPF_Y

        self.lastLPF_X = LPF_X
        self.lastLPF_Y = LPF_Y
        return LPF_X,LPF_Y



    def filtering2(self,input_val):
        LPF = self.time_constant/(self.sampling + self.time_constant) * self.lastLPF + self.sampling/(self.sampling + self.time_constant) * input_val

        self.lastLPF = LPF
        return LPF
    

    #gpsのダミー読み込み
    def get_gps_dummy(self):

        #csvファイルから座標のみ抽出
        df = pd.read_csv(self.dummy_file)
        #数値だけにする
        self.gps_df = df.select_dtypes(include=['number'])

        """
        for prm in numeric_data:
            if not prm:
                continue
            self.gps_list.append(prm)
        """

        #print(numeric_data)

    def filtering_test(self):
        self.gps_df.plot()

        


def main():
    result=[]

    tester = LowpassTest()
    tester.get_gps_dummy()

    for gps in tester.gps_df:
        tmp = tester.filtering_test()
        result.append(tmp)
        print(gps)


    #print(result)


if __name__ == '__main__':
    main()