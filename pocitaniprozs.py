# -*- coding: utf-8 -*-
"""
@author: Lachtyyy
"""

import tkinter as tk
from tkinter import Label, Entry, END, Radiobutton, Button,
import random


hlavni= tk.Tk()
Label(hlavni, text="Operace:").grid(row=0, column=0, columnspan=1)

                    ###### ZNAMENKO ######

znamenko=tk.StringVar()
def getznamenko():
    selection=str(znamenko.get())
    Znak.config(text=selection)

znamenko=tk.StringVar()   
def novypriklad():
    cisloA= random.randint(1,10)
    cisloB= random.randint(1,10)
    cisloAentry.delete(0, END)
    cisloAentry.insert(0, str(cisloA))
    cisloBentry.delete(0, END)
    cisloBentry.insert(0,str(cisloB))
    
                    ###### MENU ######
radioplus=Radiobutton(hlavni, text="+", value="+", variable=znamenko, command=getznamenko)
radioplus.grid(row=0, column=1)
radiominus=Radiobutton(hlavni, text="-", value="-", variable=znamenko, command=getznamenko)
radiominus.grid(row=0, column=2)
radionasobeni=Radiobutton(hlavni, text="*", value="*", variable=znamenko, command=getznamenko)
radionasobeni.grid(row=0, column=3)
radiodeleno=Radiobutton(hlavni, text="/", value="/", variable=znamenko, command=getznamenko)
radiodeleno.grid(row=0, column=4)
novypriklad=Button(hlavni, text="Nový příklad", command=novypriklad)
novypriklad.grid(row=0, column=5)

                ##### CISLA A VYSLEDEK #####
cisloAentry= Entry(hlavni, width=3)
cisloAentry.grid(row=1, column=0)

Znak= Label(hlavni, text="")
Znak.grid(row=1, column=1)

cisloBentry= Entry(hlavni, width=3)
cisloBentry.grid(row=1, column=2)

rovnase= Label(hlavni, text="=", width=5)
rovnase.grid(row=1, column=3)

Vysledek= Entry(hlavni, width=4)
Vysledek.grid(row=1, column=4)


hlavni.mainloop()