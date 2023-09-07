from tkinter import *
from tkinter import ttk
import pyperclip
import random

root = Tk()
root.title("Password Generator v1.0")
root.resizable(width=False, height=False)
frm = ttk.Frame(root, padding=5)
frm.grid()

def genPassword():
    letterCount = 0
    tPassword = ""
    
    while True:
        if letterCount == dropOption.get():
            break
        
        nextLetterASCII = random.randint(33, 125)
        nextLetter = chr(nextLetterASCII)
        tPassword = tPassword + nextLetter
        
        letterCount += 1
    
    passString.set(tPassword)
    
def copyToClipboard():
    pyperclip.copy(passString.get())

lengths = [8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

titleLabel = Label(frm, text="Password Generator!")

passString = StringVar()
password = Entry(frm, textvariable=passString, state=DISABLED, justify=CENTER)   

copyButton = Button(frm, 
    text="Copy",
    command=copyToClipboard
    ) 
    
dropOption = IntVar()
dropOption.set(14) #default password length 
drop = OptionMenu(frm, dropOption, *lengths)    

genButton = Button(frm, 
    text="Generate Password",
    command=genPassword
    )
quitButton = Button(frm, 
    text="Quit.", 
    command=root.destroy
    )

titleLabel.grid(column=0, row=0)
password.grid(column=0, row=1)
copyButton.grid(column=1, row=1)
genButton.grid(column=0, row=2)
drop.grid(column=1, row=2)
quitButton.grid(column=0, row=3)
    
root.mainloop()