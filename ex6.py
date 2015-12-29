print "example1: make a list of letters in a string"
print [letter for letter in "hello, wolrd"]

print [letter+"!" for letter in "hello world"]

print [letter for letter in "hello world" if letter != 'o']