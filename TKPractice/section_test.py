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
    try:
        while True :
            jclass = TKTimeJudge.TKTimeJudge()
            result = jclass.test() #タイムジャッジのテスト関数
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
                runner.set_param(5,0,0,0,0)

            runner.run(mMotorMgmt)
            time.sleep(1)

    except KeyboardInterrupt:
        pass

if __name__=="__main__":
     main()