import math
a = int(input("podaj długość pierwszego boku "))
b = int(input("podaj długość drugiego boku "))
c = int(input("podaj długość trzeciego boku "))
halfCircumference = (a+b+c)/2
Field = round(math.sqrt(halfCircumference*((halfCircumference-a)*(halfCircumference-b)*(halfCircumference-a))), 2)
def pole_trojkata(a, b, c):
    if a>0 and b>0 and c>0:
        if a+b > c and a+c>b and b+c>a:
            return Field
        else:
            print("to nie jest trójkąt")
    else:
        print("tut mir leid taki trójkąt nie może istnieć")
print(pole_trojkata(a, b, c))