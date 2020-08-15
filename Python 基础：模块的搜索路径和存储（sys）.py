import sys

print(type(sys.path))
print(sys.path)

for i in sys.path:
    print(i)

# 添加搜索路径
# sys.path.append(dir)

# 模块的加载顺序
# - 搜索内存中已经加载的模块
# - 搜索python的内置模块
# - 搜索sys.path路径