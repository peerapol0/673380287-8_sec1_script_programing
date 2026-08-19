def is_even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

def is_positive_negative_zero(num):

    if num == 0:
        return "Zero"
    elif num > 0:
        return "Positive"
    else:
        return "negative"

num = int(input("Enter your number: "))
check1 = is_even_odd(num)
check2 = is_positive_negative_zero(num)
if num == 0:
    print(f"The number is {check2}.")
else:
    print(f"The number is {check2} and {check1}.")