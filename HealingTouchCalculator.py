#Healing Touch Rank Calculator
#Written by Joseph Whitt
#With help from Wowhead for spell coefficients and min/max data

from tkinter import *

window = Tk()
window.title("Healing Touch Calculator")
window.geometry('300x500')


#######################
#Labels and Text Boxes#
#######################

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

#Healing Touch Rank 6 text label
lblTxt3 = StringVar()
lblTxt3.set("Average HT6 Amount:")
lbl = Label(window, textvariable=lblTxt3)
lbl.grid(column=0, row=5, padx=5, pady=5)

#Healing Touch Rank 6 number label
lblTxtHT6 = StringVar()
lblHT6 = Label(window, textvariable=lblTxtHT6)
lblHT6.grid(column=1, row=5, padx=5, pady=5)

#Healing Touch Rank 7 text label
lblTxt4 = StringVar()
lblTxt4.set("Average HT7 Amount:")
lbl = Label(window, textvariable=lblTxt4)
lbl.grid(column=0, row=6, padx=5, pady=5)

#Healing Touch Rank 7 number label
lblTxtHT7 = StringVar()
lblHT7 = Label(window, textvariable=lblTxtHT7)
lblHT7.grid(column=1, row=6, padx=5, pady=5)

#Healing Touch Rank 8 text label
lblTxt5 = StringVar()
lblTxt5.set("Average HT8 Amount:")
lbl = Label(window, textvariable=lblTxt5)
lbl.grid(column=0, row=7, padx=5, pady=5)

#Healing Touch Rank 8 number label
lblTxtHT8 = StringVar()
lblHT8 = Label(window, textvariable=lblTxtHT8)
lblHT8.grid(column=1, row=7, padx=5, pady=5)

#Entry Box
txtBox = Entry(window)
txtBox.grid(column=0, row=1, padx=5, pady=5)



###########################
#Main Calculation Function#
########################### 	
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

        HTmin = round(762 + (int(txtBox.get()))) #Rank 6, 100% Spellpower Coefficient
        HTmax = round(914 + (int(txtBox.get())))
        lblTxtHT6.set(int((HTmin + HTmax) / 2))
        
        HTmin = round(958 + (int(txtBox.get()))) #Rank 7, 100% Spellpower Coefficient
        HTmax = round(1143 + (int(txtBox.get())))
        lblTxtHT7.set(int((HTmin + HTmax) / 2))
        
        HTmin = round(1225 + (int(txtBox.get()))) #Rank 8, 100% Spellpower Coefficient
        HTmax = round(1453 + (int(txtBox.get())))
        lblTxtHT8.set(int((HTmin + HTmax) / 2))
    else:
        lblTxt.set("Invalid Input!")

txtBtn = Button(window, text="Calculate Healing Amount", command = CalculateHT)
txtBtn.grid(column=0, row=2, padx=5, pady=5)

window.mainloop()