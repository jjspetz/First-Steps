"""
    Pig Latin translator
    This program translates single words, phrases, and sentences into Pig Latin.
    The first section is functions
"""


def welcome(): # prints the welcome text
    print('Welcome to the Pig Latin translator 2.0.')
    print("You can translate single words or sentences into Pig Latin!")

# this function is recursive and will run again if an error in the input is detected by the check_func function
def original_string_creator():
    global string_list # set to pass values after all checks are made
    global punctuation # holds the punctuation until it is add back in final step

    original = input('Enter a word or sentence to translate:')  # input
    original = original.lower()
    punctuation = original[len(original)-1]
    original = original.rstrip(".!?;,")
    string_list = original.split()
    check_func(string_list)

# this function makes sure there are no "numeral" words (exp. 7778), or words with numerals in them. (exp. martian566)
def check_func(string):
    for word in string:
        if len(word) < 1 or hasNumbers(word) == True: # could use refinement
            print ("Enter a sting of at least one alphabetic character")
            original_string_creator()
        else:
            continue
    print (sent_trans(string_list))

def hasNumbers(inputString): #iterates through word to check for digits
    return any(char.isdigit() for char in inputString)

def word_translation(word):
    vowels = word.startswith('a') or word.startswith('e') or word.startswith('i') or \
        word.startswith('o') or word.startswith('u')
    if word[len(word)-1] == ','or word[len(word)-1] == ';': # takes care of words that end with commas or semicolons
        comma_holder = word[len(word)-1]
        word = word.rstrip(',;')
        first = word[0]
        if vowels: # for words that start with a vowel and have a comma
            new_word = word + first + 'way' + comma_holder
            return new_word[1:]
        else:
            new_word = word + first + 'ay' + comma_holder
            return new_word[1:]

    else:
        if word.startswith("qu"): # check for 'qu' start word
            first = word[:2]
            new_word = word + first + 'ay'
            return new_word[2:]

# checks if the word starts with a vowel and adds 'way' instead of 'ay' to the end.
        elif vowels:
            first = word[0]
            new_word = word + first + 'way'
            return new_word[1:]

        elif word == "i": # returns I to its capitalized state
            new_word = "Iway"

        else: # normal cases
            first = word[0]
            new_word = word + first + 'ay'
            return new_word[1:]

def sent_trans(string): # should be accepting a list or single string
    new_sentence = ""
    for word in string:
        new_word = word_translation(word)
        new_sentence += " " + new_word
    if punctuation == "." or punctuation == "?" or punctuation == "!":
        return (new_sentence[1].upper()+new_sentence[2:]+punctuation)
    else:
        return (new_sentence[1].upper()+new_sentence[2:])

def doagain():
    endprog = False

    while endprog != True:
        print()
        convar = input('Would you like to translate another word?')
        if convar.lower() == 'yes' or convar.lower() == 'y':
            original_string_creator()
        elif convar.lower() == 'no' or convar.lower() == 'n':
            endprog = True
        else:
            print('Enter yes or no\n')


# execution starts
welcome()
print ()
original_string_creator()
doagain()
print ("\nOodbyegay")
