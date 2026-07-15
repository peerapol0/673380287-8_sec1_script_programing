# lab4_1.py - Student Management System (List Operations)
# หมายเหตุ: โค้ดนี้ตัดส่วน "Challenge" (ระบบเมนูแบบ while loop) ออก
#          เพื่อให้นักศึกษานำ concept ด้านล่างไปต่อยอดคิดเองเป็นแบบฝึกหัด

print("--- Lab 4.1: Student Management System ---")

# 1) เริ่มต้นด้วย list ว่างสำหรับเก็บชื่อนักศึกษา
student_names = []



user_choice = 0
while user_choice != 6:
    Choice = ["Add Student", "Find Student", "Remove Student", "Sort Students","Count Students", "Exit"]
    print("\nMenu Options:")
    for i in range(len(Choice)):
        print(f"{i + 1}. {Choice[i]}")
    user_choice = int(input("Select an option (1-5): "))
    if user_choice == 1:
        # 2) เพิ่มนักศึกษา: รับชื่อจากผู้ใช้ 3 คน แล้ว append() เข้า list
        print("\n[1] Add Students")
        for i in range(3): #กำหนดตัวแปรใน loop 👈ต้องทำ
            name = input(f"Enter student name #{i + 1}: ") #กำหนดตัวแปร 👈ต้องทำ
            student_names.append(name)

        print(f"Current list: {student_names}")

    elif user_choice == 2:
        # 3) ค้นหานักศึกษา: ใช้ 'in' เพื่อเช็คว่ามีชื่อนี้อยู่ใน list หรือไม่
        #    ถ้าพบ ให้แสดง index ด้วย index()
        print("\n[2] Find a Student")
        search_name = input("Enter a name to search for: ")

        if search_name in student_names: #เขียนเงื่อนไข ถ้าหากมีชื่อในลิส: 👈ต้องทำ
            position = student_names.index(search_name)
            print(f"Found '{search_name}' at index {position}")
        else:
            print(f"'{search_name}' not found in the list")

    elif user_choice == 3:
        # 4) ลบนักศึกษา: เช็คก่อนว่ามีอยู่จริงหรือไม่ (กัน error) แล้วค่อย remove()
        print("\n[3] Remove a Student")
        remove_name = input("Enter a name to remove: ")

        if remove_name in student_names:
            student_names.remove(remove_name) #เติมฟังก์ชัน remove(remove_name) 👈ต้องทำ
            print(f"'{remove_name}' has been removed")
        else:
            print(f"'{remove_name}' not found, nothing removed")

        print(f"Updated list: {student_names}")

    elif user_choice == 4:
        # 5) เรียงลำดับรายชื่อตามตัวอักษรด้วย sort()
        print("\n[4] Sort Students")
        student_names.sort() #เติมฟังก์ชันsort()
        print(f"Sorted list: {student_names}")
    elif user_choice == 5:
        # 6) นับจำนวนนักศึกษาทั้งหมดด้วย len()
        print("\n[5] Count Students")
        print(f"Total students: {len(student_names)}") #ใช้คำสั่งlen() หาจำนวนนักศึกษาในลิส student_names👈ต้องทำ
    elif user_choice == 6:
        break

    else:
        print("Invalid option. Please select a number between 1 and 5.")

 
# --------------------------------------------------------------------
# ให้นักศึกษาลองต่อยอดเอง (Challenge):
# ลองเขียนระบบเมนูด้วย while loop (จาก Week 3) ที่ให้ผู้ใช้เลือกได้ว่า
# จะเพิ่ม / ลบ / ค้นหา / เรียงลำดับ / หรือออกจากโปรแกรม
# โดยนำโค้ดแต่ละส่วนด้านบนไปจัดเป็นฟังก์ชันหรือเงื่อนไขในเมนู
# --------------------------------------------------------------------