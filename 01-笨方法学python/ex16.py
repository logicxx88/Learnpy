#做一个简单的文本编辑器
#引入sys.argv，从命令行获取信息
from sys import argv
#将命令行命令赋值给变量filename，将文件名赋值给变量script
script,filename=argv
#打印若干提示信息，通过C-C去打断程序，用过Return继续运行程序
print("We`re going to erase %r."%filename)
print("If you don't want that ,the CTRL_C.")
print("If you do want that, hit Return.")
#打断程序，输入Return就继续运行啦
input("?")
#打印程序运行提示，并打开一个内存，用target指向，这就成为了一个对象，其中w的意思应该是openforwriting ,truncate for the file first
print("Opening the file...")
target=open(filename,'w')
#打印提示提示符，清空文件
print("Truncating the file. Goodbye!")
target.truncate()
#打印提示，现在向文件中写入三行
print("Now I'm going to ask you for three lines.")
#获取写入的内容命令
line1=input("line 1:")
line2=input("line 2:")
line3=input("line 3:")
#打印写入提示
print("I'm going to write these to the file.")
#target是open的一个对象，开始写入
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
#打印写入提示，准备关闭文件，此时内存中将不保存文件了。
print("And finally, we close it.")
target.close()

#用命令行$python3 ex16.py testex16.txt 运行

