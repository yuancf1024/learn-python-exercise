# 生成 list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(range(1,11))
print(list(range(1,11)))

# 生成[1x1, 2x2, 3x3, ..., 10x10]
# 方法一 循环
L = []
for x in range(1, 11):
    L.append(x * x)

print(L)

# 方法二 列表生成式
print([x * x for x in range(1,11)])

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
print([x *x for x in range(1, 11) if x % 2 ==0])

# 使用两层循环，可以生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])

# 列出当前目录下的所有文件和目录名
import os # 导入os 模块，模块的概念后面讲到
print([d for d in os.listdir('.')]) # os.listdir可以列出文件和目录

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)

# 列表生成式可以使用两个变量来生成list
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

# 把一个List中的所有字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])