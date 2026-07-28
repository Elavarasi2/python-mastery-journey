def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year % 4 ==0 and year%100 != 0) or year % 400==0:
        leap = True 
    else:
        leap = False
         
    return leap

year = int(input())
print(is_leap(year))

# The Three RulesDivisible by 4: 
# The year must be evenly divisible by 4 (year % 4 == 0).
# The Century Exception: If it is also divisible by 100 (year % 100 == 0), it is not a leap year, unless the next rule applies.
# The 400-Year Rule: If it is divisible by 400 (year % 400 == 0), it is a leap year
