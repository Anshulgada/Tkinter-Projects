import tkinter as tk
from tkinter import ttk

# def btn_func(entry_str):
#     print('Button was pressed')
#     print(entry_str.get())

def outer_func(parameter):
    def inner_func():
        print('Button was pressed')
        print(parameter.get())
    return inner_func

# Create a window
window = tk.Tk()
window.title('')
window.geometry('800x500')

# Entry
entry_str = tk.StringVar(value = 'Test')
entry = ttk.Entry(window, textvariable = entry_str)
entry.pack()

# Button
# btn = ttk.Button(window, text = 'A button', command = lambda: btn_func(entry_str))   # By adding in lambda we make it
# btn.pack()                                                                           # so that the func is not called

btn = ttk.Button(window, text = 'A button', command = outer_func(entry_str))  # To directly call, use nested func
btn.pack()

# Run
window.mainloop()
print('\n----- Closed mainloop window -----')