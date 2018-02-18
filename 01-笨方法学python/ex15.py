#引入sys 模块，argv变量，准备复制给内部变量
from sys import argv
#将命令行输入的变量传递给filename变量
script,filename=argv
#利用open函数打开file，并传递给txt变量，其实应该是生成了一个txt对象，txt这个变量指向了系统内的内存，这个打开filename后，将要持续占用内存，这个file真的不能大啊
txt=open(filename)
#打印出你要复制的文件名
print("Here is you file %r:"%filename)
#打印出txt文件里面的所有内容
print(txt.read())
#向用户要一个想复制进去的文件名
print("Type the filename again:")
file_again=input("> ")
#重复操作，再打个一个文件，这个文件占用了内存，用txt_again名字指向了这个内存，生成了tet_again对象
txt_again=open(file_again)
#打印出txt_again的内容
print(txt_again.read())
