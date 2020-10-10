'''递归实现：找出列表中最大的数字'''
def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

print(max([1, 2, 3, 4, 5]))