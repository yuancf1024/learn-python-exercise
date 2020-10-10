# -*- coding: utf-8 -*-
# L[0]的值应该迭代前就赋值
def findMinAndMax(L):
    if len(L) != 0:
        max = min = L[0]
        for i in L:
            if i >= max:
                max = i
        for j in L:
            if j <= min:
                min = j
        return (min, max)
    else:
        return (None, None)
print(findMinAndMax([7,1,3,9,5]))
# 测试

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
