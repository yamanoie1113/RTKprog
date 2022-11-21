import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Walker import Run
from Sensors import MotorMgmt
import Timer2,TKTimeJudge,time,threading


def main():
    runner =Run.Run()
    mMotorMgmt = MotorMgmt.MotorMgmt()
    while True :
        jclass = TKTimeJudge.TKTimeJudge()
        result = jclass.test()
        print("result:",end="")
        print(result)


        #10秒ごとに動きが変化する予定
        if result  == True :
            #カーブとか
            print("curve")
            runner.set_param(0,0,0,0,0)

        else :
            #シンプルラン
            print("simple")
            runner.set_param(30,0,0,0,0)

        runner.run(mMotorMgmt)
        time.sleep(1)

if __name__=="__main__":
     main()