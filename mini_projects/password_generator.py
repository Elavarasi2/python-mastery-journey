import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
print("Welcome to the PyPassword Generator")
letter = int(input("How many letters would you like in your password? "))
sym = int(input("How many symbols would you like? "))
num = int(input("How many numbers would you like? "))
f_let = []
f_num = []
f_sym = []
for i in range(letter):
    f_let += random.choice(letters)
print(f_let)

for j in range(num):
    f_num += random.choice(numbers)
print(f_num)

for k in range(sym):
    f_sym += random.choice(symbols)
print(f_sym)
final_pass = f_let + f_num + f_sym
print(final_pass)

random.shuffle(final_pass)
print(final_pass)
print(''.join(final_pass))
# result=""
# for lat in final_pass:
#     result+=random.choice(final_pass)
# print(result)
# print(random.shuffle(final_passkey))


# Another Method - Shorter Version
import random
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers=["0","1","2","3","4","5","6","7","8","9"]
symbols=["!","#","$","%","&","(",")","*","+"]
print("Welcome to the PyPassword Generator")
letter=int(input("How many letters would you like in your password? "))
sym=int(input("How many symbols would you like? "))
num=int(input("How many numbers would you like? "))
password_list=[]
for i in range(letter):
    password_list.append(random.choice(letters))
for i in range(sym):
    password_list.append(random.choice(symbols))
for i in range(num):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)
result=""
for i in password_list:
    result+=i
print(f"the final password is {result}")
  
