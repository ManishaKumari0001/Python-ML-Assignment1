# generate the first n numbers in the Fibonacci sequence
def fibonacci_sequence(n):
    fibonacci_numbers = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_numbers.append(a)
        a, b = b, a + b
    return fibonacci_numbers

n = int(input("Enter the number of Fibonacci numbers to generate: "))

fibonacci_numbers = fibonacci_sequence(n)

print(f"The first {n} numbers in the Fibonacci sequence are:")
print(fibonacci_numbers)
