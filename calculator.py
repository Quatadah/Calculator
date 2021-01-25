import tkinter as tk
from tkinter import messagebox
from tkinter import font
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

def modulo():
    x = ToCalculate.get()
    ToCalculate.set("{}%".format(x))

def power():
    x = ToCalculate.get()
    ToCalculate.set("{}^".format(x))

def equal():
	try:
		n1=0
		n2=0
		cursor = 0
		string = ToCalculate.get()
		
		while string[cursor]!='+' or string[cursor]!='+' or string[cursor]!='*' or string[cursor]!='/' :
			try:
				n1 += int(string[cursor])
				n1 *= 10
				cursor += 1
			except ValueError:
				break;
		n1 /= 10
		if string[cursor]=='+':
			operation = "addition"
		elif string[cursor]=='*':
			operation = "multiplication"
		elif string[cursor] == '-':
			operation = "substraction"
		elif string[cursor] == '/':
			operation = "division"
		elif string[cursor] == '%':
			operation = "modulo"
		elif string[cursor] == '^':
			operation = "power"

		cursor += 1
		while cursor<len(string):
				n2 += int(string[cursor])
				n2 *=10
				cursor +=1 
		n2/=10
		
		if operation == "addition" : 
			ToCalculate.set(int(n1+n2))
			
		elif operation== "multiplication" : 
			ToCalculat.set(int(n1*n2))
		elif operation == "substraction" :
			ToCalculate.set(int(n1-n2))
		elif operation == "division" :
			ToCalculate.set(int(n1/n2))
		elif operation == "modulo":
			ToCalculate.set(int(n1%n2))
		elif operation == "power":
			ToCalculate.set(int(n1**n2))
		else:
			return "Nothing"
	except IndexError:
		showWarning()
		
def showWarning():
	messagebox.showinfo("Warning","There is no operation yet")

def clear():
    ToCalculate.set("")


"""
def equal():
    op = []
    string = ToCalculate.get()
    for i in range(len(string)):
        try: 
            int(string[i])
        except:
            op.append(string[i])
"""
def set0():
    ToCalculate.set("{}0".format(ToCalculate.get()))


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

myFont = font.Font(family='Helvetica', size=10, weight='bold')


Welcome_msg=tk.Label(app, text="A Calculator made with Tkinter by Quatadah \n")
Welcome_msg.place(x=30,y=8)

ToCalculate = tk.StringVar()
Calculate = tk.Entry(app, textvariable=ToCalculate, width=50,borderwidth=10,bg='grey')
Calculate.place(x=0,y=30)

Button1 = tk.Button(app,text="1",width=10,height=5,command=set1,borderwidth=3,bg='white')
Button1['font']=myFont
Button1.place(x=0,y=70)

Button2 = tk.Button(app,text="2",width=10,height=5,command=set2,borderwidth=3,bg='white')
Button2['font']=myFont
Button2.place(x=80,y=70)

Button3 = tk.Button(app,text="3",width=10,height=5,command=set3,borderwidth=3,bg='white')
Button3['font']=myFont
Button3.place(x=160,y=70)

Button4 = tk.Button(app,text="4",width=10,height=5,command=set4,borderwidth=3,bg='white')
Button4['font']=myFont
Button4.place(x=0,y=155)

Button5 = tk.Button(app,text="5",width=10,height=5,command=set5,borderwidth=3,bg='white')
Button5['font']=myFont
Button5.place(x=80,y=155)

Button6 = tk.Button(app,text="6",width=10,height=5,command=set6,borderwidth=3,bg='white')
Button6['font']=myFont
Button6.place(x=160,y=155)

Button7 = tk.Button(app,text="7",width=10,height=5,command=set7,borderwidth=3,bg='white')
Button7['font']=myFont
Button7.place(x=0,y=240)

Button8 = tk.Button(app,text="8",width=10,height=5,command=set8,borderwidth=3,bg='white')
Button8['font']=myFont
Button8.place(x=80,y=240)

Button9 = tk.Button(app,text="9",width=10,height=5,command=set9,borderwidth=3,bg='white')
Button9['font']=myFont
Button9.place(x=160,y=240)

Button0 = tk.Button(app,text="0",width=10,height=4,command=set0,borderwidth=3,bg='white')
Button0['font']=myFont
Button0.place(x=0,y=325)

moduloButton = tk.Button(app, text="%",width=10,height=4,command=modulo,borderwidth=3)
moduloButton['font']=myFont
moduloButton.place(x=80,y=325)

powerButton = tk.Button(app, text="x^y",width=10,height=4, command=power, borderwidth=3)
powerButton['font']=myFont
powerButton.place(x=160,y=325)

addButton = tk.Button(app, text="+",width=10,height=4,command=add,borderwidth=3)
#addButton['font']=myFont
addButton.place(x=240,y=135)

equalButton = tk.Button(app, text="=",width=10,height=4,command=equal,borderwidth=3)
#equalButton['font']=myFont
equalButton.place(x=240,y=70)

subButton = tk.Button(app, text="-",width=10,height=4, command=substraction,borderwidth=3)
#subButton['font']=myFont
subButton.place(x=240,y=205)

divButton = tk.Button(app, text="/",width=10,height=4,command=division,borderwidth=3)
#divButton['font']=myFont
divButton.place(x=240,y=275)

clearButton = tk.Button(app, text="clear",width=10,height=3, command=clear,borderwidth=3)
#clearButton['font']=myFont
clearButton.place(x=240,y=342)

app.mainloop()
