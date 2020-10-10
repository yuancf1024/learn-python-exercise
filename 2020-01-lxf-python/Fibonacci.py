def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib(2))
print(fib(10))

# 将Fib函数变成generator, 只需要把print(b)改为 yield b
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(6)
print(f)

for n in fib(6):
    print(n)

'''用for循环调用generator时，发现拿不到generator的return语句的返回值。
如果想要拿到返回值，必须捕获StopIteration错误，
返回值包含在StopIteration的value中
'''

g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
