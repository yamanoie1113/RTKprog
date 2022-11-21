import Run,Timer2,TKTimeJudge,time,threading

def main():
    while True :
        jclass = TKTimeJudge.TKTimeJudge()
        result = jclass.test()
        print("result:",end="")
        print(result)


        #10秒ごとに動きが変化する予定
        if result  == True :
            #カーブとか
            print("curve")

        else :
            #シンプルラン
            print("simple")

        time.sleep(1)

if __name__=="__main__":
     main()