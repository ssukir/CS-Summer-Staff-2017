import serial
import time

ARDUINO =  "/dev/cu.usbmodemFA121"

ser =  serial.Serial(ARDUINO, 115200, timeout=5)
msg = ser.readline()      #  (ser.inWaiting()) # read all characters in buffer
print (msg)

ser.close()




