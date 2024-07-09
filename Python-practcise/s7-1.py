def find_minimum_element(arr):
    if not arr:
        return None
    return min(arr)

n = int(input("Enter number of elements in the array: "))
arr = []
print("Enter the elements: ")
for i in range(n):
    arr.append(int(input()))

minimum_element = find_minimum_element(arr)
if minimum_element is not None:
    print("Minimum element in the array is:", minimum_element)
else:
    print("Array is empty.")
