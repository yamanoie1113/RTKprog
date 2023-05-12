# coding:utf-8
import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')

import math
from Judgement import Judge
from Sensors import TurnAngleSensor as TASensor,PositionMgmt as PMgmt

class TurnAngleJudge(Judge.Judge):

    current_angle=0.0
    finish_angle=0.0

    diff_angle = 0.0
    previos_angle = 0.0
    start_x = 0.0
    start_y = 0.0

    #instance
    angget = TASensor.TurnAngleSensor()


    def __init__(self):
        #旋回角度取得
        #sensehatからジャイロ取得


        #sectionからstatusを渡す位置を考える initかsetparamか
        #とりあえずダミーを設置する
        #status = float(input("input_finish_angle?"))

        #self.set_param(status)
        self.get_Position()

        self.get_ang()

    def get_Position(self):
        #現在値取得メソッド

        self.pget = PMgmt.PositionMgmt()
        #positionXY = pget.getvalue()

        #start_x,start_yに座標をセット
        #self.start_x = positionXY[0]
        #self.start_y = positionXY[1]

        #test_position
        self.start_x = 1
        self.start_y = 0

    def get_ang(self):
        self.current_angle = self.angget.getvalue()

    def judge(self,XYpos):
        #print("ANGLE_judge")

        #目標地点goal_x,goal_yを設定
        goal_x = XYpos[0]
        goal_y = XYpos[1]
        
        #現在地の更新
        self.get_ang()
        
        #目標地点までの旋回角度を計算 finish_angleを更新
        self.CalcAng(goal_x,goal_y)
                
        #前回地と現在角度の差を求める
        self.diff_angle = abs(self.current_angle - self.previos_angle)
        
        
        #現在角度と差分を表示
        print("current:" + str(self.current_angle) + "\n" + " diff:" + str(self.diff_angle)+ "\n" + "\033[2A",end='')
        
        #差分が180度を越えたか判定

        
        
<<<<<<< HEAD
        if self.finish_angle >= self.current_angle :

            if self.get_ang() >= self.finish_angle :
=======
        
        if self.diff_angle < 180:
            #通常の処理
        
            if self.current_angle > self.finish_angle :

>>>>>>> e8bf13557ebc2f50cc33eefbab5c4efd6a8c4a13
                return True

            else :
                return False
            
            if self.current_angle < self.finish_angle :
                return False

            else :
                return True
        else :
            pass
            #360度を超えていた時の処理


    #目標地点との角度の計算 self.finish_angleに結果格納
    def CalcAng(self,goal_x,goal_y):
        #前回の値を前回値として保存
        self.previos_angle = self.finish_angle


        #現在地取得
        self.get_Position()
        start_x = 0.0
        start_y = 0.0

        x = (goal_x - start_x)
        y = (goal_y - start_y)

        r = math.atan2(y,x)

        if r < 0 :
            r = r + 2 * math.pi

        self.finish_angle = math.floor(r * 360 / (2 * math.pi))


    def set_param(self,status):
        #print(self.current_angle)

        #終了角度をセクションから受け取る場合
        self.finish_angle = status

        #旋回したい角度をセクションから受け取る場合
        #self.finish_angle = self.current_angle + status
               



#testrun
def main():
    testclass = TurnAngleJudge()
    judge_val = False
    
    """
    #calc_Test
    rtnAng = testclass.CalcAng(5,5)
    print(rtnAng)
    """
    
    #Judge_Test
    array=[5,5]
    while judge_val == False:
        judge_val = testclass.judge(array)
        #print(testclass.angget.getvalue(),":",testclass.finish_angle)

    print("-------------------------END-------------------------------")

if __name__ == '__main__':
    main()