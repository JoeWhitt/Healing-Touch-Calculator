#Healing Touch Rank Calculator
#Written by Joseph Whitt
#With help from Wowhead for spell coefficients and min/max data

from tkinter import *

window = Tk()
window.title("Healing Touch Calculator")
window.geometry('300x500')

#Top text label
lblTxt = StringVar()
lblTxt.set("Enter your total healing power:")
lbl = Label(window, textvariable=lblTxt)
lbl.grid(column=0, row=0, padx=5, pady=5)

#Healing Touch Rank 4 text label
lblTxt2 = StringVar()
lblTxt2.set("Average HT4 Amount:")
lbl = Label(window, textvariable=lblTxt2)
lbl.grid(column=0, row=3, padx=5, pady=5)

#Healing Touch Rank 4 number label
lblTxtHT4 = StringVar()
lblHT4 = Label(window, textvariable=lblTxtHT4)
lblHT4.grid(column=1, row=3, padx=5, pady=5)

#Healing Touch Rank 5 text label
lblTxt2 = StringVar()
lblTxt2.set("Average HT5 Amount:")
lbl = Label(window, textvariable=lblTxt2)
lbl.grid(column=0, row=4, padx=5, pady=5)

#Healing Touch Rank 5 number label
lblTxtHT5 = StringVar()
lblHT5 = Label(window, textvariable=lblTxtHT5)
lblHT5.grid(column=1, row=4, padx=5, pady=5)

#Entry Box
txtBox = Entry(window)
txtBox.grid(column=0, row=1, padx=5, pady=5)




	
def CalculateHT():
    lblTxt.set("Enter your total healing power:") #Reset the text after typing a valid number
    healpower = txtBox.get()
    if (healpower.isnumeric()) == True:
        HTmin = round(376 + (int(txtBox.get()) * .857)) #Rank 4, 85.7% Spellpower Coefficient
        HTmax = round(459 + (int(txtBox.get()) * .857))
        lblTxtHT4.set(int((HTmin + HTmax) / 2))

        HTmin = round(589 + (int(txtBox.get()))) #Rank 5, 100% Spellpower Coefficient
        HTmax = round(712 + (int(txtBox.get())))
        lblTxtHT5.set(int((HTmin + HTmax) / 2))
    else:
        lblTxt.set("Invalid Input!")

txtBtn = Button(window, text="Calculate Healing Amount", command = CalculateHT)
txtBtn.grid(column=0, row=2, padx=5, pady=5)

window.mainloop()