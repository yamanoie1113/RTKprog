import time
count=0
count2=0
print("perf_counter")
for j in range(10):
    start = time.perf_counter()
    time.sleep(1)
    count+=1
    count2+=(time.perf_counter() - start)
    if count==5:
        print(round(count2),"5秒経過")
    else:
        print(round(count2))
        pass