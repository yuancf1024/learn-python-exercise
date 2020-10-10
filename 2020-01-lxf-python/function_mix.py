'''
 f1位置参数a,b 
 默认参数c=0
 可变参数 args
 关键字参数 kw
 '''
def f1(a, b, c=0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)

'''
 f2位置参数a,b 
 默认参数c=0
 命名关键字参数 d
 关键字参数 kw
 '''
def f2(a, b, c=0, *, d, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)

f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

# 通过一个tuple和dict也可以调用上述函数
args = (1, 2, 3, 4)
kw = {'d': 99,'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88,'x': '#'}
f2(*args, **kw)