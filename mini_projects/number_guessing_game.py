import random
print("Welcome to the random number generator game")
computer=random.randint(1,100)
print("You have only five chances")
print("Guess a number between 1-100")

for x in range(5):
    user_input=int(input("Enter your number : "))
    if user_input==computer:
        print("You won the game")
        break
    elif user_input>computer:
        print("think less number")
        
    elif user_input<computer:
        print("think high number")
else:   
    print("you lost the game")
    print(f"the correct number is {computer} ")
