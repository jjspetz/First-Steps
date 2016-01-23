
# Pig Latin translator for a single word

"""
    def welcome() creates a welcome header.
    This is done as a single module, just so I can play around at how module imports work.
"""

def welcome():
    print('Welcome to the Pig Latin translator 1.1.')
    print("You can translate single words into Pig Latin.")

def translation():
    original = input('Enter a word:')  # input

    if len(original) > 0 and original.isalpha():
        word = original.lower()
        first = word[0]
        new_word = word + first + 'ay'
        print (new_word[1:])

    else:
        print('Enter a single word with no numbers of at least 1 alpha character')
        translation()
