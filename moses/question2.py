#Question 2: Fibonacci Sequence
#Write a program to generate the Fibonacci sequence up to 100

def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]  # Initialize with first two Fibonacci numbers
    while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= n:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence

fibonacci_numbers = generate_fibonacci(100)
print("Fibonacci sequence up to 100:", fibonacci_numbers)
        