def merge_files(file1, file2, merged_file):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2, open(merged_file, 'w') as merged:
            merged.write(f1.read())
            merged.write(f2.read())
        print(f"Merged contents of '{file1}' and '{file2}' into '{merged_file}' successfully.")
    except FileNotFoundError:
        print("One or more files not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file1 = 'file1.txt'   # Replace with your file path
file2 = 'file2.txt'   # Replace with your file path
merged_file = 'merged_file.txt'   # Replace with your desired output file path

merge_files(file1, file2, merged_file)
