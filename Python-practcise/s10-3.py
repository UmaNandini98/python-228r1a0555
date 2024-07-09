def find_common_values(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    common_values = set1.intersection(set2)
    return list(common_values)

# Example usage
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]

common_values = find_common_values(arr1, arr2)
print("Common values between arr1 and arr2:", common_values)
