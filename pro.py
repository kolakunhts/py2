from tkinter import *
from PIL import Image, ImageTk

def show_name():
    name = name_var.get()
    password = pass_var.get()

    if name == "z" and password == "1234567890":
        print("Name:", name)
        print("Password:", password)
        print("True")
        result_label.config(text="ຂໍ້ມູນຖືກຕ້ອງແລ້ວນ້ອງ", fg="green")
        open_welcome_window(name)
    else:
        print("Wrong")
        result_label.config(text="ລະຫັດຜ່ານບໍ່ຖືກຕ້ອງ!!!!", fg="red")
        error_message()

def open_welcome_window(name):
    welcome_window = Toplevel(root)
    welcome_window.title("Welcome")
    welcome_window.geometry("400x200+500+400")

    welcome_label = Label(welcome_window, text=f"ຍິນດີຕ້ອນຮັບ {name}!", font=("Arial", 20), fg="green")
    welcome_label.pack(pady=50)

    welcome_button = Button(welcome_window, text="click me", bg='#FF0000', command=message1)
    welcome_button.pack(pady=10)

def message1():
    mess_window = Toplevel(root)
    mess_window.title("Message")
    mess_window.geometry("400x200+500+400")

    mess_label = Label(mess_window, text="ກົດເຂົ້າມາເຮັດຫຍັງ", font=("Arial", 20), fg="green")
    mess_label.pack(pady=50)

    mess_button = Button(mess_window, text="click me", bg='#FF0000', command=message2)
    mess_button.pack(pady=10)

def message2():
    mess_window2 = Toplevel(root)
    mess_window2.title("Message")
    mess_window2.geometry("400x200+500+400")

    mess_label2 = Label(mess_window2, text="ກົດເຂົ້າມາເຮັດຫຍັງອີກ~~~~~~~~~", font=("Arial", 20), fg="green")
    mess_label2.pack(pady=50)

    mess_button2 = Button(mess_window2, text="click me", bg='#FF0000')
    mess_button2.pack(pady=10)

def error_message():
    error_window = Toplevel(root)
    error_window.title("Error")
    error_window.geometry("400x200+500+400")

    error_label = Label(error_window, text="ລະຫັດຜ່ານບໍ່ຖືກຕ້ອງ", font=("Arial", 20), fg="red")
    error_label.pack(pady=50)

root = Tk()
root.title("login game888")
root.geometry("600x400+400+300")

img = Image.open("hh.jpg").resize((100, 100))
photo = ImageTk.PhotoImage(img)
level_label = Label(root, image=photo, borderwidth=0)
level_label.pack(padx=20, pady=20)

name_var = StringVar()
pass_var = StringVar()

MyLabel1 = Label(root, text="Username")
MyLabel1.pack()

MyLabel2 = Entry(root, textvariable=name_var, bg='#008080', highlightbackground="#0A5E7F")
MyLabel2.pack()

MyLabel3 = Label(root, text="Password")
MyLabel3.pack()

MyLabel4 = Entry(root, textvariable=pass_var, bg='#008080', show='*', highlightbackground="#0A5E7F")
MyLabel4.pack()

Mybutton = Button(root, text="Click Me", bg='#FF0000', command=show_name)
Mybutton.pack()

result_label = Label(root, text="", font=("Arial", 30))
result_label.pack()

root.mainloop()