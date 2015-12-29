#enciper

phrase = raw_input("enter sentence to encrypt:")
shift = raw_input("enter shift value:")

encoded_phrase = ''

#'A' Asc is 65, 'a' Asc is 97
for c in phrase:
    asc_code = ord(c)
    if asc_code >= 97 and asc_code < 97+26:
        encoded_phrase += chr((asc_code+4-97)%26+97)
    elif asc_code >= 65 and asc_code < 65+26 :
        encoded_phrase += chr((asc_code+4-65)%26+65)
    else:
        encoded_phrase += c

print encoded_phrase
