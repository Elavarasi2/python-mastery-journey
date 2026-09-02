# Divide a string into chunks of size k

word = "AAABBCDDDAA"
k = 3

for i in range(0, len(word), k):
    print(word[i:i+k])
