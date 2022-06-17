from tkinter import font
from tkinter import *
import constants as c

def open_win(main=False):

	if main:
		root = Tk()
	else:
		root = Toplevel()
	
	c.root_config(root, "Standard Calculator", (320,447))

	main_font = font.Font(family=c.MAIN_FONT, size=c.SMALL_SIZE, weight="bold")
	entry_font = font.Font(family=c.MAIN_FONT, size=35, weight="bold")

	number_input = Entry(root, bg=c.BACKGROUND, fg="white", font=entry_font, justify=RIGHT, width=12, bd=0)
	number_input.grid(row=1, column=1, columnspan=4, ipady=5, pady=(35, 35))
	number_input.focus_set()
	number_input.insert(0, "0")

	standard_label = Label(root, text="Standard", bg=c.BACKGROUND, fg="white", font=main_font)
	standard_label.grid(row=0, column=1, sticky=SW, columnspan=2)



	def opposite():
		try:
			number_input.insert(0, "-") if number_input.get()[0] != "-" else number_input.delete(0, 1)
		except IndexError:
			pass


	def operation(op):
		global num1

		try:
			num1 = float(number_input.get())
		except ValueError:
			pass

		global operation_
		operation_ = op

		number_input.delete(0, END)


	def equal():
		try:
			num2 = float(number_input.get())

			if operation_ == "+":
				ans = num1 + num2	
			elif operation_ == "-":
				ans = num1 - num2
			elif operation_ == "*":
				ans = num1 * num2
			elif operation_ == "/":
				ans = num1 / num2
			elif operation_ == "**":
				ans = num1 ** num2

			desc = f"Standard: {num1} {operation_} {num2} = {ans:.3f}"
			c.history.append(desc)
			# print(desc)

			number_input.delete(0, END)
			number_input.insert(0, str(ans))
		except Exception:
			pass


	def oneoverx():
		try:
			x = float(number_input.get())

			number_input.delete(0, END)
			number_input.insert(0, str(1/x))
			ans_ = 1/x

			desc = f"Standard: 1 / {x} = {ans_:.3f}"
			c.history.append(desc)
			# print(desc)
			
		except Exception:
			pass


	def sqr():
		try:
			x = float(number_input.get())

			number_input.delete(0, END)
			number_input.insert(0, str(x**2))

			ans_ = x**2
			desc = f"Standard: {x} ** 2 = {ans_:.3f}"
			c.history.append(desc)
			# print(desc)

		except Exception:
			pass



	number_input.bind("+", lambda event: operation("+"))
	number_input.bind("-", lambda event: operation("-"))
	number_input.bind("*", lambda event: operation("*"))
	number_input.bind("/", lambda event: operation("/"))
	number_input.bind("<Key>", lambda event: equal)

	config_black = {"bg": c.BLACK, "bd": 0, "fg": "white", "font": main_font}
	config_gray = {"bg": c.GRAY, "bd": 0, "fg": "white", "font": main_font}
	config_blue = {"bg": c.BLUE, "bd": 0, "fg": "white", "font": main_font}
	grid_config = {"sticky": W+E, "padx": 2, "pady": 2, "ipady": 7}


	clear_button = Button(root, text="Clear", **config_gray, command=lambda: c.clear(number_input))
	back_button = Button(root, text="Backspace", **config_gray, command=lambda: c.back(number_input))

	divide_button = Button(root, text="÷", **config_gray, command=lambda: operation("/"))
	multiply_button = Button(root, text="×", **config_gray, command=lambda: operation("*"))
	subtract_button = Button(root, text="-", **config_gray, command=lambda: operation("-"))
	add_button = Button(root, text="+", **config_gray, command=lambda: operation("+"))
	equal_button = Button(root, text="=", **config_blue, command=equal)

	sqr_button = Button(root, text="x²", **config_gray, command=sqr)
	exp_button = Button(root, text="x^y", **config_gray, command=lambda: operation("**"))
	frac_button = Button(root, text="1/x", **config_gray, command=oneoverx)

	button_0 = Button(root, text="0", **config_black, command=lambda: c.insert_num(0, number_input))
	button_1 = Button(root, text="1", **config_black, command=lambda: c.insert_num(1, number_input))
	button_2 = Button(root, text="2", **config_black, command=lambda: c.insert_num(2, number_input))
	button_3 = Button(root, text="3", **config_black, command=lambda: c.insert_num(3, number_input))
	button_4 = Button(root, text="4", **config_black, command=lambda: c.insert_num(4, number_input))
	button_5 = Button(root, text="5", **config_black, command=lambda: c.insert_num(5, number_input))
	button_6 = Button(root, text="6", **config_black, command=lambda: c.insert_num(6, number_input))
	button_7 = Button(root, text="7", **config_black, command=lambda: c.insert_num(7, number_input))
	button_8 = Button(root, text="8", **config_black, command=lambda: c.insert_num(8, number_input))
	button_9 = Button(root, text="9", **config_black, command=lambda: c.insert_num(9, number_input))

	dec_button = Button(root, text=".", **config_black, command=lambda: c.insert_num(".", number_input))
	neg_button = Button(root, text="+/-", **config_black, command=opposite)



	clear_button.grid(row=2, column=1, columnspan=2, **grid_config)
	back_button.grid(row=2, column=3, columnspan=2, **grid_config)

	divide_button.grid(row=3, column=4, **grid_config)
	multiply_button.grid(row=4, column=4, **grid_config)
	subtract_button.grid(row=5, column=4, **grid_config)
	add_button.grid(row=6, column=4, **grid_config)
	equal_button.grid(row=7, column=4, **grid_config)

	sqr_button.grid(row=3, column=2, **grid_config)
	exp_button.grid(row=3, column=3, **grid_config)
	frac_button.grid(row=3, column=1, **grid_config)

	button_0.grid(row=7, column=2, **grid_config)
	button_1.grid(row=6, column=1, **grid_config)
	button_2.grid(row=6, column=2, **grid_config)
	button_3.grid(row=6, column=3, **grid_config)
	button_4.grid(row=5, column=1, **grid_config)
	button_5.grid(row=5, column=2, **grid_config)
	button_6.grid(row=5, column=3, **grid_config)
	button_7.grid(row=4, column=1, **grid_config)
	button_8.grid(row=4, column=2, **grid_config)
	button_9.grid(row=4, column=3, **grid_config)

	dec_button.grid(row=7, column=3, **grid_config)
	neg_button.grid(row=7, column=1, **grid_config)


if __name__ == "__main__":
	open_win(main=True)