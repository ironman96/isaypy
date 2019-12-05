"""
Morse v1.0.0
Type in text to have it converted to Morse code.
 
By Steve Krishnendu Dec 2019,
stevepython.wordpress.com
 
Based on Python Dictionaries(https://www.python-course.eu/python3_dictionaries.php)
"""
morse = {
    'A' : '.-',
    'B' : '-...',
    'C' : '-.-.',
    'D' : '-..',
    'E' : '.',
    'F' : '..-.',
    'G' : '--.',
    'H' : '....',
    'I' : '..',
    'J' : '.---',
    'K' : '-.-',
    'L' : '.-..',
    'M' : '--',
    'N' : '-.',
    'O' : '---',
    'P' : '.--.',
    'Q' : '--.-',
    'R' : '.-.',
    'S' : '...',
    'T' : '-',
    'U' : '..-',
    'V' : '...-',
    'W' : '.--',
    'X' : '-..-',
    'Y' : '-.--',
    'Z' : '--..',
    '0' : '-----',
    '1' : '.----',
    '2' : '..---',
    '3' : '...--',
    '4' : '....-',
    '5' : '.....',
    '6' : '-....',
    '7' : '--...',
    '8' : '---..',
    '9' : '----.',
    '.' : '.-.-.-',
    ',' : '--..--',
    '?' : '..--..',
    '!' : '-.-.--'
    ' ' : ' '
    }
# Get user input of a letter\word\phrase.
users_text = input('Input text to convert to Morse code:')
 
# Make uppercase, as in dictionary above.
users_text = users_text.upper()
 
# Split the word into a list of single single_letters.
single_letters = list(users_text)
 
# Print(single_letters) #would look like this,['T', 'W', 'A', 'T']
 
print_this = ''
 
# Iterate through the single_letters list.
for x in single_letters:
    # Store the Morse for each letter from Morse dict into string 'arse'
    # Build new string to print called print_this, containing all the arses
    arse = (morse[x])
    print_this = print_this +arse+' '
 
#print original inputted word and the Morse code for it
print()
print(users_text +' in morse is:\n '+print_this)
