lista = [54,212,44,45,89,12,-3,2,89,74,5,6,2,88,-6]

for i in range(len(lista)):
    for j in range(len(lista)-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]


print(lista)
    
