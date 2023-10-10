
class Lowpass():
    sampling = 240  #サンプリング周波数
    time_constant = 0.5 #時定数

    lastLPF = 0.0   #LPFの前回値

    rate = 0.6  #減衰率

    def __init__(self):
        pass

    def filtering(self,input_val):
        LPF = (1 - self.rate)* input_val + self.rate *self.lastLPF
        self.lastLPF = LPF
        return LPF       



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