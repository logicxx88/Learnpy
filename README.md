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

