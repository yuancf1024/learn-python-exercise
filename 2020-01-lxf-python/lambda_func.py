a = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(a,)

# 通过对比可以看出，匿名函数lambda x: x * x实际上就是

def f(x):
    return x * x

# 匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
f = lambda x: x * x
print(f, f(5))