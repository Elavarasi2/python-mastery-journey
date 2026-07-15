import random
game=["rock","paper","scissors"]
user_choice=int(input())
if user_choice>=0 and user_choice<=2:
    print(game[user_choice])
computer_choice=random.randint(0,2)
print(game[computer_choice])

if user_choice>=3 or user_choice<0:
    print("invalid")
elif user_choice==0 and computer_choice==2:
    print("You win")
elif user_choice==2 and computer_choice==0:
    print("Computer win")
elif user_choice<computer_choice:
    print("You lose")
elif user_choice>computer_choice:
    print("You win")
elif user_choice==computer_choice:
    print("draw")
