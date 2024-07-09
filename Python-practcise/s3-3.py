def count_freq(n,li,find_no):
    c = 0
    for i in range(n):
        if li[i] == find_no:
            c += 1
    return c

n = int(input("Enter number of elements in list : "))
lst = []
print("Enter number of elements : ")
for i in range(n):
    lst.append(int(input()))

find_count = int(input("Enter the number to count its frequency  : "))

print(f"The frequency of {find_count} is : {count_freq(n,lst,find_count)}")
