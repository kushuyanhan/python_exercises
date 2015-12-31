# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq




# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()


# TO DO: your code begins here!
word = []
def play_ghost(word_list):

    current_player = 1
    print 'welcome to Ghost!'
    print 'player1 goes first.'
    print 'current word fragment: '''
    while True:

        print 'player %d turn' %(current_player)
        print 'player %d says letter:' %(current_player),
        user_letter = raw_input()

        while not is_valid_letter(user_letter):
            print 'This is not a letter, please enter a letter:'

        update_word = update_fragment(user_letter)
        display_fragment(update_word)

        isCompleteWord = is_complete_word(update_word,word_list)
        if isCompleteWord:
            print 'player  %d loses because %s is a word!' %(current_player,update_word)
            print 'player %d wins'  %((current_player+1)%2)
            break
        else:
            isValid = is_valid_word(update_word, word_list)
            if not isValid:
                print 'player %d loses because no word begins with %s' %(current_player, update_word)
                print 'player %d wins' %((current_player+1)%2)
                break

        if current_player >= 2:
            current_player = (current_player+1)%2
        else:
            current_player += 1


def update_fragment(letter):
    word.append(letter)
    return ''.join(word)

def display_fragment(update_word):
    print 'current word fragment is:', update_word

def is_valid_letter(letter):
    return letter in string.ascii_letters

def is_valid_word(update_word,word_list):
    for word in word_list:
        if update_word == word.lower()[0:len(update_word)]:
            return True
    return False

def is_complete_word(fragment,word_list):
    return fragment in word_list

if __name__ == '__main__':
    word_list = load_words()
    play_ghost(word_list)


