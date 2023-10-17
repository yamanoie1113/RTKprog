print#coding:utf-8
import socket
import time

def get():
    
    # サーバーIPとポート番号

    IPADDR = "localhost"
    PORT = 2101
    
    # AF_INET：IPv4形式でソケット作成(省略可)

    sock_sv = socket.socket(socket.AF_INET)
    
    # IPアドレスとポート番号でバインド、タプルで指定
    sock_sv.connect((IPADDR, PORT))
    # 接続・受信の無限ループ
    
    #屋内テスト用コード
    #return 1,2



#本番用
    #print("GPS_loading....")
    while True:
        #実行速度の計算
        #start_time = time.perf_counter()
        

        while True:
            # ソケットから byte 形式でデータ受信
            data = sock_sv.recv(1)
            #print(data)

            if data==b"$":
                #print("break1")
                break
            

        data = sock_sv.recv(5)
        #print(data)
        if data==b'GNGGA':
            #debug
            #print("getGGA")
            GGA=data.decode('utf-8')
            while True:
                tmp = sock_sv.recv(1)
                GGA += tmp.decode('utf-8')
                if tmp==b'\n':
                    #print(tmp)
                    break
                    
                #GNGGAをカンマ区切りでリスト化
                list_GGA = GGA.split(",")

            if list_GGA[2] != '' and list_GGA[4] !='':
                #print(list_GGA[2],list_GGA[4])
                #print("NMEA_実行時間")
                #print(time.perf_counter() - start_time)
                return list_GGA[2],list_GGA[4]


def main():
    while True:
        start_time = time.perf_counter()        
        #print("enter1")
        get()
        print("NMEA_実行時間")
        print(time.perf_counter() - start_time)


if __name__ == '__main__':
    main()


