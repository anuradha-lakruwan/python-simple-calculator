from tkinter import *
import math

root = Tk()
root.title("Scientific Calculator")
root.configure(bg="#333333")

operation = None
current_number = 0
memory = 0

e = Entry(root, width=50, borderwidth=5, font=("Arial", 18), bg="#ffffff")
e.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def operation_click(op):
    global operation, current_number
    try:
        current_number = float(e.get())
        operation = op
        e.delete(0, END)
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Error")

def equals_click():
    global operation, current_number
    try:
        second_number = float(e.get())
        e.delete(0, END)

        if operation == "add":
            result = current_number + second_number
        elif operation == "subtract":
            result = current_number - second_number
        elif operation == "multiply":
            result = current_number * second_number
        elif operation == "divide":
            if second_number == 0:
                raise ZeroDivisionError
            result = current_number / second_number
        elif operation == "percent":
            result = (current_number * second_number) / 100
        elif operation == "power":
            result = current_number ** second_number
        
        e.insert(0, result)
        operation = None
    except ValueError:
        e.insert(0, "Error")
    except ZeroDivisionError:
        e.insert(0, "Cannot divide by zero")

def clear_entry():
    global operation, current_number
    operation = None
    current_number = 0
    e.delete(0, END)

def add_point():
    current = e.get()
    if "." not in current:
        e.insert(END, ".")

def positive_negative():
    current = e.get()
    if current:
        if "-" in current:
            e.delete(0, 1)
        else:
            e.insert(0, "-")

def backspace():
    current = e.get()
    e.delete(0, END)
    e.insert(0, current[:-1])

def percentage():
    global operation, current_number
    try:
        current_number = float(e.get())
        operation = "percent"
        e.delete(0, END)
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Error")

def square_root():
    try:
        current = float(e.get())
        e.delete(0, END)
        e.insert(0, math.sqrt(current))
    except ValueError:
        e.insert(0, "Error")

def square():
    try:
        current = float(e.get())
        e.delete(0, END)
        e.insert(0, current ** 2)
    except ValueError:
        e.insert(0, "Error")

def sine():
    try:
        current = float(e.get())
        e.delete(0, END)
        e.insert(0, math.sin(math.radians(current)))
    except ValueError:
        e.insert(0, "Error")

def cosine():
    try:
        current = float(e.get())
        e.delete(0, END)
        e.insert(0, math.cos(math.radians(current)))
    except ValueError:
        e.insert(0, "Error")

def tangent():
    try:
        current = float(e.get())
        e.delete(0, END)
        e.insert(0, math.tan(math.radians(current)))
    except ValueError:
        e.insert(0, "Error")

def logarithm():
    try:
        current = float(e.get())
        e.delete(0, END)
        e.insert(0, math.log10(current))
    except ValueError:
        e.insert(0, "Error")

def natural_log():
    try:
        current = float(e.get())
        e.delete(0, END)
        e.insert(0, math.log(current))
    except ValueError:
        e.insert(0, "Error")

def exponentiation():
    global operation, current_number
    try:
        current_number = float(e.get())
        operation = "power"
        e.delete(0, END)
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Error")

def hyperbolic_sine():
    try:
        current = float(e.get())
        e.delete(0, END)
        e.insert(0, math.sinh(current))
    except ValueError:
        e.insert(0, "Error")

def hyperbolic_cosine():
    try:
        current = float(e.get())
        e.delete(0, END)
        e.insert(0, math.cosh(current))
    except ValueError:
        e.insert(0, "Error")

def hyperbolic_tangent():
    try:
        current = float(e.get())
        e.delete(0, END)
        e.insert(0, math.tanh(current))
    except ValueError:
        e.insert(0, "Error")

def exponential():
    try:
        current = float(e.get())
        e.delete(0, END)
        e.insert(0, math.exp(current))
    except ValueError:
        e.insert(0, "Error")

def pi():
    e.insert(END, str(math.pi))

def euler():
    e.insert(END, str(math.e))

def factorial():
    try:
        current = int(e.get())
        e.delete(0, END)
        e.insert(0, math.factorial(current))
    except ValueError:
        e.insert(0, "Error")

def inverse_sine():
    try:
        current = float(e.get())
        e.delete(0, END)
        e.insert(0, math.degrees(math.asin(current)))
    except ValueError:
        e.insert(0, "Error")

