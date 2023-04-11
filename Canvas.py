import tkinter as tk

# Create a window
window = tk.Tk()
window.title('')
window.geometry('800x500')

# Canvas
canvas = tk.Canvas(window)
canvas.pack()



# Run
window.mainloop()
print('\n----- Closed mainloop window -----')
