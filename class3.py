# Minimo y maximo, Clasificación de listas, sumando lista,como unir conjunto de datos y contar número de apariciones.
# Además de la utilización de instrumentos de cuerda y actualización de cadenas.

numeros = [10,45,2,89,54,1,-3]
maximo = max(numeros)
minimo = min(numeros)
print(maximo)
print(minimo)
numeros.sort()
print(numeros)

nombres = ["Christopher","Karla","Daniel","Erick","Kevin"]
nombres.sort()
print(nombres)

# sumar listas
promedios = [85, 95, 65]
print(sum(promedios))

# unir listas o conjuntos de datos

ventas_sab = [50,150,90,85]
ventas_dom = [250,300,100,900]

print(ventas_sab + ventas_dom)

# como saber la moda

pregunta1 = [1,1,1,5,5,5,5,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,1,1,1,1,1,1,1,5,5,5,5,5,4,4,4,4,1,1,1,1,1,1,1,1,1,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4]
print(pregunta1.count(4))
print(30 in pregunta1)

# isntrumentos de cuerda

nuevo_usuario = "Christopher Murillo Gómez"
usuario_lista = nuevo_usuario.split()
print(usuario_lista)

direccion = "Urb El Peregrino, Volcán, BUenos Aires, Puntarenas, Costa Rica, 60301"
nueva_direccion = direccion.replace("Volcán", "Volcancito")
dataset_direccion = direccion.split(",")
print(dataset_direccion)
print(nueva_direccion)