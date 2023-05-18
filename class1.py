# Vamos a observar como funcionan las estructuras de control

saludo = False

if saludo:
    print("hola Chris")
else:
    print("no hay saludos")


is_online = True

if is_online:
    print("Kevin is online")

respuesta = "Tortuga"

if respuesta != "Lagarto":
    print(respuesta,"es correcto")

edad = 18
if edad >= 18:
    print("Es mayor de edad")

nota = 90

if nota < 60:
    print("El alumno se quedó")
elif nota < 70:
    print("El alumno se fue a penales")
else:
    print("El alumno pasó el año")


# Vamos a realizar ejemplos de bucles o ciclos
# Variables e control

num1 = 1


# Bucle Mientras o While
# control = True
# while control == True:
#     print(num1)
#     num1 += 1
#     if num1 == 101:
#         control = False

contador = 0
online = True
num2 = 1
while contador < 100 and online:
    print(num2)
    num2 += 1
    contador += 1  

# Bucle o ciclo FOR

for i in range(4):
    print(i)

for c in range(2):
    print("we will")

print("Rock you!")

for num in range(0, 11, 2):
    print(num)

