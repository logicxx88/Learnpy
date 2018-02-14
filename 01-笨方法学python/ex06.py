#定义多个字符串
x="There are %d types of people."%10
binary="binary"
do_not="don't"
y="Those who know %s and those who %s."%(binary,do_not)
#打印字符串
print(x)
print(y)
#按格式打印字符串
print("I said: %r."%x)
print("I also said: %s"%y)

hilarious=False
# %r是要完全打印
joke_evalutation="Isn't that joke so sunny?! %r"
# 原来是可以把代码分开的，很灵活
print(joke_evalutation % hilarious)
#定义字符串
w="This is the left side of ..."
e="a string with a right side."
#合并字符串，并且打印
print(w+e)

