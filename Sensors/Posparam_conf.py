# coding: utf-8
import sys
import pathlib,csv
import PositionMgmt

current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
dir = pathlib.Path(__file__).resolve().parent
dir = (str(dir) + '/../parameter/')

class Posparam_conf():

    array_counter= 0
    Max_array = 5

    GPS_getter = PositionMgmt.PositionMgmt()
    
    position = None

    while True:
        #パラメータファイルの種類を選択
        print("設定するパラメータファイルの種類を選択")
        print("八の字（Normal）はn、REIWAはr、Circuitはc、直線テストはtsp、その他新規ファイルは o,終了するにはqを入力して下さい")
        
        get_key = input()

        if get_key == "n":
            print("八の字コース")
            paramfile = "Normal_Pos.prm"
            break

        elif get_key == "r":
            print("REIWAポイントコース")
            paramfile = "REIWA_Pos.prm"
            break

        elif get_key == "c":
            print("サーキットコース")
            paramfile = "Circuit_Pos.prm"
            break
        
        elif get_key == "tsp":
            print("Test_Straight_Pos")
            paramfile = "Test_Straight_Pos.prm"
            break
        
        elif get_key == "o":
            print("新規ログファイル名を入力")
            paramfile = input() + ".prm"
            break
        


        elif get_key == "q":
            sys.exit()
        


    #paramfile = "PosPram.prm"

    #ENTERで設定する座標を確定,その他コマンド入力を受付
    def GET_Pos(self):
        #prmファイルの初期化
        self.clear()

        self.f = open(dir + self.paramfile,"a")
        while True:
            print("未入力ENTERで座標を確定,dでprmファイルを初期化、qで終了")
            get_key = input()

            if get_key == "":
                self.Write_Param()
            
            if get_key == "d":
                self.clear()

            elif get_key == "q":
                break
        
        self.f.close()
        print("END")
        
    #prmファイルへの書き込み処理
    def Write_Param(self):

        print("WRITE")
        pos = self.GPS_getter.Conf_Param()

        self.f.write(str(pos[0]) + "," + str(pos[1]) + "\n")

        print("setpos:" + str(pos))

    #パラメータファイルの内容を消去する
    def clear(self):
        f = open(dir + self.paramfile,"w")
        f.close()
        print(self.paramfile + " cleared")





def main():
    test = Posparam_conf()
    test.GET_Pos()

if __name__ == '__main__':
    main()