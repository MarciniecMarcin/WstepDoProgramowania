#ciag arytmetyczny
#an=a1+(n-1)*r
n=int(input("do którego wyrazu ciągu liczymy? "))
a=int(input("podaj pierwszy wyraz ciągu "))
r=int(input("podaj różnice ciągu "))
for i in range(1, n+1):
    an=a+(i-1)*r
    print(an)

#opcja2
if(r>0):
    koniec = a + (n - 1) * r + 1
else:
    koniec = a + (n - 1) * r - 1

for i in range(a, koniec+1, r):
    print(i)