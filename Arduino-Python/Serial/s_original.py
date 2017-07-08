import serial
import time

ARDUINO =  "/dev/cu.usbmodemFA121"

def main():
  ser =  serial.Serial(ARDUINO, 115200, timeout=5)
  prevVal = None
  if True:
    time.sleep(1) # I shortened this to match the new value in your Arduino code
    # Serial read section
    msg = ser.read(ser.inWaiting()) # read all characters in buffer
    print ("Message from arduino: ")
    print (msg)
  ser.close()
    # i = i + 1
    #   print(" 42 ")
    #   # Read the serial value
    #   ser.flushInput()
    #   ser.flush()
    #   serialValue = ser.read().strip()
    #   # Catch any bad serial data:
    #   try:
    #       if serialValue != prevVal:
    #           # Print the value if it differs from the prevVal:
    #           print ("New Val: ", serialValue)
    #           prevVal = serialValue
    #   except ValueError:
    #       pass

if __name__ == '__main__':
  main()
