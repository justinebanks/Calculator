from tkinter import font
from tkinter import *
import conversion_funcs as cf
import constants as c


LENGTH_UNITS = ["centimeters", "meters", "kilometers", "inches", "feet", "yards", "miles"]
ENERGY_UNITS = ["joules", "volts", "calories"]
WEIGHT_UNITS = ["milligrams", "grams", "kilograms", "ounces", "pounds", "tons"]
DATA_UNITS   = ["bits", "bytes", "kilobytes", "megabytes", "gigabytes", "terabytes"]
TIME_UNITS   = ["milliseconds", "seconds", "minutes", "hours", "days", "weeks", "years"]
TEMP_UNITS   = ["fahrenheit", "celcius"]

CONVERSION_FUNCS = {
	"length": cf.convert_length,
	"weight": cf.convert_weight,
	"energy": cf.convert_energy,
	"temperature": cf.convert_temp,
	"time": cf.convert_time,
	"data": cf.convert_data,
}


def open_win(conversion_val, unit_options, main=False):
	if main:
		root = Tk()
	else:
		root = Toplevel()

	c.root_config(root, f"{conversion_val} Converter")

	main_font = font.Font(family=c.MAIN_FONT, size=c.SMALL_SIZE, weight="bold")
	entry_font = font.Font(family=c.MAIN_FONT, size=30, weight="bold")

	length_label = Label(root, text=f"{conversion_val}", font=main_font, bg=c.BACKGROUND, fg="white").grid(row=0, column=1, columnspan=2, sticky=SW)


	unit1 = StringVar()
	unit2 = StringVar()
	unit1.set(unit_options[0])
	unit2.set(unit_options[1])

	number_input1 = Entry(root, bg=c.BACKGROUND, fg="white", width=14, bd=0, font=entry_font, justify=CENTER)
	number_input1.grid(row=1, column=1, columnspan=3, ipady=5, pady=(10, 5))
	number_input1.focus_set()
	number_input1.insert(0, "0")

	# unit_options = units
	default1 = StringVar()
	default1.set("meters") 

	unit_choice1 = OptionMenu(root, unit1, *unit_options)
	unit_choice1.config(bg=c.GRAY, fg="white", relief=SOLID, bd=0, font=main_font)
	unit_choice1.grid(row=2, column=1, ipadx=20, columnspan=3)



	output = Label(root, text="0", bg=c.BACKGROUND, fg="white", bd=0, font=entry_font)
	output.grid(row=3, column=1, pady=(5, 0), columnspan=3)

	default2 = StringVar()
	default2.set("miles") 
	unit_choice2 = OptionMenu(root, unit2, *unit_options)
	unit_choice2.config(bg=c.GRAY, fg="white", relief=SOLID, bd=0, font=main_font)
	unit_choice2.grid(row=4, column=1, ipadx=20, columnspan=3, pady=(0, 20))


	def _convert():
		try:
			num = float(number_input1.get())
		except ValueError:
			return

		val1 = unit1.get()
		val2 = unit2.get()

		if num > 9999.9999:
			# print(f"{conversion_val}: Number Is Too Large")
			return


		ans = float("%.3f" % CONVERSION_FUNCS[conversion_val.lower()](val1, val2, num))
		output.config(text=str(ans))

		desc = f"{conversion_val}: {num} {val1}  -->  {ans:.3f} {val2}"
		c.history.append(desc)
		# print(desc)


	config_black = {"bg": c.BLACK, "bd": 0, "fg": "white", "font": main_font}
	config_gray = {"bg": c.GRAY, "bd": 0, "fg": "white", "font": main_font}
	config_blue = {"bg": c.BLUE, "bd": 0, "fg": "white", "font": main_font}
	grid_config = {"sticky": W+E, "padx": 2, "pady": 2, "ipady": 7}


	clear_button = Button(root, text="C", **config_gray, command=lambda: c.clear(number_input1))
	back_button = Button(root, text="<--", **config_gray, command=lambda: c.back(number_input1))
	dec_button = Button(root, text=".", **config_black, command=lambda: c.insert_num(".", number_input1))
	conv_button = Button(root, text="Convert", **config_blue, command=_convert)

	button_0 = Button(root, text="0", **config_black, command=lambda: c.insert_num(0, number_input1))
	button_1 = Button(root, text="1", **config_black, command=lambda: c.insert_num(1, number_input1))
	button_2 = Button(root, text="2", **config_black, command=lambda: c.insert_num(2, number_input1))
	button_3 = Button(root, text="3", **config_black, command=lambda: c.insert_num(3, number_input1))
	button_4 = Button(root, text="4", **config_black, command=lambda: c.insert_num(4, number_input1))
	button_5 = Button(root, text="5", **config_black, command=lambda: c.insert_num(5, number_input1))
	button_6 = Button(root, text="6", **config_black, command=lambda: c.insert_num(6, number_input1))
	button_7 = Button(root, text="7", **config_black, command=lambda: c.insert_num(7, number_input1))
	button_8 = Button(root, text="8", **config_black, command=lambda: c.insert_num(8, number_input1))
	button_9 = Button(root, text="9", **config_black, command=lambda: c.insert_num(9, number_input1))



	clear_button.grid(row=5, column=2, **grid_config)
	back_button.grid(row=5, column=3, **grid_config)
	dec_button.grid(row=5, column=1, **grid_config)
	conv_button.grid(row=9, column=1, columnspan=2, **grid_config)

	button_0.grid(row=9, column=3, **grid_config)
	button_1.grid(row=8, column=1, **grid_config)
	button_2.grid(row=8, column=2, **grid_config)
	button_3.grid(row=8, column=3, **grid_config)
	button_4.grid(row=7, column=1, **grid_config)
	button_5.grid(row=7, column=2, **grid_config)
	button_6.grid(row=7, column=3, **grid_config)
	button_7.grid(row=6, column=1, **grid_config)
	button_8.grid(row=6, column=2, **grid_config)
	button_9.grid(row=6, column=3, **grid_config)


if __name__ == "__main__":
	open_win("Length", LENGTH_UNITS, main=True)
