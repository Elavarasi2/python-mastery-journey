# Toggle uppercase and lowercase using ord() and chr()

name = "PyThOn123"
res = ""

for letter in name:
    if 65 <= ord(letter) <= 90:
        res += chr(ord(letter) + 32)

    elif 97 <= ord(letter) <= 122:
        res += chr(ord(letter) - 32)

    else:
        res += letter

print(res)
