

def palindrome(string):
    length=0
    for i in string:
        length+=1
    str1=""
    for j in range(length-1,-1,-1):
        str1+=string[j]
    print(str1)

    if(string==str1):
        print("palindrome")
    else:
        print("not a palindrome")

palindrome("madam")
palindrome("hibaskar")