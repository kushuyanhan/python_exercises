# # Name:
# # Section:
# # strings_and_lists.py
#
# # **********  Exercise 2.7 **********
#
# def sum_all(number_list):
#     # number_list is a list of numbers
#     total = 0
#     for num in number_list:
#         total += num
#
#     return total
#
# # Test cases
# print "sum_all of [4, 3, 6] is:", sum_all([4, 3, 6])
# print "sum_all of [1, 2, 3, 4] is:", sum_all([1, 2, 3, 4])
#
#
# def cumulative_sum(number_list):
#     # number_list is a list of numbers
#
#     ##### YOUR CODE HERE #####
#     for i in range(1,len(number_list)):
#         number_list[i] += number_list[i-1]
#
#     return number_list
#
# # Test Cases
# ##### YOUR CODE HERE #####
# print "cumulative sum of [4,3,6] is:",cumulative_sum([4,3,6])
# print "cumulative sum of [1,2,3,4] is:",cumulative_sum([1,2,3,4])
#
#
# # **********  Exercise 2.8 **********
#
# def report_card():
#     ##### YOUR CODE HERE #####
#     i = 0
#     classes = int(raw_input("How many classes did you take"))
#     my_list = []
#
#
#     while i < classes:
#         elt = {'name':None,'grade':0};
#         name = raw_input("what was the name of this class?")
#         grade = int(raw_input("what was your grade"))
#         elt['name'] = name
#         elt['grade'] = grade
#         my_list.append(elt)
#         i += 1
#
#
#     print "report card:"
#     total = 0
#     for elt in my_list:
#         print elt['name'],elt['grade']
#         total += elt['grade']
#     print "overall gpa", total/len(my_list)
#
#
# # Test Cases
# ## In comments, show the output of one run of your function.
# report_card()
# # **********  Exercise 2.9 **********
#
# # Write any helper functions you need here.
#
# VOWELS = ['a', 'e', 'i', 'o', 'u']
#
# def pig_latin(word):
#     # word is a string to convert to pig-latin
#     if word[0] in VOWELS:
#         word = word + 'hay'
#     else:
#         word = word[1:]+word[0]+'ay'
#     ##### YOUR CODE HERE #####
#     return word
#
# # Test Cases
# ##### YOUR CODE HERE #####
# print pig_latin('boot')
# print pig_latin('image')

# **********  Exercise 2.10 **********
# Test Cases
##### YOUR CODE HERE #####
S = [x**3 for x in range(10)]
print S

V = []
print V

def returnAllVowels(str):
    vowel_elements = ['a','e','i','o','u']
    vowels = [x for x in str if x in vowel_elements]
    return vowels
print returnAllVowels("this is cool")


T = [x+y for x in [10,20,30] for y in [1,2,3]]
print T

# **********  Exercise OPT.1 **********
# If you do any work for this problem, submit it here
VOWELS = ['a', 'e', 'i', 'o', 'u']



def pig_latin(word):
    # word is a string to convert to pig-latin
    if word[0] in VOWELS:
        word = word + 'hay'
    else:
        word = word[1:]+word[0]+'ay'
    return word

def translate(sentence):
    newSentence = ''
    word_list = sentence.split()

    for word in word_list:
        newSentence += pig_latin(word)

    return newSentence

print translate('boot image')


#ootbay
#imagehay
