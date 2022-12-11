lista = [2,4,6,8,10,2,2]
print(lista)
print(lista[2], lista[3])
lista[2] = 1
print(lista)


print(lista[2:4])
print(lista[2:])
print(lista[1:-1])

lista.insert(1,55)
lista.append(100)
print(lista)
lista.append(2)
print(lista)
lista.remove(2)
print(lista)

while 2 in lista:
    lista.remove(2)
    print(lista)
