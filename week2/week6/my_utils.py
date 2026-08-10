def greet(name):
    print(f"Hello, {name}!")

def is_prime(number):
    """คืนค่า True ถ้า number เป็นจำนวนเฉพาะ, False ถ้าไม่ใช่"""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True