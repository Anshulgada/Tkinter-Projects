import tkinter as tk
from tkinter import ttk

# Create a window
window = tk.Tk()
window.title('Buttons')
window.geometry('600x400')

# def btn_func():
#     print('Basic Btn')
#     print(radio_var.get())

# # Button
# btn_str = tk.StringVar(value = 'A btn with string var')
# btn = ttk.Button(window, text = 'A button', command = btn_func, textvariable = btn_str)
# btn.pack()

# # Check Button
# check_var1 = tk.IntVar(value = 10)      # Start Value is 10   # Can be StringVar / BooleanVar also
# check2 = ttk.Checkbutton(
#     window,
#     text = 'Checkbox 1',
#     command = lambda: print(check_var1.get()),
#     variable = check_var1,
#     onvalue = 10,
#     offvalue = 5)
# check2.pack()

# check2 = ttk.Checkbutton(
#     window,
#     text = 'Checkbox 2',
#     command = lambda: print())
# check2.pack()


# # Radio Buttons
# radio_var = tk.StringVar()
# radio1 = ttk.Radiobutton(
#     window,
#     text = 'Radio Btn 1',
#     value = 'Radio 1',
#     variable = radio_var,
#     command = lambda: print(radio_var.get()))
# radio1.pack()

# radio2 = ttk.Radiobutton(
#     window,
#     text = 'Radio Btn 2',
#     value = 2,
#     variable = radio_var,
#     command = lambda: print(radio_var.get()))
# radio2.pack()



# Exercise ------------
    
def rad_func():
    print(check_bool.get())
    check_bool.set(False)
    

# Radio Buttons
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(
    window,
    text = 'Radio A',
    value = 'A',
    command = rad_func,
    variable = radio_var)
radio1.pack()

radio2 = ttk.Radiobutton(
    window, 
    text = 'Radio B', 
    value = 'B',
    command = rad_func,
    variable = radio_var)
radio2.pack()

# Check Button
check_bool = tk.BooleanVar()
check = ttk.Checkbutton(
    window, 
    text = 'Checkbox',
    command = lambda: print(radio_var.get()),
    variable = check_bool)
check.pack()

# Run
window.mainloop()
print('\n----- Closed mainloop window -----')
