def max_in_arr(arr):
    return max(arr)

n = int(input("Enter number of elements in the array: "))
arr = []
print("Enter the elements: ")
for i in range(n):
    arr.append(int(input()))

print("Maximum element in the array is:", max_in_arr(arr))