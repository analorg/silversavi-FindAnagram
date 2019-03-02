# Enter the word that is used for anagrams
WORD_TO_USE = input('Enter the word: ')

# The code follows:
import time

# Start timing
start = time.time()


# The original dictionary
dictionary = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37,
              'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 'š': 71, 't': 73, 'u': 79, 'v': 83,
              'w': 89, 'ö': 97, 'ä': 101, 'õ': 103, 'ü': 107, 'x': 109, 'y': 113, 'z': 127, ' ': 131}
# The custom dictionary based on frequency
dictionary2 = {'a': 2, 'i': 3, 'e': 5, 's': 7, 't': 11, 'u': 13, 'l': 17, 'k': 19, 'r': 23, 'n': 29, 'o': 31, 'm': 37,
               'p': 41, 'v': 43, 'd': 47, 'h': 53, 'g': 59, 'ä': 61, 'õ': 67, 'j': 71, 'ü': 73, 'b': 79, 'ö': 83,
               'f': 89, 'š': 97, '-': 101, 'ž': 103, ' ': 107, 'c': 109, 'z': 113, 'y': 127, 'x': 139,
               'w': 149, 'q': 151}


# Take a word as input and output the unique key describing the word
def find_key_value(input_word):
    key_total = 1
    for i in input_word:
        if i in dictionary2:
            key_total = key_total * dictionary2.get(i)
        else:
            pass
    return key_total


# Take the FULL path to words list, length of the word to search anagrams for, the key and find all anagrams
def find_anagrams(path, word_length, word_key):
    repeats = 0
    nag_a_rams = list()
    with open(path, encoding='iso-8859-13') as f:
        for line in f:
            s = str(line.strip().lower())
            if len(s) != word_length:
                pass
            elif len(s) == word_length:
                key_value_x = find_key_value(s)
                if key_value_x == word_key:
                    nag_a_rams.append(s)
            else:
                print('error')
            repeats += 1
    return nag_a_rams



WORD_TO_USE = WORD_TO_USE.lower()  # Make it case-insensitive
# print('Searching anagrams for the word: ' + WORD_TO_USE) #
PATH = 'lemmad.txt'   # Path to file
WORD_LENGTH = len(WORD_TO_USE)    # The word length to consider
WORD_KEY = find_key_value(WORD_TO_USE)  # Key value of the original word
nag_a_rams = find_anagrams(PATH, WORD_LENGTH, WORD_KEY)   # Looking for other matching keys (which translate to unique words)


# Making the list unique and removing the original word from the output list if exists
nag_a_rams = set(nag_a_rams)
try:
  nag_a_rams.remove(WORD_TO_USE)
except:
  pass
output = ", ".join(nag_a_rams)   # joining the list


# Ending timing and formating the output string
end = time.time()
aeg = (end - start) * float(1000000)
print("{:.2f}".format(aeg) + ", " + output)
