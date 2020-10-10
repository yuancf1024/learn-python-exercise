# -*- coding:utf-8 -*-
'''def trim(s):
    if s =='' or s =='  ':
        print(s)
    elif s[0] == '' and s[len(s)-1] == '':
        print(s[1:len(s)-2])
    elif s[0] == '':
        print(s[1:len(s)-1])
    elif s[len(s)-1] == '':
        print(s[0:len(s)-2])
    else:
        print(s[:])
        
    return s
'''

def trim(s):
    if s[:1] == ' ':
        return trim(s[1:])
    elif s[-1:] ==' ':
        return trim(s[:-1])
    else:
        return s

print(trim(' hello '))
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')