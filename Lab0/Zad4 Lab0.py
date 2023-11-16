#zadanie4 Lab0
i = int(input("podaj ile kilometrów przejechałeś: "))
j = int(input("podaj średnie spalanie[L/100km]: "))
k = 6.50 #koszt paliwa
a = i * j / 100
b = a * k
print("koszt paliwa wyniósł: ", b)
