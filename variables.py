# variable

nombre = "Gabriel Lascano"
edad = 25
casado = False
escritura = 1.75
colores = ["Negro", "Azul", "Blanco", 25, 1.75]

colores = colores + ["Gris"]
colores.append("Verde")
colores2 = colores.copy()

colores.clear()

colores2.pop(0)

colores2.remove("Dorado")



print(colores)
print(colores2)

print(type(edad))