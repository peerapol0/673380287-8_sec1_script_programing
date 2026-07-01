# Block A: Evaluation Check
temp = 25
is_raining = True

if temp > 20 and not is_raining:
    print("Perfect day for a picnic!")
elif temp <= 20 or is_raining:
    print("Stay indoors or bring an umbrella.") # Expected output matches here
else:
    print("Unsure about the weather.")
#คำตอบ Block A
#โปรแกรมนี้เป็นการตรวจสอบสภาพอากาศจากตัวเลขอุณหภูมิและตัวแปรฝนตก
#โดยในส่วนแรกจะตรวจสอบอุณหภูมิและสภาพอากาศว่าควรออกไปปิกนิกหรือไม่ 
#ถ้าอุณหภูมิมากกว่า 20 องศาเซลเซียสและไม่ฝนตกคือ is_raining = False จะแสดงข้อความว่า "Perfect day for a picnic!"
#ถ้าอุณหภูมิต่ำกว่าหรือเท่ากับ 20 องศาเซลเซียสหรือฝนตก is_raining = True จะแสดงข้อความว่า "Stay indoors or bring an umbrella."




# Block B: Vectorized Filter
phrase = "Python 2026 Engine"
consonants = {c.lower() for c in phrase if c.isalpha() and c.lower() not in 'aeiou'}
print(f"Unique consonants: {consonants}")


#คำตอบ Block B
#โปรแกรมนี้จะเป็นการตรวจข้อความ"Python 2026 Engine"
#โดยจะทำการตรวจสอบตัวอักษรในข้อความนั้นว่ามีตัวอักษรใดบ้างที่เป็นพยัญชนะ
#และตัวอักษรนั้นไม่ใช่สระ (a, e, i, o, u)
