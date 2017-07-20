import serial
import time

ARDUINO =  "/dev/cu.usbmodemFA121"
ser =  serial.Serial(ARDUINO, 115200, timeout=5)

try:
  while True:
    msg = ser.readline()      #  (ser.inWaiting()) # read all characters in buffer
    print (msg)
    time.sleep(1)
except:
  print("Control c !")
  ser.close()




