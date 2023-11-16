x = int(input("wprowadź wiek klienta: "))
if x < 4:
    print("wstęp za free")
elif x >= 4 and x < 18:
    print("koszt biletu 10zł")
else:
    print("koszt biletu 20zł")
