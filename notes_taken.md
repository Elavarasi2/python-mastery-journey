# l1=[1,2,3]
# l2=[4,5,6]
# l3=[l1,l2]
# print(l3)
------------------------------------------------------------------------------------------------------
m=[]

# print(type(m))
for i in range(5):
    m.append([]) // append nested empty loop
    for j in range(5):
        m[i].append(j) // m[0]=>0,1,2,3,4 similarly goes on
print(m)

------------------------------------------------------------------------------------------------------

# String objects and reference
x="hi"
y="hi"

print(id(x))
print(id(y))
if x==y:
    print("true")
y="hello"
print(id(x))
print(id(y))
------------------------------------------------------------------------------------------------------
Whenever you apply string manipulations, such as .replace() or string concatenation (+), 
Python leaves the original data intact and allocates a brand new string object in a different memory location

message = "Hello"
print(id(message))
message = message + " World"  # "Hello" is discarded; a new "Hello World" object is made
print(id(message))

------------------------------------------------------------------------------------------------------
Why is this allowed?

Because variables are mutable in the sense that they can be rebound to different objects.

Objects may be immutable, but variables can always point somewhere else.
a="ELavarasi"
b=a
a="ela"
print(a)
print(b)

Before:

message
   │
   ▼
"Hello"

After:

        "Hello"

message
   │
   ▼
"Hello World"

The variable moved.

The string did not change.

------------------------------------------------------------------------------------------------------
#### LOOPS ####

fruits=["cherry","pineapple","apple","ela"]
print(fruits[:2])
print(fruits[:])

for i in range(1,6):
    print(f"Elavarsi , this is {i} warning")

OR 

for i in range(1,6):
    print("Elavarsi , this is "+str(i)+" warning")

^^^ Error ^^^
for i in range(6):
    print(f"Elavarsi , this is "+{i}+" warning")

for i in range(6):
    print("Elavarsi , this is "+i+" warning")

-------------------Highest Score of students(My answer)

student_scores=[50,100,80,70,50,120,30,50,60,70,80]
max=student_scores[0] or max=0
for result in student_scores: # result=50
    if max<result: #50 
        max=result
print(max)
-------------------------sum of numbers using LOOPS
student_scores=[50,100,80,70,50,120,30,50,60,70,80]
sum=0 #50
for result in student_scores: # result=50
    sum=sum+result // sum+=result
print(sum)

for i in range(0,10,-1):
    print(i)
    
## FizzBuzz Game
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
------------------------------------------------------------------------------------------------------
#### WHILE LOOPS ####   
num=123
sum=0
while num>0:
    rem=num%10 # 3
    sum+=rem
    num//=10
print(sum)

num=123
result=""
while num>0:
    rem=num%10 # 6
    print(rem,end="")
    num//=10

num=321
rev=0
while num>0:
    rem=num%10 #3-2-1
    rev=rev*10+rem #3-32-321
    num//=10 #12-1-0
print(rev)

------------------------------------------------------------------------------------------------------
##### Functions with paramaters ####

def say_hello(name):
    print("Hello ",name)
    
say_hello("Elavarasi")
say_hello("John")


def multiply(a,b):
    print(a*b)
    
multiply(5,6)

def country(city, country_name):
    print(city , " is in ",country_name)
    
country("Chennai","India")