def inverse_cosine():
    try:
        current = float(e.get())
        e.delete(0, END)
        e.insert(0, math.degrees(math.acos(current)))
    except ValueError:
        e.insert(0, "Error")

def inverse_tangent():
    try:
        current = float(e.get())
        e.delete(0, END)
        e.insert(0, math.degrees(math.atan(current)))
    except ValueError:
        e.insert(0, "Error")

def memory_clear():
    global memory
    memory = 0

def memory_recall():
    e.delete(0, END)
    e.insert(0, memory)

def memory_add():
    global memory
    try:
        current = float(e.get())
        memory += current
    except ValueError:
        e.insert(0, "Error")

def memory_subtract():
    global memory
    try:
        current = float(e.get())
        memory -= current
    except ValueError:
        e.insert(0, "Error")

button_color = "#4CAF50"
button_text_color = "white"
button_font = ("Arial", 14)

# Number buttons
Button(root, text="1", padx=27, pady=20, command=lambda: button_click(1), bg=button_color, fg=button_text_color, font=button_font).grid(row=3, column=0, padx=5, pady=5)
Button(root, text="2", padx=27, pady=20, command=lambda: button_click(2), bg=button_color, fg=button_text_color, font=button_font).grid(row=3, column=1, padx=5, pady=5)
Button(root, text="3", padx=27, pady=20, command=lambda: button_click(3), bg=button_color, fg=button_text_color, font=button_font).grid(row=3, column=2, padx=5, pady=5)

Button(root, text="4", padx=27, pady=20, command=lambda: button_click(4), bg=button_color, fg=button_text_color, font=button_font).grid(row=2, column=0, padx=5, pady=5)
Button(root, text="5", padx=27, pady=20, command=lambda: button_click(5), bg=button_color, fg=button_text_color, font=button_font).grid(row=2, column=1, padx=5, pady=5)
Button(root, text="6", padx=27, pady=20, command=lambda: button_click(6), bg=button_color, fg=button_text_color, font=button_font).grid(row=2, column=2, padx=5, pady=5)

Button(root, text="7", padx=27, pady=20, command=lambda: button_click(7), bg=button_color, fg=button_text_color, font=button_font).grid(row=1, column=0, padx=5, pady=5)
Button(root, text="8", padx=27, pady=20, command=lambda: button_click(8), bg=button_color, fg=button_text_color, font=button_font).grid(row=1, column=1, padx=5, pady=5)
Button(root, text="9", padx=27, pady=20, command=lambda: button_click(9), bg=button_color, fg=button_text_color, font=button_font).grid(row=1, column=2, padx=5, pady=5)

Button(root, text="0", padx=27, pady=20, command=lambda: button_click(0), bg=button_color, fg=button_text_color, font=button_font).grid(row=4, column=1, padx=5, pady=5)

# Operation buttons
Button(root, text="+", padx=25, pady=20, command=lambda: operation_click("add"), bg="#FF9800", fg=button_text_color, font=button_font).grid(row=1, column=3, padx=5, pady=5)
Button(root, text="-", padx=26, pady=20, command=lambda: operation_click("subtract"), bg="#FF9800", fg=button_text_color, font=button_font).grid(row=2, column=3, padx=5, pady=5)
Button(root, text="X", padx=25, pady=20, command=lambda: operation_click("multiply"), bg="#FF9800", fg=button_text_color, font=button_font).grid(row=3, column=3, padx=5, pady=5)
Button(root, text="/", padx=26, pady=20, command=lambda: operation_click("divide"), bg="#FF9800", fg=button_text_color, font=button_font).grid(row=4, column=3, padx=5, pady=5)

Button(root, text="=", padx=25, pady=20, command=equals_click, bg="#2196F3", fg=button_text_color, font=button_font).grid(row=5, column=5, padx=5, pady=5)
Button(root, text="CE", padx=22, pady=20, command=clear_entry, bg="#F44336", fg=button_text_color, font=button_font).grid(row=4, column=0, padx=5, pady=5)
Button(root, text="+/-", padx=22, pady=20, command=positive_negative, bg="#9C27B0", fg=button_text_color, font=button_font).grid(row=4, column=2, padx=5, pady=5)
Button(root, text=".", padx=27, pady=20, command=add_point, bg="#9C27B0", fg=button_text_color, font=button_font).grid(row=4, column=4, padx=5, pady=5)

