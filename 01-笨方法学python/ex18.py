#定义了一个可以传入多个参数的函数
def print_two(*args):
    arg1,arg2=args
    print("arg1:%s,arg2:%s."%(arg1,arg2))
#定义了传入两个参数的函数
def print_two_again(arg1,arg2):
    print("arg1:%s,arg2:%s."%(arg1,arg2))
#定义了传入一个参数的函数
def print_one(arg1):
    print("arg1:%s"%arg1)
#定义了没有参数的函数
def print_none():
    print("I got nothing.")
#在这个地方才开始call函数
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
