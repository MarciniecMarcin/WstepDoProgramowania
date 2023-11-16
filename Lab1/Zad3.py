from pprint import pprint

pprint("1 dodawanie "
       "2 odejmowanie "
       "3 mnożenie "
       "4 dzielenie "
       "5 potęgowanie")
x = int(input("jaką operację chcesz wykonać? wprowadź numer: "))
i = int(input("podaj pierwszy argument: "))
j = int(input("podaj drugi argument: "))
z = i + j
k = i - j
p = i * j
w = i / j
c = i ** j

if x == 1:
    print("wynik z dodawania: ", z)
elif x == 2:
    print("wynik z odejmowania: ", k)
elif x == 3:
    print("wynik z mnożenia: ", p)
elif x == 4:
    print("wynik z dzielenia: ", w)
elif x == 5:
    print("wynik z potęgowania: ", c)

