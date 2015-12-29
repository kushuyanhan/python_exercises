x = None
while not x:
    try:
        x = int(raw_input())
    except:
        print 'Invalid number'

