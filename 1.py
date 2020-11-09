import tkinter as tk


LARGE_FONT= ("Verdana", 19)
SMALL_FONT= ("Times", 14)
BIG_FONT= ("Times", 25)


class python(tk.Tk):   

    def __init__(self, *args, **kwargs):    #__init__ function for class python
        
        tk.Tk.__init__(self, *args, **kwargs)    #__init__ function for class TK
        container = tk.Frame(self)   #creating a container

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}     #setting frames to an empty array

        for F in (subjectPage, maths, science, real_numbers, hcf_lcm, poly_, deg_poly, typ_poly_on_terms,typ_poly_on_deg,metals_non_metals,our_envir,elec):

            frame = F(container, self)

            self.frames[F] = frame   #iterating a tuple consisting of pagelayouts

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(subjectPage)
    def show_frame(self, cont):

        frame = self.frames[cont]   #displaying current frame passed as parameter
        frame.tkraise()

        
class subjectPage(tk.Frame):    #first window frame subjectpage

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Welcome to Class 10 CBSE", font=LARGE_FONT)
        label.pack(pady=10,padx=10)   #labeling the text
        
        label = tk.Label(self, text="Select your Subject:", font=LARGE_FONT)
        label.pack(pady=15,padx=5)
 #assigning buttons in subjet page to switch to the chapter page       
        button = tk.Button(self, text="MATHEMATICS",  
                            command=lambda: controller.show_frame(maths))
        button.pack()

        button2 = tk.Button(self, text="SCIENCE",
                            command=lambda: controller.show_frame(science))
        button2.pack()

class maths(tk.Frame):   #for chapters in maths window

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="MATHEMATICS", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        label = tk.Label(self, text="Select chapter", font=LARGE_FONT)
        label.pack(pady=15,padx=5)

        button1 = tk.Button(self, text="Real Numbers", #assigning buttons for topics to move into another windows
                            command=lambda: controller.show_frame(real_numbers))
        button1.pack()

        button2 = tk.Button(self, text="Polynomials",
                            command=lambda: controller.show_frame(poly_))
        button2.pack()
        
        button3 = tk.Button(self, text="Back to subjects",
                            command=lambda: controller.show_frame(subjectPage))
        button3.pack()


class science(tk.Frame):

    def __init__(self, parent, controller):     #__init__ function for function science
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="SCIENCE", font=LARGE_FONT)
        label.pack(pady=10,padx=10)                 #labeling the text
        
        label = tk.Label(self, text="select chapter:", font=LARGE_FONT)
        label.pack(pady=15,padx=5)

        button1 = tk.Button(self, text="Metals and Non-metals",    #assigning buttons to move into another windows
                            command=lambda: controller.show_frame(metals_non_metals))
        button1.pack()

        button2 = tk.Button(self, text="Our Environment",
                            command=lambda: controller.show_frame(our_envir))
        button2.pack()
        
        button3 = tk.Button(self, text="Back to subjects",
                            command=lambda: controller.show_frame(elec))
        button3.pack()
        
        button3 = tk.Button(self, text="Back to subjects",
                            command=lambda: controller.show_frame(subjectPage))
        button3.pack()
        
