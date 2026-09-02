# Count uppercase, lowercase, digits and ASCII special characters
word = "Ela@!2026"
upper = 0
lower = 0
special = 0
digits = 0
for ch in word:
    if 65<= ord(ch) <=90:
        upper += 1
    elif 97<= ord(ch) <=122:
        lower += 1
    elif 48<= ord(ch) <=57:
        digits += 1
    elif 33<= ord(ch) <=47 or 91<= ord(ch) <=96 or 123<= ord(ch) <=126 or 58<= ord(ch) <=64:
        special += 1
print("Uppercase = ",upper)
print("Lowercase = ",lower)

print("Digits = ",digits)
print("Special Characters = ",special)
