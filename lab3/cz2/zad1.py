import random
#a
n=int(input("ile elementów ma lista "))
x=int(input("ile znaków maksymalnie "))
s=int(input("ile jest ciągów znaków dłuższych "))
#ascii 65-90
print(random.randint(65, 90))
koniec=0
słowo=""
lista=[]
for i in range(n):
    #losowanie pojedynczego słowa
    for i in range(x-1):
        if koniec >= 0.7:
            break
        else:
            słowo+=chr(random.randint(65, 90))
            print(słowo)
        koniec=random.random()
        print(koniec)
    lista.append(słowo)
    koniec=0
    słowo=""
print(lista)
krotka=tuple(lista)
print(krotka)
#a
print(len(lista))
znaki=0
for i in range(len(krotka)):
    znaki+=len(krotka[i-1])
print(znaki)

#b
k=0
for i in range(len(lista)):
   k+=lista[i].count("K")
print(k)
#c
kt=0
for i in range(len(lista)):
   kt+=lista[i].count("kt")
print(kt)
#d
ciagZnakow=[]
for i in lista:
    if len(i) > s:
        ciagZnakow.append(i)

print(len(ciagZnakow))