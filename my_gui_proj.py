#Python program for a Graphical User Interface
#A Calculator using Tkinter

#importation from tkinter module
from tkinter import *

#global formation variable
formation = ""

def press(num):
    #global expression variable
    global formation
    #concatenation of string
    formation = formation + str(num)
    #use of set method to update formation
    calculation.set(formation)

def clear():
    #special function for the clear button
    global formation
    
    formation = ""
    calculation.set("")

def equalpress():
    #function for the evaluation of equals
    try:
        global formation
        #eval function takes formation and evaluates it
        overall = str(eval(formation))
        calculation.set(overall)
        formation = ""
    #if something wrong mistake is announced
    except:
        calculation.set(" mistake ")
        formation = ""  

#Code for the driver
if __name__ == "__main__":

    #GUI window generattion
    my_gui = Tk()

    #setting of background colour. 
    my_gui.configure(background = "blue")

    my_gui.title("Calculator")

    my_gui.geometry("500x500")

    #using variable class StringVar()

    #creation of instance of the StringVar() class
    calculation = StringVar()

    #create text entry box
    field = Entry(my_gui, textvariable = calculation)

    #need to place widgets at respective positions in table like structure
    field.grid(columnspan= 6, ipadx = 70)

    #buttons at a particular location inside my_gui
    button9 = Button(my_gui, text= '9', fg = 'gray', bg= 'green', pady = 1,
                      command= lambda: press(9), height=2, width=4)
    button9.grid(row=2, column=0)
    button8 = Button(my_gui, text = '8', fg= 'gray', bg = 'green', pady = 1,
                     command= lambda: press(8), height=2, width = 4)
    button8.grid(row=2, column=1)
    button7 = Button(my_gui, text = '7', fg= 'gray', bg = 'green', pady = 1,
                     command= lambda: press(7), height=2, width = 4)
    button7.grid(row=2, column=2)
    button6 = Button(my_gui, text= '6', fg = 'gray', bg = 'green', pady = 1,
                     command = lambda: press(6), height=2, width = 4)
    button6.grid(row=3, column=0)
    button5 = Button(my_gui, text= '5', fg= 'gray', bg = 'green', pady = 1,
                     command= lambda: press(5), height = 2, width = 4)
    button5.grid(row=3, column=1)
    button4 = Button(my_gui, text = '4', fg= 'gray', bg= 'green', pady = 1,
                     command= lambda: press(4), height = 2, width = 4)
    button4.grid(row=3, column=2)
    button3 = Button(my_gui, text = '3', fg= 'gray', bg= 'green', pady = 1,
                     command= lambda: press(3), height = 2, width = 4)
    button3.grid(row=4, column=0)
    button2 = Button(my_gui, text = '2', fg = 'gray', bg= 'green', pady = 1,
                     command= lambda: press(2), height = 2, width = 4)
    button2.grid(row=4, column=1)
    button1 = Button(my_gui, text = '1', fg = 'gray', bg= 'green', pady = 1,
                     command= lambda: press(1), height = 2, width = 4)
    button1.grid(row=4, column=2)
    button0 = Button(my_gui, text = '0', fg = 'gray', bg = 'green', pady = 1,
                     command = lambda: press(0), height = 2, width = 4)
    button0.grid(row=5, column=0)
    buttonDecimal = Button(my_gui, text= '.', fg = 'gray', bg = 'green', pady = 1,
                       command = lambda: press('.'), height = 2, width = 4)
    buttonDecimal.grid(row=5, column=1)
    buttonClear = Button(my_gui, text= 'Clear', fg= 'gray', bg = 'green', pady = 1,
                         command = clear, height = 2, width = 4)
    buttonClear.grid(row=5, column = 2)
    buttonMult = Button(my_gui, text= '*', fg= 'gray', bg = 'green', pady = 1,
                        command = lambda: press("*"), height = 2, width = 4)
    buttonMult.grid(row= 2, column = 3)
    buttonDiv = Button(my_gui, text = '/', fg = 'gray', bg = 'green', pady = 1,
                       command = lambda: press("/"), height = 2, width = 4)
    buttonDiv.grid(row = 3, column = 3)
    buttonAdd = Button(my_gui, text = '+', fg = 'gray', bg = 'green', pady = 1,
                       command = lambda: press("+"), height = 2, width = 4)
    buttonAdd.grid(row = 4, column = 3)
    buttonSubt = Button(my_gui, text = '-', fg = 'gray', bg = 'green', pady = 1,
                        command = lambda: press("-"), height = 2, width = 4)
    buttonSubt.grid(row= 5, column = 3)
    buttonEqual = Button(my_gui, text = '=', fg= 'purple', bg = 'yellow', pady = 1,
                         command = equalpress, height = 2, width = 4)
    buttonEqual.grid(row = 6, column = 3)

    my_gui.mainloop()
    
    
    
    
    
    
    
    



    

    

