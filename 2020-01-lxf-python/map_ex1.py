# -*- coding: utf-8 -*-
def normalize(name):
    return name[0].upper() + name[1:len(name)].lower()
    pass

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)