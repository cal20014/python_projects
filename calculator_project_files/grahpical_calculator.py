# Python GUI Calculator
from tkinter import *
from unittest import result
# import tkinter as tk

WHITE = "#F8F8F8" # black/white
TAN = "#F1EABC" # black/tan
ORANGE = "#ECA527"

RESULT = 0
display_text = ""

def main():


    def button_press(num):

        global display_text

        display_text = display_text + str(num)

        display_label.set(display_text)

    def equals():

        global display_text

        try:

            calculation_total = str(eval(display_text))

            display_label.set(calculation_total)

            display_text = calculation_total
            
            global RESULT

            RESULT = calculation_total
            
            

        except SyntaxError:

            display_label.set("syntax error")

            display_text = ""

        except ZeroDivisionError:

            display_label.set("calculation error")

            display_text = ""

        return results

    def clear():

        global display_text

        display_label.set("")

        display_text = ""

    def clear_entry():

        global display_text

        display_label.set("")

        display_text = ""

    calculator_window = Tk()
    calculator_window.title("Python GUI Calculator📱")
    calculator_window.geometry("400x525")

    display_text = ""

    display_label = StringVar()

    label = Label(calculator_window, textvariable=display_label, font=('consolas',20), bg="black", fg='red', width=24, height=2)
    label.pack()

    frame = Frame(calculator_window)
    frame.pack()

    clear = Button(frame, text='C', height=4, width=9, font=35, bg=TAN,
                    command=clear)
    clear.grid(row=0, column=0)

    clear_entry = Button(frame, text='CE', height=4, width=9, font=35, bg=TAN,
                    command=clear_entry)
    clear_entry.grid(row=0, column=1)

    percent = Button(frame, text='%', height=4, width=9, font=35, bg=TAN,
                    command=lambda: button_press('%'))
    percent.grid(row=0, column=2)

    divide = Button(frame, text='/', height=4, width=9, font=35, bg=TAN,
                    command=lambda: button_press('/'))
    divide.grid(row=0, column=3)

    button7 = Button(frame, text=7, height=4, width=9, font=35,
                    command=lambda: button_press(7))
    button7.grid(row=1, column=0)

    button8 = Button(frame, text=8, height=4, width=9, font=35,
                    command=lambda: button_press(8))
    button8.grid(row=1, column=1)

    button9 = Button(frame, text=9, height=4, width=9, font=35,
                    command=lambda: button_press(9))
    button9.grid(row=1, column=2)

    button1 = Button(frame, text=1, height=4, width=9, font=35,
                    command=lambda: button_press(1))
    button1.grid(row=3, column=0)

    button2 = Button(frame, text=2, height=4, width=9, font=35,
                    command=lambda: button_press(2))
    button2.grid(row=3, column=1)

    button3 = Button(frame, text=3, height=4, width=9, font=35,
                    command=lambda: button_press(3))
    button3.grid(row=3, column=2)

    button4 = Button(frame, text=4, height=4, width=9, font=35,
                    command=lambda: button_press(4))
    button4.grid(row=2, column=0)

    button5 = Button(frame, text=5, height=4, width=9, font=35,
                    command=lambda: button_press(5))
    button5.grid(row=2, column=1)

    button6 = Button(frame, text=6, height=4, width=9, font=35,
                    command=lambda: button_press(6))
    button6.grid(row=2, column=2)



    button0 = Button(frame, text=0, height=4, width=9, font=35,
                    command=lambda: button_press(0))
    button0.grid(row=4, column=0)

    plus = Button(frame, text='+', height=4, width=9, font=35, bg=TAN,
                    command=lambda: button_press('+'))
    plus.grid(row=3, column=3)

    minus = Button(frame, text='-', height=4, width=9, font=35, bg=TAN,
                    command=lambda: button_press('-'))
    minus.grid(row=2, column=3)

    multiply = Button(frame, text='*', height=4, width=9, font=35, bg=TAN,
                    command=lambda: button_press('*'))
    multiply.grid(row=1, column=3)

    results = Button(frame, text='=', height=4, width=19, font=35, bg=ORANGE,
                    command=equals)
    results.grid(row=4, column=2, columnspan=3)

    decimal = Button(frame, text='.', height=4, width=9, font=35,
                    command=lambda: button_press('.'))
    decimal.grid(row=4, column=1)

    calculator_window.mainloop()

if __name__ == "__main__":
    main()