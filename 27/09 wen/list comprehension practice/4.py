# Remove all of the vowels in a string
str1 = "This is a sample string with spaces."
vowel = ['a', 'e', 'i', 'o', 'u']
s = ""
vow = "".join([i for i in str1 if i not in vowel])
print(vow)
