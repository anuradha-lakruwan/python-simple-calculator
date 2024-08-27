from tkinter import *

root = Tk()
root.title("Simple Calculator")

operation = None
current_number = 0

e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=4)

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

# Number buttons
button_1 = Button(root, borderwidth=2, text="1", padx=40, pady=20, command=lambda: button_click(1)).grid(row=3, column=0)
button_2 = Button(root, borderwidth=2, text="2", padx=40, pady=20, command=lambda: button_click(2)).grid(row=3, column=1)
button_3 = Button(root, borderwidth=2, text="3", padx=40, pady=20, command=lambda: button_click(3)).grid(row=3, column=2)

button_4 = Button(root, borderwidth=2, text="4", padx=40, pady=20, command=lambda: button_click(4)).grid(row=2, column=0)
button_5 = Button(root, borderwidth=2, text="5", padx=40, pady=20, command=lambda: button_click(5)).grid(row=2, column=1)
button_6 = Button(root, borderwidth=2, text="6", padx=40, pady=20, command=lambda: button_click(6)).grid(row=2, column=2)

button_7 = Button(root, borderwidth=2, text="7", padx=40, pady=20, command=lambda: button_click(7)).grid(row=1, column=0)
button_8 = Button(root, borderwidth=2, text="8", padx=40, pady=20, command=lambda: button_click(8)).grid(row=1, column=1)
button_9 = Button(root, borderwidth=2, text="9", padx=40, pady=20, command=lambda: button_click(9)).grid(row=1, column=2)

button_0 = Button(root, borderwidth=2, text="0", padx=40, pady=20, command=lambda: button_click(0)).grid(row=4, column=1)

# Operation buttons
button_sum = Button(root, borderwidth=2, text="+", padx=37, pady=20, command=lambda: operation_click("add")).grid(row=1, column=3)
button_minus = Button(root, borderwidth=2, text="-", padx=38, pady=20, command=lambda: operation_click("subtract")).grid(row=2, column=3)
button_multiply = Button(root, borderwidth=2, text="X", padx=37, pady=20, command=lambda: operation_click("multiply")).grid(row=3, column=3)
button_divide = Button(root, borderwidth=2, text="/", padx=38, pady=20, command=lambda: operation_click("divide")).grid(row=4, column=3)

button_equals = Button(root, borderwidth=2, text="=", padx=36, pady=20, command=equals_click).grid(row=5, column=3)
button_clear = Button(root, borderwidth=2, text="CE", padx=37, pady=20, command=clear_entry).grid(row=4, column=0)
button_negative_positive = Button(root, borderwidth=2, text="+/-", padx=37, pady=20, command=positive_negative).grid(row=4, column=2)
button_point = Button(root, borderwidth=2, text=".", padx=41, pady=20, command=add_point).grid(row=5, column=1)

root.mainloop()
