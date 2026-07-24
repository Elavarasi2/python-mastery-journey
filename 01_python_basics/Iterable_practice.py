

# String Iterable
word = input("Enter your name : ")
count = 0
for letter in word:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        count+=1
print(f"The vowel count in this name is {count}")
