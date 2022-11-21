import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Walker import Run
import Timer2,TKTimeJudge,time,threading


def main():
    runner =Run.Run()
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

        time.sleep(1)

if __name__=="__main__":
     main()