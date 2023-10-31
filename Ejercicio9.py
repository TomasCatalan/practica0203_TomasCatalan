x = input("introduzca una palabra")
y = x.lower()

a = 0
e = 0
i = 0
o = 0
u = 0

for z in y:
    if z == "a":
        a += 1
    elif z == "e":
        e += 1
    elif z == "i":
        i += 1
    elif z == "u":
        u += 1
    elif z == "o":
        o +=1

print("A aparece", a, "veces")
print("E aparece", e, "veces")
print("I aparece", i, "veces")
print("O aparece", o, "veces")
print("U aparece", u, "veces")