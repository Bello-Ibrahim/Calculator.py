from cmath import cos
from tkinter import*
import math
import parser
import tkinter.messagebox

cal = Tk()
cal.title("Scientific Calculator")
cal.configure(background = "powder blue")
cal.resizable(width = False, height = False)
cal.geometry("480x568+0+0")

calc = Frame(cal)
calc.grid()

class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False
    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def clearEntry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def clearAll(self):
        self.clearEntry()
        self.total = 0

    def mathsPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(txtDisplay.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(float(txtDisplay.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)

    def expm1(self):
        self.result = False
        self.current = math.expm1(float(txtDisplay.get()))
        self.display(self.current)

    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(txtDisplay.get()))
        self.display(self.current)

    def acosh(self):
        self.result = False
        self.current =math.acosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def deg(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)
added_value = Calc()

txtDisplay = Entry(calc, font = ("Arial", 18, "bold"), bg = "powder blue", bd = 30, width = 28, justify = RIGHT)
txtDisplay.grid(row = 0, column = 0, columnspan = 4, pady = 1)
txtDisplay.insert(0, "0")

numpad = "789456123"
i = 0
button = []
for p in range(2,5):
    for q in range(3):
        button.append(Button(calc, width = 6, height = 2, font = ("Arial", 18, "bold"), bd = 4, text = numpad[i]))
        button[i].grid(row = p, column = q, pady = 1)
        button[i]["command"] = lambda x = numpad [i]:added_value.numberEnter(x)
        i += 1
#*****************************#*************************#**********************
clrbutton = Button(calc, text=chr(67), width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = added_value.clearEntry).grid(row=1, column=0, pady=1)
clrAllbutton = Button(calc, text=chr(67) + chr(69), width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = added_value.clearAll).grid(row=1, column=1, pady=1)

sqrbutton = Button(calc, text="√", width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = added_value.squared).grid(row=1, column=2, pady=1)
addbutton = Button(calc, text="+", width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = lambda: added_value.operation("add")).grid(row=1, column=3, pady=1)
subtrbutton = Button(calc, text="-", width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = lambda: added_value.operation("sub")).grid(row=2, column=3, pady=1)
multibutton = Button(calc, text="x", width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = lambda: added_value.operation("multi")).grid(row=3, column=3, pady=1)
divbutton = Button(calc, text=chr(247), width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = lambda: added_value.operation("divide")).grid(row=4, column=3, pady=1)

zerobutton = Button(calc, text="0", width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = lambda: added_value.numberEnter(0)).grid(row=5, column=0, pady=1)
decbutton = Button(calc, text=".", width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = lambda: added_value.numberEnter(".")).grid(row=5, column=1, pady=1)
PMbutton = Button(calc, text=chr(177), width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = added_value.mathsPM).grid(row=5, column=2, pady=1)
equalbutton = Button(calc, text="=", width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = added_value.sum_of_total).grid(row=5, column=3, pady=1)
#*************************Scientific Calculator*******************************
pibutton = Button(calc, text="n", width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = added_value.pi).grid(row=1, column=4, pady=1)

cosbutton = Button(calc, text="cos", width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = added_value.cos).grid(row=1, column=5, pady=1)

tanbutton = Button(calc, text="tan", width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = added_value.tan).grid(row=1, column=6, pady=1)

sinbutton = Button(calc, text="sin", width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = added_value.sin).grid(row=1, column=7, pady=1)
#******************************************************************************
pi2button = Button(calc, text="2n", width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = added_value.tau).grid(row=2, column=4, pady=1)

coshbutton = Button(calc, text="cosh", width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = added_value.cosh).grid(row=2, column=5, pady=1)

tanhbutton = Button(calc, text="tanh", width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = added_value.tanh).grid(row=2, column=6, pady=1)

sinhbutton = Button(calc, text="sinh", width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = added_value.sinh).grid(row=2, column=7, pady=1)
#*************************************************************************************
logbutton = Button(calc, text="log", width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = added_value.log).grid(row=3, column=4, pady=1)

expbutton = Button(calc, text="Exp", width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = added_value.exp).grid(row=3, column=5, pady=1)

modbutton = Button(calc, text="Mod", width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = lambda: added_value.operation("mod")).grid(row=3, column=6, pady=1)

Ebutton = Button(calc, text="e", width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = added_value.e).grid(row=3, column=7, pady=1)
#*****************************************************************************************
log2button = Button(calc, text="log2", width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = added_value.log2).grid(row=4, column=4, pady=1)

degbutton = Button(calc, text="deg", width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = added_value.deg).grid(row=4, column=5, pady=1)

acoshbutton = Button(calc, text="acosh", width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = added_value.acosh).grid(row=4, column=6, pady=1)

asinhbutton = Button(calc, text="asinh", width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = added_value.asinh).grid(row=4, column=7, pady=1)
#*********************************************************************************************
log10button = Button(calc, text="log10", width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = added_value.log10).grid(row=5, column=4, pady=1)

Cosbutton = Button(calc, text="loglp", width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = added_value.log1p).grid(row=5, column=5, pady=1)

expm1button = Button(calc, text="expm1", width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = added_value.expm1).grid(row=5, column=6, pady=1)

lgammabutton = Button(calc, text="lgamma", width=6, height = 2, font = ("Arial", 18, "bold"),bd = 4, bg = "powder blue", command = added_value.lgamma).grid(row=5, column=7, pady=1)

displabel = Label(calc, text="Scientific Calculator", font = ("Arial", 30, "bold"), justify=CENTER)
displabel.grid(row = 0, column = 4, columnspan = 4)
#**********************Menu and Function***************************************
def iClose(): 
    iClose = tkinter.messagebox.askyesno("Scientific Calculator", "confirm, if yes")
    if iClose > 0:
        cal.destroy()
        return

def scientific():
    cal.resizable(width = False, height = False)
    cal.geometry("944x568+0+0")

def normal():
    cal.resizable(width = False, height = False)
    cal.geometry("480x568+0+0")

menubar = Menu(calc)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "Normal", command = normal)
filemenu.add_command(label = "Scientific", command = scientific)
filemenu.add_separator()
filemenu.add_command(label = "Close", command = iClose)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Edit", menu = editmenu)
editmenu.add_command(label = "Cut")
editmenu.add_command(label = "Copy")
editmenu.add_separator()
editmenu.add_command(label = "Paste")

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Help", menu = helpmenu)
helpmenu.add_command(label = "View Help")

cal.config(menu = menubar)
cal.mainloop()




