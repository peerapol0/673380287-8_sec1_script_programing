import my_utils
import math
import random

my_utils.greet("Alice")

for n in [7, 10]:
    print(f"{n} is prime: {my_utils.is_prime(n)}")

print("Square root of 16:", math.sqrt(16))
print("Random number 1-100:", random.randint(1, 100))