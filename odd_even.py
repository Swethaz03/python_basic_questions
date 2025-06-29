
list=[1,2,3,4,5,6]
oddsum=0
evensum=0

for i in list:
    if i%2==0:
        evensum+=i
    else:
        oddsum+=i

print("odd sum is : ",oddsum)
print("even sum is : ",evensum)
