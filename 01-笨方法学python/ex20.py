#看看函数和文件之间的操作，这个例子相对简单，是根据已经设定好的命令逐行读文件中的内容
#引入命令行参数
from sys import argv
script,input_file=argv
#这个函数就相当于在内存中打开了文件，用f指向了文件，也就是产生了一个传入的文件的对象
def print_all(f):
    print(f.read())
#这个函数也是对文件做了操作，跳转到文件的第一个字符
def rewind(f):
    f.seek(0)
#这个函数表示读的第几行，逐行读取
def print_a_line(line_count,f):
    print(line_count,f.readline())

current_file=open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("now let's rewind,kind like a tape")

rewind(current_file)

print("Let's print three lines:")

current_line=1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)
