import tkinter as tk
from tkinter import ttk

def btn_func():
    # Get content of Entry widget
    entry_text = entry.get()

    # Update Label
    label.configure(text = 'Updated text')  # Or use this syntax --> label['text'] = 'Updated text' --> Same thing!
    label['text'] = entry_text
    entry['state'] = 'disabled'         # Disables the entry widget after one use case
    # print(label.configure())            # Print attributes of label

def btn_old():
    label.configure(text = 'Lorem Ipsum')
    entry['state'] = 'enabled'


# Create a window
window = tk.Tk()
window.title('Get and Set Widgets')
window.geometry('600x300')

# Widgets
label = ttk.Label(master = window, text = 'Lorem Ipsum')
label.pack(pady = 5)

entry = ttk.Entry(master = window)
entry.pack(pady = 5)

button = ttk.Button(master = window, text = 'The button', command = btn_func) 
button.pack(pady = 3)

button_back = ttk.Button(master = window, text = 'To old text', command = btn_old) 
button_back.pack(pady = 0)

# Run
window.mainloop()
print("Closed mainloop window")