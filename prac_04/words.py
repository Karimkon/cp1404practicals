"""
Word Occurrences
Estimate: 15 minutes
Actual:   25 minutes
"""

# Ask the user for a string input
text = input("Text: ")

# Split the text into words
words = text.split()

# Create a dictionary to count occurrences
word_counts = {}

# Count each word's occurrences
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

# Sort the words
sorted_words = sorted(word_counts.items())

# Find the longest word length for formatting
max_length = max(len(word) for word in word_counts.keys())

# Print the results with aligned formatting
for word, count in sorted_words:
    print(f"{word:{max_length}} : {count}")
