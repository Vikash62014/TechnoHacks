import tkinter as tk

# Function to update the display when a button is clicked
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Function to clear the display
def clear():
    entry.delete(0, tk.END)

# Function to perform arithmetic operations
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the entry widget for input and display
entry = tk.Entry(window, width=20, font=("Helvetica", 20))
entry.grid(row=0, column=0, columnspan=4)

# Create the number buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(
        window,
        text=button,
        padx=30,
        pady=30,
        font=("Helvetica", 20),
        command=lambda b=button: button_click(b) if b != "=" else calculate()
    ).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create the clear button
tk.Button(
    window,
    text="C",
    padx=20,
    pady=20,
    font=("Helvetica", 20),
    command=clear
).grid(row=row_val, column=col_val)

# Start the GUI event loop
window.mainloop()
