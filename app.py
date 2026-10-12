# ບົດຮຽນເກົ່າ: Tkinter GUI ພື້ນຖານ
# ສາມາດເປີດໃຊ້ແຕ່ລະຕົວຢ່າງໄດ້ໂດຍເອົາ # ອອກ
#
# from tkinter import *
# root = Tk()
# root.title("My First GUI")
# root.geometry("400x300")
# Label(root, text="Hello World!").pack()
# root.mainloop()
#
# ປ່ຽນສີ Label:
# from tkinter import *
# root = Tk()
# root.title("My First GUI")
# root.geometry("400x300")
# Label(root, text="Hello World!", fg="red").pack()
# Label(root, text="kolakun", fg="white", bg="blue").pack()
# Label(root, text="Custom Color", fg="#2ecc71", bg="#34495e").pack()
# root.mainloop()
#
# ບົດຮຽນປຸ່ມກົດ:
# import tkinter as tk
# def show_thanks():
#     label.config(text="ຂອບໃຈ")
#     button.config(bg="red")
# mac = tk.Tk()
# mac.title("Python GUI")
# mac.geometry("300x200")
# label = tk.Label(mac, text="ກົດປຸ່ມ")
# label.pack(pady=30)
# button = tk.Button(mac, text="ກົດທີ່ນີ້", command=show_thanks,
#                    bg="blue", fg="white", activebackground="red")
# button.pack()
# mac.mainloop()
#
# ບົດຮຽນເປີດໜ້າຕ່າງທີ 2:
# from tkinter import *
# root = Tk()
# root.title("My First GUI1")
# root.geometry("400x300")
# label1 = Label(root, text="ສະບາຍດີ", fg="red")
# label1.pack(pady=10)
# def open_second_window():
#     label1.config(text="ກົດແລ້ວ")
#     window2 = Toplevel(root)
#     window2.title("My Second GUI")
#     window2.geometry("400x300+50+200")
#     Label(window2, text="ຂອບໃຈເດີ", fg="blue").pack(pady=20)
# Button(root, text="ກົດບ່ອນນີ້", command=open_second_window,
#        bg="green", fg="white").pack(pady=10)
# root.mainloop()

# ໂຕໃໝ່: GUI ປ້ອນຂໍ້ມູນ ແລະສະແດງຜົນດ້ານລຸ່ມ
# import tkinter as tk
# from tkinter import messagebox, ttk


# def save_data():
#     name = name_var.get().strip()
#     age = age_var.get().strip()
#     phone = phone_var.get().strip()

#     if not name or not age or not phone:
#         messagebox.showwarning("ຂໍ້ມູນບໍ່ຄົບ", "ກະລຸນາປ້ອນຂໍ້ມູນໃຫ້ຄົບທຸກຊ່ອງ")
#         return

#     if not age.isdigit() or int(age) <= 0:
#         messagebox.showwarning("ອາຍຸບໍ່ຖືກຕ້ອງ", "ກະລຸນາປ້ອນອາຍຸເປັນຕົວເລກ")
#         age_entry.focus_set()
#         return

#     result_table.insert("", "end", values=(name, age, phone))
#     name_var.set("")
#     age_var.set("")
#     phone_var.set("")
#     name_entry.focus_set()


# def delete_selected():
#     for item in result_table.selection():
#         result_table.delete(item)


# root = tk.Tk()
# root.title("ໂປຣແກຣມປ້ອນຂໍ້ມູນ")
# root.geometry("650x500")
# root.minsize(560, 400)
# root.configure(bg="#042857")

# style = ttk.Style()
# style.theme_use("clam")
# style.configure("Title.TLabel", font=("Arial", 20, "bold"), foreground="#061322")
# style.configure("Form.TLabel", font=("Arial", 12), foreground="#05111C")
# style.configure("Save.TButton", font=("Arial", 12, "bold"), padding=(16, 8))
# style.configure("Treeview.Heading", font=("Arial", 11, "bold"))
# style.configure("Treeview", font=("Arial", 11), rowheight=30)

# name_var = tk.StringVar()
# age_var = tk.StringVar()
# phone_var = tk.StringVar()

# main_frame = ttk.Frame(root, padding=24)
# main_frame.pack(fill="both", expand=True)

# ttk.Label(main_frame, text="ປ້ອນຂໍ້ມູນ", style="Title.TLabel").pack(pady=(0, 18))

# form_frame = ttk.Frame(main_frame)
# form_frame.pack(fill="x")
# form_frame.columnconfigure(1, weight=1)

# ttk.Label(form_frame, text="ຊື່:", style="Form.TLabel").grid(row=0, column=0, sticky="w", padx=(0, 10), pady=7)
# name_entry = ttk.Entry(form_frame, textvariable=name_var, font=("Arial", 12))
# name_entry.grid(row=0, column=1, sticky="ew", pady=7)

