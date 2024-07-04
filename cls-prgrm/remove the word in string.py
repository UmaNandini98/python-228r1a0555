def remove_word(Str,word):
 Str=Str.replace(word,'')
 return Str
Str2="hello good morning hi hello goodmorning"
print("Before remove")
print(Str2)
Str3=remove_word(Str2,"hello")
print(Str3)



