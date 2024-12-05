from tkinter import *
from tkinter import ttk


def calculate(*args):
    try:
        value_1 = float(mass.get())
        value_22 = float(height.get())
        value_2 = value_22 / 100
        imt = (value_1) / (value_2 ** 2)
        bmi.set(int(imt))

        if imt <= 16:
            puk.set("Выраженный дефицит массы тела")
        elif 16 < imt <= 18.5:
            puk.set("Недостаточная (дефицит) масса тела")
        elif 18.5 < imt <= 25:
            puk.set("Нормальная масса тела")
        elif 25 < imt <= 30:
            puk.set("Избыточная масса тела (предожирение)")
        elif 30 < imt <= 35:
            puk.set("Ожирение 1 степени")
        elif 35 < imt <= 40:
            puk.set("Ожирение 2 степени")
        elif imt >= 40:
            puk.set("Ожирение 3 степени")

        status_message.set("Вне зависимости от этих цифр, вы все равно прекрасны!")

    except ValueError:
        pass


root = Tk()
root.title("BMI Calculator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mass = StringVar()
mass_entry = ttk.Entry(mainframe, width=7, textvariable=mass)
mass_entry.grid(column=2, row=1, sticky=(W, E))

height = StringVar()
height_entry = ttk.Entry(mainframe, width=7, textvariable=height)
height_entry.grid(column=2, row=2, sticky=(W, E))

bmi = StringVar()
ttk.Label(mainframe, textvariable=bmi).grid(column=2, row=3, sticky=(W, E))

puk = StringVar()
ttk.Label(mainframe, textvariable=puk).grid(column=2, row=4, sticky=(W, E))

status_message = StringVar()
ttk.Label(mainframe, textvariable=status_message).grid(column=1, row=5, columnspan=2)

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=4, row=4, sticky=W)

ttk.Label(mainframe, text="Введи массу в килограммах").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Введи рост в сантиметрах").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Индекс массы тела:").grid(column=1, row=3, sticky=E)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

mass_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()