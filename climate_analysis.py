climate_data = open('sc_climate_data10.csv', 'r')

""" Climate Analysis Tools """
import temp_conversion
import signal
signal.signal(signal.SIGPIPE,
signal.SIG_DFL)
import sys


filename = sys.argv[1]
climate_data = open(filename, 'r')
for line in climate_data:
	data = line.rstrip()
	data = data.split(',')
	if data[0][0] == '#':
		# don't want to process comment lines, which start with '#'
		pass
	else:
		# print 4th column (max temperature)
		fahr = float(data[3])
		celsius = temp_conversion.fahr_to_celsius(fahr)
		kelvin = temp_conversion.fahr_to_kelvin(fahr)
		print('Max temperature', data[3])
		print('Max temperature in Celsius:', celsius, 'kelvin', kelvin)