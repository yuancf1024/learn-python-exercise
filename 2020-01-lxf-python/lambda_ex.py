# -*- coding: utf-8 -*-

def is_odd(n):
    return n % 2 == 1

L = list(filter(lambda n: n % 2 ==1, range(1, 20)))

print(L)
