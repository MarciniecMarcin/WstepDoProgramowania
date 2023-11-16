#zadanie4.1 Lab0
import random

i = random.randint(1, 100000)
j = int(input("podaj średnie spalanie[L/100km]: "))
k = 6.50 #koszt paliwa
a = i * j / 100
b = a * k
print("długość drogi wynosi", i)
print("koszt paliwa wyniósł: ", b)

