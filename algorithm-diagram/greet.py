'''调用栈的示例'''
def greet(name):
    print("hello, " + name + "!")
    greet2(name)
    print("getting ready to say bey...")
    bye()

def greet2(name):
    print("how are you," + name + "?")

def bye():
    print("ok bye!")

greet('Chenfeng Yaun')