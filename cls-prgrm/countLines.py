fp=open("count.txt","r")
words=[]
lines=0
charcount=0
for i in fp:
    words+=i.split()
count=count++

print(len(words))
