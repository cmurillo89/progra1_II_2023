# Ser capaz de organizar muchos datos relaciones, es una parte escencial de la ciencia de datos.

age_1 = 27
age_2 = 35
age_3 = 25
age_4 = 13

# Listas
# Los datos dentro de la lista se llaman ELEMENTOS

tareas = ["Read","Workout","Code"]

print(tareas)

user = ["cmurillo", "aarauz", "jgamboa", "kprado",5, True]

print(user)

temperaturas = [17,20,26,24]
print(temperaturas[2])
temperaturas[2] = 35
print(temperaturas[2])

laps = [320,315,321]

laps.append(365)
laps.insert(1,319)
eliminado = laps.pop(0)
print(laps)
print("El elemento eliminado es:",eliminado)

# Recorrer listas por medio de un bucle

notas = [98,80,74,96,50,45]


for nota in notas:
    print(nota)

artistas = ["Roses","franco"]

for artista in artistas:
    print(artista)

# Para averiguar el numero de elementos que tiene una lista es con la palabra reservada LEN()

users = ["cmurillo", "aarauz", "jgamboa", "kprado"]
user_cont = len(users)
print(user_cont)

# Podemos usar la longitud de la lista para crear declaraciones condicionales basadas en la cantidad de elemntos como el anterior

if user_cont > 0:
    print("Empieza a trabajar")

lista_compras = ["papas","pasta","arroz"]
print(lista_compras[-1])

if len(lista_compras) > 0:
    print("Tu lista de compras es la siguiente:")
    for arti in lista_compras:
        print(arti)
else:
    print("No tienes nada en tu lista de compras.")