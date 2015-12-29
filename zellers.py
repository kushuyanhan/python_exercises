first_name = raw_input("enter your first name:")
last_name = raw_input("enter your last name:")
print("enter your birth date:")
month = raw_input("month?")
day = raw_input("day?")
year = raw_input("year?")
print first_name,last_name,"was born on", month, day, year

#compute the day of the week of birthday
#A: the month of year, March-1,,,Dec-10,
# Jan and Feb being counted as 11 and 12
# but should minus 1. If month is Jan or Feb
# then the preceding year is used for computation.
#B: the day of the month(1,2,,,31)
#C: the year of the century(c = 89 for the year 1989)
#D: the century(D = 19 for the year 1989)

#Computation:
# W = (13 * A-1)/5
# X = C/4
# Y = D/4
# Z = W+X+Y+B+C-2*D
# R = the remainder when Z is divided by 7

# R is the day of the week.0 is Sun,1 is Sat.
# if R is negative, add 7 to get positive number.


#http://www.timeanddate.com/calendar/
if month == 'March':
    A = 1
elif month == 'April':
    A = 2
elif month == 'May':
    A = 3
elif month == "June":
    A = 4
elif month == "July":
    A = 5
elif month == "Augest":
    A = 6
elif month == "September":
    A = 7
elif month == "October":
    A = 8
elif month == "November":
    A = 9
elif month == "December":
    A = 10
elif month == "January":
    A = 10
elif month == "February":
    A = 11
else:
    print "enter a valid month"

W = (13 * A-1)/5
B = int(day)
C = int(year[2:4])
X = C / 4
D = int(year[0:2])
Y = D / 4

Z = W+X+Y+B+C-2*D

R = Z%7

print R

