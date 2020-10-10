'''递归函数实现计算列表所包含的元素数'''
def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])

print(count([1, 2, 3, 4, 5]))