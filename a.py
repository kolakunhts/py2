# import tkinter as tk
# from tkinter import ttk, messagebox

# root = tk.Tk()
# root.title("ໂປຣແກຣມປ້ອນຂໍ້ມູນ")
# root.geometry("650x500")
# root.minsize(560, 400)

# # ເຟຣມສຳລັບຈັດວາງ Widget
# form_frame = ttk.Frame(root, padding=20)
# form_frame.pack()

# # 1. ສ້າງ Label ແລະ Entry ສຳລັບປ້ອນຊື່
# ttk.Label(form_frame, text="ກະລຊື່:", style="Form.TLabel").grid(row=0, column=0, sticky="w", padx=(0, 10), pady=7)
# name_entry = ttk.Entry(form_frame, width=30)
# name_entry.grid(row=0, column=1, pady=7)

# # 2. ຟັງຊັນເມື່ອກົດປຸ່ມບັນທຶກ
# def save_data():
#     name = name_entry.get() # ດຶງຂໍ້ຄວາມຈາກ Entry
#     if name.strip():
#         # ແຈ້ງເຕືອນເມື່ອບັນທຶກ ສຳເລັດ
#         messagebox.showinfo("ບັນທຶກ", f"ບັນທຶກຊື່: {name} ຮຽບຮ້ອຍແລ້ວ!")
#         name_entry.delete(0, tk.END) # ລ້າງຂໍ້ຄວາມໃນຊ່ອງປ້ອນ
#     else:
#         messagebox.showwarning("ເຕືອນ", "ກະລຸນາປ້ອນຊື່ກ່ອນ!")

# # 3. ສ້າງປຸ່ມບັນທຶກ
# save_button = ttk.Button(form_frame, text="ບັນທຶກ", command=save_data)
# save_button.grid(row=1, column=0, columnspan=2, pady=15)

# root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("ໂປຣແກຣມປ້ອນຂໍ້ມູນ")
root.geometry("650x500")
root.minsize(560, 400)

# ເຟຣມສຳລັບຟອມປ້ອນຂໍ້ມູນ
form_frame = ttk.Frame(root, padding=20)
form_frame.pack()

# 1. ຊ່ອງປ້ອນຊື່
ttk.Label(form_frame, text="ຊື່:", style="Form.TLabel").grid(row=0, column=0, sticky="w", padx=(0, 10), pady=7)
name_entry = ttk.Entry(form_frame, width=30)
name_entry.grid(row=0, column=1, pady=7)

# 2. ຟັງຊັນບັນທຶກ ແລະ ເພີ່ມຊື່ລົງໃນ Listbox ດ້ານລຸ່ມ
def save_data():
    name = name_entry.get().strip() # ດຶງຂໍ້ຄວາມ
    if name:
        # ເພີ່ມຊື່ເຂົ້າໄປໃນ Listbox ດ້ານລຸ່ມ
        name_listbox.insert(tk.END, name)
        
        # ລ້າງຂໍ້ຄວາມໃນຊ່ອງປ້ອນ
        name_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("ເຕືອນ", "ກະລຸນາປ້ອນຊື່ກ່ອນ!")

# 3. ປຸ່ມບັນທຶກ
save_button = ttk.Button(form_frame, text="ບັນທຶກ", command=save_data)
save_button.grid(row=1, column=0, columnspan=2, pady=10)

# -------------------------------------------------------------
# 4. ສ່ວນສະແດງຜົນດ້ານລຸ່ມ (ເພີ່ມສ່ວນນີ້)
# -------------------------------------------------------------
ttk.Label(form_frame, text="ລາຍຊື່ທີ່ບັນທຶກແລ້ວ:").grid(row=2, column=0, columnspan=2, sticky="w", pady=(15, 5))

# ສ້າງ Listbox ສະແດງລາຍຊື່
name_listbox = tk.Listbox(form_frame, width=40, height=10)
name_listbox.grid(row=3, column=0, columnspan=2, pady=5)

root.mainloop()