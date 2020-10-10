# -*- coding: utf-8 -*-

'''方法二
'''
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}

def str2float(s):
    def f1(s):
        return DIGITS[s]
    for i in range(len(s)):
        if s[i]=='.':
            s1 = s[:i]
            s2 = s[i+1:]
    def f2(x, y):
        return x * 10 + y
    return reduce(f2, map(f1, s1)) + reduce(f2, map(f1, s2))/pow(10, len(s2))
    pass

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')