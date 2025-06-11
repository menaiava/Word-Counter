# Word Counter App

# Ask user to enter a sentence
sentence = input("Enter a sentence: ")

# --- Count words ---

# Split the sentence by spaces
words = sentence.split(" ")

# Count words
num_words = len(words)

# Show number of words
print("Number of words:", num_words)

# --- Count letters ---

# Make sentence lowercase to count letters better
sentence_lower = sentence.lower()

# Remove spaces
sentence_no_spaces = sentence_lower.replace(" ", "")

# Now count letters
i = 0
letter_counts = {}

while i < len(sentence_no_spaces):
    letter = sentence_no_spaces[i]
    if letter not in letter_counts:
        letter_counts[letter] = 1
    else:
        letter_counts[letter] = letter_counts[letter] + 1
    i = i + 1

# Show letter counts
print("Letter counts:")
for letter in letter_counts:
    print(letter + ": " + str(letter_counts[letter]))
