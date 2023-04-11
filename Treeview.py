import tkinter as tk
from tkinter import ttk
from random import choice

# Create a window
window = tk.Tk()
window.title('Treeview')
window.geometry('800x500')

# Data 
first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

# Treeview 
table = ttk.Treeview(window, columns = ('first', 'last', 'email'), show = 'headings')
table.heading('first', text = 'First name')
table.heading('last', text = 'Surname')
table.heading('email', text = 'Email')
table.pack(fill = 'both', expand = True)

# Insert values into a table
# table.insert(parent = '', index = 0, values = ('John', 'Doe', 'JohnDoe@email.com'))

for i in range(100):
	first = choice(first_names)
	last = choice(last_names)
	email = f'{first[0:3]}{last}@email.com'
	data = (first, last, email)
	table.insert(parent = '', index = tk.END, values = data)

table.insert(parent = '', index = 0, values = ('XXXXX', 'YYYYY', 'ZZZZZ'))

# Events
def item_select(_):
	print(table.selection())
	for i in table.selection():
		print(table.item(i)['values'])		# Only show values
	# table.item(table.selection())

def delete_items(_):
	print('Deleted')
	for i in table.selection():
		table.delete(i)

table.bind('<<TreeviewSelect>>', item_select)
table.bind('<Delete>', delete_items)

# Run
window.mainloop()
print('\n----- Closed mainloop window -----')