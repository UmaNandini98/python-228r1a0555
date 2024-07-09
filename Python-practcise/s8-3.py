import numpy as np

# Function to convert list to array
def list_to_array(lst):
    return np.array(lst)

# Function to convert tuple to array
def tuple_to_array(tup):
    return np.array(tup)

# Example usage
lst = [1, 2, 3, 4, 5]
tup = (6, 7, 8, 9, 10)

arr_from_list = list_to_array(lst)
arr_from_tuple = tuple_to_array(tup)

print("Array from list:", arr_from_list)
print("Array from tuple:", arr_from_tuple)
