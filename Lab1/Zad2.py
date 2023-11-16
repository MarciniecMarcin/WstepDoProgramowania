a = input("Podaj literę: ")

if a.isalpha():
    if a.isupper():
        print("wpisana litera jest duża.")
    elif a.islower():
        print("wpisana litera jest mała.")
else:
    print("To nie jest litera.")