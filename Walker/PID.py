# coding:utf-8
from ast import Num
from curses import KEY_DC, qiflush
from math import nan


class PID:

    # コンストラクタ
    def __init__(self,delta=0.01):

        # クラス変数
        self.limit=100
        self.diff = [nan for i in range(2)]
        self.diff[0]=self.diff[1]=0.0
        self.last_integral = [nan for i in range(40)]
        self.integral=0
        self.DELTAT=delta
        self.KPID={"kp":nan,"ki":nan,"kd":nan}
        self.resetFlg=True
        self.tgt_limit
        self.sec
        self.cnt
    
    #デストラクト
    def __del__(self):
        pass


    #デルタ設定
    def set_delta(self,delta):
        self.DELTAT=delta

    #リミット設定
    def set_limit(self,limit):
        self.limit=limit

    #目標値設定
    def set_target(self,t):
        self.target=t

    #オペレーション取得
    def get_operation(self,value):

        self.buf[256]

        self.diff[0]=self.diff[1]
        self.diff[1]=self.target-value
        self.prev_i=self.integral

        self.delta=(self.diff[1]-self.diff[0])/self.DELTAT
        #self.integral+=(self.diff[0]+self.diff[1])/2.0*self.DELTAT
        self.last_integral[self.cnt]=(self.diff[0]+self.diff[1])/2.0*self.DELTAT
        self.integral+=self.last_integral[self.cnt]
        self.integral-=self.last_integral[(self.cnt+1)%self.sec]

        self.cnt=(self.cnt+1)%self.cnt

        if (self.resetFlg):
            self.diff[0]=self.diff[1]
            self.delta=float(0.0)
            self.integral=float(0.0)

            for i in range(self.sec):
                self.last_integral[i]=0.0
            
            self.cnt=0
            self.resetFlg=False

#積分地のオーバーを防ぐ
        '''
        if (self.integral)>11.0:
            self.integral=11.0

        if (self.integral)<-11.0:
            self.integral=-11.0
        '''
        
        self.val=self.diff[1]*self.KPID["kp"]+self.delta*self.KPID["ki"]+self.integral*self.KPID["kd"]

        #if (self.debug):

            #self.sprintf(self.buf,"pid:(float(%3.1),self.diff:float(%4.2) d:float(%4.2) i:float(%4.2) op:float(%5.3)",self.target,value,self.diff[1],self.delta,self.integral,self.val)
            #self.msg_log (self.buf) 

        if (self.val>self.limit):
            self.val=self.limit

        if (self.val<-self.limit):
            self.val=-self.limit

        return self.val
        

        #PID設定
    def set_Kpid(self,kp,ki,kd):

        self.KPID["kp"]=kp
        self.KPID["ki"]=ki
        self.KPID["kd"]=kd
    #def set_Ki(self,ki):

        

    #def set_Kd(self,kd):

    def get_diff(self):

        return self.diff[1]

        #積分値取得
    def get_integral(self):

        return self.integral

        #パラメータリセット
    def reset_param(self):
        self.diff[0]=self.diff[1]=0.0
        self.integral=0
        self.resetFlg=True

        #ターゲット取得
    def get_target(self):

        return self.target

        #デルタ設定
    def set_deltat(self,delta):

        self.DELTAT=delta





