# import tkinter as tk
# from tkinter import messagebox

# # สร้างหน้าต่างหลัก (Main Window)
# root = tk.Tk()
# root.title("ລະບົບເມນູສັ່ງອາຫານ / Menu System")
# root.geometry("450x550")
# root.configure(bg="#f4f4f9")

# # รายการเมนูและราคา (Lao Kip)
# MENU = {
#     "ກາເຟເຢັນ (Iced Coffee)": 25000,
#     "ຊານົມເຢັນ (Milk Tea)": 20000,
#     "ນ້ຳປັ້ນ (Smoothie)": 30000,
#     "ເຂົ້າຜັດ (Fried Rice)": 35000,
#     "ຕຳຫົ່ມຫຸ່ງ (Papaya Salad)": 25000,
# }

# # ตัวแปรเก็บจำนวนสินค้าแต่ละรายการ
# quantities = {}

# # หัวข้อ
# title_label = tk.Label(
#     root,
#     text="🍽️ ເມນູອາຫານ ແລະ ເຄື່ອງດື່ມ",
#     font=("Phetsarath OT", 16, "bold"),
#     bg="#f4f4f9",
#     fg="#333",
# )
# title_label.pack(pady=15)

# # กรอบแสดงรายการเมนู
# menu_frame = tk.Frame(root, bg="#ffffff", bd=1, relief=tk.SOLID)
# menu_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

# # สร้างรายการเมนู + ช่องใส่จำนวน
# for item, price in MENU.items():
#     row_frame = tk.Frame(menu_frame, bg="#ffffff")
#     row_frame.pack(fill=tk.X, padx=15, pady=8)

#     label_text = f"{item} ({price:,} ກີບ)"
#     item_label = tk.Label(
#         row_frame,
#         text=label_text,
#         font=("Phetsarath OT", 11),
#         bg="#ffffff",
#         anchor="w",
#     )
#     item_label.pack(side=tk.LEFT, fill=tk.X, expand=True)

#     qty_var = tk.IntVar(value=0)
#     quantities[item] = qty_var

#     spinbox = tk.Spinbox(
#         row_frame,
#         from_=0,
#         to=20,
#         textvariable=qty_var,
#         width=5,
#         font=("Phetsarath OT", 11),
#         justify="center",
#     )
#     spinbox.pack(side=tk.RIGHT)


# # ฟังก์ชันคำนวณเงินและแสดงบิล
# def calculate_total():
#     total = 0
#     receipt_text = "🧾 **ໃບເສັດລາຍການສັ່ງຊື້**\n-----------------------------------\n"
#     has_order = False

#     for item, qty_var in quantities.items():
#         qty = qty_var.get()
#         if qty > 0:
#             item_total = qty * MENU[item]
#             total += item_total
#             receipt_text += f"• {item} x {qty} = {item_total:,} ກີບ\n"
#             has_order = True

#     if not has_order:
#         messagebox.showwarning(
#             "ເຕືອນ", "ກະລຸນາເລືອກຢ່າງນ້ອຍ 1 ລາຍການ!"
#         )
#         return

#     receipt_text += "-----------------------------------\n"
#     receipt_text += f"💰 **ລວມທັງໝົດ: {total:,} ກີບ**"

#     messagebox.showinfo("ສະຫຼຸບຍອດເງິນ", receipt_text)


# # ฟังก์ชันรีเซ็ตข้อมูล
# def reset_order():
#     for qty_var in quantities.values():
#         qty_var.set(0)


# # กรอบปุ่มกดด้านล่าง
# btn_frame = tk.Frame(root, bg="#f4f4f9")
# btn_frame.pack(pady=15)

# btn_calc = tk.Button(
#     btn_frame,
#     text="ຄິດໄລ່ເງິນ",
#     command=calculate_total,
#     font=("Phetsarath OT", 11, "bold"),
#     bg="#28a745",
#     fg="white",
#     padx=15,
#     pady=5,
#     relief=tk.FLAT,
# )
# btn_calc.pack(side=tk.LEFT, padx=10)

