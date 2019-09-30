'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Howard C Davis
Final Tk
'''

from tkinter import *
from tkinter import ttk

amount = 0
temp_price_selection = 0
temp_price_combo = 0

root = Tk()
root.title("Pricing Calculator")

mainframe = Frame(root, borderwidth=10, height=1500, width=1500)
mainframe.grid(column=10, row=10, sticky=(N, W, E, S))
mainframe.anchor(CENTER)

frame2 = Frame(mainframe, borderwidth=10, height=150, width=150)
frame2.grid(column=10, row=10, sticky=(N, W, E, S))
frame2.anchor(CENTER)

notes = StringVar()
label = StringVar()
howship = StringVar()
shipping = ["Fed Ex", "USPS", "UPS"]
shipping_price = [7.50, 10.00, 5.00]

items = ["Vase", "Amythest", "Game", "Plushie", "Monopoly", "Fortnite Pickaxe", "Rock", "Cup", "Headphones", "Lamp",
         "Poster", "Glass", "Cutlery", "Computer", "Microphone"]
price = [10.50, 1.50, 3.50, 7.50, 5.50, 16.50, 12.50, 11.50, 5.50, 17.50, 15.50, 13.50, 18.50, 19.50, 20.50]

scrollbar = Scrollbar(frame2, orient=VERTICAL)
listbox = Listbox(frame2, height=10, selectmode=MULTIPLE, listvariable=items, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
scrollbar.grid(column=1, row=2)

P1 = ttk.Progressbar(frame2, orient=HORIZONTAL, length=200, mode='determinate')
P1.grid(column=4, row=1)

CB1 = ttk.Combobox(frame2, values=shipping, width=10, textvariable=howship)

progress_list = {'Items': False, 'Ship': False, 'Calc': False}


def progress_check():
    global progress_list, P1
    temp_prog_var = 0
    if progress_list['Items'] == True:
        temp_prog_var += 33
    if progress_list['Ship'] == True:
        temp_prog_var += 33
    if progress_list['Calc'] == True:
        temp_prog_var += 34
    P1['value'] = temp_prog_var


def submit():
    global P1, amount, progress_list
    if P1['value'] < 66:
        label.set('Not all areas filled out,Your current total is $' + str(amount))
    else:
        CB1.configure(state=DISABLED)
        listbox.configure(state=DISABLED)
        label.set('Thanks for shopping! Your total is $' + str(amount))
        progress_list['Calc'] = True
        progress_check()


def price_add():
    global amount, temp_price_combo, temp_price_selection
    amount = 0
    amount += (temp_price_selection)
    amount += (temp_price_combo)
    label.set('Your total is $' + str(amount))


def combo_selection(event):
    global amount, temp_price_combo
    progress_list['Ship'] = True
    progress_check()

    temp_price_combo = 0
    temp_cbvar = CB1.get()
    temp_index = shipping.index(temp_cbvar)
    temp_price_combo = shipping_price[temp_index]
    price_add()


def selection(event):
    global amount, P1, CB1, temp_price_selection
    temp_var = listbox.curselection()
    if str(temp_var) != '()':
        progress_list['Items'] = True
    else:
        progress_list['Items'] = False

    progress_check()

    temp_price_selection = 0
    for x in temp_var:
        temp_xvar = items[x]
        temp_price_selection += price[x]
    price_add()


CB1.bind("<<ComboboxSelected>>", combo_selection)
listbox.bind('<<ListboxSelect>>', selection)

for value in items:
    listbox.insert(END, value)

listbox.grid(column=1, row=2, pady=10)
CB1.grid(column=1, row=1, padx=10)

L1 = Label(
    frame2, textvariable=label
).grid(column=1, row=3)

L2 = Label(
    frame2, text="Notes:"
).grid(column=2, row=1)

T1 = Text(frame2, height=10, width=15).grid(column=2, row=2, padx=10)
B1 = Button(
    frame2, command=submit, height=1, width=7, text="Submit"
).grid(column=3, row=3)

frame2.columnconfigure(0, weight=1)
frame2.rowconfigure(0, weight=1)

root.mainloop()