from multiprocessing import Process, Value
import time

def func1(a: Value):
    print("[1]スタート")
    time.sleep(5)
    print("5秒経過")
    a.value = 1

def func2(a: Value):
    print("[2]スタート")
    while True:
        if a.value == 1:
            print("値を通知")
            break

if __name__ == "__main__":
    a = Value('d', 0)
    func1_proc = Process(target=func1, args=(a,))
    func2_proc = Process(target=func2, args=(a,))
    func1_proc.start()
    func2_proc.start()

    func1_proc.join()
    func2_proc.join()
    print(a.value)