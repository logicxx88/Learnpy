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

## 练习10：那是什么-测试转义字符和其他特殊字符

```
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
```

#### 附加思考

>1.通过把它们写在卡片上记住所有的转义序列。 2.使用'''(三个单引号)取代三个双引号，看看效果是不是一样的？ 3.结合转义序列和格式字符串创建一个更复杂的格式。 4.记得 %r 格式化字符串吗？使用 %r 搭配单引号和双引号转义字符打印一些字符串出来。 将 %r 和 %s 比较一下。 注意到了吗？%r 打印出来的是你写在脚本里的内容，而 %s 打印的是你应该看到的内容。

## 练习11 提问

```
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
```

## 练习12：提示输入

```
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
```

## 练习13：参数、变量、解包

```
from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
```

这个地方开始引入模块sys，并使用了内置的功能

## 练习14：
这节练习让我们使用 argv 和 raw_input 一起来向用户提一些特别的问题。下一节习题你会学习如何读写文件，这节练习是下节的基础。在这道习题里我们将用略微不同的方法使用 raw_input，让它打出一个简单的 > 作为提示符。这和一些游戏中的方式类似，例如 Zork 或者 Adventure 这两款游戏。

```
from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)
```

#### 附加思考
>1.查一下 Zork 和 Adventure 是两个怎样的游戏。看看能不能下载到一版，然后玩玩看。 2.将 prompt 变量改成完全不同的内容再运行一遍。 3.给你的脚本再添加一个参数，让你的程序用到这个参数，像你在上一个练习中用到的解包操作 first, second = ARGV。 4.确认你弄懂了三个引号 """ 可以定义多行字符串，而 % 是字符串的格式化工具。

## 练习15
这节练习涉及到写两个文件。一个正常的 ex15.py 文件，另外一个是 ex15_sample.txt，第二个文件并不是脚本，而是供你的脚本读取的文本文件。以下是后者的内容：

```
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.
```

我们要做的是用我们的脚本“打开(open)”这个文件，然后打印出来。然而把文件名 ex15_sample.txt 写死在代码中并不是一个好主意，这些信息应该是用户输入的才对。如果我们碰到其他文件要处理，写死的文件名就会给你带来麻烦了。我们的解决方案是使用 argv 和 raw_input 来从用户获取信息，从而知道哪些文件该被处理。

```
from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
```

#### 附加思考
>1.在每一行的上面加上注释。 
>
>2.如果你不确定答案，就问别人，或者上网搜索。大部分时候，只要搜索 “python” 加上你要搜的东西就能得到你要的答案。比如搜索一下“python open”。 
>
>3.我使用了“命令”这个词，不过实际上它们的名字是“函数（function）”和“方法（method）。上网搜索一下这两者的意义和区别。看不明白也没关系，这本书后面也会讲到这些。
>
>4.删掉 10-15 行使用到 raw_input 的部分，再运行一遍脚本。
>
>5.只用 raw_input 写这个脚本，想想哪种得到文件名称的方法更好？为什么？ 
>
>6.运行 python 在命令行下使用 open 打开一个文件，这种 open 和 read 的方法也值得你一学。 
>
>7.让你的脚本对 txt 和 txt_again 两个变量执行一下 close()，处理完文件后你需要将其关闭，这是很重要的一点。

## 练习16：读写文件
应该记住的命令：
>
- close -- 关闭文件。跟你编辑器的 文件->保存.. 一个意思。
- read -- 读取文件内容。你可以把结果赋给一个变量。
- readline -- 读取文本文件中的一行。
- truncate -- 清空文件，请谨慎使用该命令。
- write('stuff') -- 将 stuff 写入文件。

使用这些命令做一个简单的文本编辑器

```
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
```

#### 附加思考
>1.如果你觉得自己没有弄懂的话，用我们的老办法，在每一行之前加上注解，为自己理清思路。就算不能理清思路，你也可以知道自己究竟具体哪里没弄明白。 2.写一个和上一个练习类似的脚本，使用 read 和 argv 读取你刚才新建的文件。 3.文件中重复的地方太多了。试着用一个 target.write() 将 line1, line2, line3 打印出来，你可以使用字符串、格式化字符、以及转义字符。 4.找出为什么我们需要给 open 多赋予一个 'w' 参数。提示： open 对于文件的写入操作态度是安全第一，所以你只有特别指定以后，它才会进行写入操作。 5.如果你使用'w' 模式打开一个文件，那么还需要 target.truncate()吗?阅读 Python 关于 open 函数的文档， 看你理解的对不对。


## 练习17：更多文件操作
现在让我们再学习几种文件操作。我们将编写一个 Python 脚本，将一个文件中的内容拷贝到另外一个文件中。这个脚本很短，不过它会让你对于文件操作有更多的了解。

```
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
```

你应该很快注意到了我们 import 了又一个很好用的命令 exists。这个命令将文件名字符串作为参数，如果文件存在的话，它将返回 True，否则将返回 False。

#### 附加思考
>1.这个脚本 实在是有点烦人。没必要在拷贝之前问一遍把，没必要在屏幕上输出那么多东西。试着删掉脚本的一些功能，让它使用起来更加友好。 
>
>2.看看你能把这个脚本改多短，我可以把它写成一行。 
>
>3.我使用了一个叫 cat 的东西，这个古老的命令的用处是将两个文件“连接(concatenate)”到一起，不过实际上它最大的用途是打印文件内容到屏幕上。你可以通过 man cat 命令了解到更多信息。(windows 下没有这个命令) 
>
>4.找出为什么你需要在代码中写 output.close() 。 
>
>5.再多读读和 import 相关的材料，将 python 运行起来，试试这一条命令。试着看看自己能不能摸出点门道，当然了，即使弄不明白也没关系。


## 练习18 命名, 变量, 代码, 函数
函数可以做三样事情：
>1.它们给代码片段命名，就跟“变量”给字符串和数字命名一样。 2.它们可以接受参数，就跟你的脚本接受 argv 一样。 3.通过使用 #1 和 #2，它们可以让你创建“微型脚本”或者“小命令”。


```
# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
```
>1.首先我们告诉 Python 创建一个函数，我们使用到的命令是 def，也就是“定义(define)”的意思。
>
>2.紧接着 def 的是函数的名称。本例中它的名称是 print_two，但名字可以随便取，就叫 peanuts 也没关系。但函数名最好能够体现出函数的功能来。 
>
>3.然后我们告诉函数我们需要*args，这和脚本的 argv 非常相似，参数必须放在圆括号 () 中才能正常工作。 
>
>4.接着我们用冒号:结束本行，然后开始下一行缩进。 冒号以下，使用 4 个空格缩进的行都是属于 print_two 这个函数的内容。 其中第一行的作用是将参数解包，这和脚本参数解包的原理差不多。 
>
>5.为了演示它的工作原理，我们把解包后的每个参数都打印出来，这和我们在之前脚本练习中所作的类似。
>
## 练习19：函数和变量
函数里边的变量和脚本里边的变量之间是没有关系的。下面的这个练习可以让你对这一点有更多的思考：

```
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
```
#### 附加思考
>1.倒着将脚本读完，在每一行上面添加一行注解，说明这行的作用。 2.从最后一行开始，倒着阅读每一行，读出所有的重要字符来。 3.自己编至少一个函数出来，然后用 10 种方法运行这个函数。
>

## 练习20：函数和文件
注意一下函数和文件是如何在一起协作发挥作用的

```
from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
```

#### 附件思考
>1.通读脚本，在每行之前加上注解，以理解脚本里发生的事情。 
>
>2.每次 print_a_line 运行时，都传递了一个叫 current_line 的变量。在每次调用函数时，打印出 current_line 的值，跟踪一下它在 print_a_line 中是怎样变成 line_count 的。 
>
>3.找出脚本中每一个用到函数的地方。检查 def 一行，确认参数没有用错。 
>
>4.上网研究一下 file 中的 seek 函数是做什么用的。试着运行 pydoc file 看看能不能学到更多。 
>
>5.研究一下+=这个简写操作符的作用，写一个脚本，把这个操作符用在里边试一下。
>
## 练习21：函数的返回值

现在我们创建了自己的加减乘除数学函数： add, subtract, multiply, 以及 divide。重要的是函数的最后一行，例如 add 的最后一行是 return a + b，它实现的功能是这样的:
>1.我们调用函数时使用了两个参数： a 和 b 。 2.我们打印出这个函数的功能，这里就是计算加法（adding） 3.接下来我们告诉 Python 让它做某个回传的动作：我们将 a + b 的值返回(return)。或者你可以这么说：“我将 a 和 b 加起来，再把结果返回。” 4.Python 将两个数字相加，然后当函数结束的时候，它就可以将 a + b 的结果赋予一个变量。
>

```
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
```
#### 附加思考
>1.如果你不是很确定 return 的功能，尝试自己写几个函数出来，让它们返回一些值。你可以将任何可以放在=右边的东西作为一个函数的返回值。 2.这个脚本的结尾是一个迷题。我将一个函数的返回值用作了另外一个函数的参数。我将它们连接一起，就像写数学等式一样。这样可能有些难懂，不过运行一下你就知道结果了。你可以试试看能不能用正常的方法实现和这个表达式一样的功能。 3.一旦你解决了这个迷题，试着修改一下函数里的某些部分，然后看会有什么样的结果。你可以有目的地修改它，让它输出另外一个值。 4.颠倒过来再做一次。写一个简单的等式，使用相同的函数来计算它。
>

## 练习22：-复习，到目前为止你学到了什么？
略

## 练习23：阅读代码
>1.浏览器登陆 bitbucket.org, github.com, 或者 gitorious.org 搜索"python." 2.随便找一个项目，然后点进去。 3.点击 Source 标签，浏览目录和文件列表，直到你看到以.py 结尾的文件。 4.从头开始阅读你找到的代码。把它的功能用笔记记下来。 5.如果你看到一些有趣的符号或者奇怪的字符，你可以把它们记下来，日后再进行研究。


## 练习24：更多的练习
>这个章节也不打算写Py文件了


```
print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
```
#### 附加思考
>1.记得仔细检查结果，从后往前倒着检查，把代码朗读出来，在不清楚的位置加上注释。 2.故意把代码改错，运行并检查会发生什么样的错误，并且确认你有能力改正这些错误。


##  练习25：更多更多的练习
>这个章节用ipython3做就好了，就不写py文件了

首先以正常的方式 python ex25.py 运行，找出里边的错误，并修正。然后你需要跟着下面的答案部分完成这节练习。

```
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
```

你看到的结果
在这节练习中，我们将在 Python 解析器中，以交互的方式和你写的 ex25.py 文件交流，你可以像下面这样在命令行中启动 python 解析器：

```
$ python
Python 2.7.1 (r271:86832, Jun 16 2011, 16:59:05)
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
```

你的输出应该和我类似，在>符号之后，你可以输入并立即执行 python 代码。我希望你用这种方式逐行输入下方的 python 代码，并看看他们有什么用：

```
import ex25
sentence = "All good things come to those who wait."
words = ex25.break_words(sentence)
words
sorted_words = ex25.sort_words(words)
sorted_words
ex25.print_first_word(words)
ex25.print_last_word(words)
words
ex25.print_first_word(sorted_words)
ex25.print_last_word(sorted_words)
sorted_words
sorted_words = ex25.sort_sentence(sentence)
sorted_words
ex25.print_first_and_last(sentence)
ex25.print_first_and_last_sorted(sentence)
```

这是我做出来的样子：

```
Python 2.7.1 (r271:86832, Jun 16 2011, 16:59:05) 
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import ex25
>>> sentence = "All good things come to those who wait."
>>> words = ex25.break_words(sentence)
>>> words
['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
>>> sorted_words = ex25.sort_words(words)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> ex25.print_first_word(words)
All
>>> ex25.print_last_word(words)
wait.
>>> words
['good', 'things', 'come', 'to', 'those', 'who']
>>> ex25.print_first_word(sorted_words)
All
>>> ex25.print_last_word(sorted_words)
who
>>> sorted_words
['come', 'good', 'things', 'those', 'to', 'wait.']
>>> sorted_words = ex25.sort_sentence(sentence)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> ex25.print_first_and_last(sentence)
All
wait.
>>> ex25.print_first_and_last_sorted(sentence)
All
who
```

#### 附加思考
>1.研究答案中没有分析过的行，找出它们的来龙去脉。确认自己明白了自己使用的是模块 ex25 中定义的函数。 
>
>2.试着执行 help(ex25)和 help(ex25.break_words)。这是你得到模块帮助文档的方式。 所谓帮助文档就是你定义函数时放在"""之间的东西，它们也被称作 documentation comments （文档注解），后面你还会看到更多类似的东西。 
>
>3.重复键入 ex25. 是很烦的一件事情。有一个捷径就是用 from ex25 import *的方式导入模组。这相当于说：“我要把 ex25 中所有的东西 import 进来。”程序员喜欢说这样的倒装句，开一个新的会话，看看你所有的函数是不是已经在那里了。 
>
>4.把你脚本里的内容逐行通过 python 编译器执行，看看会是什么样子。你可以通过输入 quit()来退出 Python。
>

## 练习26：考试
修正现有的程序，你需要访问下面的网站：

```
http://learnpythonthehardway.org/book/exercise26.txt
```
练习代码 1ex26.py如下：

```
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words)
    """Prints the first word after popping it off."""
    word = words.poop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 5
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans \ 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates == secret_formula(start-point)

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_pont


sentence = "All god\tthings come to those who weight."

words = ex25.break_words(sentence)
sorted_words = ex25.sort_words(words)

print_first_word(words)
print_last_word(words)
.print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = ex25.sort_sentence(sentence)
prin sorted_words

print_irst_and_last(sentence)

   print_first_a_last_sorted(senence)

```

## 练习27：记住逻辑
在 python 中我们会用到下面的术语（字符或者词汇）来定义事物的真(True)或者假(False)。计算机的逻辑就是在程序的某个位置检查这些字符或者变量组合在一起表达的结果是真是假。
>
>- and 与
- or 或
>- not 非
>- != (not equal) 不等于
>- == (equal) 等于
>- = (greater-than-equal) 大于等于
>- <= (less-than-equal) 小于等于
>- True 真
>- False 假


## 练习27：布尔表达式
在这节练习中，你将在 python 里使用到上节学到的逻辑表达式。先为下面的每一个逻辑问题写出你认为的答案，每一题的答案要么为 True 要么为 False。写完以后，你需要将 python 运行起来，把这些逻辑语句输入进去，确认你写的答案是否正确。

```
True and True
False and True
1 == 1 and 2 == 1
"test" == "test"
1 == 1 or 2 != 1
True and 1 == 1
False and 0 != 0
True or 1 == 1
"test" == "testing"
1 != 0 and 2 == 1
"test" != "testing"
"test" == 1
not (True and False)
not (1 == 1 and 0 != 1)
not (10 == 1 or 1000 == 1000)
not (1 != 10 or 3 == 4)
not ("testing" == "testing" and "Zed" == "Cool Guy")
1 == 1 and (not ("testing" == 1 or 1 == 0))
"chunky" == "bacon" and (not (3 == 4 or 3 == 3))
3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))
```

## 练习29：IF 语句
这节练习会向你介绍“if 语句”。把这段代码输入脚本，让它正常运行，看看你有没有什么收获。

```
people = 20
cats = 30
dogs = 15

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!
if people > dogs:
    print "The world is dry!"

dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."
```

## 练习30：Else 和 If

```
people = 30
cars = 40
trucks = 15

if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."
```

## 练习31：做出决定
上一个脚本中你写了一系列的简单提问测试。这节的脚本中，你将需要向用户提问，依据用户的答案来做出决定。把脚本写下来，多多鼓捣一阵子，看看它的工作原理是什么。

```
print "You enter a dark room with two doors.  Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake.  What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off.  Good job!"
    elif bear == "2":
        print "The bear eats your legs off.  Good job!"
    else:
        print "Well, doing %s is probably better.  Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello.  Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck.  Good job!"

else:
    print "You stumble around and fall on a knife and die.  Good job!"
```

## 练习32：循环和列表

```
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print "Element was: %d" % i
```

## 练习33：while 循环

```
i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num
```
## 练习34：访问列表元素

定义列表

```
animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
```

写代码输出

```
The animal at 1.
The third (3rd) animal.
The first (1st) animal.
The animal at 3.
The fifth (5th) animal.
The animal at 2.
The sixth (6th) animal.
The animal at 4.
The 1st animal is at 0 and is a bear.
The animal at 0 is the 1st animal and is a bear.
```

#### 附加思考
>1.以你对于这些不同的数字类型的了解，解释一下为什么 “January 1, 2010” 里是 2010 而不是 2009？（提示：你不能随机挑选年份。） 
>
>2.再写一些列表，用一样的方式作出索引，确认自己可以在两种数字之间互相翻译。 
>
>3.使用 python 检查自己的答案。

>Warning: 会有程序员告诉你让你去阅读一个叫“Dijkstra”的人写的关于数字的话题。我建议你还是不读为妙。除非你喜欢听一个在编程这一行刚兴起时就停止从事编程的人对你大喊大叫。
>

## 练习35:分支和函数
弄懂它实现的是什么功能。

```
from sys import exit

def gold_room():
    print "This room is full of gold.  How much do you take?"

    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
```

#### 附加思考
>1.把这个游戏的地图画出来，把自己的路线也画出来。 2.改正你所有的错误，包括拼写错误。 3.为你不懂的函数写注释。 4.为游戏添加更多元素。通过怎样的方式可以简化并且扩展游戏的功能呢？ 5.这个 gold_room 游戏使用了奇怪的方式让你键入数字。这种方式会导致什么样的 bug？ 你可以用比检查 0、1 更好的方式判断输入是否是数字吗？int() 这个函数可以给你一些头绪。
>

## 练习36：设计和调试
#### 调试的小技巧
>1.不要使用 “debugger”。Debugger 所作的相当于对病人的全身扫描。你不会得到某方面的有用信息，而且你会发现它输出的信息大部分没有用，或者只会让你更困惑。 2.最好的调试程序的方法是使用 print,在各个你想要检查的关键环节将关键变量打印出来，从而检查哪里是否有错。 3.让程序一部分一部分地运行起来。不要等一个很长的脚本写完后才去运行它。写一点，运行一点，修改一点。

#### 作业

写一个和上节类似的小游戏。任何题材的游戏都可以。尽量花一周的时间让这个游戏有趣一些，作为附加题，你可以尽量多的使用列表，函数和模块（还记得练习 13 吗？），而且，尽量弄一些新的 Python 代码让你的游戏运行起来。

在你开始编码之前，你应该先画一张地图出来，提前设计出玩家可能遇到的房间、怪物以及陷阱等。

当你画好了梯度，你就可以开始编码了。如果你发现地图有问题的话，修改一下，让代码和地图相匹配。

完成一个软件的最好方式是把它们拆解为像下面这样的小块：
>1.在纸上写下你完成这个软件所需要做的所有任务。这就是你的待办事项列表。 2.先找到你列表中最容易的事情。 3.在你的源代码中增加注释，作为你完成这项任务的指南。 4.在这些注释下面，开始编码。 5.然后立即运行你的代码，看它是否正常工作。 6.循环的进行代码编写，测试运行，以及代码修正，直到代码正常运行。 7.在你的列表中划掉刚完成的任务，然后再挑选下一个最容易完成的任务，重复进行以上步骤。
>

## 练习37：复习符号
略

## 练习38：列表操作
下面的练习将字符串和列表混在一起，看看你能不能在里边找出点乐子来：

```
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop()
print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:5]) # super stellar!
```

#### 什么情况下使用列表
>1.如果你需要维护一组次序，记住，这是把次序编成列表，而不是给次序排序，列表不会帮你排序。 2.如果你需要根据一个随机数访问列表内容，记住，这时候基数从 0 开始。 3.如果你需要从头到尾操作列表内容，记住，这就是 for 循环。
>

#### 附加思考
>1.将每一个被调用的函数以上述的方式翻译成 Python 实际执行的动作。比如 more_stuff.pop() 是 pop(more_stuff). 2.将这两种方式翻译为自然语言。 3.上网阅读一些关于“面向对象编程(Object Oriented Programming)”的资料。晕了吧？嗯，我以前也是。别担心。你将从这本书学到足够用的关于面向对象编程的基础知识，而以后你还可以慢慢学到更多。 4.查一下 Python 中的 “class” 是什么东西。不要阅读关于其他语言的 “class” 的用法，这会让你更糊涂。 5.如果你不知道我讲的是些什么东西，别担心。程序员为了显得自己聪明，于是就发明了 Opject Oriented Programming，简称为 OOP，然后他们就开始滥用这个东西了。如果你觉得这东西太难，你可以开始学一下 “函数编程(functional programming)”。 6.找出 10 种可以放在列表中的例子，并用它们写一些脚本。







