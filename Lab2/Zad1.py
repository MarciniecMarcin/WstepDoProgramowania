#petle while
a = int(input("podaj liczbę całkowitą a: "))
b = int(input("podaj liczbę całkowitą b: "))

if a>b:
    while b <= a:
        if b % 2 == 0:
            print(b)
        b+=1
elif a==b and a%2==0:
    print("a jest równe b")

else:
    while a <= b:
        if a % 2 == 0:
            print(a)
        a+=1
