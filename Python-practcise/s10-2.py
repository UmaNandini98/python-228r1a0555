def check_character_type(char):
    if char.isdigit():
        print(f"{char} is a digit.")
    elif char.islower():
        print(f"{char} is a lowercase character.")
    elif char.isupper():
        print(f"{char} is an uppercase character.")
    else:
        print(f"{char} is a special character.")

# Example usage
input_char = input("Enter a character: ")
check_character_type(input_char)
