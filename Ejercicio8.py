x = input("introduzca una plabara")
y = x.lower()

if y != y[::-1]:
    print(x, "no es un palindromo")
else:
    print(x, "es un palindromo")