# Local vs Global Scope

result = 100

def calculate():
    result = 50
    return result

x = calculate()

print(x)
print(result)
