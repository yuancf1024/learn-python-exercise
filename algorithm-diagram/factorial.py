'''计算阶乘的递归函数'''
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

print(fact(3))