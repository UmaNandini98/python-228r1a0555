def print_even_numbers(start, end):
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i, end=" ")

# Example usage
start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))
print(f"Even numbers between {start} and {end}:")
print_even_numbers(start, end)
