# 2020-01-12 Bug: 程序运行没有输出
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

add_end()