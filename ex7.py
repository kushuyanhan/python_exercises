new_tuple = (5,6,7,8)
print "new_tupe is:", new_tuple

print "new_tupe[2] is:", new_tuple[2]

for item in new_tuple:
    print item

print "Tuple length is:", len(new_tuple)

for index in range(len(new_tuple)):
    print "index is:", index
    print "value at that index is:", new_tuple[index]

(a,b,c,d) = new_tuple
print "a is:", a
print "b is:", b
print "c is:", c
print "d is:", d

b = 77

new_tuple =(a,b,c,d)
print "new_tupe is now:", new_tuple