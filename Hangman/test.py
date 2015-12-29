


def print_guessed():
    '''
    Prints out the characters you have guessed in the secret word so far
    '''
    secret_word = 'claptrap'
    letters_guessed = ['p']
    character_list = []
    ####### YOUR CODE HERE ######
    for i in secret_word:
        if i in letters_guessed:
            character_list.append(i)
        else:
            character_list.append('-')
    return ''.join(character_list)

print print_guessed()