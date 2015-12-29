def is_palindrome(s):
    #if s is palindrome return True, else return False
    for i in range(0,len(s)/2):
        if s[i] != s[-(i+1)]:
            return False
    return True

print is_palindrome('aha')
print is_palindrome('abcd')
print is_palindrome('able was i ere i saw elba')