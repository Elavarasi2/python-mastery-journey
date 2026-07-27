foo = "AAAA"
result = []
for c in foo:
    if c not in result:
        result.append(c)       
result = ''.join(result)
print(result)

## -------------------------- USING SET --------------------------

foo = "AAABCADDE"
seen = set()
result = []
for c in foo:
    if c not in seen:
        result.append(c)
        seen.add(c)
result = ''.join(result)
print(result)
