x = input("introduzca una serie de numeros separados por comas")
y = x.split(",")
z = [float(a) for a in y]

b = sum(z)/len(z)

print("la media de", z, "es", b)