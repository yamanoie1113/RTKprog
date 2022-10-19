from Judgement.Judge import Judge


class DistenceJudge(Judge):
    
    mx=0    #X座標系　オブジェクト
    my=0    #Y座標系　オブジェクト
    mdir=0  #方位計   オブジェクト
    startpoint=0
    endpoint=0
    finishlength=0



    def init(self):
        #mdir.get_value
        #mydir.get_value()
        #mx.get_value()
        #my.get_value()
        #XYから値取得
        self.endpoint=self.find_end_point()

        #座標計算
    def find_end_point(self):

        #移動距離、現在の座標、走行体の向きから終了座標を求める
        endpoint=0
        return endpoint
    
    def judge():

        #X、Y座標を取得し、その値が基準値をこえていたらtrueを返す。それ以外はfalse

        pass

    def set_param(self,judgevalue):
        self.finishlength=judgevalue

        pass
