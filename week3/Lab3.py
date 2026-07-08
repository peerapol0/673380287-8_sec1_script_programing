#Lab3.1 part 1

num = int(input("Enter a number for its multiplication table (e.g., 7): "))
for i in range(1,13):
    print(f"{num} * {i} = {num*i}")

print("\n")

#Lab3.1 part 2
print("12x12 Multiplication Table:")
for i in range(1, 13):
    for j in range(1, 13):
        print(f"{i*j:3}", end=' ')
    print(" ")  
    
print("\n")

#Lab3.2 part 1
num2 = int(input("Countdown Timer: "))
while num2 != 0:
    print(num2)
    num2 -= 1
print("Blast off!\n")

#Lab3.2 part 2
secret_number = 99
limit = 5
while True:
    user = int(input("Guess the number:"))
    if user < secret_number:
        print(f"{user} is Too low! Try again.")
    elif user > secret_number:
        print(f"{user} is Too high! Try again.")
    else:
        print("Congratulations! You guessed it!")
        break
    limit -= 1
    if limit == 0:
        print("Sorry, you've run out of attempts!")
        break
    