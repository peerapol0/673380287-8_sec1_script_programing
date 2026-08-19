def add(a, b):
    """คืนค่าผลบวกของ a และ b"""
    return a + b

def subtract(a, b):
    """คืนค่าผลลบ a - b"""
    return a - b

def multiply(a, b):
    """คืนค่าผลคูณของ a และ b"""
    return a * b

def divide(a, b):
    """คืนค่าผลหาร a / b จัดการกรณีหารด้วย 0"""
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(base, exponent=2):
    """คืนค่า base ยกกำลัง exponent (ค่าเริ่มต้น = 2 คือยกกำลังสอง)"""
    return base ** exponent


while True:
    print("\n1) Add  2) Subtract  3) Multiply  4) Divide  5) Power  6) Exit")
    choice = input("เลือกเมนู: ")

    if choice == "6":
        break
    elif choice == "5":
        x = float(input("ใส่ base: "))
        exp_input = input("ใส่ exponent (Enter = 2): ")
        if exp_input == "":
            print("ผลลัพธ์:", power(x))
        else:
            print("ผลลัพธ์:", power(x, float(exp_input)))
    elif choice in ("1", "2", "3", "4"):
        x = float(input("ใส่เลขตัวที่ 1: "))
        y = float(input("ใส่เลขตัวที่ 2: "))
        if choice == "1":
            print("ผลลัพธ์:", add(x, y))
        elif choice == "2":
            print("ผลลัพธ์:", subtract(x, y))
        elif choice == "3":
            print("ผลลัพธ์:", multiply(x, y))
        elif choice == "4":
            print("ผลลัพธ์:", divide(x, y))
    else:
        print("โปรดใส่ตัวเลขที่ถูกต้อง")