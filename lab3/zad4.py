#a
"""imie=input("wpisz imie ")

print("witaj", imie)
#b
wiek=int(input("podaj swój wiek "))
print("twój wiek to ", wiek)
#c
nazwisko=input("Wpisz swoje nazwisko ")
imie1 = input("wpisz imie ")
print(list(imie1[0]), list(nazwisko[0]))
#d

for i in range(0,5):
    tekst = "python jest super"
    print(tekst)
    i += 1
#e
nazwisko=input("Wpisz swoje nazwisko ")
imie2 = input("wpisz imie ")
print(nazwisko +" " + imie2)"""

#f
import math
nazwisko=input("Wpisz swoje nazwisko ")
imie3 = input("wpisz imie ")
dltekst1 = math.ceil(len(list(nazwisko))/2)
tekst1 = str(nazwisko[:dltekst1])

dltekst2 = math.ceil(len(list(imie3))/2)
tekst2 = str(imie3[:dltekst2])

listafinal = tekst1 + tekst2
print(tekst1+tekst2)