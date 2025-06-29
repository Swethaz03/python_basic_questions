
sentence=input("enter the sentences")
dict={}
words=sentence.split()
for i in words:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]