# ttk.Label(form_frame, text="ອາຍຸ:", style="Form.TLabel").grid(row=1, column=0, sticky="w", padx=(0, 10), pady=7)
# age_entry = ttk.Entry(form_frame, textvariable=age_var, font=("Arial", 12))
# age_entry.grid(row=1, column=1, sticky="ew", pady=7)

# ttk.Label(form_frame, text="ເບີໂທລະສັບ:", style="Form.TLabel").grid(row=2, column=0, sticky="w", padx=(0, 10), pady=7)
# phone_entry = ttk.Entry(form_frame, textvariable=phone_var, font=("Arial", 12))
# phone_entry.grid(row=2, column=1, sticky="ew", pady=7)

# button_frame = ttk.Frame(main_frame)
# button_frame.pack(fill="x", pady=(14, 22))
# ttk.Button(button_frame, text="ບັນທຶກ", style="Save.TButton", command=save_data).pack(side="left")
# ttk.Button(button_frame, text="ລຶບລາຍການທີ່ເລືອກ", command=delete_selected).pack(side="left", padx=10)

# ttk.Label(main_frame, text="ຜົນການບັນທຶກ", style="Form.TLabel").pack(anchor="w", pady=(0, 7))

# table_frame = ttk.Frame(main_frame)
# table_frame.pack(fill="both", expand=True)
# table_frame.rowconfigure(0, weight=1)
# table_frame.columnconfigure(0, weight=1)

# result_table = ttk.Treeview(table_frame, columns=("name", "age", "phone"), show="headings", selectmode="extended")
# result_table.heading("name", text="ຊື່")
# result_table.heading("age", text="ອາຍຸ")
# result_table.heading("phone", text="ເບີໂທລະສັບ")
# result_table.column("name", width=220)
# result_table.column("age", width=100, anchor="center")
# result_table.column("phone", width=200)
# result_table.grid(row=0, column=0, sticky="nsew")

# scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=result_table.yview)
# scrollbar.grid(row=0, column=1, sticky="ns")
# result_table.configure(yscrollcommand=scrollbar.set)

# name_entry.focus_set()
# root.mainloop()

# from tkinter import *
# from PIL import Image, ImageTk
# root = Tk()
# photo = ImageTk.PhotoImage(Image.open("k.png").resize((100, 100)))
# Button(root, image=photo, command=lambda: print("Button clicked")).pack(pady=20)
# photo=ImageTk.PhotoImage(Image.open("hh.jpg").resize((100, 100)))
# label = Label(root, image=photo,width=100,height=100,borderwidth=0)
# label.pack(pady=20,side=LEFT)
# root.mainloop()

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Food Menu Assignment")
root.geometry("900x400")

# 1. โຫຼດຮູບພາບ ແລະ ແຍກຊື່ໂຕແປໃຫ້ຊັດເຈນ
photo1 = ImageTk.PhotoImage(Image.open("k.png").resize((100, 100)))
photo2 = ImageTk.PhotoImage(Image.open("hh.jpg").resize((100, 100)))
photo3 = ImageTk.PhotoImage(Image.open("k.png").resize((100, 100)))
photo4 = ImageTk.PhotoImage(Image.open("hh.jpg").resize((100, 100)))
photo5 = ImageTk.PhotoImage(Image.open("k.png").resize((100, 100)))

# 2. ສ້າງ Frame ຫຼັກໄວ້ລວມທັງໝົດ
container = Frame(root)
container.pack(expand=True)


# --- ເມນູທີ 1: Coffee ---
frame1 = Frame(container)
frame1.pack(side=LEFT, padx=10)
Label(frame1, image=photo1, borderwidth=0).pack(pady=5)
Label(frame1, text="Coffee\n25,000 kip", font=("Arial", 11), justify=CENTER).pack()


# --- ເມນູທີ 2: Soft drink ---
frame2 = Frame(container)
frame2.pack(side=LEFT, padx=10)
Label(frame2, image=photo2, borderwidth=0).pack(pady=5)
Label(frame2, text="Soft drink\n35,000 kip", font=("Arial", 11), justify=CENTER).pack()


# --- ເມນູທີ 3: Burger ---
frame3 = Frame(container)
frame3.pack(side=LEFT, padx=10)
Label(frame3, image=photo3, borderwidth=0).pack(pady=5)
Label(frame3, text="Burger\n40,000 kip", font=("Arial", 11), justify=CENTER).pack()


# --- ເມນູທີ 4: Cupcake ---
frame4 = Frame(container)
frame4.pack(side=LEFT, padx=10)
Label(frame4, image=photo4, borderwidth=0).pack(pady=5)
Label(frame4, text="Cupcake\n25,000 kip", font=("Arial", 11), justify=CENTER).pack()


# --- ເມນູທີ 5: Doughnut ---
frame5 = Frame(container)
frame5.pack(side=LEFT, padx=10)
Label(frame5, image=photo5, borderwidth=0).pack(pady=5)
Label(frame5, text="Doughnut\n30,000 kip", font=("Arial", 11), justify=CENTER).pack()


root.mainloop()
