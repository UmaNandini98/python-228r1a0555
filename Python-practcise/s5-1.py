def sum(arr,n):
    sum = 0
    for i in arr:
        sum = sum + i
    return sum

n = int(input("Enter number of elements : "))
arr = []
print("Enter elements of array : ")
for i in range(n):
    arr.append(int(input()))

print("Sum of array element is : ",sum(arr,n))