vowel = ['a', 'e', 'i', 'o', 'u']
word = input("Enter a string : ")
count = 0
for character in word:
    if character in vowel:
        count += 1
print("Number of vowels = ",count)

