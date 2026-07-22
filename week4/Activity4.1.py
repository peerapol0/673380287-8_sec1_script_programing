'''
Activity 4.1: List vs. Tuple: Scenario Matching
○ Format: Small group discussion, followed by a class debrief.
○ Instructions: Present students with a list of real-world data scenarios. For each
scenario, they must decide whether a list or a tuple would be the more appropriate
Python data structure and explain their reasoning (focus on mutability/immutability and
ordered nature).
○ Scenarios:
1. A collection of daily temperatures recorded over a week.
2. The RGB color values for a specific shade (e.g., (255, 0, 0) for red).
3. Items in a shopping cart that can be added or removed.
4. The days of the week in order.
5. Student scores on a series of assignments, which might be updated.
6. GPS coordinates for a fixed landmark.
○ Purpose: Reinforce understanding of when to use which data structure based on their
characteristics.
'''
#ตอบคำถาม
#1. A collection of daily temperatures recorded over a week.
#ตอบ: List เพราะอุณหภูมิสามารถเปลี่ยนแปลงได้ตลอดเวลา และอาจต้องการเพิ่มหรือลบข้อมูลอุณหภูมิในอนาคต
#2. The RGB color values for a specific shade (e.g., (255, 0, 0) for red).
#ตอบ: Tuple เพราะค่าของสี RGB เป็นค่าคงที่และไม่ควรเปลี่ยนแปลงถ้าแก้ไขค่าจะทำให้สีอาจจะเปลี่ยนไป
#3. Items in a shopping cart that can be added or removed.
#ตอบ: List เพราะรายการในตะกร้าสามารถเพิ่มหรือลบได้ตามความต้องการของผู้ใช้
#4. The days of the week in order.
#ตอบ: Tuple เพราะวันในสัปดาห์เป็นค่าคงที่และไม่ควรเปลี่ยนแปลง
#5. Student scores on a series of assignments, which might be updated.
#ตอบ: List เพราะคะแนนของนักเรียนสามารถเปลี่ยนแปลงได้และต้องการเก็บข้อมูลที่สามารถแก้ไขได้
#6. GPS coordinates for a fixed landmark.
#ตอบ: Tuple เพราะพิกัด GPS ของสถานที่คงที่ไม่ควรเปลี่ยนแปลง ถ้าเปลี่ยนแปลงจะทำให้ข้อมูลไม่ถูกต้อง
