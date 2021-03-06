import socket

# 模拟服务器的函数
def serverFunc():
    # 1. 建立socket
    # socket.AF_INET：使用IPV4 protocol
    # socket.SOCK_DGRAM：使用UDP通信
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 绑定IP和PORT
    # 127.0.0.1：这个IP地址代表的是自己机器本身
    # 7852：随手指定的端口号
    # 地址是一个tuple类型，（IP, PORT）
    addr = ('127.0.0.1', 7852)
    sock.bind(addr)

    # 3. 接受对方消息
    # 等待方式为死等，没有其他方式
    # recvfrom接受的返回值是一个元组，前一项表示数据，后一项表示地址
    # 参数的含义是缓冲区大小
    # rst = sock.recvfrom(500)
    data, addr = sock.recvfrom(500)
    print(data)
    print(type(data))

    # 4. 发送过来的数据是bytes格式，必须通过解码才能得到str格式的内容
    text = data.decode()
    print(text)
    print(type(text))

    # 5. 给对方返回的消息
    rsp = 'Ich hab keine Hunge'
    # 发送的数据需要编码成bytes格式，默认是utf8
    data = rsp.encode()
    sock.sendto(data, addr)

if __name__ == '__main__':
    print('Starting server.......')
    serverFunc()
    print('Ending server......')