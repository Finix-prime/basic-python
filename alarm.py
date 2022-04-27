import datetime
import time
from tkinter import *
from tkinter import messagebox

tins = []
def stamp1(e):
    global tins
    e = enh.get()
    tins.append(e)
    enm.focus_set()
    print(e)

def stamp2(e):
    global tins
    e = enm.get()
    tins.append(e)
    save.focus_set()
    print(e)

def stamptime(tset):
    while True:
        global tins
        tset = datetime.datetime.today()
        print(tset)
        dnow = tset.date()
        dnowup = dnow.day+1
        alarm = tset.replace(hour=int(tins[0]),minute=int(tins[1]))
        time.sleep(1)
        if alarm < tset:
            alarm = alarm.replace(day=dnowup)
        else:
            alarm = alarm

        if tset == alarm:
            messagebox.showinfo("","Wake Up !!!!")
            break

root = Tk()
root.title("Alarm Clock")
root.option_add("*font","tahoma 20")
frame = Frame(root)
frame.pack()
hl = Label(frame,text="   Hour : Minute")
hl.grid(row=0,column=0,columnspan=2)
enh = Entry(frame,width=10)
enh.grid(row=1,column=0)
enh.bind("<Return>",stamp1)
enm = Entry(frame,width=10)
enm.grid(row=1,column=1)
enm.bind("<Return>",stamp2)
save = Button(frame,text="Save Time")
save.grid(row=2,column=0,columnspan=2)
save.bind("<Return>",stamptime)
save.bind("<Button-1>",stamptime)
enh.focus_set()
root.mainloop()
