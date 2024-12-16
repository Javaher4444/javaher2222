import tkinter as tk
from time import strftime

root = tk.Tk()
root.title('Digital Clock')

lbl = tk.Label(root, font = ('calibri', 40, 'bold'),
			    background = 'purple',
			    foreground = 'white')

lbl.pack(anchor = 'center')

def time():
	string = strftime(' %a | %I:%M:%S %p ')
	lbl.config(text = string)
	lbl.after(1000, time)

time()

root.mainloop()
