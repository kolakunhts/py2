# import tkinter as tk
# from tkinter import ttk, messagebox

# root = tk.Tk()
# root.title("ໜ້າລັອກອິນ")
# root.geometry("350x250")
# root.resizable(False, False)

# # ຟັງຊັນກວດສອບການລັອກອິນ
# def login():
#     username = user_entry.get().strip()
#     password = pass_entry.get().strip()
    
#     # ກວດສອບວ່າປ້ອນຂໍ້ມູນຄົບຫຼືບໍ່
#     if username and password:
#         messagebox.showinfo("ສຳເລັດ", "ເຂົ້າສູ່ລະບົບສຳເລັດ!")
#         # ລ້າງຂໍ້ມູນໃນຊ່ອງປ້ອນ
#         user_entry.delete(0, tk.END)
#         pass_entry.delete(0, tk.END)
#     else:
#         messagebox.showwarning("ເຕືອນ", "ກະລຸນາປ້ອນຊື່ຜູ້ໃຊ້ ແລະ ລະຫັດຜ່ານ!")

# # ເຟຣມຈັດວາງ
# frame = ttk.Frame(root, padding=20)
# frame.pack(expand=True)

# # 1. ຊ່ອງປ້ອນຊື່ຜູ້ໃຊ້ (Username)
# ttk.Label(frame, text="ຊື່ຜູ້ໃຊ້:").grid(row=0, column=0, sticky="w", pady=5)
# user_entry = ttk.Entry(frame, width=25)
# user_entry.grid(row=0, column=1, pady=5)

# # 2. ຊ່ອງປ້ອນລະຫັດຜ່ານ (Password) - ໃຊ້ show="*" ເພື່ອເຊື່ອງລະຫັດ
# ttk.Label(frame, text="ລະຫັດຜ່ານ:").grid(row=1, column=0, sticky="w", pady=5)
# pass_entry = ttk.Entry(frame, width=25, show="*")
# pass_entry.grid(row=1, column=1, pady=5)

# # 3. ປຸ່ມລັອກອິນ
# login_btn = ttk.Button(frame, text="ເຂົ້າສູ່ລະບົບ", command=login)
# login_btn.grid(row=2, column=0, columnspan=2, pady=15)

# root.mainloop()



# from tkinter import *
# root = Tk()
# root.title("ໜ້າລັອກອິນ")
# root.geometry("350x250")

# def user():
#       Message=txt.get("1.0","end-1c")
#       print(Message)
#       label=Label(root,text=Message)
#       label.pack()
# txt=Text(root,height=1.5,width=25)
# txt.pack()
# myButton=Button(root,text="ສົ່ງ",command=user)
# myButton.pack()
# root.geometry("350x250")
# root.mainloop()


from tkinter import *
from tkinter import messagebox

def open_welcome_window(username):
    """ເປີດໜ້າທີສອງຫຼັງຈາກລັອກອິນສຳເລັດ"""
    welcome_window = Toplevel(root)
    welcome_window.title("ໜ້າຫຼັກ")
    welcome_window.geometry("500x300+450+350")
    welcome_window.configure(bg="#eef4ff")
    welcome_window.resizable(False, False)
    Label(welcome_window,text="ຍິນດີຕ້ອນຮັບ!",bg="#867f81",fg="#787c82",font=("Arial", 26, "bold"),
    ).pack(pady=(55, 12))
    Label(welcome_window,text=f"ສະບາຍດີ, {username}\nລັອກອິນເຂົ້າລະບົບສຳເລັດແລ້ວ",bg="#105f93",fg="#1d2a3a",font=("Arial", 14),justify="center",
    ).pack(pady=10)

    Button(welcome_window,text="ປິດໜ້ານີ້",command=welcome_window.destroy,bg="#246bce",fg="white",
     activebackground="#1c56a5",relief="flat",cursor="hand2",font=("Arial", 11, "bold"),padx=18,pady=8,
    ).pack(pady=18)
    welcome_window.transient(root)
    welcome_window.grab_set()
    welcome_window.focus_set()


def show_name():
    username = name_var.get().strip()
    password = pass_var.get().strip()

    if username == "admin" and password == "1234":
        result_label.config(text="ລັອກອິນຜ່ານ", fg="green")
        messagebox.showinfo("ສຳເລັດ", "ລັອກອິນຜ່ານ")
        open_welcome_window(username)
    else:
        result_label.config(text="ຊື່ຜູ້ໃຊ້ ຫຼື ລະຫັດຜ່ານບໍ່ຖືກຕ້ອງ", fg="red")
        messagebox.showerror("ຜິດພາດ", "ຊື່ຜູ້ໃຊ້ ຫຼື ລະຫັດຜ່ານບໍ່ຖືກຕ້ອງ")

root = Tk()
root.title("GUI")
root.geometry("600x400+400+300")

name_var = StringVar()
pass_var = StringVar()

MyLabel1 = Label(root, text="Username")
MyLabel1.pack()

MyLabel2 = Entry(root, textvariable=name_var, bg='#008080')
MyLabel2.pack()

MyLabel3 = Label(root, text="Password")
MyLabel3.pack()

MyLabel4 = Entry(root, textvariable=pass_var, bg='#008080', show='*')
MyLabel4.pack()

Mybutton = Button(root, text="ລັອກອິນ", bg='#FF0000', fg='white', command=show_name)
Mybutton.pack()

result_label = Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=15)

root.bind("<Return>", lambda event: show_name())

root.mainloop()
