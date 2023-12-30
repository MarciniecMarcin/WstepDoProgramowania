n = int(input("podaj który wyraz ciągu fibonacciego chcesz znaleźć "))

def Fibonacci_sequence(n):
    if n < 1:
        return 0
    if n < 2:
        return 1
    return Fibonacci_sequence(n - 1) + Fibonacci_sequence(n - 2)

print(Fibonacci_sequence(n))