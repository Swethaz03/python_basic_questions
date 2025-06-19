
def reverse(string1):
    str=string1[::-1]

    print(str)
        
string2="hijava"
reverse(string2)


print("---------------------------------------")

def reverse1(str1):
    leng=len(str1)
    str2=""

    for i in range(leng-1,-1,-1):
       str2+=str1[i] 
    print(str2)

word="ramo"
reverse1(word)