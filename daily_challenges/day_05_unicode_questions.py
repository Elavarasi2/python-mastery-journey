# Unicode Practice Problems
# Date: Add today's date

# 1. Print Unicode value of every character
word = "Python"
for ch in word:
    print(ch, ord(ch))


# 2. Print only uppercase letters
word = "PyTHonAB"
for ch in word:
    if 65 <= ord(ch) <= 90:
        print(ch)


# 3. Count uppercase letters
word = "PyTHon"
count = 0

for ch in word:
    if 65 <= ord(ch) <= 90:
        count += 1

print(f"Uppercase = {count}")


# 4. Reverse a string without slicing
word = "Python"
end = len(word)

for i in range(end, 0, -1):
    print(word[i - 1], end="")


# 5. Swap uppercase and lowercase without upper()/lower()
word = "PyTHoN123"

for ch in word:
    if 65 <= ord(ch) <= 90:
        small = ord(ch) + 32
        print(chr(small), end="")
    elif 97 <= ord(ch) <= 122:
        cap = ord(ch) - 32
        print(chr(cap), end="")
    else:
        print(ch, end="")


  # Convert uppercase into lowercase without .lower().
word = "PyTHoN"
for ch in word :
    if 65 <= ord(ch) < 97:
        fin = ord(ch) + 32
        print(chr(fin), end = "")
    else :
        print(ch, end="")


# Print the ASCII/Unicode sum.
word = "ABC"
word_sum = 0
for ch in word:
    word_sum+=ord(ch)
print(word_sum)


# Check whether a character is uppercase.
word = "A"
if ord(word) < 97 and ord(word)>64:
    print("Uppercase")




