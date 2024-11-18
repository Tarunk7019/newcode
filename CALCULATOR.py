import tkinter as tk

# Function to update the input field with the pressed button's value
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# Function to clear the input field
def clear():
    entry.delete(0, tk.END)

# Function to perform arithmetic operations
def calculate():
    try:
        result = eval(entry.get())  # Using eval to evaluate the expression
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Creating the main window
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg='#1f1f1f')  # Setting background color of the window

# Creating the entry widget for displaying input and output
entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right", bg='#d1e7f7', fg='#003366')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Defining button values
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Creating and placing buttons on the window
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2, command=calculate, bg='#4CAF50', fg='white')
    elif text == 'C':
        button = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2, command=clear, bg='#FF6347', fg='white')
    else:
        button = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2, command=lambda val=text: button_click(val), bg='#f0f8ff', fg='#003366')
    button.grid(row=row, column=col, padx=5, pady=5)

# Running the Tkinter event loop
root.mainloop()
