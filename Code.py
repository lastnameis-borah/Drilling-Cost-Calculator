from tkinter import *

root = Tk()
root.geometry("350x200")
root.title("Drilling cost calculator")

l1 = Label(root, text="Enter drilling time")
l1.grid(row=0, column=0)
# l1.pack()

l2 = Label(root, text="Enter bit cost")
l2.grid(row=1, column=0)

l3 = Label(root, text="Enter rig cost")
l3.grid(row=2, column=0)

l4 = Label(root, text="Enter round trip")
l4.grid(row=3, column=0)

l5 = Label(root, text="Enter footage per bit")
l5.grid(row=4, column=0)

drill_time=StringVar()
e1 = Entry(root, width=30)
e1.grid(row=0, column=1)
# e1.pack()
# e1.insert(0, "Enter drilling time")

bit_cost=StringVar()
e2 = Entry(root, width=30, textvariable=bit_cost)
e2.grid(row=1, column=1)

rig_cost=StringVar()
e3 = Entry(root, width=30, textvariable=rig_cost)
e3.grid(row=2, column=1)

round_trip=StringVar()
e4 = Entry(root, width=30, textvariable=round_trip)
e4.grid(row=3, column=1)

footage=StringVar()
e5 = Entry(root, width=30, textvariable=footage)
e5.grid(row=4, column=1)

def button():
    t=float(e1.get())
    B=float(e2.get())
    CR=float(e3.get())
    T=float(e4.get())
    F=float(e5.get())
    x=(B+CR*t+CR*T)/F
    
    f1=Label(text=x)
    f1.grid(row=5,column=1) 

b1=Button(root, text="Calculate time", command=button)
b1.grid(row=5,column=0)
# b.pack(side=BOTTOM)

root.mainloop()


