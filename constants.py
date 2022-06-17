from tkinter import END


# Background Color Constants
BACKGROUND = "#1f1f1f"
BLACK = "#060606"
GRAY = "#131313"
BLUE = "#134369"

# Font Constants
MAIN_FONT = "Helvetica"
SMALL_SIZE = 12


history = []

def clear(input_box):
	input_box.delete(0, END)


def back(input_box):
	nums = input_box.get()
	list_nums = list(nums)

	try:
		list_nums.pop(-1)
	except IndexError:
		pass

	string = ""
	for i in list_nums:
		string = string + i

	input_box.delete(0, END)
	input_box.insert(0, string)


def insert_num(n, input_box):
	nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
	if str(n) in nums:
		if n == ".":
			if "." not in input_box.get():
				input_box.insert(END, str(n))
		else:
			input_box.insert(END, str(n))


def root_config(win, title, size=(320,470)):
	x, y = (size[0], size[1])

	win.geometry(f"{x}x{y}")
	win.config(bg=BACKGROUND)
	win.title(title)
	win.attributes("-alpha", 0.9)
	win.iconbitmap("calculator_icon.ico")
	win.minsize(x, y)
	win.maxsize(x, y)


