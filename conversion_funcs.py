# Conversion Functions

def convert_length(from_, to, val):
	if   (from_ == "centimeters")  and (to == "meters"):       ans = val / 100
	elif (from_ == "centimeters")  and (to == "kilometers"):   ans = val / 100000
	elif (from_ == "centimeters")  and (to == "inches"):       ans = val / 2.54
	elif (from_ == "centimeters")  and (to == "feet"):         ans = val / 30.48
	elif (from_ == "centimeters")  and (to == "yards"):        ans = val / 91.44
	elif (from_ == "centimeters")  and (to == "miles"):        ans = val / 160934
	elif (from_ == "inches")       and (to == "centimeters"):  ans = val * 2.54
	elif (from_ == "inches")       and (to == "kilometers"):   ans = val / 39370
	elif (from_ == "inches")       and (to == "meters"):       ans = val / 39.37
	elif (from_ == "inches")       and (to == "feet"):         ans = val / 12
	elif (from_ == "inches")       and (to == "yards"):        ans = val / 36
	elif (from_ == "inches")       and (to == "miles"):        ans = val / 63360
	elif (from_ == "feet")         and (to == "centimeters"):  ans = val * 30.48
	elif (from_ == "feet")         and (to == "inches"):       ans = val * 12
	elif (from_ == "feet")         and (to == "meters"):       ans = val * 0.3048
	elif (from_ == "feet")         and (to == "yards"):        ans = val * 0.333333
	elif (from_ == "feet")         and (to == "kilometers"):   ans = val * 0.0003048
	elif (from_ == "feet")         and (to == "miles"):        ans = val * 0.000189394	
	elif (from_ == "yards")        and (to == "centimeters"):  ans = val * 91.94
	elif (from_ == "yards")        and (to == "inches"):       ans = val * 36
	elif (from_ == "yards")        and (to == "meters"):       ans = val * 0.9144
	elif (from_ == "yards")        and (to == "feet"):         ans = val * 3
	elif (from_ == "yards")        and (to == "kilometers"):   ans = val * 0.0009144
	elif (from_ == "yards")        and (to == "miles"):        ans = val * 0.000568182
	elif (from_ == "meters")       and (to == "centimeters"):  ans = val * 100
	elif (from_ == "meters")       and (to == "inches"):       ans = val * 39.3701
	elif (from_ == "meters")       and (to == "yards"):        ans = val * 1.09361
	elif (from_ == "meters")       and (to == "feet"):         ans = val * 3.28084
	elif (from_ == "meters")       and (to == "kilometers"):   ans = val * 0.001
	elif (from_ == "meters")       and (to == "miles"):        ans = val * 0.000621371
	elif (from_ == "kilometers")   and (to == "centimeters"):  ans = val * 100000
	elif (from_ == "kilometers")   and (to == "inches"):       ans = val * 39370.1             
	elif (from_ == "kilometers")   and (to == "yards"):        ans = val * 1093.61
	elif (from_ == "kilometers")   and (to == "feet"):         ans = val * 3280.84
	elif (from_ == "kilometers")   and (to == "meters"):       ans = val * 1000
	elif (from_ == "kilometers")   and (to == "miles"):        ans = val * 0.621371
	elif (from_ == "miles")        and (to == "centimeters"):  ans = val * 160934
	elif (from_ == "miles")        and (to == "inches"):       ans = val * 63360           
	elif (from_ == "miles")        and (to == "yards"):        ans = val * 1760
	elif (from_ == "miles")        and (to == "feet"):         ans = val * 5280
	elif (from_ == "miles")        and (to == "meters"):       ans = val * 1609.34
	elif (from_ == "miles")        and (to == "kilometers"):   ans = val * 1.60934
	else: ans = val
	return ans


