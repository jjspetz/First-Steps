import sys
# Pig Latin translator for a single word

pyg = 'ay'

print (" Welcome to the Pig Latin translator 1.0.")  # welcome text
print (" You can translate single words into Pig Latin.")

original = input('Enter a word:') #input

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:]
    print (new_word)
else:
    print ('Enter a single word with no numbers of at least 1 alpha character.')