# Additional buttons
Button(root, text="←", padx=27, pady=20, command=backspace, bg="#FF5722", fg=button_text_color, font=button_font).grid(row=5, column=0, padx=5, pady=5)
Button(root, text="%", padx=23, pady=20, command=percentage, bg="#FFEB3B", fg="black", font=button_font).grid(row=5, column=2, padx=5, pady=5)
Button(root, text="√", padx=25, pady=20, command=square_root, bg="#3F51B5", fg=button_text_color, font=button_font).grid(row=5, column=3, padx=5, pady=5)
Button(root, text="x²", padx=23, pady=20, command=square, bg="#3F51B5", fg=button_text_color, font=button_font).grid(row=5, column=4, padx=5, pady=5)

# Scientific buttons
Button(root, text="sin", padx=23, pady=20, command=sine, bg="#8BC34A", fg=button_text_color, font=button_font).grid(row=1, column=5, padx=5, pady=5)
Button(root, text="cos", padx=23, pady=20, command=cosine, bg="#8BC34A", fg=button_text_color, font=button_font).grid(row=2, column=5, padx=5, pady=5)
Button(root, text="tan", padx=23, pady=20, command=tangent, bg="#8BC34A", fg=button_text_color, font=button_font).grid(row=3, column=5, padx=5, pady=5)
Button(root, text="log", padx=20, pady=20, command=logarithm, bg="#8BC34A", fg=button_text_color, font=button_font).grid(row=4, column=5, padx=5, pady=5)
Button(root, text="ln", padx=23, pady=20, command=natural_log, bg="#8BC34A", fg=button_text_color, font=button_font).grid(row=5, column=1, padx=5, pady=5)
Button(root, text="x^y", padx=20, pady=20, command=exponentiation, bg="#8BC34A", fg=button_text_color, font=button_font).grid(row=5, column=4, padx=5, pady=5)

# New Scientific buttons
Button(root, text="sinh", padx=18, pady=20, command=hyperbolic_sine, bg="#8BC34A", fg=button_text_color, font=button_font).grid(row=6, column=1, padx=5, pady=5)
Button(root, text="cosh", padx=18, pady=20, command=hyperbolic_cosine, bg="#8BC34A", fg=button_text_color, font=button_font).grid(row=6, column=2, padx=5, pady=5)
Button(root, text="tanh", padx=18, pady=20, command=hyperbolic_tangent, bg="#8BC34A", fg=button_text_color, font=button_font).grid(row=6, column=3, padx=5, pady=5)
Button(root, text="exp", padx=20, pady=20, command=exponential, bg="#8BC34A", fg=button_text_color, font=button_font).grid(row=6, column=4, padx=5, pady=5)
Button(root, text="π", padx=25, pady=20, command=pi, bg="#8BC34A", fg=button_text_color, font=button_font).grid(row=6, column=0, padx=5, pady=5)
Button(root, text="e", padx=25, pady=20, command=euler, bg="#8BC34A", fg=button_text_color, font=button_font).grid(row=6, column=5, padx=5, pady=5)
Button(root, text="n!", padx=23, pady=20, command=factorial, bg="#8BC34A", fg=button_text_color, font=button_font).grid(row=7, column=0, padx=5, pady=5)
Button(root, text="asin", padx=18, pady=20, command=inverse_sine, bg="#8BC34A", fg=button_text_color, font=button_font).grid(row=7, column=1, padx=5, pady=5)
Button(root, text="acos", padx=18, pady=20, command=inverse_cosine, bg="#8BC34A", fg=button_text_color, font=button_font).grid(row=7, column=2, padx=5, pady=5)
Button(root, text="atan", padx=18, pady=20, command=inverse_tangent, bg="#8BC34A", fg=button_text_color, font=button_font).grid(row=7, column=3, padx=5, pady=5)

# Memory buttons
Button(root, text="MC", padx=20, pady=20, command=memory_clear, bg="#4CAF50", fg=button_text_color, font=button_font).grid(row=7, column=4, padx=5, pady=5)
Button(root, text="MR", padx=20, pady=20, command=memory_recall, bg="#4CAF50", fg=button_text_color, font=button_font).grid(row=7, column=5, padx=5, pady=5)
Button(root, text="M+", padx=20, pady=20, command=memory_add, bg="#4CAF50", fg=button_text_color, font=button_font).grid(row=8, column=4, padx=5, pady=5)
Button(root, text="M-", padx=20, pady=20, command=memory_subtract, bg="#4CAF50", fg=button_text_color, font=button_font).grid(row=8, column=5, padx=5, pady=5)

root.mainloop()
