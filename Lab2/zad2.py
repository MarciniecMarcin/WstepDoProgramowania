#y=2x2-5x-8
"""moje próby rozwiązania zadania
    nie wiem jak doprowadzić funkcję do pełnego działania
        """
"""
xs = (x * 0.5 for x in range(-8, 9))
dziedzina = list((xs))"""


"""for i in dziedzina:
    print(i)
y = (i**2)*2 - 5*i - 8

while i >= -4 and i <=4:
    c = 0
    for i in dziedzina:
        c == (i**2)*2 - 5*i - 8
        i += 1
        print(i, y)

wyniki = list(filter(lambda i: i == (i**2)*2 - 5*i - 8, dziedzina))
print(wyniki)"""
"""
def calculate_argument(*args):
    value = [] #lista gdzie przechowujemy wartośc funkcji
    for arg in args:
        print(arg)
        value = (arg**2)*2 - arg*5 - 8
    return value
calculate_argument(dziedzina)"""

xValue = [-4, -3.5, -3, -2.5, -2, -1.5, -1, 0, 1, 1.5, 2, 2.5, 3, 3.5, 4]
print(xValue)
def calculate_value(*args):
    value = []
    for x in xValue:
        value = (x**2)*2 - 5*x -8
        x += 1
    return value



print(calculate_value(xValue))