print("program do porządkowania 3 liczb od najmniejszej do największej")
x = int(input("wprowadź pierwszą liczbę: "))
y = int(input("wprowadź drugą liczbę: "))
z = int(input("wprowadź trzecia liczbę: "))
lista1 = (x, y, z) #zmienna pobierająca dane od użytkownika
lista  = list(lista1) #zmiana na listę
def sortowanie(lista):
    n = len(lista)

    while n > 1:
        zamien = False
        for l in range(0, n - 1):
            if lista[l] > lista[l + 1]:
                lista[l], lista[l + 1] = lista[l + 1], lista[l]
                zamien = True

        n -= 1
        print(lista)
        if zamien == False: break

    return lista
sortowanie(lista)