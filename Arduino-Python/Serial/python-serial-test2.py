import serial
arduino = serial.Serial('/dev/cu.usbmodemFA121', 9600, timeout=.1)
while True:
	data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
	if data:
		print (data)
