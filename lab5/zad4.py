import datetime

ostZajęcia = datetime.date(2023,12,10)
dzisiaj = datetime.date.today()
kolokwium = datetime.date(2024,2, 11)
print("od ostatnich zajęć minęło", ostZajęcia - dzisiaj)

print("do kolokwium zostało", kolokwium - dzisiaj)


