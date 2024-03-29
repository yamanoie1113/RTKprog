# coding:utf-8
import math
from ast import Num
#from curses import KEY_DC, qiflush
from math import nan


class PID:

        error_sum = 0
        error_pre = 0

        def __init__(self):
            pass
		
        def PID(self,kp,ki,kd,theta_goal,theta_current):
            
            #pidが小さい時
            '''
            if theta_current < 1 and theta_current > 0:
                theta_current = theta_current *100
            elif theta_current > -1 and theta_current < 0:
                theta_current = theta_current *10
            '''
            #print("goal:",theta_goal," current:",theta_current)

            #error = theta_goal*10 - theta_current*10# 偏差（error）を計算
            error = theta_goal - theta_current# 偏差（error）を計算
            
            #error_sum += error*0.5 # 偏差の総和（積分）を計算
            self.error_sum += error # 偏差の総和（積分）を計算
            #ki = 0
    
    		
            #error_diff = (error-error_pre) /0.1 # PI制御からの追加：1時刻前の偏差と現在の偏差の差分（微分）を計算
            error_diff = (error-self.error_pre) # PI制御からの追加：1時刻前の偏差と現在の偏差の差分（微分）を計算
    		
            m = (kp * error) + (ki * self.error_sum) + (kd * error_diff) # 操作量を計算
            
            #print("m",m)
            m = math.floor(m)
            if m >= 100:
                m = 90
            elif m <= -100:
                m = -90
            #print("m",m)
            self.error_pre = error
            
            

            return m
	
def main():
    mPID=PID()



if __name__=="__main__":
    main()

'''# 係数などの設定 --------------------
kp = 0.1 # 比例ゲイン
ki = 0.5 # 積分ゲインの値を大きくして，意図的に振動を発生させる
theta_start = 0.0 # 初期角度
theta_goal = 90.0 # 目標角度
time_length = 200 # 計測時間 
theta_current = theta_start # 現在角度
error_sum = 0.0 # 偏差の総和（積分）
#time_list = [0] # 時刻のリスト（描画用）
#theta_list = [theta_start] # 現在地のリスト（描画用）
kd = 0.5 # 微分ゲイン：急激な変化を抑える
error_pre = 0.0 # 1時刻前の偏差
# PI制御の時の数値を初期化
theta_start = 0.0; theta_current = theta_start; error_sum = 0.0; time_list = [0]; theta_list = [theta_start] 
'''

'''
# PID制御 -----------------------
for time in range(time_length):
    m, error_sum, error = PID(kp, ki, kd, theta_goal, theta_current, error_sum, error_pre) # 操作量を計算
    theta_current += m # 現在角度に操作量を足す（実際は，この操作量をもとにモータを動かす）
    error_pre = error # 一時刻前の偏差として保存しておく（D制御用）
    #time_list.append(time) # 描画用
    #theta_list.append(theta_current) # 描画用
'''

'''# 描画
plt.plot(time_list, theta_list, label="PID", color="blue") # PID制御のグラフを描画
plt.xlabel(r'$t$') 
plt.ylabel(r'$\theta$') 
plt.legend(loc='lower right') # 凡例を表示
plt.show() # グラフの表示
'''