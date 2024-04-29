#!/usr/bin/python3
#==========#
#TkWine By #
#RobiTheGit#
# 4-28-24  #
#==========#
import tkinter as tk
from tkinter import *
from tkinter.messagebox import *
from re import sub
from sys import exit
import os
from tkinter.filedialog import *
global Shortcuts, Shortcut_File, ShortCut_List
Shortcut_File = open("shortcuts.csv", 'r') # We'll open this for write at times too
Shortcuts = {}
ShortCut_List = []
root = Tk(className="TkWine")

def Mk_List(Data, Dict, List):
    Data_Tmp = Data.readlines()
    res = []
    [res.append(x) for x in Data_Tmp if x not in res]
    for x in range(len(res)):
        List.append((res[x].split('\n'))[0])
    for x in range(len(List)):
        dataitem = List[x].split(',')
        for y in range(len(dataitem)):
            Dict[x] = List[x].split(',')
            Dict[x][y] = dataitem[y]
    print(Dict)

class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
    global ShortcutsFrame, Dsp_Entr, FP_Entr, Args_Entr
    ShortcutsFrame = Frame(root, relief=RIDGE, bd=1)
    ShortcutsFrame.pack(side = LEFT, fill=Y)
    Main = Frame(root, relief=RIDGE, bd=1)
    Main.pack(fill=BOTH, side=TOP)

    Label(Main, text='\n\n').pack()
     # Add a text input for Disp. Name
    Label(Main, text='Display Name').pack()
    Dsp_Entr = Entry(Main)
    contents = StringVar()
    contents.set("")
    Dsp_Entr["textvariable"] = contents
    Dsp_Entr.pack()
    # Add a text input for filepath
    Label(Main, text='Filepath').pack()
    FP_Entr = Entry(Main)
    contents2 = StringVar()
    contents2.set("")
    FP_Entr["textvariable"] = contents2
    FP_Entr.pack()
    # Add a Text input for arguments
    Label(Main, text='Arguments').pack()
    Args_Entr = Entry(Main)
    contents2 = StringVar()
    contents2.set("")
    Args_Entr["textvariable"] = contents2
    Args_Entr.pack()

    def make_Btn():
        Mk_List(Shortcut_File, Shortcuts, ShortCut_List)
        for widget in ShortcutsFrame.winfo_children():
            widget.destroy()
        Label(ShortcutsFrame, text='').pack()
        global y, names
        names = []
        for y in Shortcuts:
            c = str(Shortcuts[y][1])
            names.append(c)
            Button(ShortcutsFrame, text=Shortcuts[y][0], command=lambda j=c : os.popen(f"wine {Shortcuts[names.index(j)][1]}") ).pack()

    # Add "Run" button
    Run = Button(Main, text="Run With Wine", command=lambda:os.popen(f'wine {FP_Entr.get()} {Args_Entr.get()}') ).pack(side = LEFT)
    make_Btn()

    def make_ShortCut():
        DispName = Dsp_Entr.get()
        Filepath = FP_Entr.get()
        Args = Args_Entr.get()
        f = open("shortcuts.csv", 'a')
        f.write(f'{DispName},{Filepath},{Args}\n')
        f.close()
        Mk_List(Shortcut_File, Shortcuts, ShortCut_List)
        for widget in ShortcutsFrame.winfo_children():
            widget.destroy()
        Label(ShortcutsFrame, text='ShortcutsFrame').pack()
        global y, names
        names = []
        for y in Shortcuts:
            c = str(Shortcuts[y][1])
            names.append(c)
            Button(ShortcutsFrame, text=Shortcuts[y][0], command=lambda j=c : os.popen(f"wine {Shortcuts[names.index(j)][1]}") ).pack()

    # Add "Add Shortcut" button
    Add_Shortcut = Button(Main, text="Add Shortcut", command=make_ShortCut).pack(side = LEFT)





root.geometry("900x500")
root.resizable(True,True)
myapp = App(root)
myapp.master.title("Tkinter Wine Frontend")
myapp.mainloop()
