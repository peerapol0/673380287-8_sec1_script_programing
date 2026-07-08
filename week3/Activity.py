#Activity 3.1
# Buggy Snippet A: Infinite Loop
print("Activity 3.1: Debugging Infinite Loops & Loop Logic Errors")
print("Buggy Snippet A: Infinite Loop")
counter = 0
while counter < 5:
     print(counter)
     # Missing counter increment!
     counter += 1 #เพิ่ม counter += 1 เพื่อให้ loop ไม่เป็น infinite loop
print("\n")

# Buggy Snippet B: Incorrect Range
print("Buggy Snippet B: Incorrect Range")
for i in range(1, 6): # Goal: print 1, 2, 3, 4, 5 #แก้ไข range ให้ถูกต้อง 5 -> 6
    print(i)
print("\n")

# Buggy Snippet C: Misplaced Break
print("Buggy Snippet C: Misplaced Break")
for char in "hello":
    # ย้ายมาไว้ข้างบนของ if statement เพื่อให้ break ทำงานเมื่อเจอ 'l'
    print(char) # This will print 'h', 'e', 'l' then break
    if char == 'l':
        print("Found 'l', stopping!")
        break
print("\n")

#Activity 3.2: Pattern Printing with Nested Loops
#Format: Individual creative coding challenge.
#Instructions: Ask students to write Python code using nested for loops to print simple ASCII art patterns.
#Examples:
#1.A square of asterisks:
#*****
#*****
#*****
#*****
#*****
print("Activity 3.2: Pattern Printing with Nested Loops")
print("1. A square of asterisks:")
for i in range(5):
    for j in range(5):
        print("*", end="")
    print(" ")  
print("\n")

#A right-angled triangle of asterisks:
#*
#**
#***
#****
#*****
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print(" ")
print("\n")

#Challenge: An inverted right-angled triangle or a pyramid.
print("Challenge: An inverted right-angled triangle of asterisks:")
for i in range(6, 1, -1):
    for j in range(i):
        print("*", end="")
    print(" ")
  