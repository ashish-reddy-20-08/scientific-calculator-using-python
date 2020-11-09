
from tkinter import *

main=Tk()
main.title("View Help")
main.resizable(width=False, height=False)
main.geometry("800x500")

class Help:
    def __init__(self,main):
        

        

       #create text widget
        self.t=Text(main,width=70,height=30,wrap=NONE)
        for i in range(50):
            self.t.insert(END, '''
        Addition
        The addition (sum function) is used by clicking on the "+" button or using the keyboard. The function results in a+b.
        Subtraction
        The subtraction (minus function) is used by clicking on the "-" button or using the keyboard. The function results in a-b.

        Multiplication
        The multiplication (times function) is used by clicking on the "x" button or using the keyboard "*" key. The function results in a*b.

        Division
        The division (divide function) is used by clicking on the "/" button or using the keyboard "/" key. The function results in a/b.

        Sign
        The sign key (negative key) is used by clicking on the "(-)" button. The function results in -1*x.

        Square
        The square function is used by clicking on the "x^2" button or type "^2". The function results in x*x.

        Square Root
        The square root function is used by clicking on the "x" button or type "sqrt()". This function represents x^.5 where the result squared is equal to x.

        Raise to the Power
        The raise to the power (y raised to the x function) is used by clicking on the "y^x" button or type "^".

        Natural Exponential
        The natural exponential (e raised to the x) is used by clicking on the "e^x" button or type "exp()". The result is e (2.71828...) raised to x.

        Logarithm
        The logarithm (LOG) is used by clicking on the "LOG" button or type "LOG()".

        Natural Logarithm
        The Natural logarithm (LN) is used by clicking on the "LN" button or type "LN()".

        Inverse
        Multiplicative inverse (reciprocal function) is used by pressing the "1/x" button or typing "inv()". This function is the same as x^-1 or dividing 1 by the number.

        Exponent
        Numbers with exponents of 10 are displayed with an "e", for example 4.5e+100 or 4.5e-100.\n
        This function represents 10^x. Numbers are automatically displayed in the format when the number is too large or too small for the display.\n
        To enter a number in this format use the exponent key "EEX". To do this enter the mantissa (the non exponent part) then press "EEX" or type"e" and then enter the exponent.

        Factorial
        The Factorial function is used by clicking the "!" button or type "!".

        PI
        PI is a mathematical constant of the ratio of a circle's circumference to its diameter.



        Online Trigonometric Functions
        Sine
        The Sine (SIN) function is used by clicking on the "SIN" button or type "SIN()".
        The result is the ratio of the length of the opposite side to the length of the hypotenuse of a right triangle.

        Inverse Sine
        The Inverse Sine (ASIN or ARCSIN) function is used by clicking on the "ASIN" button or type "ASIN()". The result is valid only from -pi/2 to pi/2.

        Cosine
        The Cosine (COS) function is used by clicking on the "COS" button or type "COS()".
        The result is the ratio of the length of the adjacent side to the length of the hypotenuse of a right triangle.

        Inverse Cosine
        The inverse cosine (ACOS or ARCCOS) function is used by clicking on the "ACOS" button or type "ACOS()". The result is valid only from 0 to pi.
    
        Tangent
        The Tangent (TAN) function is used by clicking on the "TAN" button or type "TAN()".
        The result is the ratio of the length of the opposite side to the length of the adjacent side of a right triangle.

        Inverse Tangent
        The inverse tangent (ATAN or ARCTAN) function is used by clicking on the "ATAN" button or type "ATAN()". The result is valid only from -pi/2 to pi/2.
    
        Cosecant
        The cosecant (CSC) function is used by typing "CSC()". The cosecant is the multiplicative inverse of the sine function.

        Inverse Cosecant
        The inverse cosecant (ACSC) function is used by typing "ACSC()". The result is only valid from -pi/2 to pi/2 excluding 0.

        Secant
        The secant (SEC) function is used by typing "SEC()". The secant is the multiplicative inverse of the cosine function.

        Inverse Secant
        The inverse secant (ASEC) function is used by typing "ASEC()". The result is only valid from 0 to pi excluding pi/2.

        Cotangent
        The cotangent (COT) function is used by typing "COT()". The cotangent is the multiplicative inverse of the tangent function.

        Inverse Cotangent
        The Inverse Cotangent (ACOT) function is used by typing "ACOT()". The result is only valid from 0 to pi.

        ''')
        self.t.pack(side=TOP, fill=X)
        #create scrollbar horizontal/vertical
        self.h=Scrollbar(main, orient=HORIZONTAL, command=self.t.xview)
        #attach text to horixzontal bar
        self.t.configure(xscrollcommand=self.h.set)
        self.h.pack(side=BOTTOM, fill=X)
        self.b=Button(main, text="Back")

ob=Help(main)
main.mainloop()
