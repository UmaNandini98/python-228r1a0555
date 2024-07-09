row = int(input("Enter number of rows : "))

i = 0
while(i<row):
    j=0
    while(j<i+1):
        print(row-i,end=" ")
        j = j+1
    i = i+1
    print("\r")