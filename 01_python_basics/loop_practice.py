# Reverse a number 
num = 123
rev   = 0
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num //= 10
print(rev)


# Palindrome
num = 101
temp = num
rev   = 0
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num //= 10
print(rev) # for checking
if temp == rev :
    print("This is a palindrome")
else :
    print("Not a palindrome")
