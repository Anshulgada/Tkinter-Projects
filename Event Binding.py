import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f'x -->{event.x} \ny -->{event.y}\n')

# Create a window
window = tk.Tk()
window.title('')
window.geometry('800x500')

# Text
text = tk.Text(window)
text.pack()

# Entry
entry = ttk.Entry(window)
entry.pack()

# Button
btn = ttk.Button(window, text = 'A button')
btn.pack()

# Events
window.bind('<Alt-KeyPress-a>', lambda event: print('A window event')) # Format --> modifier-type-detail | works throughout
btn.bind('<Alt-KeyPress-a>', lambda event: print('A btn event'))    # Only works when btn is pressed

# window.bind('<Motion>', get_pos)        # Gives mouse posisiion in whole window
# text.bind('<Motion>', get_pos)            # Gives mouse posisiion in text field

window.bind('<KeyPress>', lambda event: print(f'This key was pressed --> ({event.char})'))  # Loooks for any key pressed

entry.bind('<FocusIn>', lambda event: print('Entry Field was selected'))    # Check if Entry field is selected
entry.bind('<FocusOut>', lambda event: print('Entry Field was unselected'))    # Check if Entry field is unselected

text.bind('<Shift-MouseWheel>', lambda event: print('MouseWheel'))

# Run
window.mainloop()
print('\n----- Closed mainloop window -----')
