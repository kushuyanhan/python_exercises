base = 10
exp = 4

def hello_world():
    base = 20
    print "inside of helloworld base is",base
    return "hello world"

print hello_world()
print "outside of hello world base is", base

def ret_5():
    print 5
print ret_5()

def compute_exp(base, exp):
    print "inside of function, base is", base
    print "inside of function, exp is",exp
    return base**exp

print "outside of function, base is", base
print "outside of function, ep is:", exp

print compute_exp(5,0)
print compute_exp(5,3)
print compute_exp(8,2)
