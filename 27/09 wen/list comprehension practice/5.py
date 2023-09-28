# Find all of the words in a string that are less than 5 letters
str1 = "Find all of the words in a string that are less than 5 letters"
word = str1.split()
print(word)
words_5 = [i for i in word if len(i) < 5]
print(words_5)
