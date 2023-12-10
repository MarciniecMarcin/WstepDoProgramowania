waga = int(input("podaj swój wzrost "))
wzrost = int(input("podaj swoją wagę "))

def BMI(waga, wzrost):
    return waga/(wzrost*wzrost/100)

print("BMI jest równe ",
