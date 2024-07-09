def reverse_array(arr):
    return arr[::-1]

n = int(input("Enter number of elements : "))
arr = []
print("Enter elements of array : ")
for i in range(n):
    arr.append(int(input()))

print("Reversed array is:", reverse_array(arr))
