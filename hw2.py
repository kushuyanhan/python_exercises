# Name:
# Section:
# hw2.py

##### Template for Homework 2, exercises 2.0 - 2.5  ######

# **********  Exercise 2.0 **********

def f1(x):
    print x + 1

def f2(x):
    return x + 1

print f1(3) #print 4, and return None
print f2(3)  #reuturn 4

#print f1(3)+1   # failed because unsupported operand type for 'int'+'str' 1+None
print f2(3)+1 # 5

# **********  Exercise 2.1 **********

# Define your function here
##### YOUR CODE HERE #####
#paper,rock, scissors
def rps(player1,player2):
    if player1 == player2:
        print "Tie game"
    elif (player1 == 'scissors' and player2 == 'paper' or
         player1 == 'rock' and player2 == 'scissors' or
         player1 == 'paper' and player2 == 'rock'):
        print "player1 wins"
    else:
        print "player2 wins"

# Test Cases for Exercise 2.1
##### YOUR CODE HERE #####
rps("scissors","paper")
rps("paper","rock")
rps("rock","scissors")

rps('paper','scissors')
rps('scissors','rock')
rps('rock','paper')

rps('scissors','scissors')
rps('paper','paper')
rps('rock','rock')
# ********** Exercise 2.2 **********

# Define is_divisible function here
##### YOUR CODE HERE #####
def is_divisible(m,n):
    if n != 0:
        if m%n == 0:
            return True
        else:
            return False
    else:
        print 'can not be divisibe by zero'
# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

print is_divisible(10, 5)  # This should return True
print is_divisible(18, 7)  # This should return False
print is_divisible(42, 0)  # What should this return?


# Define not_equal function here
##### YOUR CODE HERE #####
def not_equal(m,n):
    if m > n or m < n:
        return True
    else:
        return False



# Test cases for not_equal
##### YOUR CODE HERE #####
not_equal(2,2)
not_equal(2,3)
# ********** Exercise 2.3 **********
import math
import random

## 1 - multadd function
##### YOUR CODE HERE #####
def multadd(a,b,c):
    return a*b+c



## 2 - Equations
##### YOUR CODE HERE #####
a = math.sin(math.pi/4)
b = 1
c = math.cos(math.pi/4)/2

print multadd(a,b,c)
# Test Cases
# angle_test =
# print "sin(pi/4) + cos(pi/4)/2 is:"
# print angle_test

# ceiling_test =
# print "ceiling(276/19) + 2 log_7(12) is:"
# print ceiling_test

## 3 - yikes function
##### YOUR CODE HERE #####


# Test Cases
# x = 5
# print "yikes(5) =", yikes(x)

# ********** Exercise 2.4 **********

## 1 - rand_divis_3 function
##### YOUR CODE HERE #####
def rand_divis_3():
    if random.randint(0,100)%3 == 0:
        return True
    else:
        return False


# Test Cases
##### YOUR CODE HERE #####
print rand_divis_3()
print rand_divis_3()
## 2 - roll_dice function - remember that a die's lowest number is 1;
                            #its highest is the number of sides it has
##### YOUR CODE HERE #####
def roll_dice(n,m):
    for i in range(0,m):
        print random.randint(1,n)


# Test Cases
##### YOUR CODE HERE #####
roll_dice(6,3)

# ********** Exercise 2.5 **********

# code for roots function
##### YOUR CODE HERE #####



# Test Cases
##### YOUR CODE HERE #####