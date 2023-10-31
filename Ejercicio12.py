x = input("introduzca una serie de numeros separados por comas")
y = x.split(",")
z = [float(a) for a in y]

print(z)