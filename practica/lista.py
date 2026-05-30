nombres = ["Rodrigo", "Juan", "Pedro", "Santiago", "Jorge", "Raymundo"]
print(nombres)

#f-strings
for i, nombre in enumerate(nombres):
    print(f"Se inscribió {nombre} en la lista con el índice {i}")

print("Bienvenido a la fiesta", nombres[:3])
print("Lo siento", nombres[3:])
