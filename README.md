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

