# Use filter to eliminate all words that are shorter than 4 letters from a list of words

# List of words
words = ["apple", "banana", "cherry", "date", "fig", "grape"]

# Use filter to eliminate words shorter than 4 letters
filtered_words = list(filter(lambda word: len(word) >= 4, words))

# Display the result
print("Original List of Words:", words)
print("Filtered List of Words (>= 4 letters):", filtered_words)
