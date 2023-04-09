import tkinter as tk
from tkinter import ttk

# Create a window
window = tk.Tk()
window.title('ComboBox & SpinBox') 
window.geometry('800x500')

# Combo Box
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

# Run
window.mainloop()
print('\n----- Closed mainloop window -----')
