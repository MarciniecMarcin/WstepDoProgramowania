#y=2x2-5x-8

xs = (x * 0.5 for x in range(-8, 9))
dziedzina = list(xs)


"""for i in dziedzina:
    print(i)
y = (i**2)*2 - 5*i - 8

while i >= -4 and i <=4:
    c = 0
    for i in dziedzina:
        c == (i**2)*2 - 5*i - 8
        i += 1
        print(i, y)"""

wyniki = list(filter(lambda i: i == (i**2)*2 - 5*i - 8, dziedzina))
print(wyniki)