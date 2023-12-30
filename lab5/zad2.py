import math
a = math.sqrt(81)
print(a)
b = math.pow(8, 10)
print(b)
c = (math.sqrt(2))+ (math.sqrt(3))+ math.sqrt(6)
print(round(c, 3))
#D
while True:
    try:
        x = math.sqrt(-5)
        break
    except ValueError:
        print("w zbiorze liczb rzeczywistych nie można zpierwiastkować liczby ujemnej")
        break
#E
pierwiastek = 125**(1/3)
print(pierwiastek)