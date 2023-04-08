import tkinter as tk
from tkinter import ttk

def button_func():
    print("A button was pressed")

def hello_btn():
    print("Hello!")

# Create a window
window = tk.Tk()
window.title('Window and Widgets') 
window.geometry('800x500')

# ttk Widgets - Label
label = ttk.Label(master = window, text = 'This is a test')
label.pack()

# Create Widgets
# tk Text
text = tk.Text(master = window)
text.pack()

# ttk Entry
entry = ttk.Entry(master = window)
entry.pack()

# Exercise Label
exe_label = ttk.Label(master = window, text = 'My Label')
exe_label.pack()

# ttk Button
btn = ttk.Button(master = window, text = 'A button', command = button_func)
btn.pack()

# Exercise Button
# exe_btn = ttk.Button(master=window, text = 'Press to say hello', command = hello_btn)
exe_btn = ttk.Button(master=window, text = 'Press to say hello', command = lambda:print("Lambda btn - Hello!")) # Can also use lambda func (One use funcs)
exe_btn.pack()

# Run
window.mainloop()
print("Closed mainloop window")