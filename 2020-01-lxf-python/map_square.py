def f(x):
    return x * x
 
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)

# 计算任意复杂度的函数
a = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(a)