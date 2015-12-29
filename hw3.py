# Name:
# Section:
# hw3.py

##### Template for Homework 3, exercises 3.1 - ######

# **********  Exercise 3.1 **********

# Define your function here
##### YOUR CODE HERE #####

def list_intersection(list1,list2):
    list_inter = []
    for i in list1:
        if i in list2:
            list_inter.append(i)
    return list_inter


# Test Cases for Exercise 3.1
##### YOUR CODE HERE #####
print list_intersection([1,3,5],[5,3,1])

print list_intersection([1,3,6,9],[10,14,3,72,9])

print list_intersection([2,3],[3,3,3,2,10])

print list_intersection([2,4,6],[1,3,5])

print '---------'


# **********  Exercise 3.2 **********

# Define your function here
import math

def ball_collide(ball1, ball2):
    ##### YOUR CODE HERE #####
    distance = math.sqrt(math.pow(ball1[0] - ball2[0],2)+ math.pow(ball1[1] - ball2[1],2))
    if distance < ball1[2] + ball2[2]:
        return False
    else:
        return True


# Test Cases for Exercise 3.2
print ball_collide((0, 0, 1), (3, 3, 1)) # Should be False
print ball_collide((5, 5, 2), (2, 8, 3)) # Should be True
print ball_collide((7, 8, 2), (4, 4, 3)) # Should be True
print '--------'
# **********  Exercise 3.3 **********

# Define your dictionary here - populate with classes from last term
my_classes = {}

def add_class(class_num, desc):
    ##### YOUR CODE HERE #####
    my_classes[class_num] = desc
    return my_classes

# Here, use add_class to add the classes you're taking next term
add_class('6.189', 'Introduction to Python')
add_class('6.01','Introduction to EECS')

def print_classes(course):
    ##### YOUR CODE HERE #####

    for key in my_classes.keys():
        if key[0][0] != course:
           print 'no course'
           break
        else:
            print key,'-', my_classes[key]


# Test Cases for Exercise 3.3
##### YOUR CODE HERE #####
print_classes('6')
print_classes('9')
# **********  Exercise 3.4 **********
print '-----3.4------'
NAMES = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank',
                 'Gary', 'Helen', 'Irene', 'Jack', 'Kelly', 'Larry']
AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]

# Define your functions here
def combine_lists(l1, l2):
    comb_dict = {}
    ##### YOUR CODE HERE #####
    for i in range(0,len(NAMES)):
        comb_dict[NAMES[i]] = AGES[i]
    return comb_dict

combined_dict = combine_lists(NAMES, AGES) # Finish this line...

def people(age):
    # Use combined_dict within this function...
    same_age = []
    for key in combined_dict.keys():
        if age == combined_dict[key]:
            same_age.append(key)
    return same_age


# Test Cases for Exercise 3.4 (all should be True)
print 'Dan' in people(18) and 'Cathy' in people(18)
print 'Ed' in people(19) and 'Helen' in people(19) and\
        'Irene' in people(19) and 'Jack' in people(19) and 'Larry'in people(19)
print 'Alice' in people(20) and 'Frank' in people(20) and 'Gary' in people(20)
print people(21) ==   ['Bob']
print people(22) ==   ['Kelly']
print people(23) ==   []

# **********  Exercise 3.5 **********
print '---3.5'
def zellers(month, day, year):
    ##### YOUR CODE HERE #####

    return "Not Yet Implemented"

# Test Cases for Exercise 3.5
print zellers("March", 10, 1940) == "Sunday" # This should be True
##### YOUR CODE HERE #####