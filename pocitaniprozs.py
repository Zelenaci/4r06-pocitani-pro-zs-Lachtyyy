#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:57:13 2019

@author: lac35158
"""

import tkinter as tk
from tkinter import LabelFrame, Radiobutton, Entry
from random import randint

class Application(tk.Tk):
    name = 'Počítání pro ZŠ'
    
    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.config(borderwidth=10)
        self.lbl = tk.Label(self, text='Počítání pro ZŠ')
        self.lbl.pack()
        self.operaceVar = tk.StringVar()
        self.operaceVar.trace('w', self.vypocet)
        self.operaceFrame = LabelFrame(self, text="Operace",padx=5, pady=5)
        self.operaceFrame.pack(anchor=tk.W)
        Radiobutton(self.operaceFrame, text="+",
                    variable=self.operaceVar, value='+').pack()
        Radiobutton(self.operaceFrame, text="-",
                    variable=self.operaceVar, value='-').pack()
        Radiobutton(self.operaceFrame, text='*',
                    variable=self.operaceVar, value='*').pack()
        Radiobutton(self.operaceFrame, text='/',
                    variable=self.operaceVar, value='/').pack()
        self.operaceVar.set('+')   # vyberu nákup
        self.kkn = tk.Button(self, text = 'Vypočitej!', command = self.vypocet)
        self.kkn.pack()
        self.bind("<Escape>", self.quit)
        
        
    def ukazka(self, event):
        print(event.x, event.y, event.num, event.type)
        print(dir(event))
    
    def plus(self):
        self.x = randint(1, 99)
        self.y = randint(0, 100-self.x)
        self.vysl = self.x + self.y
        
    def mínus(self):
        self.x = randint(1, 99)
        self.y = randint(0,self.x)
        self.vysl = self.x - self.y
    
    def krat(self):
        self.x = randint(1, 9)
        self.y = randint(1, 9)
        self.vysl = self.x * self.y
    
    def deleno(self):
        self.x = randint(1, 9)
        self.y = randint(1, 9)
        self.vysl = self.x * self.y
    
    def vypocet(self):
        operace = (self.plus, self.mínus, self.krat, self.deleno)
        random = randint(0, 3)
        funkce = operace[random]
        funkce()
        print()
        print(self.x, funkce.__name__,self.y, '=')
    
    
    def quit(self, event=None):
        super().quit()    
    
app = Application()
app.mainloop()