#print decimal equivalents of 1/2,1/3,1/4
for i in range(1,11):
    print 1.0/i

#print out countdown
var = int(raw_input("enter a number"))
while var < 0:
    var = int(raw_input("enter a positive number"))

while True:
    print var
    var -= 1
    if var < 0:
       var = int(raw_input("enter a number"))




#calculate base and exp
base = int(raw_input("enter a base"))
exp = int(raw_input("enter an exp"))

result = base ** exp
print result

#enter an even number
number = int(raw_input("enter an even number"))
while number%2 != 0:
    number = int(raw_input("enter an even number"))
    if number%2 == 0:
        print "congrats"
        break



