print("program do porządkowania 3 liczb od najmniejszej do największej")
x = int(input("wprowadź pierwszą liczbę: "))
y = int(input("wprowadź drugą liczbę: "))
z = int(input("wprowadź trzecia liczbę: "))

if x > y and x > z and y > z:
    print(z, y, x)
elif x < y and x > z and y > z:
    print(z, x, y)
elif