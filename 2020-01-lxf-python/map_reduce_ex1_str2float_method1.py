# -*- coding: utf-8 -*-

'''方法一： 使用lambda
'''
from functools import reduce

def str2float(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}
    flag = len(s) - s.index('.') - 1
    s = s.replace('.', '')
    def char2num(s):
        return DIGITS[s]
    result = reduce(lambda x, y: x*10 + y, map(char2num,s))/10**flag
    return result
    pass

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')