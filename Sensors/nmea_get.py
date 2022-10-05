#coding:utf-8
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

    while True:

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
            print("getGGA")
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
                print(list_GGA[2],list_GGA[4])
                return list_GGA[2],list_GGA[4]


  
def main():
    while True:
        #print("enter1")
        get()


if __name__ == '__main__':
    main()


