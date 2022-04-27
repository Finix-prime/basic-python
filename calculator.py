from tkinter import *
import math

eq = ""
def click(num):
    global eq
    eq += str(num)
    tv1.set(eq)

def cal():
    global eq
    total = str(eval(eq))
    tv2.set(total)

def clear():
    global eq
    tv1.set("")
    tv2.set("")
    eq = ""

def per():
    global eq
    total = math.sqrt(eval(eq))
    #total = str(eval(eq)/100)
    tv2.set(total)



root = Tk()
root.title("easy calculator")
root.option_add("*Font","tahoma 30")
frame = Frame(root)
frame.pack()
tv1 = StringVar()
tv2 = StringVar()
zero = Button(frame,text="0",command=lambda : click(0))
zero.grid(column=0,row=6,columnspan=2,sticky="news")

one = Button(frame,text="1",command=lambda : click(1))
one.grid(column=0,row=5,sticky="news")

four = Button(frame,text="4",command=lambda : click(4))
four.grid(column=0,row=4,sticky="news")

seven = Button(frame,text="7",command=lambda : click(7))
seven.grid(column=0,row=3,sticky="news")

ac = Button(frame,text="AC",command= clear)
ac.grid(column=0,row=2,columnspan=2,sticky="news")

two = Button(frame,text="2",command=lambda : click(2))
two.grid(column=1,row=5,sticky="news")

five = Button(frame,text="5",command=lambda : click(5))
five.grid(column=1,row=4,sticky="news")

eight = Button(frame,text="8",command=lambda : click(8))
eight.grid(column=1,row=3,sticky="news")

dot = Button(frame,text=".",command=lambda : click("."))
dot.grid(column=2,row=6,sticky="news")

three = Button(frame,text="3",command=lambda : click(3))
three.grid(column=2,row=5,sticky="news")

six = Button(frame,text="6",command=lambda : click(6))
six.grid(column=2,row=4,sticky="news")

nine = Button(frame,text="9",command=lambda : click(9))
nine.grid(column=2,row=3,sticky="news")

percent = Button(frame,text="sqrt",command= per)
percent.grid(column=2,row=2,sticky="news")

equal = Button(frame,text="=",command= cal)
equal.grid(column=3,row=6,sticky="news")

plus = Button(frame,text="+",command=lambda : click("+"))
plus.grid(column=3,row=5,sticky="news")

minus = Button(frame,text="-",command=lambda : click("-"))
minus.grid(column=3,row=4,sticky="news")

multipile = Button(frame,text="*",command=lambda : click("*"))
multipile.grid(column=3,row=3,sticky="news")

devide = Button(frame,text="/",command=lambda : click("/"))
devide.grid(column=3,row=2,sticky="news")

screen1 = Entry(frame,state=DISABLED,textvariable=tv1)
screen1.grid(column=0,row=0,columnspan=4,sticky="news")
screen2 = Label(frame,state=DISABLED,textvariable=tv2)
screen2.grid(column=0,row=1,columnspan=4,sticky="news")


root.mainloop()
