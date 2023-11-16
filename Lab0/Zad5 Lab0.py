i = int(input("podaj długość:" ))
j = int(input("podaj szerokość:" ))

z = i * j
x = i * 2 + j * 2

print(f"pole prostokąta to {z}")
print(f"obwód prostokąta to {x}")

#zadanie4 Lab0
i = int(input("podaj ile kilometrów przejechałeś: "))
j = int(input("podaj średnie spalanie[L/100km]: "))
k = 6.50 #koszt paliwa
a = i * j / 100
b = a * k
print(f"koszt paliwa wyniósł {b}")
