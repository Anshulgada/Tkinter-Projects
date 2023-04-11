import tkinter as tk
from tkinter import ttk

# Create a window
window = tk.Tk()
window.title('')
window.geometry('800x500')

# Canvas
canvas = tk.Canvas(window, bg = 'white')
canvas.pack()

# canvas.create_rectangle(
#     (50,20,100,200), fill = 'red',                      # LEFT-TOP-RIGHT-BOTTOM Arrangement
#     width = 10, dash = (40,2,1,1), outline = 'blue')
# canvas.create_oval((200,10,300,100), fill = 'yellow')       # LEFT-TOP-RIGHT-BOTTOM Arrangement
# canvas.create_line((0,0,100,150), fill = 'black')               # Start-x / Start-y || End-x / End-y
# # canvas.create_polygon((80,0, 100,200, 300,50), fill = 'gray')           # x1,y1 | x2,y2 | x3,y3
# canvas.create_arc(
#     (200,10,300,100),                # x1,y1 | x2,y2
#     fill = 'red',
#     start = 45, extent = 140,    # Start is angle-start (45deg)  # Extent is total angle (180 deg)
#     style = tk.CHORD, outline = 'red', width = 5
#     )

# canvas.create_text(
#     (150,200), text = 'Some text',
#     fill = 'green', width = 15)

# canvas.create_window((200,150), window = ttk.Label(window, text = 'Text in a canvas'))


# Excercise
def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval(
        (x - brush_size/2, y - brush_size/2, x + brush_size/2, y + brush_size/2),
        fill = 'black')

def brush_size_adjust(event):
    global brush_size

    if event.delta > 0:
        brush_size += 4      # MouseWheel forward = plus_size
    else:
        brush_size -= 4     # MouseWheel backward = minus_size

    brush_size = max(0, min(brush_size, 50))           # Control Brush Size in this range only

brush_size = 2
canvas.bind('<Motion>', draw_on_canvas)
canvas.bind('<MouseWheel>', brush_size_adjust)


# Run
window.mainloop()
print('\n----- Closed mainloop window -----')