# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
L = [x * x for x in range(10)]
print(L)

g = (x * x for x in range(10))
print(g)

# 输出generator 的所有元素
g = (x * x for x in range(10))
for n in g:
    print(n)
