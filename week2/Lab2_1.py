num = int(input("Enter your number:"))


if num%2==0:
    check1 = "even"
else:
     check1 = "odd"

if num == 0:
    check2 = "Zero"
elif num > 0:
    check2 = "Positive"
else:
    check2 ="negative"
if num == 0:
    print(f"The number is {check2}.")
else:
    print(f"The number is {check2} and {check1}.")  