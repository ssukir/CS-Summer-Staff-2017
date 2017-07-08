import serial
import time

ARDUINO =  "/dev/cu.usbmodemFA121"
ser =  serial.Serial(ARDUINO, 115200, timeout=5)
c = 0
try:
  while True:
    c+=1
    msg = ser.readline()
    print (msg)
    time.sleep(1)
    if c%2==0:
        ser.write(b"1")
    elif c%2==1:
        ser.write(b"0")
    # ser.flush()
except Exception as e:
  print("e is", e)
  ser.close()
except:
  print(" Bye! (ctrl + c)")
  ser.close()
