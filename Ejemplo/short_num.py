# En Python, puedes ordenar una lista de números de menor a mayor utilizando la función sorted(). Aquí tienes un ejemplo:

numeros = [5, 3, 1, 4, 2]
numeros.sort()

print(numeros)


# Este algoritmo funciona mediante el intercambio de elementos adyacentes en la lista si están en el orden equivocado (de menor a mayor en este caso). El bucle exterior itera el número de veces equivalente al tamaño de la lista, mientras que el bucle interior compara cada par adyacente de elementos de la lista y los intercambia si es necesario.

numeros = [5, 3, 1, 4, 2]

# Implementar el algoritmo de burbuja
for i in range(len(numeros)):
    for j in range(len(numeros)-1):
        if numeros[j] > numeros[j+1]:
            numeros[j], numeros[j+1] = numeros[j+1], numeros[j]

print(numeros)