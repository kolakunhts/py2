import tkinter as tk
from tkinter import messagebox

# ສ້າງ Window ຫຼັກ
root = tk.Tk()
root.title("Assignment")
root.geometry("850x400")
root.configure(bg="#e8ecf8")  # ສີພື້ນຫຼັງຕາມຮູບ

# ຂໍ້ມູນລາຍການອາຫານ/ເຄື່ອງດື່ມ (ຊື່, ລາຄາ, ສີ ຫຼື ສັນຍາລັກ)
items = [
    {"name": "Coffee", "price": "25,000kip", "icon": "☕"},
    {"name": "Soft drink", "price": "35,000kip", "icon": "🥤"},
    {"name": "Burger", "price": "40,000kip", "icon": "🍔"},
    {"name": "Cupcake", "price": "25,000kip", "icon": "🧁"},
    {"name": "Doughnut", "price": "30,000kip", "icon": "🍩"},
]

# ຟັງຊັນເມື່ອຖືກ ກົດປຸ່ມ
def select_item(item_name, price):
    messagebox.showinfo("Order", f"ທ່ານໄດ້ເລືອກ: {item_name}\nລາຄາ: {price}")

# Container ສໍາລັບຈັດວາງແຖວ
main_frame = tk.Frame(root, bg="#e8ecf8")
main_frame.pack(expand=True, fill="both", pady=50)

# ສ້າງ Card / ປຸ່ມ ແຕ່ລະລາຍການ
for i, item in enumerate(items):
    # Frame ຍ່ອຍຂອງແຕ່ລະ Item
    item_frame = tk.Frame(main_frame, bg="#e8ecf8")
    item_frame.grid(row=0, column=i, padx=15, pady=10)

    # ປຸ່ມຮູບວົງມົນ (ໃຊ້ Canvas)
    canvas = tk.Canvas(item_frame, width=110, height=110, bg="#e8ecf8", highlightthickness=0)
    canvas.pack()
    
    # ແຕ້ມວົງມົນສີເທົາເຂັ້ມ
    circle = canvas.create_oval(5, 5, 105, 105, fill="#343a40", outline="")
    # ໃສ່ Icon / Text ທາງໃນວົງມົນ
    canvas.create_text(55, 55, text=item["icon"], font=("Arial", 36), fill="white")

    # ເຮັດໃຫ້ Canvas ສາມາດກົດໄດ້
    canvas.bind("<Button-1>", lambda e, name=item["name"], price=item["price"]: select_item(name, price))

    # Label ສະແດງຊື່
    lbl_name = tk.Label(item_frame, text=item["name"], font=("Arial", 12, "bold"), bg="#e8ecf8", fg="#212529")
    lbl_name.pack(pady=(10, 2))

    # Label ສະແດງລາຄາ
    lbl_price = tk.Label(item_frame, text=item["price"], font=("Arial", 11), bg="#e8ecf8", fg="#6c757d")
    lbl_price.pack()

root.mainloop()
