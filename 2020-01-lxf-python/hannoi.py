# -*- coding: utf-8 -*-
# 汉诺塔函数 7行代码搞定
''' n = 1 -> 1
n = 2 -> 3
n = 3 -> 7
n = 4 -> 15
n = 5 -> 31
'''

def move(n, a, b, c):
    if n == 1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        print(a,'-->',c)
        move(n-1,b,a,c)
        
       
       # print(b,'-->',a)
        #move(n-1,b,c,a)
        #print(a,'-->',c)
        #move(n-1,a,b,c)
move(1,'A', 'B', 'C')
print('间隔')
move(2,'A', 'B', 'C')
print('间隔')
move(3, 'A', 'B', 'C')
print('间隔')
move(4, 'A', 'B', 'C')
print('间隔')
move(5,'A','B','C')