class real_numbers(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Real Numbers", font=BIG_FONT)
        label.pack(pady=10,padx=10)
        
        label = tk.Label(self, text="Select topic", font=LARGE_FONT)
        label.pack(pady=15,padx=5)

        button1 = tk.Button(self, text="Highest Common Factor",
                            command=lambda: controller.show_frame(hcf_lcm))
        button1.pack()
        
        button2 = tk.Button(self, text="Least Common Multiple",
                            command=lambda: controller.show_frame(hcf_lcm))
        button2.pack()
        
        button3 = tk.Button(self, text="Back to subjects",
                            command=lambda: controller.show_frame(subjectPage))
        button3.pack()
        
class hcf_lcm(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Highest Common Factor:-", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        label = tk.Label(self, text="HCF defines the greatest factor present in between given two or more numbers\nfor example:-", font=SMALL_FONT)
        label.pack(pady=14,padx=5)
    
        label = tk.Label(self, text=" For example, take 8 and 12. The H.C.F. of 8 and 12 will be 4 because the highest number that can divide both 8 and 12 is 4", font=SMALL_FONT)
        label.pack(pady=17,padx=5)
        
        label = tk.Label(self, text="Least Common Multiple:-", font=LARGE_FONT)
        label.pack(pady=21,padx=10)
        
        label = tk.Label(self, text="LCM defines least number which is exactly divisible by two or more numbers\nfor example:-", font=SMALL_FONT)
        label.pack(pady=23,padx=5)
        
        label = tk.Label(self, text="let us take positive integers 4 and 6.The common multiples for 4 and 6 are 12,24,36,48…and so on. The least common multiple in that lot would be 12.", font=SMALL_FONT)
        label.pack(pady=25,padx=5)
        
        button1 = tk.Button(self, text="Back to Topics",
                            command=lambda: controller.show_frame(real_numbers))
        button1.pack()
        
        button2 = tk.Button(self, text="Back to Subject Page",
                            command=lambda: controller.show_frame(subjectPage))
        button2.pack()
        
        
class poly_(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Polynomials:-", font=BIG_FONT)
        label.pack(pady=10,padx=10)
        
        label = tk.Label(self, text="The propeties of polynomials includes :", font=SMALL_FONT)
        label.pack(pady=12,padx=5)
        
        button1 = tk.Button(self, text="Degree of a Polynomial",
                            command=lambda: controller.show_frame(deg_poly))
        button1.pack()
        
        button2 = tk.Button(self, text="Types of Polynomial based on number of terms",
                            command=lambda: controller.show_frame(typ_poly_on_terms))
        button2.pack()
        
        button3 = tk.Button(self, text="Types of polynomials based on degree",
                            command=lambda: controller.show_frame(typ_poly_on_deg))
        button3.pack()
        
        button1 = tk.Button(self, text="Back to Topics",
                            command=lambda: controller.show_frame(poly_))
        button1.pack()
        
        button2 = tk.Button(self, text="Back to Subject Page",
                            command=lambda: controller.show_frame(subjectPage))
        button2.pack()
        
class deg_poly(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Degree of Polynomial:-", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        label = tk.Label(self, text="For a polynomial in one variable – the highest exponent on the variable in a polynomial is the degree of the polynomial.", font=SMALL_FONT)
        label.pack(pady=12,padx=5)
        
        label = tk.Label(self, text="for example:-", font=LARGE_FONT)
        label.pack(pady=13,padx=5)
        
        label = tk.Label(self, text=" The degree of the polynomial x2+2x+3 is 2, as the highest power of x in the given expression is x2.", font=LARGE_FONT)
        label.pack(pady=14,padx=5)
        
        button1 = tk.Button(self, text="Back to Topics",
                            command=lambda: controller.show_frame(poly_))
        button1.pack()
        
        button2 = tk.Button(self, text="Back to Subject Page",
                            command=lambda: controller.show_frame(subjectPage))
        button2.pack()
        
        button2 = tk.Button(self, text="Back to Polynomials",
                            command=lambda: controller.show_frame(poly_))
        button2.pack()
        
class typ_poly_on_terms(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Types of polynomial based on number of terms:-", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        label = tk.Label(self, text="a) Monomial – A polynomial with just one term\n b) Binomial – A polynomial with two terms \n c)Trinomial – A polynomial with three terms", font=SMALL_FONT)
        label.pack(pady=12,padx=5)
        
        label = tk.Label(self, text="for example :- Monomial=2x,6xy\n binomial=5x+4\n trinomial=x^2+3x+4", font=SMALL_FONT)
        label.pack(pady=13,padx=5)
        
        button1 = tk.Button(self, text="Back to Topics",
                            command=lambda: controller.show_frame(poly_))
        button1.pack()
        
        button2 = tk.Button(self, text="Back to Subject Page",
                            command=lambda: controller.show_frame(subjectPage))
        button2.pack()
        
        button2 = tk.Button(self, text="Back to Properties",
                            command=lambda: controller.show_frame(poly_))
        button2.pack()
        
class typ_poly_on_deg(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Types of polynomials based on degree:-", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        label = tk.Label(self, text="A polynomial whose degree is one is called a linear polynomial\nA polynomial of degree two is called a quadratic polynomial", font=SMALL_FONT)
        label.pack(pady=13,padx=5)
        
        label = tk.Label(self, text=" 2x+1 is a linear polynomial.\n 3x2+8x+5 is a quadratic polynomial.", font=SMALL_FONT)
        label.pack(pady=14,padx=5)
        
        button1 = tk.Button(self, text="Back to Topics",
                            command=lambda: controller.show_frame(poly_))
        button1.pack()
        
        button2 = tk.Button(self, text="Back to Subject Page",
                            command=lambda: controller.show_frame(subjectPage))
        button2.pack()
        
        button2 = tk.Button(self, text="Back to Properties",
                            command=lambda: controller.show_frame(poly_))
        button2.pack()
        

        
        
class metals_non_metals(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Metals and non metals \n ", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        label = tk.Label(self, text="Metals: Metals are solids which passes electricity and have properties of conductivity etc..,   ", font=SMALL_FONT)
        label.pack(pady=12,padx=5)
        
        label = tk.Label(self, text="Non Metals:a nonmetal (or non-metal) is a chemical element that mostly lacks the characteristics of a metal. ", font=SMALL_FONT)
        label.pack(pady=14,padx=5)
        
        label = tk.Label(self, text="Properties of metals:Shiny,good conductor of heat,good conductor of electricity,malleable,ductile etc,,. ", font=SMALL_FONT)
        label.pack(pady=16,padx=5)
        
        label = tk.Label(self, text=" Properties of non metals: not shiny,poor conductor of heat,poot conductor of electricity,not malleable,not ductile etc,,; ", font=SMALL_FONT)
        label.pack(pady=18,padx=5)
        
        label = tk.Label(self, text="Examples of Metals are :- Aluminium,Copper,Lead etc,,.\n Examples of Non-Metals are:- Wood,Glass,Plastic,Rubber etc..,", font=SMALL_FONT)
        label.pack(pady=20,padx=5)
        
        button3 = tk.Button(self, text="Back to Chapters",
                            command=lambda: controller.show_frame(science))
        button3.pack()
        
        button3 = tk.Button(self, text="Back to subjects",
                            command=lambda: controller.show_frame(subjectPage))
        button3.pack()
        
class our_envir(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Our Environment ", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        label = tk.Label(self, text="Saprophytes:-Saprophytes are plants, fungi, and microorganisms that feed on the dead and decaying materials.\nDecmposers:- Decomposers break down the organic matter or waste material and release nutrients into the soil.  For example, bacteria, worms, slugs, and snails. ", font=SMALL_FONT)
        label.pack(pady=12,padx=10)
        
        label = tk.Label(self, text="Abiotic components:-Nonliving chemical and physical components of the environment like the soil, air, water, temperature, etc.\nBiotic components:-Living organisms of the environment like the plants, animals, microbes, and fungi. ", font=SMALL_FONT)
        label.pack(pady=14,padx=5)
        
        label = tk.Label(self, text=" ECOSYSTEM\n Includes both biotic and abiotic components.\nIn a given area, all the living things such as plants, animals and organisms interacting with each other, and also with their non-living environments, i.e., weather, earth, sun, soil, climate, atmosphere.", font=SMALL_FONT)
        label.pack(pady=16,padx=5)
        
        button3 = tk.Button(self, text="Back to Chapters",
                            command=lambda: controller.show_frame(science))
        button3.pack()
        
        button3 = tk.Button(self, text="Back to subjects",
                            command=lambda: controller.show_frame(subjectPage))
        button3.pack()
class elec(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ELECTRICITY", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        label = tk.Label(self, text="Electricity is the powerful form of energy. All the devices which run by electricity have an electric current flow through them. \nSome examples are the electric bulb, heater, refrigerator, iron, fan, oven etc.", font=SMALL_FONT)
        label.pack(pady=13,padx=5)
        
        label = tk.Label(self, text="ELECTRICITY CELL:-\n  There are two terminals- metal cap for positive and metal disc for negative. \nThe electric current is produced through the chemical present in it.\n Electric cells are used in may devices like a torch, alarm clock, wristwatch, radios, camera and many other devices", font=SMALL_FONT)
        label.pack(pady=15,padx=5) 
        
        label = tk.Label(self, text="ELECTRIC CIRCUIT:-\nElectricity flows through the positive terminal to negative terminal through a path. \n A connection is required outside the electric cell that can support the flow of \n current from positive to negative terminal of the cell.\n The path through which connection is passed is known as an electric circuit.", font=SMALL_FONT)
        label.pack(pady=17,padx=5)
        
        label = tk.Label(self, text="CONDUCTORS:-\n Conductors are the materials which allow current to flow through them.\nEXAMPLE:-\n  All metal wires, non-metal like graphite, gas carbon, the solution of acids in water, solution alkali in water, the solution of salts in water etc.", font=SMALL_FONT)
        label.pack(pady=19,padx=5)
        
        label = tk.Label(self, text="INSULATOR:-\n Insulators are the materials which do not allow current to flow through them.\n Example-\n rubber, plastic paper, petrol, diesel, alcohol etc.", font=SMALL_FONT)
        label.pack(pady=20,padx=5)
        
        button3 = tk.Button(self, text="Back to subjects",
                            command=lambda: controller.show_frame(subjectPage))
        button3.pack()
        
        button3 = tk.Button(self, text="Back to chapters",
                            command=lambda: controller.show_frame(science))
        button3.pack()
        

        
        
        
        
        
        
        
        
        
        
app = python()
app.mainloop()