def convert_time(from_, to, val):
	if   (from_ == "milliseconds") and (to == "seconds"):      ans = val * 0.001
	elif (from_ == "milliseconds") and (to == "minutes"):      ans = val * 0.000017
	elif (from_ == "milliseconds") and (to == "hours"):        ans = val * 0.000000277777778
	elif (from_ == "milliseconds") and (to == "days"):         ans = val * 0.000000011574074
	elif (from_ == "milliseconds") and (to == "weeks"):        ans = val * 0.000000001653439
	elif (from_ == "milliseconds") and (to == "years"):        ans = val * 0.000000000031688
	elif (from_ == "seconds")      and (to == "milliseconds"): ans = val * 1000
	elif (from_ == "seconds")      and (to == "minutes"):      ans = val * 0.016667
	elif (from_ == "seconds")      and (to == "hours"):        ans = val * 0.000278
	elif (from_ == "seconds")      and (to == "days"):         ans = val * 0.000012
	elif (from_ == "seconds")      and (to == "weeks"):        ans = val * 0.000002
	elif (from_ == "seconds")      and (to == "years"):        ans = val * 0.000000031688088
	elif (from_ == "minutes")      and (to == "milliseconds"): ans = val * 60000
	elif (from_ == "minutes")      and (to == "seconds"):      ans = val * 60
	elif (from_ == "minutes")      and (to == "hours"):        ans = val * 0.016667
	elif (from_ == "minutes")      and (to == "days"):         ans = val * 0.000694
	elif (from_ == "minutes")      and (to == "weeks"):        ans = val * 0.000099
	elif (from_ == "minutes")      and (to == "years"):        ans = val * 0.000002
	elif (from_ == "hours")        and (to == "milliseconds"): ans = val * 3600000
	elif (from_ == "hours")        and (to == "seconds"):      ans = val * 3600
	elif (from_ == "hours")        and (to == "minutes"):      ans = val * 60
	elif (from_ == "hours")        and (to == "days"):         ans = val * 0.041667
	elif (from_ == "hours")        and (to == "weeks"):        ans = val * 0.005952
	elif (from_ == "hours")        and (to == "years"):        ans = val * 0.000114
	elif (from_ == "days")         and (to == "milliseconds"): ans = val * 86400000
	elif (from_ == "days")         and (to == "seconds"):      ans = val * 86400
	elif (from_ == "days")         and (to == "minutes"):      ans = val * 1440
	elif (from_ == "days")         and (to == "hours"):        ans = val * 24
	elif (from_ == "days")         and (to == "weeks"):        ans = val * 0.142857
	elif (from_ == "days")         and (to == "years"):        ans = val * 0.002738
	elif (from_ == "weeks")        and (to == "milliseconds"): ans = val * 604800000
	elif (from_ == "weeks")        and (to == "seconds"):      ans = val * 604800
	elif (from_ == "weeks")        and (to == "minutes"):      ans = val * 10080
	elif (from_ == "weeks")        and (to == "hours"):        ans = val * 168
	elif (from_ == "weeks")        and (to == "days"):         ans = val * 7
	elif (from_ == "weeks")        and (to == "years"):        ans = val * 0.019165
	elif (from_ == "years")        and (to == "milliseconds"): ans = val * 31557600000
	elif (from_ == "years")        and (to == "seconds"):      ans = val * 31557600
	elif (from_ == "years")        and (to == "minutes"):      ans = val * 525960
	elif (from_ == "years")        and (to == "hours"):        ans = val * 8766
	elif (from_ == "years")        and (to == "days"):         ans = val * 365.25
	elif (from_ == "years")        and (to == "weeks"):        ans = val * 52.17857
	else: ans = val
	return ans


def convert_data(from_, to, val):
	if   (from_ == "bits")        and (to == "bytes"):         ans = val * 0.125
	elif (from_ == "bits")        and (to == "kilobytes"):     ans = val * 0.000125
	elif (from_ == "bits")        and (to == "megabytes"):     ans = val * 0.000000125
	elif (from_ == "bits")        and (to == "gigabytes"):     ans = val * 0.000000000125
	elif (from_ == "bits")        and (to == "terabytes"):     ans = val * 0.000000000000125
	elif (from_ == "bytes")       and (to == "bits"):          ans = val * 8
	elif (from_ == "bytes")       and (to == "kilobytes"):     ans = val * 0.001
	elif (from_ == "bytes")       and (to == "megabytes"):     ans = val * 0.000001
	elif (from_ == "bytes")       and (to == "gigabytes"):     ans = val * 0.000000001
	elif (from_ == "bytes")       and (to == "terabytes"):     ans = val * 0.000000000001
	elif (from_ == "kilobytes")   and (to == "bits"):          ans = val * 8000
	elif (from_ == "kilobytes")   and (to == "bytes"):         ans = val * 1000
	elif (from_ == "kilobytes")   and (to == "megabytes"):     ans = val * 0.001
	elif (from_ == "kilobytes")   and (to == "gigabytes"):     ans = val * 0.000001
	elif (from_ == "kilobytes")   and (to == "terabytes"):     ans = val * 0.000000001
	elif (from_ == "megabytes")   and (to == "bits"):          ans = val * 8000000
	elif (from_ == "megabytes")   and (to == "bytes"):         ans = val * 1000000
	elif (from_ == "megabytes")   and (to == "kilobytes"):     ans = val * 1000
	elif (from_ == "megabytes")   and (to == "gigabytes"):     ans = val * 0.001
	elif (from_ == "megabytes")   and (to == "terabytes"):     ans = val * 0.000001
	elif (from_ == "gigabytes")   and (to == "bits"):          ans = val * 8000000000
	elif (from_ == "gigabytes")   and (to == "bytes"):         ans = val * 1000000000
	elif (from_ == "gigabytes")   and (to == "kilobytes"):     ans = val * 1000000
	elif (from_ == "gigabytes")   and (to == "megabytes"):     ans = val * 1000
	elif (from_ == "gigabytes")   and (to == "terabytes"):     ans = val * 0.001
	elif (from_ == "terabytes")   and (to == "bits"):          ans = val * 8000000000000
	elif (from_ == "terabytes")   and (to == "bytes"):         ans = val * 1000000000000
	elif (from_ == "terabytes")   and (to == "kilobytes"):     ans = val * 1000000000
	elif (from_ == "terabytes")   and (to == "megabytes"):     ans = val * 1000000
	elif (from_ == "terabytes")   and (to == "gigabytes"):     ans = val * 1000
	else: ans = val
	return ans


