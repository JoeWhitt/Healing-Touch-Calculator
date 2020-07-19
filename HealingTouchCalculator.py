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
lblTxt7 = StringVar()
lblTxt7.set("Average HT4 Amount:")
lbl = Label(window, textvariable=lblTxt7)
lbl.grid(column=0, row=3, padx=5, pady=5)

#Healing Touch Rank 4 number label
lblTxtHT4 = StringVar()
lblHT4 = Label(window, textvariable=lblTxtHT4)
lblHT4.grid(column=1, row=3, padx=5, pady=5)

#Healing Touch Rank 5 text label
lblTxt5 = StringVar()
lblTxt5.set("Average HT5 Amount:")
lbl = Label(window, textvariable=lblTxt5)
lbl.grid(column=0, row=4, padx=5, pady=5)

#Healing Touch Rank 5 number label
lblTxtHT5 = StringVar()
lblHT5 = Label(window, textvariable=lblTxtHT5)
lblHT5.grid(column=1, row=4, padx=5, pady=5)

#Healing Touch Rank 6 text label
lblTxt6 = StringVar()
lblTxt6.set("Average HT6 Amount:")
lbl = Label(window, textvariable=lblTxt6)
lbl.grid(column=0, row=5, padx=5, pady=5)

#Healing Touch Rank 6 number label
lblTxtHT6 = StringVar()
lblHT6 = Label(window, textvariable=lblTxtHT6)
lblHT6.grid(column=1, row=5, padx=5, pady=5)

#Healing Touch Rank 7 text label
lblTxt7 = StringVar()
lblTxt7.set("Average HT7 Amount:")
lbl = Label(window, textvariable=lblTxt7)
lbl.grid(column=0, row=6, padx=5, pady=5)

#Healing Touch Rank 7 number label
lblTxtHT7 = StringVar()
lblHT7 = Label(window, textvariable=lblTxtHT7)
lblHT7.grid(column=1, row=6, padx=5, pady=5)

#Healing Touch Rank 8 text label
lblTxt8 = StringVar()
lblTxt8.set("Average HT8 Amount:")
lbl = Label(window, textvariable=lblTxt8)
lbl.grid(column=0, row=7, padx=5, pady=5)

#Healing Touch Rank 8 number label
lblTxtHT8 = StringVar()
lblHT8 = Label(window, textvariable=lblTxtHT8)
lblHT8.grid(column=1, row=7, padx=5, pady=5)

#Healing Touch Rank 9 text label
lblTxt9 = StringVar()
lblTxt9.set("Average HT9 Amount:")
lbl = Label(window, textvariable=lblTxt9)
lbl.grid(column=0, row=8, padx=5, pady=5)

#Healing Touch Rank 9 number label
lblTxtHT9 = StringVar()
lblHT9 = Label(window, textvariable=lblTxtHT9)
lblHT9.grid(column=1, row=8, padx=5, pady=5)

#Healing Touch Rank 10 text label
lblTxt10 = StringVar()
lblTxt10.set("Average HT10 Amount:")
lbl = Label(window, textvariable=lblTxt10)
lbl.grid(column=0, row=9, padx=5, pady=5)

#Healing Touch Rank 10 number label
lblTxtHT10 = StringVar()
lblHT10 = Label(window, textvariable=lblTxtHT10)
lblHT10.grid(column=1, row=9, padx=5, pady=5)

#Entry Box
txtBox = Entry(window)
txtBox.grid(column=0, row=1, padx=5, pady=5)



###########################
#Main Calculation Function#
########################### 	
def CalculateHT():
    lblTxt.set("Enter your total healing power:") #Reset the text after typing a valid number.
    healpower = txtBox.get()
    if (healpower.isnumeric()) == True:
        HTmin = round(376 + (int(txtBox.get()) * .857)) #Rank 4, 376-459 with 85.7% Spellpower Coefficient
        HTmax = round(459 + (int(txtBox.get()) * .857))
        lblTxtHT4.set(int((HTmin + HTmax) / 2))

        HTmin = round(589 + (int(txtBox.get()))) #Rank 5, 589-712 with 100% Spellpower Coefficient
        HTmax = round(712 + (int(txtBox.get())))
        lblTxtHT5.set(int((HTmin + HTmax) / 2))

        HTmin = round(762 + (int(txtBox.get()))) #Rank 6, 762-914 with 100% Spellpower Coefficient
        HTmax = round(914 + (int(txtBox.get())))
        lblTxtHT6.set(int((HTmin + HTmax) / 2))
        
        HTmin = round(958 + (int(txtBox.get()))) #Rank 7, 985-1143 with 100% Spellpower Coefficient
        HTmax = round(1143 + (int(txtBox.get())))
        lblTxtHT7.set(int((HTmin + HTmax) / 2))
        
        HTmin = round(1225 + (int(txtBox.get()))) #Rank 8, 1225-1453 with 100% Spellpower Coefficient
        HTmax = round(1453 + (int(txtBox.get())))
        lblTxtHT8.set(int((HTmin + HTmax) / 2))

        HTmin = round(1545 + (int(txtBox.get()))) #Rank 9, 1545-1826 with 100% Spellpower Coefficient
        HTmax = round(1826 + (int(txtBox.get())))
        lblTxtHT9.set(int((HTmin + HTmax) / 2))

        HTmin = round(1916 + (int(txtBox.get()))) #Rank 10, 1916-2257 with 100% Spellpower Coefficient
        HTmax = round(2257 + (int(txtBox.get())))
        lblTxtHT10.set(int((HTmin + HTmax) / 2))
    else:
        lblTxt.set("Invalid Input!")

txtBtn = Button(window, text="Calculate Healing Amount", command = CalculateHT)
txtBtn.grid(column=0, row=2, padx=5, pady=5)

window.mainloop()