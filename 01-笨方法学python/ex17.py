#这次要将一个文件中的内容copy到另一个文件中，也就是复制文件的命令，copyandpaste
#同样的为了引入命令行输入，引入exists函数
from sys import argv
from os.path import exists
#从命令行复制给三个变量
script ,from_file, to_file=argv
#打印提示，从XX文件复制到XX文件啦
print("Copying from %s to %s"%(from_file,to_file))
#如果用一行代码写应该是
#indata=open(from_file).read()
#意思就新建一个文件对象infile，然后将内容读出来，写入indata变量中
infile=open(from_file)
indata=infile.read()
#打印要复制的内容
print("The input file is %d bt=ytes long"%len(indata))
#测试是否生成了新的文件
print("Dose the output file exists? %r"%exists(to_file))
print("Ready,hit RETURN to continue,CTRL-C to abort.")
input("?")
#新建了一个文件对象outfile，并且写入indata中的内容
outfile=open(to_file,'w')
outfile.write(indata)
#这就写完了，也就复制好啦
print("Alright,all done.")
#关闭两个文件
outfile.close()
infile.close()

#使用命令行操作，要先新建一个文件，比如test17.txt，然后copy到test17-复制件。txt中


