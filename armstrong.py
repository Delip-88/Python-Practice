
num = input("Enter a number : ")
lenth = len(num)
sqr = lambda x,y: x**y

sqr_num_sum = sum([sqr(int(x),lenth) for x in list(num)])
# print(sqr_num_sum)


if str(sqr_num_sum) == num:
    print("IT is armstrong number")
else:
    print("Its not armstrong number")