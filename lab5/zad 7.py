import random
from math import prod

def losuj_krotke(ilosc_elementow, Min, Max):
    return tuple(random.uniform(Min, Max) for _ in range(ilosc_elementow))

def srednia_geometryczna(krotka):
    if len(krotka) == 0:
        return None
    return prod(krotka) ** (1/len(krotka))

# Pytaj użytkownika o przedział
Min = int(input("Podaj dolny przedział: "))
Max = int(input("Podaj górny przedział: "))

# Losuj krotkę
ilosc_elementow = 10
moja_krotka = losuj_krotke(ilosc_elementow, Min, Max)

# Oblicz średnią geometryczną
srednia_geo = srednia_geometryczna(moja_krotka)

# Wyświetl wyniki
print("Losowa krotka:", moja_krotka)
print("Średnia geometryczna:", srednia_geo)
