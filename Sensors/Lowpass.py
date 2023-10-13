
class Lowpass():
    sampling = 240  #サンプリング周波数
    time_constant = 0.5 #時定数

    lastLPF_X = 0.0   #LPF_Xの前回値
    lastLPF_Y = 0.0   #LPF_Yの前回値

<<<<<<< HEAD
    X_rate = 0.2  #X減衰率
    Y_rate = 0.4  #Y減衰率
=======
    rate = 0.2645 #減衰率
>>>>>>> fcdefbfc76c33bd90ef0ace1f35a15761b929cbc

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
    

def main():
    tesclass = Lowpass()
    output = tesclass.filtering(1.0)
    print(output)


if __name__ == '__main__':
    main()