import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# Create a window
window = tk.Tk()
window.title('Sliders')
window.geometry('800x500')


# Slider
scale_float = tk.DoubleVar(value = 12.5)
scale = ttk.Scale(
	window, 
	command = lambda value: progress.stop(), 
	from_ = 0, 
	to = 25,
	length = 450,
	orient = 'horizontal',          # Default --> Horizontal
	variable = scale_float)
scale.pack()


# Progress Bar
progress = ttk.Progressbar(
	window, 
	variable = scale_float, 
	maximum = 25,
	orient = 'horizontal',
	mode = 'indeterminate',
	length = 400)
progress.pack()
# progress.start(1000)


# ScrolledText
scrolled_text = scrolledtext.ScrolledText(window, width = 100, height = 5)
scrolled_text.pack()


# Exercise 
# create a progress that is vertical, starts automatically and also show the progress as a number
# there should also be a scale slider that is affected by the progress bar
exercise_int = tk.IntVar()
exercise_progress = ttk.Progressbar(window, orient = 'vertical', variable = exercise_int)
exercise_progress.pack()
exercise_progress.start()

label = ttk.Label(window, textvariable = exercise_int)
label.pack()

exercise_scale = ttk.Scale(window, variable = exercise_int, from_ = 0, to = 100)
exercise_scale.pack()

# Run
window.mainloop()
print('\n----- Closed mainloop window -----')