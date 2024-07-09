def print_squares(start, end):
    for number in range(start, end + 1):
        print(f"The square of {number} is {number**2}")

start = int(input("Enter  starting number : "))
end = int(input("Enter ending number : "))
print_squares(start, end)
