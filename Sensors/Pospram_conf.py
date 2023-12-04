# coding: utf-8
import sys
import pathlib
import PositionMgmt

current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
dir = pathlib.Path(__file__).resolve().parent
dir = (str(dir) + '/../Sensors/')

class Pospram_conf():

    array_counter= 0
    Max_array = 5

    GPS_getter = PositionMgmt.PositionMgmt()
    
    position = None

    paramfile = "PosPram.csv"

    #ENTERで設定する座標を確定,その他コマンド入力を受付
    def GET_Pos(self):
        self.clear()
        self.f = open(self.paramfile,"a")
        while True:
            print("未入力ENTERで座標を確定,qで終了")
            get_key = input()

            if get_key == "":
                self.Write_Param()

            elif get_key == "q":
                break
        
        self.f.close()
        
    #パラメータファイルへの書き込み処理
    def Write_Param(self):
        print("WRITE")
        pos = str(self.GPS_getter.getvalue())
        self.f.write(pos + "\n")

    #パラメータファイルの内容を消去する
    def clear(self):
        f = open(self.paramfile,"w")
        f.close()





def main():
    test = Pospram_conf()
    test.GET_Pos()

if __name__ == '__main__':
    main()