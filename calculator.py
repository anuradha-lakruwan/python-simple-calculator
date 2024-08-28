from tkinter import *
import math

root = Tk()
root.title("Simple Calculator")
root.configure(bg="#333333")

operation = None
current_number = 0

e = Entry(root, width=50, borderwidth=5, font=("Arial", 18), bg="#ffffff")
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def operation_click(op):
    global operation, current_number
    current_number = float(e.get())
    operation = op
    e.delete(0, END)

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
    current_number = float(e.get())
    operation = "percent"
    e.delete(0, END)

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

button_color = "#4CAF50"
button_text_color = "white"
button_font = ("Arial", 14)

# Number buttons
Button(root, text="1", padx=35, pady=20, command=lambda: button_click(1), bg=button_color, fg=button_text_color, font=button_font).grid(row=3, column=0, padx=5, pady=5)
Button(root, text="2", padx=35, pady=20, command=lambda: button_click(2), bg=button_color, fg=button_text_color, font=button_font).grid(row=3, column=1, padx=5, pady=5)
Button(root, text="3", padx=35, pady=20, command=lambda: button_click(3), bg=button_color, fg=button_text_color, font=button_font).grid(row=3, column=2, padx=5, pady=5)

Button(root, text="4", padx=35, pady=20, command=lambda: button_click(4), bg=button_color, fg=button_text_color, font=button_font).grid(row=2, column=0, padx=5, pady=5)
Button(root, text="5", padx=35, pady=20, command=lambda: button_click(5), bg=button_color, fg=button_text_color, font=button_font).grid(row=2, column=1, padx=5, pady=5)
Button(root, text="6", padx=35, pady=20, command=lambda: button_click(6), bg=button_color, fg=button_text_color, font=button_font).grid(row=2, column=2, padx=5, pady=5)

Button(root, text="7", padx=35, pady=20, command=lambda: button_click(7), bg=button_color, fg=button_text_color, font=button_font).grid(row=1, column=0, padx=5, pady=5)
Button(root, text="8", padx=35, pady=20, command=lambda: button_click(8), bg=button_color, fg=button_text_color, font=button_font).grid(row=1, column=1, padx=5, pady=5)
Button(root, text="9", padx=35, pady=20, command=lambda: button_click(9), bg=button_color, fg=button_text_color, font=button_font).grid(row=1, column=2, padx=5, pady=5)

Button(root, text="0", padx=35, pady=20, command=lambda: button_click(0), bg=button_color, fg=button_text_color, font=button_font).grid(row=4, column=1, padx=5, pady=5)

# Operation buttons
Button(root, text="+", padx=33, pady=20, command=lambda: operation_click("add"), bg="#FF9800", fg=button_text_color, font=button_font).grid(row=1, column=3, padx=5, pady=5)
Button(root, text="-", padx=34, pady=20, command=lambda: operation_click("subtract"), bg="#FF9800", fg=button_text_color, font=button_font).grid(row=2, column=3, padx=5, pady=5)
Button(root, text="X", padx=33, pady=20, command=lambda: operation_click("multiply"), bg="#FF9800", fg=button_text_color, font=button_font).grid(row=3, column=3, padx=5, pady=5)
Button(root, text="/", padx=34, pady=20, command=lambda: operation_click("divide"), bg="#FF9800", fg=button_text_color, font=button_font).grid(row=4, column=3, padx=5, pady=5)

Button(root, text="=", padx=33, pady=20, command=equals_click, bg="#2196F3", fg=button_text_color, font=button_font).grid(row=5, column=4, padx=5, pady=5)
Button(root, text="CE", padx=30, pady=20, command=clear_entry, bg="#F44336", fg=button_text_color, font=button_font).grid(row=4, column=0, padx=5, pady=5)
Button(root, text="+/-", padx=30, pady=20, command=positive_negative, bg="#9C27B0", fg=button_text_color, font=button_font).grid(row=4, column=2, padx=5, pady=5)
Button(root, text=".", padx=35, pady=20, command=add_point, bg="#9C27B0", fg=button_text_color, font=button_font).grid(row=5, column=1, padx=5, pady=5)

# Additional buttons
Button(root, text="←", padx=35, pady=20, command=backspace, bg="#FF5722", fg=button_text_color, font=button_font).grid(row=5, column=0, padx=5, pady=5)
Button(root, text="%", padx=31, pady=20, command=percentage, bg="#FFEB3B", fg="black", font=button_font).grid(row=5, column=2, padx=5, pady=5)
Button(root, text="√", padx=33, pady=20, command=square_root, bg="#3F51B5", fg=button_text_color, font=button_font).grid(row=5, column=3, padx=5, pady=5)
Button(root, text="x²", padx=30, pady=20, command=square, bg="#3F51B5", fg=button_text_color, font=button_font).grid(row=5, column=4, padx=5, pady=5)

root.mainloop()
