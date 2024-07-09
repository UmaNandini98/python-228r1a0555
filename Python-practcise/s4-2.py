def print_natural_numbers(n):
    for i in range(1, n + 1):
        print(i, end=" ")

n = int(input("Enter the value of n: "))
print("First", n, "natural numbers:",end=" ")
print_natural_numbers(n)