
num=int(input("enter the number"))
binary=bin(num)

b=binary[2:]
print("binary is : ",b)

n1=b.replace('0','o')
n1=n1.replace('1','0')
n1=n1.replace('o','1')
print(n1)