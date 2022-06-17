from tkinter import font
from tkinter import *
import constants as c

import standard
import conversion
import history

def main():
	root = Tk()
	c.root_config(root, "Calculator Navigation")

	def open_anchor(event):
		options[menu.get(ANCHOR)]()


	main_font = font.Font(family=c.MAIN_FONT, size=12, weight="bold")

	options = {
		"Standard": standard.open_win,
		"Length": lambda: conversion.open_win("Length", conversion.LENGTH_UNITS),
		"Temperature": lambda: conversion.open_win("Temperature", conversion.TEMP_UNITS),
		"Time": lambda: conversion.open_win("Time", conversion.TIME_UNITS),
		"Energy": lambda: conversion.open_win("Energy", conversion.ENERGY_UNITS),
		"Data": lambda: conversion.open_win("Data", conversion.DATA_UNITS),
		"History": history.open_win,
	}

	menu = Listbox(root, bg=c.BLACK, font=main_font, fg="white", justify=CENTER)
	[menu.insert(END, i) for i in options.keys()]

	menu.pack(pady=100, ipady=60)
	menu.bind("<Return>", open_anchor)
	menu.bind("<Double-Button-1>", open_anchor)

	root.mainloop()


if __name__ == '__main__':
	main()

