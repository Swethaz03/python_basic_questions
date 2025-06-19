
"""using for loop"""
n=int(input("enter the number : "))
fact=1

for i in range(1,n+1):
    fact=fact*i
print(fact)

# enter the number : 5
# 120

"""using while loop"""

y=int(input("enter the number :"))
fact=1
i=1
while i <= y:
     fact=fact*i
     i+=1
print(fact)


