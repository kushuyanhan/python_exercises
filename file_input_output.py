with open('input_text.txt','r') as txt:
    for line in txt:
        print line

for line in open('input_text.txt','r'):
    print line[0]

f = open('input_text.txt','r')
for line in f:
    print line[0]
f.close()





for i in range(10):
    print i,
print >> f, 'hello world'