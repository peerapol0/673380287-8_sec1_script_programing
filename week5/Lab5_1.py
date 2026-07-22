# ============================================================
# 🔧 เติมโค้ด: Lab 5.1 - Simple Contact Book Manager (Dictionary Focus)
# ------------------------------------------------------------
# โจทย์: สร้างระบบจัดการสมุดโทรศัพท์แบบ Text-based โดยใช้ Dictionary
#
# คำใบ้ (ทบทวนจากบทเรียน):
#   - สร้าง Dictionary ว่าง: contacts = {}
#   - เพิ่ม/แก้ไขข้อมูล: contacts[key] = value
#   - อ่านข้อมูลอย่างปลอดภัย: contacts.get(key)
#   - วนลูปอ่านทั้ง key และ value: for key, value in contacts.items():
#   - ลบข้อมูล: contacts.pop(key, default) หรือ del
# ============================================================

# --- ข้อที่ 1: สร้าง Dictionary ว่างสำหรับเก็บข้อมูลผู้ติดต่อ ---
# todo (1): สร้าง dictionary ว่างชื่อ contacts
contacts = {}

#challenge: สร้างฟังก์ชัน normalize_name เพื่อปรับชื่อผู้ติดต่อให้เป็นรูปแบบมาตรฐาน 
def normalize_name(name):
    return name.strip().title()


while True:
    # แสดงเมนูตัวเลือก
    print("\n=== Contact Book Manager ===")
    print("1. Add/Update Contact")
    print("2. View Contact Details")
    print("3. List All Contacts")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    # --- เมนูที่ 1: เพิ่มหรืออัปเดตข้อมูลผู้ติดต่อ ---
    if choice == '1':
        name = input("Enter contact name: ")
        if name in contacts:
            print(f"Contact '{name}' already exists. Updating information.")
        else:
            print(f"Adding new contact '{name}'.")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        normalized_name = normalize_name(name)

        # todo (2): เก็บข้อมูลลงใน contacts โดยใช้ name เป็น key
        # และ value เป็น dictionary ที่เก็บข้อมูล "phone" และ "email"
        contacts[normalized_name] = {
            "phone": phone,
            "email": email
        }
        print(f"Contact '{normalized_name}' saved successfully!")

    # --- เมนูที่ 2: ดูรายละเอียดผู้ติดต่อ ---
    elif choice == '2':
        name = input("Enter contact name to view: ")
        normalized_name = normalize_name(name)

        # todo (3): ใช้เมธอด .get() เพื่อดึงข้อมูลของผู้ติดต่อตามชื่อ name
        info = contacts.get(normalized_name)

        if info:
            print(f"\nName: {normalized_name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
        else:
            print("Contact not found.")

    # --- เมนูที่ 3: แสดงรายการผู้ติดต่อทั้งหมด ---
    elif choice == '3':
        if not contacts:
            print("No contacts available.")
        else:
            print("\n--- All Contacts ---")
            # todo (4): ใช้เมธอด .items() วนลูปเพื่อดึงชื่อ (key) และรายละเอียด (value)
            for name, details in contacts.items():
                print(f"Name: {name} | Phone: {details['phone']} | Email: {details['email']}")

    # --- เมนูที่ 4: ลบข้อมูลผู้ติดต่อ ---
    elif choice == '4':
        name = input("Enter contact name to delete: ")
        normalized_name = normalize_name(name)

        # todo (5): ใช้เมธอด .pop() ลบ key ตามชื่อ name
        # และใส่ค่า default เป็น None หากไม่พบชื่อเพื่อป้องกันการเกิด Error
        removed_contact = contacts.pop(normalized_name, None)

        if removed_contact:
            print(f"Contact '{normalized_name}' deleted successfully!")
        else:
            print("Contact not found.")

    # --- เมนูที่ 5: ออกจากโปรแกรม ---
    elif choice == '5':
        print("Exiting Contact Book Manager. Goodbye!")
        # todo (6): เขียนคำสั่งเพื่อหยุดการทำงานของ while loop
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 5.")
     