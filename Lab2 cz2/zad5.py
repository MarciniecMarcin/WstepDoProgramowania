liczba = int(input("podaj liczbę naturalną "))
if liczba > 0:
    while True:
        silnia = 1
        for i in range(2, liczba+1):
            silnia *= i
        print(silnia)
        break
    liczba = int(input("podaj liczbę naturalną "))
if liczba < 0:
    print("liczba naturalna jest większa od zera")

