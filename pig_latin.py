VOWELS = ['a', 'e', 'i', 'o', 'u']

def pig_latin(word):
    # word is a string to convert to pig-latin
    if word[0] in VOWELS:
        word = word + 'hay'
    else:
        word = word[1:]+word[0]+'ay'
    ##### YOUR CODE HERE #####
    return word

# Test Cases
##### YOUR CODE HERE #####
print pig_latin('boot')
print pig_latin('image')
