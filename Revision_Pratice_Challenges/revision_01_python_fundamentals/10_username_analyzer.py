# Username Analyzer

word = "Ela_Developer2026"

print("Length:", len(word))

upper = 0
lower = 0
special = 0
digits = 0

for ch in word:

    if 65 <= ord(ch) <= 90:
        upper += 1

    elif 97 <= ord(ch) <= 122:
        lower += 1

    elif 48 <= ord(ch) <= 57:
        digits += 1

    elif (33 <= ord(ch) <= 47 or
          91 <= ord(ch) <= 96 or
          123 <= ord(ch) <= 126 or
          58 <= ord(ch) <= 64):
        special += 1

print("Uppercase =", upper)
print("Lowercase =", lower)
print("Digits =", digits)
print("Special Characters =", special)
print("Reversed:", word[::-1])


# Username Validation

if len(word) >= 8 and upper >= 1 and lower >= 1 and digits >= 1:
    print("Valid Username!")
else:
    print("Invalid Username!")
