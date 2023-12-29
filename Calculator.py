from tkinter import*

def btnClick(number):
    global val
    val=val+str(number)
    data.set(val)

def btnClear():
    global val
    val=""
    data.set("")

def btnEquals():
    global val
    result=str(eval(val))
    data.set(result)

def backspace():
    global val
    val = val[:-1]
    data.set(val)

cal = Tk()
cal.title("Calculator")
cal.configure(bg="#17161b")
val=""
data=StringVar()

Display=Entry(cal,font=('arial',20,'bold'),textvariable=data,bd=20,insertwidth=3,
              bg="grey",justify='right').grid(columnspan=4)

Button(cal,text="C",width=4, height=0, font=("arial",20,"bold"),bd=1,fg="#fff",bg="peachpuff",command=btnClear).grid(row=1,column=0)
Button(cal,text="",width=4, height=0, font=("arial",20,"bold"),bd=1,fg="#fff",bg="peachpuff",command=backspace).grid(row=1,column=1)
Button(cal,text="±",width=4, height=0, font=("arial",20,"bold"),bd=1,fg="#fff",bg="peachpuff",command=lambda:btnClick('±')).grid(row=1,column=2)
Button(cal,text="÷",width=4, height=0, font=("arial",20,"bold"),bd=1,fg="#fff",bg="peachpuff",command=lambda:btnClick('÷')).grid(row=1,column=3)

Button(cal,text="7",width=4, height=0, font=("arial",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:btnClick(7)).grid(row=2,column=0)
Button(cal,text="8",width=4, height=0, font=("arial",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:btnClick(8)).grid(row=2,column=1)
Button(cal,text="9",width=4, height=0, font=("arial",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:btnClick(9)).grid(row=2,column=2)
Button(cal,text="*",width=4, height=0, font=("arial",20,"bold"),bd=1,fg="#fff",bg="peachpuff",command=lambda:btnClick('*')).grid(row=2,column=3)

Button(cal,text="4",width=4, height=0, font=("arial",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:btnClick(4)).grid(row=3,column=0)
Button(cal,text="5",width=4, height=0, font=("arial",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:btnClick(5)).grid(row=3,column=1)
Button(cal,text="6",width=4, height=0, font=("arial",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:btnClick(6)).grid(row=3,column=2)
Button(cal,text="-",width=4, height=0, font=("arial",20,"bold"),bd=1,fg="#fff",bg="peachpuff",command=lambda:btnClick('-')).grid(row=3,column=3)

Button(cal,text="1",width=4, height=0, font=("arial",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:btnClick(1)).grid(row=4,column=0)
Button(cal,text="2",width=4, height=0, font=("arial",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:btnClick(2)).grid(row=4,column=1)
Button(cal,text="3",width=4, height=0, font=("arial",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:btnClick(3)).grid(row=4,column=2)
Button(cal,text="+",width=4, height=0, font=("arial",20,"bold"),bd=1,fg="#fff",bg="peachpuff",command=lambda:btnClick('+')).grid(row=4,column=3)

Button(cal,text="%",width=4, height=0, font=("arial",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:btnClick('%')).grid(row=5,column=0)
Button(cal,text="0",width=4, height=0, font=("arial",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:btnClick(0)).grid(row=5,column=1)
Button(cal,text=".",width=4, height=0, font=("arial",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:btnClick('.')).grid(row=5,column=2)
Button(cal,text="=",width=4, height=0, font=("arial",20,"bold"),bd=1,fg="#fff",bg="peachpuff",command=btnEquals).grid(row=5,column=3)
       
cal.mainloop()

