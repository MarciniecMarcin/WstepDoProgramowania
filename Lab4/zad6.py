def pole_trojkata(a, b, c):
    if a>0 and b>0 and c>0:
        if a+b > c and a+c>b and b+c>a:
            return (a+b+c)/2
        else:
            print("to nie jest trójkąt")
    else:
        print("tut mir leid taki trójkąt nie może istnieć")
print(pole_trojkata(4, 5, 6))