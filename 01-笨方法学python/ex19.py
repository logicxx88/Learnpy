#函数里面的变量和脚本里面的变量之间是没有关系的
#下面打印的英文解释已经很清楚了
def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print("you have %d cheese!"%cheese_count)
    print("you have %d boxes of crackers"%boxes_of_crackers)
    print("Man that;s enough for a party!")
    print("Get a blank,\n")

print("We can just give the function numvers direcly:")
cheese_and_crackers(20,30)

print("OR ,we can use variables from our scripts:")
amount_of_cheese=10
amount_of_crackers=50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10+20,5+6)


