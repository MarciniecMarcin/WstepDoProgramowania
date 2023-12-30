waga = int(input("podaj swoją wagę "))
wzrost = int(input("podaj swój wzrost "))

def BMI(waga, wzrost):
    heightInQubikMeters = wzrost*wzrost/10000
    return round(waga/heightInQubikMeters, 2)

print("BMI jest równe ", BMI(waga, wzrost))

if BMI(waga, wzrost) <= 18.5:
    print("masz niedowagę")
elif 18.5 < BMI(waga, wzrost)  <= 24.9:
    print("waga jest w normie")
elif 25 < BMI(waga, wzrost) <= 29.3:
    print("masz nadwagę")
else:
    print("jesteś otyły")