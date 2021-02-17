import socket

# 模拟服务器的函数
def serverFunc():
    # 1. 建立socket
    # socket.AF_INET：使用IPV4 protocol
    # socket.SOCK_DGRAM：使用UDP通信
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
