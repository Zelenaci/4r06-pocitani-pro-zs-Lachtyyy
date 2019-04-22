Created on Mon Apr 22 19:10:40 2019

@author: Lachtyyy
"""

import tkinter as tk
from tkinter import Label, Entry, Radiobutton, Button, END
import random

hlavni= tk.Tk()

Label(hlavni, text=u"Operace: ").grid(row=0, column=0, columnspan=1)

znamenko=tk.StringVar()
def vyberznamenko():
    selection=str(znamenko.get())
    Znak.config(text=selection)

znamenko=tk.StringVar()    
def newpriklad():
    cisloA= random.randint(1,100)
    cisloB= random.randint(1,100)
    cisloAentry.delete(0, END)
    cisloAentry.insert(0, str(cisloA))
    cisloBentry.delete(0, END)
    cisloBentry.insert(0,str(cisloB))
    
#########  MENU  ##########
    
radioplus=Radiobutton(hlavni, text="+", value="+", variable=znamenko, command=vyberznamenko)
radioplus.grid(row=0, column=1)

radiominus=Radiobutton(hlavni, text="-", value="-", variable=znamenko, command=vyberznamenko)
radiominus.grid(row=0, column=2)

radionasob=Radiobutton(hlavni, text="*", value="*", variable=znamenko, command=vyberznamenko)
radionasob.grid(row=0, column=3)

radiodel=Radiobutton(hlavni, text="/", value="/", variable=znamenko, command=vyberznamenko)
radiodel.grid(row=0, column=4)

newpriklad=Button(hlavni, text="Nový příklad", height = 1,command=newpriklad)
newpriklad.grid(row=1, column=5)

#########   ČÍSLA   ###########

cisloAentry= Entry(hlavni, width=5)
cisloAentry.grid(row=1, column=0)

Znak= Label(hlavni, text="?")
Znak.grid(row=1, column=1)

cisloBentry= Entry(hlavni, width=5)
cisloBentry.grid(row=1, column=2)

rovnase= Label(hlavni, text="=", width=5)
rovnase.grid(row=1, column=3)

Vysledek= Entry(hlavni, width=5)
Vysledek.grid(row=1, column=4)
    
hlavni.mainloop()
