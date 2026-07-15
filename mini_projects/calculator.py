a=8.563356789
#Round function
print(round(a))
print(round(a,2))
# F strings
print(f"hi this is = {10}")
#Calculator Task
print("Welcome to the tip calculator!")
total_bill=float(input("What was the total bill? "))
tip=int(input("How much tip would you like to give? 10, 12, or 15?"))
split=int(input("How many people to split the bill?"))
total_amount=(total_bill+(total_bill*tip/100))/split
print(f"Each person should pay: {round(total_amount,2)}")
