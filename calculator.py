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

def insert_value(value):
    e.insert(END, value)

def update_display(value):
    e.delete(0, END)
    e.insert(0, value)

def safe_operation(func, *args):
    try:
        result = func(*args)
        update_display(result)
    except ValueError:
        update_display("Error")
    except ZeroDivisionError:
        update_display("Cannot divide by zero")

def button_click(number):
    current = e.get()
    update_display(str(current) + str(number))

def operation_click(op):
    global operation, current_number
    current_number = safe_operation(float, e.get())
    operation = op
    e.delete(0, END)

def equals_click():
    global operation, current_number
    second_number = safe_operation(float, e.get())
    result = {
        "add": current_number + second_number,
        "subtract": current_number - second_number,
        "multiply": current_number * second_number,
        "divide": current_number / second_number if second_number != 0 else "Cannot divide by zero",
        "percent": (current_number * second_number) / 100,
        "power": current_number ** second_number
    }.get(operation, "Error")
    update_display(result)
    operation = None

def clear_entry():
    global operation, current_number
    operation = None
    current_number = 0
    e.delete(0, END)

def add_point():
    current = e.get()
    if "." not in current:
        insert_value(".")

def positive_negative():
    current = e.get()
    if current:
        update_display(current[1:] if current.startswith("-") else "-" + current)

def backspace():
    current = e.get()
    update_display(current[:-1])

def percentage():
    global operation, current_number
    current_number = safe_operation(float, e.get())
    operation = "percent"
    e.delete(0, END)

def square_root():
    safe_operation(lambda x: math.sqrt(x), float(e.get()))

def square():
    safe_operation(lambda x: x ** 2, float(e.get()))

def sine():
    safe_operation(lambda x: math.sin(math.radians(x)), float(e.get()))

def cosine():
    safe_operation(lambda x: math.cos(math.radians(x)), float(e.get()))

def tangent():
    safe_operation(lambda x: math.tan(math.radians(x)), float(e.get()))

def logarithm():
    safe_operation(lambda x: math.log10(x), float(e.get()))

def natural_log():
    safe_operation(lambda x: math.log(x), float(e.get()))

def exponentiation():
    global operation, current_number
    current_number = safe_operation(float, e.get())
    operation = "power"
    e.delete(0, END)

def hyperbolic_sine():
    safe_operation(lambda x: math.sinh(x), float(e.get()))

def hyperbolic_cosine():
    safe_operation(lambda x: math.cosh(x), float(e.get()))

def hyperbolic_tangent():
    safe_operation(lambda x: math.tanh(x), float(e.get()))

def exponential():
    safe_operation(lambda x: math.exp(x), float(e.get()))

def pi():
    insert_value(str(math.pi))

def euler():
    insert_value(str(math.e))

def factorial():
    safe_operation(lambda x: math.factorial(int(x)), float(e.get()))

def inverse_sine():
    safe_operation(lambda x: math.degrees(math.asin(x)), float(e.get()))

def inverse_cosine():
    safe_operation(lambda x: math.degrees(math.acos(x)), float(e.get()))

def inverse_tangent():
    safe_operation(lambda x: math.degrees(math.atan(x)), float(e.get()))

def memory_clear():
    global memory
    memory = 0

def memory_recall():
    update_display(memory)

def memory_add():
    global memory
    memory = safe_operation(lambda x: memory + x, float(e.get()))

def memory_subtract():
    global memory
    memory = safe_operation(lambda x: memory - x, float(e.get()))

button_color = "#4CAF50"
button_text_color = "white"
button_font = ("Arial", 14)

buttons = [
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), 
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("0", 4, 1), (".", 4, 4), ("+/-", 4, 2), 
    ("←", 5, 0), ("%", 5, 2), ("√", 5, 3), ("x²", 5, 4), ("+", 1, 3), ("-", 2, 3), 
    ("X", 3, 3), ("/", 4, 3), ("=", 5, 5), ("CE", 4, 0), ("sin", 1, 5), ("cos", 2, 5), 
    ("tan", 3, 5), ("log", 4, 5), ("ln", 5, 1), ("x^y", 5, 4), ("sinh", 6, 1), 
    ("cosh", 6, 2), ("tanh", 6, 3), ("exp", 6, 4), ("π", 6, 0), ("e", 6, 5), 
    ("n!", 7, 0), ("asin", 7, 1), ("acos", 7, 2), ("atan", 7, 3), ("MC", 7, 4), 
    ("MR", 7, 5), ("M+", 8, 4), ("M-", 8, 5)
]

for (text, row, col) in buttons:
    Button(root, text=text, padx=25, pady=20, command=lambda t=text: button_click(t) if t.isdigit() or t == "." else globals()[t.replace('X', 'multiply').replace('+/-', 'positive_negative').replace('←', 'backspace').replace('%', 'percentage').replace('√', 'square_root').replace('x²', 'square').replace('=', 'equals_click').replace('CE', 'clear_entry').replace('+', 'operation_click').replace('-', 'operation_click').replace('/', 'operation_click').replace('sin', 'sine').replace('cos', 'cosine').replace('tan', 'tangent').replace('log', 'logarithm').replace('ln', 'natural_log').replace('x^y', 'exponentiation').replace('sinh', 'hyperbolic_sine').replace('cosh', 'hyperbolic_cosine').replace('tanh', 'hyperbolic_tangent').replace('exp', 'exponential').replace('π', 'pi').replace('e', 'euler').replace('n!', 'factorial').replace('asin', 'inverse_sine').replace('acos', 'inverse_cosine').replace('atan', 'inverse_tangent').replace('MC', 'memory_clear').replace('MR', 'memory_recall').replace('M+', 'memory_add').replace('M-', 'memory_subtract')](text), bg=button_color if text.isdigit() or text in ['.', 'π', 'e'] else "#FF9800" if text in ['+', '-', 'X', '/'] else "#2196F3" if text == '=' else "#F44336" if text == 'CE' else "#9C27B0" if text in ['+/-', '.'] else "#FFEB3B" if text == '%' else "#3F51B5" if text in ['√', 'x²'] else "#8BC34A", fg=button_text_color, font=button_font).grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
