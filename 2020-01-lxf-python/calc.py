# 可变参数，允许传入0个或任意个参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

#print()
#calc([1, 2, 3])
#calc([1, 3, 5, 7])
print(calc(1,2,3),calc())
nums = [1, 2, 3]
print(calc(nums[0], nums[1], nums[2]))
print(calc(*nums))