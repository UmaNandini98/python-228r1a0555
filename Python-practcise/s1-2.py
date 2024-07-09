def count_repeated(li):
    dict = {}
    for item in li:
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1

    max=0
    repeatedvalue = 0
    for item in dict:
        if dict[item]>max:
            max= dict[item]
            repeatedvalue=[item]
    return repeatedvalue


n = int(input("Enter number of elements : "))

li = []
print("Enter elements : ")
for i in range(n):
    li.append(int(input()))

print("Most repeated value is : ", count_repeated(li))
print("Mode is : ", count_repeated(li))



