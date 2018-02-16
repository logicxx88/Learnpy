"""
在python3下，是没有raw_input函数的，要自己根据事情情况去转换格式
"""
print("how old are you?:")
age=str(input())
print("how tall are you?:")
height=str(input())
print("how much do u weigh?:")
weight=str(input())

print("So,you're %r old,%r tall and %r heavy."%(age,height,weight))



