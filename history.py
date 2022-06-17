from tkinter import font
from tkinter import *
import constants as c


def open_win():
	root = Toplevel()
	c.root_config(root, "History")

	def update():
		history_list.delete(0, END)
		[history_list.insert(0, i) for i in c.history]


	main_font = font.Font(family=c.MAIN_FONT, size=c.SMALL_SIZE, weight="bold")
	history_list = Listbox(root, relief=FLAT, bg=c.GRAY, fg="white", font=main_font, bd=0, width=40, height=20, justify=LEFT)
	history_list.pack(pady=10)
	[history_list.insert(0, i) for i in c.history]

	reload_button = Button(root, text="Reload", bg=c.BLUE, fg="white", font=main_font, command=update)
	reload_button.pack()