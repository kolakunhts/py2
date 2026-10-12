import tkinter as tk
from tkinter import messagebox


BG = "#eef4ff"
NAVY = "#173b72"
BLUE = "#246bce"
TEXT = "#1d2a3a"
MUTED = "#718096"
WHITE = "#ffffff"


def login():
    username = username_var.get().strip()
    password = password_var.get()

    if not username or not password:
        status_var.set("ກະລຸນາປ້ອນຊື່ຜູ້ໃຊ້ ແລະ ລະຫັດຜ່ານ")
        status_label.configure(fg="#d64545")
        return

    # ບັນຊີສຳລັບທົດສອບ GUI: admin / admin123
    if username == "admin" and password == "admin123":
        status_var.set("ລັອກອິນສຳເລັດແລ້ວ ✓")
        status_label.configure(fg="#218739")
        messagebox.showinfo("ສຳເລັດ", f"ຍິນດີຕ້ອນຮັບ, {username}!")
    else:
        status_var.set("ຊື່ຜູ້ໃຊ້ ຫຼື ລະຫັດຜ່ານບໍ່ຖືກຕ້ອງ")
        status_label.configure(fg="#d64545")
        password_entry.select_range(0, tk.END)
        password_entry.focus_set()


def toggle_password():
    password_entry.configure(show="" if show_password_var.get() else "•")


def show_forgot_password():
    messagebox.showinfo("ລືມລະຫັດຜ່ານ", "ກະລຸນາຕິດຕໍ່ຜູ້ດູແລລະບົບເພື່ອຕັ້ງລະຫັດໃໝ່")


root = tk.Tk()
root.title("ລັອກອິນ")
root.geometry("760x500")
root.minsize(620, 430)
root.configure(bg=BG)

# ກ່ອງຫຼັກ
card = tk.Frame(root, bg=WHITE, highlightthickness=1, highlightbackground="#d9e4f4")
card.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.78, relheight=0.78)

# ດ້ານຊ້າຍ: ສ່ວນຕ້ອນຮັບ
welcome = tk.Frame(card, bg=NAVY)
welcome.place(relx=0, rely=0, relwidth=0.42, relheight=1)
tk.Label(welcome, text="ສະບາຍດີ", bg=NAVY, fg=WHITE,
         font=("Arial", 25, "bold")).pack(anchor="w", padx=28, pady=(66, 8))
tk.Label(welcome, text="ຍິນດີຕ້ອນຮັບກັບລະບົບ", bg=NAVY, fg="#dbeafe",
         font=("Arial", 13)).pack(anchor="w", padx=28)
tk.Label(welcome, text="ເຂົ້າສູ່ບັນຊີຂອງທ່ານ\nເພື່ອໃຊ້ງານຕໍ່", bg=NAVY, fg="#a9c5ec",
         justify="left", font=("Arial", 11), pady=34).pack(anchor="w", padx=28)
tk.Label(welcome, text="●  ປອດໄພ  •  ງ່າຍ  •  ໄວ", bg=NAVY, fg="#a9c5ec",
         font=("Arial", 10)).pack(anchor="w", padx=28, side="bottom", pady=28)

# ດ້ານຂວາ: ຟອມລັອກອິນ
form = tk.Frame(card, bg=WHITE)
form.place(relx=0.42, rely=0, relwidth=0.58, relheight=1)

tk.Label(form, text="ເຂົ້າສູ່ລະບົບ", bg=WHITE, fg=TEXT,
         font=("Arial", 21, "bold")).pack(anchor="w", padx=42, pady=(48, 5))
tk.Label(form, text="ປ້ອນຂໍ້ມູນຂອງທ່ານດ້ານລຸ່ມ", bg=WHITE, fg=MUTED,
         font=("Arial", 10)).pack(anchor="w", padx=42, pady=(0, 25))

username_var = tk.StringVar()
password_var = tk.StringVar()
show_password_var = tk.BooleanVar(value=False)
status_var = tk.StringVar()

tk.Label(form, text="ຊື່ຜູ້ໃຊ້", bg=WHITE, fg=TEXT,
         font=("Arial", 11, "bold")).pack(anchor="w", padx=42)
username_entry = tk.Entry(form, textvariable=username_var, bg="#f7faff", fg=TEXT,
                          insertbackground=BLUE, relief="flat", font=("Arial", 12),
                          highlightthickness=1, highlightcolor=BLUE,
                          highlightbackground="#d5dfec")
username_entry.pack(fill="x", padx=42, ipady=9, pady=(7, 16))

tk.Label(form, text="ລະຫັດຜ່ານ", bg=WHITE, fg=TEXT,
         font=("Arial", 11, "bold")).pack(anchor="w", padx=42)
password_entry = tk.Entry(form, textvariable=password_var, show="•", bg="#f7faff", fg=TEXT,
                          insertbackground=BLUE, relief="flat", font=("Arial", 12),
                          highlightthickness=1, highlightcolor=BLUE,
                          highlightbackground="#d5dfec")
password_entry.pack(fill="x", padx=42, ipady=9, pady=(7, 8))

options = tk.Frame(form, bg=WHITE)
options.pack(fill="x", padx=42)
tk.Checkbutton(options, text="ສະແດງລະຫັດຜ່ານ", variable=show_password_var,
               command=toggle_password, bg=WHITE, fg=MUTED, activebackground=WHITE,
               activeforeground=TEXT, selectcolor=WHITE, font=("Arial", 9),
               highlightthickness=0).pack(side="left")
tk.Button(options, text="ລືມລະຫັດຜ່ານ?", command=show_forgot_password,
          bg=WHITE, fg=BLUE, activebackground=WHITE, activeforeground=NAVY,
          relief="flat", borderwidth=0, cursor="hand2", font=("Arial", 9)).pack(side="right")

status_label = tk.Label(form, textvariable=status_var, bg=WHITE, fg="#d64545",
                        font=("Arial", 9))
status_label.pack(anchor="w", padx=42, pady=(15, 0))

login_button = tk.Button(form, text="ເຂົ້າສູ່ລະບົບ", command=login, bg=BLUE, fg=WHITE,
                         activebackground="#1c56a5", activeforeground=WHITE,
                         relief="flat", cursor="hand2", font=("Arial", 12, "bold"),
                         pady=10)
login_button.pack(fill="x", padx=42, pady=(10, 0))

root.bind("<Return>", lambda event: login())
username_entry.focus_set()
root.mainloop()
