import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())             # Print val of strig entered to terminal
    string_var.set('Button Pressed')    # Changes the text to entry and Label to Button Pressed

# Create a window
window = tk.Tk()
window.title('Variables')
window.geometry('800x500')

# tkinter Variable
string_var = tk.StringVar(value = 'test')

# Label
label = ttk.Label(master = window, text = 'Label', textvariable = string_var)
label.pack()

# Entry 1
entry1 = ttk.Entry(master = window, textvariable = string_var)
entry1.pack()

# Entry 2
entry2 = ttk.Entry(master = window, textvariable = string_var)
entry2.pack()

# Button
btn = ttk.Button(master = window, textvariable = string_var, command = button_func)
btn.pack()


# Run
window.mainloop()
print("Closed mainloop window")