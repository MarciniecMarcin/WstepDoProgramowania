a = int(input("podaj liczbę "))
n = int(input(("podaj stopień potęgi ")))

def rekurencja(a, n):
    if a > 0 and n > 0:
        while True:
            potega = a
            for i in range(1, n):
                potega *= a
            print(potega)
            break
rekurencja(a, n)
