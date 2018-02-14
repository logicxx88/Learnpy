开始通过撸代码的方式学习Python
# 做完《笨方法学python》
素材均取自极客学院(http://wiki.jikexueyuan.com/project/learn-python-hard-way/)

虽然书中介绍不用vim编辑器、不采用python3，但是我还是打算这么做，电脑都配置好了，难道再滚回去~~~
## 练习1、第一个程序
将下面的内容写到一个文件中，取名为"ex1.py"

```
print "Hello World!"
print "Hello Again"
print "I like typing this."
print "This is fun."
print 'Yay! Printing.'
print "I'd much rather you 'not'."
print 'I "said" do not touch this.'
```
## 练习2：注释和井号“#”
注释在编程中是很重要的部分。它能告诉你这段代码是干什么用的，或者用来删除一部分你暂时不需要执行的代码。下面演示的是如何在 python 中使用注释：

```
# A comment, this is so you can read your program later.
# Anything after the # is ignored by python.

print("I could have code like this.") # and the comment after is ignored

# You can also use a comment to "disable" or comment out a piece of code:
# print "This won't run."

print("This will run.")
```

## 练习3：测试数学与数学计算

```
print "I will now count my chickens:"

print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2
```
附加考虑

>1.使用#在代码每一行的前一行为自己写一个注释，说明这一行的作用。 2.记得练习 0 的内容吧？用里边的方法把 Python 运行起来，然后使用刚才学到的运算符号，把 Python 当做计算器玩玩。 3.自己找个需要计算的东西，写一个 .py 文件把它计算出来。 4.有没有发现有些计算结果是”错”的呢？计算结果只有整数，没有小数部分。研究一下这是为什么，搜索一下“浮点数(floating point number)” 是什么东西。 5.使用浮点数重写一遍 ex3.py，让它的计算结果更准确(提示: 20.0 是一个浮点数)。

## 练习4：变量和命名

```
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
```
##### 附加思考
当我第一次写这个程序时我犯了个错误，python 告诉我这样的错误信息：

```
Traceback (most recent call last):
  File "ex4.py", line 8, in <module>
    average_passengers_per_car = car_pool_capacity / passenger
NameError: name 'car_pool_capacity' is not defined
```

用自己的话解释一下这个错误信息，解释时记得使用行号，而且要说明原因。

更多的附加题
>1.我在程序里用了 4.0 作为space_in_a_car的值，这样做有必要吗？如果只用 4 会有什么问题? 2.记住 4.0 是一个浮点数，自己研究一下这是什么意思。浮点数是带有小数点的数字。 3.在每一个变量赋值的上一行加上一行注释。 4.记住=的名字是等于(equal)，它的作用是为东西取名。 5.记住_是下划线字符(underscore)。 6.将 python 作为计算器运行起来，就跟以前一样，不过这一次在计算过程中使用变量名来做计算，常见的变量名有 i, x, j 等等。

## 练习5：更多的变量和打印

```
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
```

#### 附加思考

>1.修改所有的变量名字，把它们前面的 my_去掉。确认将每一个地方的都改掉，不只是你使用=赋值过的地方。 2.试着使用变量将英寸和磅对应转换成厘米和千克。不要直接键入答案。使用 Python 的计算功能来完成。 3.在网上搜索所有的 Python 格式化字符。 4.试着使用更多的格式化字符。例如 %r 就是是非常有用的一个，它的含义是“不管什么都打印出来”。

## 练习6：字符串和文本

```
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
```

#### 附加思考

>1.通读程序，并给每一行加上注释，解释下这行的作用。 2.找到所有的”字符串包含字符串”的位置，总共有四个位置。 3.你确定只有四个位置吗？你怎么知道的？也许我在骗你呢。 4.解释一下为什么用+连起来 w 和 e 就可以生成一个更长的字符串。

## 练习7：更多的打印

```
print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10  # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12
```

#### 附加思考

>1.逆向阅读，给每一行的加上注释。 2.倒着朗读出来，找出自己的错误。 3.从现在开始，把你犯过的错误记录一张纸上。 4.在开始下一节习题时，阅读一遍你记录下来的错误，并且尽量避免在下个练习中再犯同样的错误。 5.记住，每个人都会犯错误。程序员和魔术师一样，他们希望大家认为他们从不犯错，不过这只是表象而已，他们每时每刻都在犯错。

## 练习8：继续打印吧

```
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
```

#### 附件思考

>1.自己检查结果，记下你犯过的错误，并且在下个练习中尽量不犯同样的错误。 2.注意最后一行程序中既有单引号又有双引号，你觉得它是如何工作的

## 练习9，还在继续打印

```
# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
```

#### 附加思考

>1.自己检查结果，记录你犯过的错误，并且在下个练习中尽量不犯同样的错误。

