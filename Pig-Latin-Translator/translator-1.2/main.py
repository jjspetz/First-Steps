from Translator import translation

welcome()
translation()

endprog = False

while endprog != True:
    convar = input('Would you like to translate another word?')
    if convar.lower() == 'yes' or convar.lower() == 'y':
        translation()
    elif convar.lower() == 'no' or convar.lower() == 'n':
        endprog = True
    else:
        print('Enter yes or no\n')

print('\ngood-bye')
