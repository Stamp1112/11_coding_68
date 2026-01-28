import tkinter as tk
from tkinter import messagebox

# --- ส่วนของการคำนวณ (Logic) ---
def calculate_bedtime():
    FALL_ASLEEP_TIME = 15
    SLEEP_CYCLE_LENGTH = 90
    
    # ดึงค่าจากช่อง Input
    wake_time_str = entry_wake.get()
    cycles_str = entry_cycles.get()

    try:
        # ตรวจสอบว่ามีการกรอกข้อมูลหรือไม่
        if not wake_time_str or not cycles_str:
            raise ValueError("กรุณากรอกข้อมูลให้ครบ")

        # แยกชั่วโมงและนาที (รองรับทั้ง : และ .)
        if ":" in wake_time_str:
            hour, minute = wake_time_str.split(":")
        elif "." in wake_time_str:
            hour, minute = wake_time_str.split(".")
        else:
            raise ValueError("รูปแบบเวลาไม่ถูกต้อง (ใช้ HH:MM)")

        sleep_cycles = int(cycles_str)
        
        # คำนวณเป็นนาที
        wake_up_minutes = int(hour) * 60 + int(minute)
        
        # คำนวณเวลาย้อนกลับ
        bed_time_minutes = wake_up_minutes - (sleep_cycles * SLEEP_CYCLE_LENGTH) - FALL_ASLEEP_TIME
        
        # ถ้าค่าติดลบ ให้บวก 24 ชม. (ข้ามวัน)
        if bed_time_minutes < 0:
            bed_time_minutes += 24 * 60
            
        bed_hour = bed_time_minutes // 60
        bed_minute = bed_time_minutes % 60
        
        # แสดงผลลัพธ์
        result_text.set(f"เวลาที่ควรเข้านอน\n{bed_hour:02d}:{bed_minute:02d}")
        
    except ValueError as e:
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกเวลาในรูปแบบ HH:MM (เช่น 06:30)\nและจำนวนรอบเป็นตัวเลข")

# --- ส่วนของการสร้างหน้าต่าง (GUI) ---
root = tk.Tk()
root.title("คำนวณเวลานอน")
root.geometry("360x650") # กำหนดขนาดหน้าต่างให้คล้ายมือถือ
root.configure(bg="white")

# ใช้ Font ภาษาไทยที่อ่านง่าย
font_title = ("Angsana New", 20, "bold") # หรือ Tahoma ถ้าไม่มี Angsana
font_label = ("Tahoma", 12)
font_input = ("Tahoma", 12)
font_result = ("Tahoma", 16, "bold")
font_advisory = ("Tahoma", 16)

# 1. หัวข้อ
lbl_title = tk.Label(root, text="คำนวณเวลานอน", font=("Tahoma", 16, "bold"), bg="white")
lbl_title.pack(pady=20)

# Frame สำหรับจัดระเบียบ Input
input_frame = tk.Frame(root, bg="white")
input_frame.pack(pady=10)

# 2. แถว Time Input
row1 = tk.Frame(input_frame, bg="white")
row1.pack(pady=5, fill="x")

# ป้าย "เวลาตื่น" (ทำสีส้มเลียนแบบปุ่ม)
lbl_wake = tk.Label(row1, text="เวลาตื่น", bg="#FFA500", fg="black", font=font_label, width=12)
lbl_wake.pack(side="left", padx=5)

# ช่องกรอกเวลา
entry_wake = tk.Entry(row1, font=font_input, width=10, justify="center", bd=2, relief="groove")
entry_wake.insert(0, "6:30") # ค่าเริ่มต้น
entry_wake.pack(side="left", padx=5)

# 3. แถว Cycle Input
row2 = tk.Frame(input_frame, bg="white")
row2.pack(pady=5, fill="x")

# ป้าย "จำนวนรอบ"
lbl_cycles = tk.Label(row2, text="จำนวนรอบ", bg="#FFA500", fg="black", font=font_label, width=12)
lbl_cycles.pack(side="left", padx=5)

# ช่องเลือกจำนวนรอบ (ใช้ Spinbox เพื่อความสะดวก)
entry_cycles = tk.Spinbox(row2, from_=1, to=10, font=font_input, width=8, justify="center", bd=2, relief="groove")
entry_cycles.delete(0, "end")
entry_cycles.insert(0, 1) # ค่าเริ่มต้น
entry_cycles.pack(side="left", padx=5)

# 4. ปุ่มคำนวณ
btn_calc = tk.Button(root, text="คำนวณ", font=font_label, bg="gray", fg="white", width=15, command=calculate_bedtime)
btn_calc.pack(pady=20)

# 5. พื้นที่แสดงผล (สีส้ม)
result_frame = tk.Frame(root, bg="#FFA500", bd=0)
result_frame.pack(pady=10, padx=40, ipadx=10, ipady=10, fill="x")

# ทำมุมโค้งไม่ได้ใน Tkinter ปกติ จึงใช้ Frame สี่เหลี่ยมแทน แต่ใส่สีส้มตามแบบ
result_text = tk.StringVar()
result_text.set("แสดงเวลาที่\nควรนอน")

lbl_result = tk.Label(result_frame, textvariable=result_text, bg="#FFA500", fg="#333333", font=font_result)
lbl_result.pack(expand=True)

# 6. ข้อความแนะนำ (สีแดง)
advisory_text = "คำแนะนำ:  ควรเลือกจำนวนรอบ\nในการนอน 4 - 6 รอบ\nเพื่อให้ได้การนอนที่\nมีประสิทธิภาพ และเพียงพอ"
lbl_advisory = tk.Label(root, text=advisory_text, font=font_advisory, fg="red", bg="white", wraplength=300, justify="left")
lbl_advisory.pack(side="bottom", pady=80, padx=20)

# เริ่มต้นโปรแกรม
root.mainloop()