import random
print(random.randint(1,10))

#b
rocznik = [1994, 1997, 1999, 2002, 2003, 2004]
print("szczęśliwy rocznik to ", (random.choice(rocznik)))

#c
print("Szczęśliwe liczby to ", (random.sample(range(1, 50), 6)))