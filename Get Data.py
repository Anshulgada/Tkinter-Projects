import tkinter as tk
from tkinter import ttk

def btn_func():
    # Get content of Entry widget
    entry_text = entry.get()

    # Update Label
    label.configure(text = 'Updated text')  # Or use this syntax --> label['text'] = 'Updated text' --> Same thing!
    label['text'] = entry_text

# Create a window
window = tk.Tk()
window.title('Get and Set Widgets')
window.geometry('600x300')

# Widgets
label = ttk.Label(master = window, text = 'Lorem Ipsum')
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = 'The button', command = btn_func) 
button.pack()

# Run
window.mainloop()
print("Closed mainloop window")