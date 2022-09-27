from curses import KEY_DC, qiflush


class PID:

    #pid
    def PID(self):

        self.limit=100
        self.diff[0]=self.diff[1]=0.0
        self.integral=0
        self.DELTAT=0.01

        self.resetFlg=True

    def PID2(self,delta):
        self.PID()
        self.DELTAT=delta

    def set_limit(self,limit):
        self.limit=limit

    def set_target(self,t):
        self.target=t

    
    def get_operation(self,value):

        self.buf[256]

        self.diff[0]=self.diff[1]
        self.diff[1]=self.target-value
        self.prev_i=self.integral

        self.delta=(self.diff[1]-self.diff[0])/self.DELTAT
        self.integral+=(self.diff[0]+self.diff[1])/2.0*self.DELTAT

        if self.resetFlg:
            self.delta=float(0.0)
            self.integral=float(0.0)
            self.resetFlg=False

        if self.integral>11.0:
            self.integral=11.0

        if self.integral<-11.0:
            self.integral=-11.0

        self.val=self.diff[1]*self.Kp + self.delta*self.Kd +self.integral*self.Ki

        if self.debug:

            self.sprintf(self.buf,"pid:(float(%3.1),self.diff:float(%4.2) d:float(%4.2) i:float(%4.2) op:float(%5.3)",self.target,value,self.diff[1],self.delta,self.integral,self.val)
            self.msg_log (self.buf) 

        if self.val>self.limit:
            self.val=self.limit

        if self.val<-self.limit:
            self.val=-self.limit

        return self.val
        


    def set_Kp(self,kp):

        self.Kp=kp


    def set_Ki(self,ki):

        self.Ki=ki

    def set_Kd(self,kd):

        self.Kd=kd

    def get_integral(self):

        return self.integral

    def reset_param(self):

        if self.debug:
            self.msg_f("reset PID",1)
        self.diff[0]=self.diff[1]=float(0.0)
        self.integral=0

    def get_target(self):

        return self.target

    def set_deltat(self,delta):

        self.DELTAT=delta





