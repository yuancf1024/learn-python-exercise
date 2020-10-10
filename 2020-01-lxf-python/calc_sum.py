# 通常情况下的求和函数
'''
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
'''
'''
但是，如果不需要立刻求和，而是在后面的代码中，
根据需要再计算怎么办？可以不返回求和的结果，
而是返回求和的函数：
'''
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

# 调用lazy_sum()时，返回的并不是求和结果，而是求和函数
f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())

# 请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)