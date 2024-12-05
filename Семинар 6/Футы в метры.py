from tkinter import *
from tkinter import ttk
import random

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(round(value * 0.3048, 4))
        compliment = random.choice(compliments)
        compliment_label.set(compliment)
    except ValueError:
        meters.set("Братишка, ошибка ввода")
        compliment_label.set("")

compliments = [
    "У тебя потрясающие глаза, в них можно утонуть!",
    "Твоя улыбка освещает всю комнату!",
    "У тебя великолепные волосы — они выглядят так здорово!",
    "Ты выглядишь просто сногсшибательно в этом наряде!",
    "У тебя идеальная кожа — она сияет!",
    "Ты обладаешь удивительным стилем!",
    "Твоя фигура просто завораживает!",
    "Ты выглядишь так свежо и энергично!",
    "У тебя невероятно привлекательная аура!",
    "Ты просто великолепен(великолепна) — в тебе есть что-то особенное!"
]

root = Tk()
root.title("футы-нуты")

mainframe = ttk.Frame(root, padding="10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()
compliment_label = StringVar()

feet_label = ttk.Label(mainframe, text="Введите футы:")
feet_label.grid(column=1, row=1, sticky=W)
feet_entry = ttk.Entry(mainframe, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters_label = ttk.Label(mainframe, text="Получите метры:")
meters_label.grid(column=1, row=2, sticky=W)
result_label = ttk.Label(mainframe, textvariable=meters)
result_label.grid(column=2, row=2, sticky=(W, E))

compliment_output_label = ttk.Label(mainframe, textvariable=compliment_label)
compliment_output_label.grid(column=1, row=3, columnspan=2)

calculate_button = ttk.Button(mainframe, text="Конвертировать", command=calculate)
calculate_button.grid(column=2, row=4, sticky=W)

root.mainloop()