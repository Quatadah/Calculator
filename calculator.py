import tkinter as tk
import time

def add():
    x = ToCalculate.get()
    ToCalculate.set("{}+".format(x))


def multiplication():
    x = ToCalculate.get()
    ToCalculate.set("{}*".format(x))


def substraction():
    x = ToCalculate.get()
    ToCalculate.set("{}-".format(x))


def division():
    x = ToCalculate.get()
    ToCalculate.set("{}/".format(x))
"""
def equal():
    n1=0
    n2=0
    cursor = 0
    string = ToCalculate.get()
    
    while string[cursor]!='+' or string[cursor]!='+' or string[cursor]!='*' or string[cursor]!='/':
        try:
            n1 += int(string[cursor])
            n1 *= 10
            cursor += 1
        except ValueError:
            break;
    n1 /= 10
    print(n1)
    if string[cursor]=='+':
        operation = "addition"
    elif string[cursor]=='*':
        operation = "multiplication"
    elif string[cursor] == '-':
        operation = "substraction"
    elif string[cursor] == '/':
        operation = "division"

    cursor += 1
    while cursor<len(string):
            n2 += int(string[cursor])
            n2 *=10
            cursor +=1 
    n2/=10
    
    if operation == "addition" : 
        ToCalculate.set(str(n1+n2))
        
    elif operation== "multiplication" : 
        ToCalculat.set(n1*n2)
    elif operation == "substraction" :
        ToCalculate.set(n1-n2)
    elif operation == "division" :
        ToCalculate.set(n1/n2)
    else:
        return "Nothing"
"""

def equal():
    op = []
    string = ToCalculate.get()
    for i in range(len(string)):
        try: 
            int(string[i])
        except:
            op.append(string[i])
    



def set1():
    ToCalculate.set("{}1".format(ToCalculate.get()))

def set2():
    ToCalculate.set("{}2".format(ToCalculate.get()))

def set3():
    ToCalculate.set("{}3".format(ToCalculate.get()))

def set4():
    ToCalculate.set("{}4".format(ToCalculate.get()))

def set5():
    ToCalculate.set("{}5".format(ToCalculate.get()))

def set6():
    ToCalculate.set("{}6".format(ToCalculate.get()))

def set7():
    ToCalculate.set("{}7".format(ToCalculate.get()))

def set8():
    ToCalculate.set("{}8".format(ToCalculate.get()))

def set9():
    ToCalculate.set("{}9".format(ToCalculate.get()))

app = tk.Tk()
app.geometry("320x400")
app.title("Calculator v 1.0")

Welcome_msg=tk.Label(app, text="A Calculator made with Tkinter by Quatadah \n")
Welcome_msg.place(x=30,y=8)

ToCalculate = tk.StringVar()
Calculate = tk.Entry(app, textvariable=ToCalculate, width=50,borderwidth=10)
Calculate.place(x=0,y=30)

Button1 = tk.Button(app,text="1",width=10,height=5,command=set1)
Button1.place(x=0,y=70)
Button2 = tk.Button(app,text="2",width=10,height=5,command=set2)
Button2.place(x=80,y=70)
Button3 = tk.Button(app,text="3",width=10,height=5,command=set3)
Button3.place(x=160,y=70)
Button4 = tk.Button(app,text="4",width=10,height=5,command=set4)
Button4.place(x=0,y=155)
Button5 = tk.Button(app,text="5",width=10,height=5,command=set5)
Button5.place(x=80,y=155)
Button6 = tk.Button(app,text="6",width=10,height=5,command=set6)
Button6.place(x=160,y=155)
Button7 = tk.Button(app,text="7",width=10,height=5,command=set7)
Button7.place(x=0,y=240)
Button8 = tk.Button(app,text="8",width=10,height=5,command=set8)
Button8.place(x=80,y=240)
Button9 = tk.Button(app,text="9",width=10,height=5,command=set9)
Button9.place(x=160,y=240)


addButton = tk.Button(app, text="+",width=10,height=4,command=add)
addButton.place(x=240,y=138)

equalButton = tk.Button(app, text="=",width=10,height=4,command=equal)
equalButton.place(x=240,y=70)

subButton = tk.Button(app, text="-",width=10,height=4, command=substraction)
subButton.place(x=240,y=206)

app.mainloop()