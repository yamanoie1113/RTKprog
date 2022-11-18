import Run,Timer2,TKTimeJudge,time,threading

def main():
    while True :
        jclass = TKTimeJudge.TKTimeJudge()
        result = jclass.judge()
        print("result:",end="")
        print(result)


        #10秒ごとに動きが変化
        if result  == True :
            #偶数 カーブ
            print("curve")

        else :
            #奇数 シンプルラン
            print("simple")

        time.sleep(1)

if __name__=="__main__":
     main()