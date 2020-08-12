class A():
    def __init__(self):
        self.name = 'haha'
        self.age = 18
    # 此功能，是对类变量进行读取操作的时候应该执行的函数功能
    def fget(self):
        print('我被读取了')
        return self.name
    # 模拟的是对变量进行写操作的时候执行的功能
    def fset(self):
        print('我背写入了')
        self.name = '图灵学院:' + name
    # 模拟的是删除变量的时候进行的操作
    def fdel(self):
        pass
    # fget, fset, fdel, doc四个参数顺序是固定的
    # 第一个参数代表读取的时候需要调用的函数
    # 第二个参数代表写入的时候需要调用的函数
    # 第三个参数代表删除
    # 第四个参数代表说明文档
    name2 = property(fget, fset, fdel, '这是一个property的例子')

a = A()
print(a.name)
print(a.name2)