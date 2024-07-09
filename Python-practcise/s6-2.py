def generate_binary_numbers(n):
    arr = []
    for i in range(n + 1):
        arr.append(bin(i)[2:])
    return arr

# Example usage
n = int(input("Enter a number: "))
binary_numbers = generate_binary_numbers(n)
print(f"Binary numbers from 0 to {n}:")
for binary in binary_numbers:
    print(binary)
