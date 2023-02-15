list_a = [0,0,0,0,0,None]
#県名のリストを追加
list_b = [0,0,0,0]
list_q=[[1,2,3],[1,1,1]]

print(list_a[4])
number=0
a=True
while a:
    if list_a[number]==None:

        break
    else:
        print(list_a[number])
        number+=1
        

print(list_q[0])
print(list_q[1])
countnum=0
judgefirst=True

while judgefirst:#trueかfalseか
            
            #走法
            #while self.walkerfirst:
            if list_a[countnum]==None:#walkerの配列がなくなったら終了
                #self.state=self.timejudge.judge(counter[self.countnum])#timejudgeにカウント数を送る
                #mwalker[self.number1].left_run(param[self.number1][self.N1])#走法にGo(曲線)
                print("ok")
                countnum+=1
                co=0
                Statment=True
                state=True
                while Statment:
                    print("待ち1")
                    pass
                    co+=1
                    if co==5:
                        state=False

                    if state==False:
                        Statment==False
                        break

                #直線
                state=True
                Statment==True
                #state=self.timejudge.judge(counter[self.countnum])
                print("ok2")
                #mwalker[self.number2].set_run(param[self.number2][self.N2])#走法にGo(直線)
                #mwalker[self.number1].left_run(param[self.number2][self.N2])

                #if counter[self.countnum]==999:

                
                while Statment:
                    print("待ち2")
                    pass
                    co+=1
                    if co==5:
                        state=False

                    if state==False:
                        Statment==False
                        break
                    
                    #print("なぜだろう",self.judgefirst)
                    #stateを戻す

            else:
                judgefirst=False
                print("灰とおりました")

            if judgefirst==False:
                print(judgefirst)
                print("owari")
            break

print(judgefirst)
print("終了")