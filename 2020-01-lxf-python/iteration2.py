from collections import Iterable
isinstance('abc', Iterable) # str是否可迭代
print(isinstance('abc', Iterable))
isinstance([1,2,3], Iterable) # list是否可迭代
print(isinstance([1,2,3], Iterable))
isinstance(123, Iterable) # 整数是否可迭代
print(isinstance(123, Iterable))