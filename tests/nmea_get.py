import socket

# サーバーIPとポート番号
IPADDR = "localhost"
PORT = 5555

# AF_INET：IPv4形式でソケット作成(省略可)
sock_sv = socket.socket(socket.AF_INET)
# IPアドレスとポート番号でバインド、タプルで指定
sock_sv.connect((IPADDR, PORT))

# 接続・受信の無限ループ
while True:

    while True:
        # ソケットから byte 形式でデータ受信
        data = sock_sv.recv(1)
        if data==b"$":
            break

    data = sock_sv.recv(2)
    if data==b'GN' or data==b'GP'  or data==b'GA' or data==b'GB' or data==b'GQ':
        nmea_data=data
        while True:
            tmp = sock_sv.recv(1)
            nmea_data += tmp
            if tmp==b'\n':
                break
        print(nmea_data)


# クライアントのソケットを閉じる
sock_sv.close()