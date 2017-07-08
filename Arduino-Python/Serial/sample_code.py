import serial

ARDUINO =  "COM4"

def main():
  ser =  serial.Serial(ARDUINO, timeout=1)
  prevVal = None
  while 1:
      # Read the serial value
      ser.flushInput()
      serialValue = ser.readline().strip()
      # Catch any bad serial data:
      try:
          if serialValue != prevVal:
              # Print the value if it differs from the prevVal:
              print ("New Val: ", serialValue)
              prevVal = serialValue
      except ValueError:
          pass

if __name__ == '__main__':
  main()
