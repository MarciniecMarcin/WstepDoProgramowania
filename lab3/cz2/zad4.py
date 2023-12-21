import random

a = random.randint(3, 7)
ZbiorX = []
for i in range(a):
    ZbiorX.append(random.randint(0, 10))
print("wartości zbioru X: ",ZbiorX)
b = random.randint(3, 7)
ZbiorY = []
for i in range(b):
    ZbiorY.append(random.randint(0, 10))
print("wartości zbioru Y: ",ZbiorY)
#a
for i in ZbiorX:
    if i == 5:
        print("zbiór X zawiera cyfrę 5")
        break
#b i #e
def zawieranie_zbiorowXwY():
    for i in ZbiorX and ZbiorY:
        c = []
        c += [i for i in ZbiorX if i in ZbiorY]
        if c != []:
            print("X jest podzbiorem Y")
            print("Y jest nadzbiorem zbioru X")
        break
print(zawieranie_zbiorowXwY())
#c i #d
def zawieranie_zbiorowYwX():
    for i in ZbiorX and ZbiorY:
        d = []
        d += [i for i in ZbiorY if i in ZbiorX]
        if d != []:
            print("Y jest podzbiorem X")
            print("X jest nadzbiorem zbioru Y")
        break
print(zawieranie_zbiorowYwX())

#f
A = set(ZbiorX) #rzutowanie zmiennej zbiorów na typ Set
B = set(ZbiorY)
print(A.union(B))

#g
print(A.difference(B))
#h
print(B.difference(A))
#i
print(A.intersection(B))
#j
print(A.symmetric_difference(B))
#k
print(max(A))
#l
print(ZbiorX)
x = ZbiorX.pop(0)
print(x)
print(ZbiorX)
ZbiorY.append(x)
print(ZbiorY)
#m
ZbiorY.extend(ZbiorX)
print(ZbiorY)
#n
ZbiorY.clear()
ZbiorX.clear()

print(ZbiorX)
print(ZbiorY)

