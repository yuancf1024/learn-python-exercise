'''以下函数允许计算两个数的乘积，请稍加改造
变成可接收一个或多个数并计算乘积
'''
# -*- coding: utf-8 -*-
def product(*args):
    cc=1
    if len(args)==0:
        raise TypeError
    else:
        for i in args:
            cc *= i
        return cc

print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')