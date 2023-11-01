x = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
y = []

for z in x:
    a = float(input(f"Ingrese la nota de {z}: "))
    y.append((z, a))

print("Notas del alumno:")
for z, a in y:
    print(f"En {z} tienes una nota de {a}")