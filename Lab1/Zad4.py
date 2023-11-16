from cmath import sqrt

print("program do rozwiązywania równania kwadratowego")
a = int(input("podaj współczynnik a: "))
b = int(input("podaj współczynnik b: "))
c = int(input("podaj współczynnik c: "))
#liczymy deltę
delta = b**2 - 4*a*c
if delta > 0:
    x1 = (-b + (sqrt(delta))) / (2*a)
    x2 = (-b - (sqrt(delta))) / (2*a)
    print("równanie ma dwa rozwiązania")
    print("x1= ", x1)
    print("x2= ", x2)
elif delta == 0:
    x = -b / (2*a)
    print("równanie ma jedno rozwiązanie")
    print("x= ", x)
else:
    print("równanie nie ma rozwiązanie w zbiorze liczb rzeczywistych")