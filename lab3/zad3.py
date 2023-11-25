#a
tekst="python jest super"
print(tekst[0])
print(tekst[-1])

#b
dl=len(tekst)
for i in range(0,dl, 2):
    print(tekst[i])
#c
for i in range(1,dl, 3):
    print(tekst[i])
#d
for i in range(10,dl):
    print(tekst[i])
"""lub"""
print(tekst[10:])
#e
print(tekst[::-1])