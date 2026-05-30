print("BIENVENIDO ACCESORIOS FLORENCIA")

num_mascarillas= 8
num_glos=12
num_camisas=20
num_sombreros_playeros=5
num_sansalias=5

accesorios_totales=num_mascarillas + num_camisas + num_glos + num_sombreros_playeros + num_sansalias

print("ingrese su nombre")
nombre=input()
print("ingrese su apellido")
apellido=input()
nombre_completo=nombre +" "+ apellido

print("Gracias por visitarnos, " , nombre_completo)


print("Actualmente contamos con:")
print("mascarillas:" , num_mascarillas, "glos:" , num_glos, "camisas:", num_camisas, "sombreros:", num_sombreros_playeros, "sandalias:" ,num_sansalias, )
print("En total tenemos",accesorios_totales, "accesorios")