# btn_reset = tk.Button(
#     btn_frame,
#     text="ລ້າງຂໍ້ມູນ",
#     command=reset_order,
#     font=("Phetsarath OT", 11),
#     bg="#dc3545",
#     fg="white",
#     padx=15,
#     pady=5,
#     relief=tk.FLAT,
# )
# btn_reset.pack(side=tk.RIGHT, padx=10)

# # รันแอปพลิเคชัน
# root.mainloop()


import tkinter as tk
from tkinter import messagebox

# ສ້າງ Window ຫຼັກ
root = tk.Tk()
root.title("Coffee & Food Menu")
root.geometry("1100x560")
root.minsize(950, 500)
root.configure(bg="#f5f1eb")

# ຂໍ້ມູນລາຍການອາຫານ/ເຄື່ອງດື່ມ
items = [
    {"name": "Coffee", "price": "25,000kip"},
    {"name": "Soft drink", "price": "35,000kip"},
    {"name": "Burger", "price": "40,000kip"},
    {"name": "Cupcake", "price": "25,000kip"},
    {"name": "Doughnut", "price": "30,000kip"},
]

# ຟັງຊັນເມື່ອຖືກ ກົດປຸ່ມ
def select_item(item_name, price):
    messagebox.showinfo("Order", f"ທ່ານໄດ້ເລືອກ: {item_name}\nລາຄາ: {price}")

# ສ່ວນຫົວຂອງໜ້າຈໍ
header = tk.Frame(root, bg="#f5f1eb")
header.pack(fill="x", pady=(25, 12))

tk.Label(
    header,
    text="ຮ້ານອາຫານ ແລະ ເຄື່ອງດື່ມ",
    font=("Arial", 24, "bold"),
    bg="#f5f1eb",
    fg="#3b2418",
).pack()
tk.Label(
    header,
    text="ເລືອກເມນູທີ່ທ່ານມັກ",
    font=("Arial", 12),
    bg="#f5f1eb",
    fg="#8a6a55",
).pack(pady=(4, 0))

# Container ສໍາລັບຈັດວາງ card ເມນູ
main_frame = tk.Frame(root, bg="#f5f1eb")
main_frame.pack(expand=True, fill="both", padx=28, pady=(8, 28))

# ໂຫຼດຮູບ k.png ແລະຫຍໍ້ໃຫ້ເໝາະກັບວົງມົນ
menu_image = tk.PhotoImage(file="k.png").subsample(8, 8)

# ສ້າງ Card / ປຸ່ມ ແຕ່ລະລາຍການ
for i, item in enumerate(items):
    # Frame ຍ່ອຍຂອງແຕ່ລະ Item
    item_frame = tk.Frame(
        main_frame,
        bg="white",
        bd=1,
        relief="solid",
        padx=14,
        pady=14,
    )
    item_frame.grid(row=0, column=i, padx=9, pady=10, sticky="nsew")
    main_frame.grid_columnconfigure(i, weight=1)

    # ສະແດງຮູບ k.png
    canvas = tk.Canvas(item_frame, width=125, height=115, bg="white", highlightthickness=0)
    canvas.pack()
    canvas.create_image(62, 57, image=menu_image)

    # ເຮັດໃຫ້ Canvas ສາມາດກົດໄດ້
    canvas.bind("<Button-1>", lambda e, name=item["name"], price=item["price"]: select_item(name, price))

    # Label ສະແດງຊື່
    lbl_name = tk.Label(item_frame, text=item["name"], font=("Arial", 13, "bold"), bg="white", fg="#3b2418")
    lbl_name.pack(pady=(9, 3))

    # Label ສະແດງລາຄາ
    lbl_price = tk.Label(item_frame, text=item["price"], font=("Arial", 11), bg="white", fg="#9a6b43")
    lbl_price.pack(pady=(0, 10))

    order_button = tk.Button(
        item_frame,
        text="ເລືອກເມນູ",
        command=lambda name=item["name"], price=item["price"]: select_item(name, price),
        font=("Arial", 10, "bold"),
        bg="#8b5e3c",
        fg="white",
        activebackground="#6f472c",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        padx=12,
        pady=6,
    )
    order_button.pack(fill="x")

root.mainloop()
