hello_world = "hello world"

letter_count = 0

for letter in hello_world:
    print "letter number", letter_count, "is",letter
    letter_count = letter_count +1

print 'there are',letter_count, "letters in the string", hello_world

for num in range(10):
    print num
for num in range(7,15):
    print num

count = 1
print "count is inintially", count

while count < 100:
    count = count * 9
    print "now count is", count
print count