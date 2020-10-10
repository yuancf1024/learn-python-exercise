def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1 , f2, f3 = count()

print(f1(),f2(),f3())

'''
如果一定要引用循环变量怎么办？方法是再创建
一个函数，用该函数的参数绑定循环变量当前的值，
无论该循环变量后续如何更改，
已绑定到函数参数的值不变：
'''
# 缺点是代码较长，可利用lambda函数缩短代码。
def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count()
print(f1(), f2(), f3())