def convert_weight(from_, to, val):
	if   (from_ == "milligrams")  and (to == "grams"):         ans = val * 0.001
	elif (from_ == "milligrams")  and (to == "kilograms"):     ans = val * 0.000001
	elif (from_ == "milligrams")  and (to == "ounces"):        ans = val * 0.000035
	elif (from_ == "milligrams")  and (to == "pounds"):        ans = val * 0.000002
	elif (from_ == "milligrams")  and (to == "tons"):          ans = val * 0.000000001102311
	elif (from_ == "grams")       and (to == "milligrams"):    ans = val * 1000
	elif (from_ == "grams")       and (to == "kilograms"):     ans = val * 0.001
	elif (from_ == "grams")       and (to == "ounces"):        ans = val * 0.035274
	elif (from_ == "grams")       and (to == "pounds"):        ans = val * 0.002205
	elif (from_ == "grams")       and (to == "tons"):          ans = val * 0.000001
	elif (from_ == "kilograms")   and (to == "milligrams"):    ans = val * 1000000
	elif (from_ == "kilograms")   and (to == "grams"):         ans = val * 1000
	elif (from_ == "kilograms")   and (to == "ounces"):        ans = val * 35.27396
	elif (from_ == "kilograms")   and (to == "pounds"):        ans = val * 2.204623
	elif (from_ == "kilograms")   and (to == "tons"):          ans = val * 0.001102
	elif (from_ == "ounces")      and (to == "milligrams"):    ans = val * 28349.52
	elif (from_ == "ounces")      and (to == "grams"):         ans = val * 28.34952
	elif (from_ == "ounces")      and (to == "kilograms"):     ans = val * 0.02835
	elif (from_ == "ounces")      and (to == "pounds"):        ans = val * 0.0625
	elif (from_ == "ounces")      and (to == "tons"):          ans = val * 0.000031
	elif (from_ == "pounds")      and (to == "milligrams"):    ans = val * 453592.4
	elif (from_ == "pounds")      and (to == "grams"):         ans = val * 453.5924
	elif (from_ == "pounds")      and (to == "kilograms"):     ans = val * 0.453592
	elif (from_ == "pounds")      and (to == "ounces"):        ans = val * 16
	elif (from_ == "pounds")      and (to == "tons"):          ans = val * 0.0005
	elif (from_ == "tons")        and (to == "milligrams"):    ans = val * 907184740
	elif (from_ == "tons")        and (to == "grams"):         ans = val * 907184.7
	elif (from_ == "tons")        and (to == "kilograms"):     ans = val * 907.1847
	elif (from_ == "tons")        and (to == "ounces"):        ans = val * 32000
	elif (from_ == "tons")        and (to == "pounds"):        ans = val * 2000
	else: ans = val
	return ans


def convert_energy(from_, to, val):
	if   (from_ == "joules")       and (to == "volts"):        ans = val * 6.241509e+18
	elif (from_ == "joules")       and (to == "calories"):     ans = val * 0.000239
	elif (from_ == "volts")        and (to == "joules"):       ans = val * 1.602177e-19
	elif (from_ == "volts")        and (to == "calories"):     ans = val * 3.829294e-23
	elif (from_ == "calories")     and (to == "joules"):       ans = val * 4184
	elif (from_ == "calories")     and (to == "volts"):        ans = val * 2.611448e+22
	else: ans = val
	return ans


def convert_temp(from_, to, val):
	if   (from_ == "fahrenheit")   and (to == "celcius"):      ans = (val - 32) / 1.8
	elif (from_ == "celcius")      and (to == "fahrenheit"):   ans = 32 + (1.8 * val)
	else: ans = val
	return ans

