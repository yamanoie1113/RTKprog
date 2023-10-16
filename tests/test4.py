import concurrent
import concurrent.futures

class Calc:
    def __init__(self, a):
        self.a = a

    def calc(self, n):
        return self.a + n

class Process:
    def __init__(self):
        self.process_list = []
        self.executor = concurrent.futures.ProcessPoolExecutor(max_workers=4)
        # self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)
        self.calc = Calc(10)  # 処理を行うクラスのインスタンス
        self.hoge = 3  # インスタンス変数

    def _process_bad(self, n):
        res = self.calc.calc(n) * self.hoge
        return res

    @staticmethod
    def _process(calc, n, hoge):
        res = calc.calc(n) * hoge
        return res

    def start_process(self, n):
        # 実行部
        # self.process_list.append(self.executor.submit(self._process_bad, n))  # NG
        self.process_list.append(self.executor.submit(self._process, self.calc, n, self.hoge))  # OK

    def get_result(self):
    # 省略





if __name__ == "__main__":
    process = Process()
    for i in range(10):
        process.start_process(i)
    result = process.get_result()
    print(result)