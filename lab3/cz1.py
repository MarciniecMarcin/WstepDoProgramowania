#zad1

lista = list(["Dawid", "Tomasz", "Artur", "Marcin"])

lista.append("Julian")
lista.append("Bogdan")
lista1 = sorted(lista)
print(lista1)
#b
imie = lista1.pop()
print(imie)

print(lista1)
#c
lista1.insert(3, "Ola")
print(lista1)
#d
lista1.reverse()
print(lista1)
listazdublowana=lista1*2
print(listazdublowana)