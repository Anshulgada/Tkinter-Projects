import tkinter as tk
from tkinter import ttk

# Create a window
window = tk.Tk()
window.title('ComboBox & SpinBox')
window.geometry('800x500')

# Combobox
items = ('Ice-cream', 'Pizza', 'Broccoli')
food_str = tk.StringVar(value = 'Choose an item')
combo = ttk.Combobox(window, textvariable = food_str)
# combo['values'] = items
combo.configure(value = items)    # Same as above, just shorter and hence easier
combo.pack()

# Events for combobox
combo.bind('<<ComboboxSelected>>', lambda event: combo_label.configure(text = f'Selected value: {food_str.get()}'))

combo_label = ttk.Label(window, text = 'A Label')
combo_label.pack()

# Spinbox
spin_int = tk.IntVar(value = 12)
spin = ttk.Spinbox(
    window,
    from_ = 3,
    to = 20,
    increment = 3,
    textvariable = spin_int,
    command = lambda: print(spin_int.get()))
spin.bind('<<Increment>>', lambda event: print('Up'))
spin.bind('<<Decrement>>', lambda event: print('Down'))
# spin['value'] = (1,2,3,4,5)       # To use specific values like items[]
spin.pack()

# Excercise
spin_options = ('A','B','C','D','E')
spin_string = tk.StringVar(value = spin_options[0])
spin_ex = ttk.Spinbox(
    window,
    textvariable = spin_string,
    value = spin_options
)
spin_ex.bind('<<Decrement>>', lambda event: print(spin_ex.get()))
spin_ex.pack(pady = 15)

# Rung
window.mainloop()
print('\n----- Closed mainloop window -----')