
# 0 1 2 3 4
# 1 2 3 4 5  n=5
# 5 1 2 3 4

# 0 1 2 3 4
# 4 5 1 2 3
   
arr=[1,2,3,4,5]
rotate=2

rotated=arr[-rotate:]+arr[:-rotate]
print(rotated)


k=2
for i in range(len(arr)):
      newarr=arr[k]
      k+=1
   