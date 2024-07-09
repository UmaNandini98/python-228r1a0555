def check_word_in_file(file_name, word_to_find):
    try:
        with open(file_name, 'r') as file:
            file_contents = file.read()
            if word_to_find in file_contents:
                print(f"The word '{word_to_find}' is present in the file.")
            else:
                print(f"The word '{word_to_find}' is not found in the file.")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_name = 'sample.txt'  # Replace with your file path
word_to_find = 'Python'   # Replace with the word you want to search for

check_word_in_file(file_name, word_to_find)
