def is_a_vowel(c):
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c =='u':
        return True
    elif c=='A'or c=='E' or c =='I' or c== 'O' or c == 'U':
        return True
    else:
        return False

print is_a_vowel("u")
print is_a_vowel("E")

def only_vowels(phrase):
    vowel_string = ''
    for letter in phrase:
        if is_a_vowel(letter):
            vowel_string += letter
    return vowel_string

    print "a line of code after the return"

print "the vowels in the phrase 'tim the beaver' are:", only_vowels("tim the beaver")

print only_vowels("hello world")
print only_vowels("klxn")