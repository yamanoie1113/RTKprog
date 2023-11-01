# coding: utf-8

import PositionMgmt

class Pospram_conf():

    array_counter= 0
    Max_array = 5

    GPS_getter = PositionMgmt.PositionMgmt()
    
    position = None

    #ENTERで設定する座標を確定,その他コマンド入力を受付
    def GET_Pos(self):
        while True:
            print("未入力ENTERで座標を確定,qで終了")
            get_key = input()

            if get_key == "":
                self.Write_Param()

            elif get_key == "q":
                break
        
    #パラメータファイルへの書き込み処理
    def Write_Param(self):
        print("WRITE")


def main():
    test = Pospram_conf()
    test.GET_Pos()

if __name__ == '__main__':
    main()