#โปรแกรมคำนวณเกรดจากคะแนน (A/B/C/D/F)

score = float(input("ใส่คะแนนของคุณ: "))

# ใช้ Loop ตรวจสอบช่วงคะแนน
for threshold, g in [(80, "A"), (70, "B"), (60, "C"), (50, "D")]:
    if score >= threshold:
        grade = g
        break
else:
    grade = "F"

print(f"เกรดของคุณคือ: {grade}")

#โดยนายภานุวัฒน์ เต้จัน ม.4/4 เลขที่ 11
