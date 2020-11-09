from tkinter import *
import math
from tkinter import messagebox
import pygame    # it is downloaded by using 
import time
import os


root=Tk()
root.title("Scientific Calculator")
root.configure(background="powder blue")
root.resizable(width=False,height=False)
root.geometry("964x565")

file='SC Voice.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.set_volume(5)
pygame.mixer.music.play()


calc=Frame(root)
calc.grid()

class Calc():
    def __init__(self):
        self.total = 0
        self.current =""
        self.input_value =True
        self.check_sum = False
        self.op=""
        self.result=False
    def numberEnter(self, num):
        self.result =False
        firstnum  = txtDisplay.get()
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
        file = open('History.txt','a')
        file.write(txtDisplay.get() +'\n')
    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

        file = open('History.txt','a')
        file.write(txtDisplay.get() +'\n')

    def display(self, value):
        txtDisplay.delete(0,END)
        txtDisplay.insert(0,value)
        
    def valid_function(self):
        if self.op=="add":
            self.total+=self.current
        if self.op=="sub":
            self.total-=self.current
        if self.op=="mul":
            self.total*=self.current
        if self.op=="div":
            self.total/=self.current    
        if self.op=="mod":
            self.total%=self.current
        if self.op=="inv":
            self.total=1/self.current
        self.input_value=True
        self.check_sum=False
        self.display(self.total)
        
    def operation(self,op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False
        
    def Clear_Entry(self):
        self.esult = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    
    
    def all_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0

    def mathsPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt (float(txtDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(math.log(float(txtDisplay.get())))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)
        
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

    def acosh(self):
        self.result = False
        self.current = math.acosh(float(txtDisplay.get()))
        self.display(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(float(txtDisplay.get()))
        self.display(self.current)


    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(float(txtDisplay.get()))
        self.display(self.current)

    def factorial(self):
        self.reuslt= False
        self.current = math.factorial(float(txtDisplay.get()))
        self.display(self.current)
    def power(self):
        self.result = False
        self.current = math.pow(float(txtDisplay.get()))
        self.display(self.current)

        
added_value = Calc()

txtDisplay = Entry(calc, font=('arial', 20, 'bold'),bg="powder blue",
                   bd=30, width=29, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0,"0")
        
numberpad="789456123"
i=0
btn=[]
for j in range(2,5):
    for k in range (3):
        btn.append(Button(calc, width=6, height=2, font=('arial', 20, 'bold'),
                          bd=4, text=numberpad[i]))
        btn[i].grid(row=j, column=k,pady=1)
        btn[i]["command"]= lambda x = numberpad [i]: added_value.numberEnter(x)
        i +=1

#=======================================================Standard calc Buttons===============
btnClear= Button(calc, text=chr(67), width=6 ,height=2, font=('arial', 20, 'bold'),
                bd=4,bg="powderblue",command= added_value.Clear_Entry).grid(row=1, column=0,pady=1)
btnAllClear= Button(calc, text="AC", width=6 ,height=2, font=('arial', 20, 'bold'),
                bd=4,bg="powderblue",command= added_value.all_Clear_Entry).grid(row=1, column=1,pady=1)

btnSq= Button(calc, text="\u221A", width=6 ,height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="powderblue",command=added_value.squared).grid(row=1, column=2,pady=1)
btnAdd= Button(calc, text="\u002B", width=6 ,height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="powderblue",command = lambda: added_value.operation("add")).grid(row=1, column=3,pady=1) 

btnSub= Button(calc, text="\u2212", width=6 ,height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="powderblue",command = lambda: added_value.operation("sub")).grid(row=2, column=3,pady=1)
btnMul= Button(calc, text="\u2715", width=6 ,height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="powderblue",command = lambda: added_value.operation("mul")).grid(row=3, column=3,pady=1)
btnDiv= Button(calc, text="\u00F7", width=6 ,height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="powderblue",command = lambda: added_value.operation("div")).grid(row=4, column=3,pady=1)


btnZero= Button(calc, text="0", width=6 ,height=2, font=('arial', 20, 'bold'),
                bd=4, command = lambda: added_value.numberEnter(0)).grid(row=5, column=1,pady=1) 

btn2Zero= Button(calc, text="00", width=6 ,height=2, font=('arial', 20, 'bold'),
                bd=4, command = lambda: added_value.numberEnter(00)).grid(row=5, column=0,pady=1) 


btnDot= Button(calc, text="\u2022", width=6 ,height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="powderblue",command = lambda: added_value.numberEnter(".")).grid(row=5, column=2,pady=1)
btnpm= Button(calc, text="\u00B1", width=6 ,height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="powderblue",command =added_value.mathsPM).grid(row=5, column=4,pady=1)
btnEquals= Button(calc, text="=", width=6 ,height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="powderblue",command= added_value.sum_of_total).grid(row=5, column=3,pady=1)

#=============================Scientific Calc buttons=======================================

btnpi= Button(calc, text="\u03C0", width=6 ,height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="powderblue",command =added_value.pi).grid(row=1, column=4,pady=1)
btnCos= Button(calc, text="Cos", width=6 ,height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="powderblue",command =added_value.cos).grid(row=1, column=5,pady=1)

btntan= Button(calc, text="Tan", width=6 ,height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="powderblue",command =added_value.tan).grid(row=1, column=6,pady=1)
btnsin= Button(calc, text="Sin", width=6 ,height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="powderblue",command =added_value.sin).grid(row=1, column=7,pady=1) 
#===========================================================================================
btn2pi= Button(calc, text="2\u03C0", width=6 ,height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="powderblue",command =added_value.tau).grid(row=2, column=4,pady=1)
btncosh= Button(calc, text="Cosh", width=6 ,height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="powderblue",command =added_value.cosh).grid(row=2, column=5,pady=1)
btntanh= Button(calc, text="Tanh", width=6 ,height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="powderblue",command =added_value.tanh).grid(row=2, column=6,pady=1)
btnsinh= Button(calc, text="Sinh", width=6 ,height=2, font=('arial', 20, 'bold'), bd=4,
                bg="powderblue",command =added_value.sinh).grid(row=2, column=7,pady=1) 

#===========================================================================================
btnlog= Button(calc, text="log", width=6 ,height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="powderblue",command =added_value.log).grid(row=3, column=4,pady=1)
btnexp= Button(calc, text="Exp", width=6 ,height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="powderblue",command =added_value.exp).grid(row=3, column=5,pady=1)
btnmod= Button(calc, text="Mod", width=6 ,height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="powderblue").grid(row=3, column=6,pady=1)
btnE= Button(calc, text="e", width=6 ,height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="powderblue",command =added_value.e).grid(row=3, column=7,pady=1)

#===========================================================================================
btnfactorial= Button(calc, text="n!", width=6 ,height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="powderblue",command =added_value.factorial).grid(row=4, column=4,pady=1)
btndeg= Button(calc, text="deg\u00B0", width=6 ,height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="powderblue",command =added_value.degrees).grid(row=4, column=5,pady=1)
btnacosh= Button(calc, text="aCosh", width=6 ,height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="powderblue",command =added_value.acosh).grid(row=4, column=6,pady=1)
btnasinh= Button(calc, text="aSinh", width=6 ,height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="powderblue",command =added_value.asinh).grid(row=4, column=7,pady=1)

#===========================================================================================
btnlog10= Button(calc, text="log10", width=6 ,height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="powderblue",command =added_value.log10).grid(row=5, column=6,pady=1)
btncos= Button(calc, text="Cos", width=6 ,height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="powderblue",command =added_value.cos).grid(row=5, column=5,pady=1)

btnsqauring= Button(calc, text="x²", width=6 ,height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="powderblue",command =added_value.power).grid(row=5, column=7,pady=0)

lblDisplay=Label(calc, text="Scientific Calculator", font=('arial', 20, 'bold'), justify=CENTER)
lblDisplay.grid(row=0,column=4, columnspan=4)

lb2Display=Label(calc, text="Standard Calculator", font=('arial', 30, 'bold'), justify =CENTER)
lb2Display.grid(row=6, column=0, columnspan=4)
#===================================Menu and function=======================================
def iExit():
    file='58827708.mp3'
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_volume(5)
    pygame.mixer.music.play()
    ans = messagebox.askyesnocancel('History', 'Do you want to clear the history?')
    if ans:
        file = open('History.txt', 'w')
        file.close()
    elif ans == None:
        pass
    else:
        pass
#       file = open('History.txt', 'r')
#       file.close()
    iExit= messagebox.askyesno("Scientific Calculator", "Conform if you want to exit..")
    if iExit == 0:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.pause()
        root.destroy()
        return
def Scientific():
    root.resizable(width=False,height=False)
    root.geometry("966x560")

    file='SC Voice.mp3'
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_volume(5)
    pygame.mixer.music.play()

def Standard():
    root.resizable(width=False,height=False)
    root.geometry("490x620")

    file='St.mp3'
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_volume(5)
    pygame.mixer.music.play()

def clr_history():
    file = open('History.txt', 'w')
    file.close()
    messagebox._show('History',"History Cleared..")
    

def history():
    his=open("History.txt", 'r')
    i=his.read()
    if i=='':
        messagebox._show('History', "No History Found")
        print('No History Found')
    else:
        his=open("History.txt", 'r')
        messagebox._show('History',his.read())
        his=open("History.txt", 'r')
        print('History',"\n", his.read())

def Viewhelp():
    os.system('help.py')
        
def feedback():
    rp=Tk()
    rp.resizable(width=False, height=False)
    rp.geometry("300x100")
    rp.title('FeedBack')
    
    file='fb.mp3'
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_volume(5)
    pygame.mixer.music.play()
    def abcd():
        feedback=text.get()
        
        #f=open("Feedback.txt","w")
        file=open("F_B_.txt","a")
        file.write("\nFeedback Received:" +feedback)        
        file.close()

        file='tnk.mp3'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.set_volume(5)
        pygame.mixer.music.play()
        
        rp.destroy()
        
    f=("Times",18,"bold italic underline")
    Label(rp,text="Please Give your Feedback", font=f).grid(row=1,column=1)
    text= StringVar()
    F_B=Entry(rp,textvariable=text).grid(row=2, column=1)
    Button(rp,text='Submit',width=5,height=1,bg="grey",
           activebackground="cyan",command=abcd).grid(row=3, column=1)

    rp.mainloop()
    
#==================================================Menu bar Creation ==========================================================

menubar=Menu(calc)

modemenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label="Mode", menu=modemenu)
modemenu.add_radiobutton(label="Standard",command= Standard)
modemenu.add_radiobutton(label="Scientific",command=Scientific)

editmenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Cut       Ctrl + X")
editmenu.add_command(label="Copy    Ctrl + C")
editmenu.add_separator()
editmenu.add_command(label="Paste    Ctrl + V")

helpmenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="View Help",command=Viewhelp)

feedbackmenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label="Feedback",command=feedback)

historymenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label="History", menu=historymenu)
historymenu.add_command(label="View History", command=history)
historymenu.add_command(label="Clear History", command=clr_history)

exitmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Exit", menu=exitmenu)
exitmenu.add_command(label="Exit",command= iExit)

root.config(menu=menubar)
root.mainloop()
