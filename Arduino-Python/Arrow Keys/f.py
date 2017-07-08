import curses
from curses import wrapper
import random
from random import choice
import serial
import time


#combining serial and keypresses using curses

ARDUINO =  "/dev/cu.usbmodemFA121"
ser =  serial.Serial(ARDUINO, 115200, timeout=5)

def main(scr):
    # Clear screen
    scr.clear()
    row = 2 #choice( range(2,10) )
    col = 2 #choice( range(2,10) )
    # scr.addstr(row,col, 'X')
    #scr.refresh()

    try:
        while True:
            msg = ser.readline()
            #print (msg)
            scr.addstr(row,col, str(msg))
            #time.sleep(1)
            c = scr.getkey()
            if c=='KEY_RIGHT':
                ser.write(b'1')
            elif c=='KEY_LEFT':
                ser.write(b'0')
            row +=1
            # if c in 'iw': row -= 1
            # if c in 'sk': row += 1
            # if c in 'aj': col -= 1
            # if c in 'dl': col += 1
            # scr.addstr(row,col, '*')
            scr.refresh()
    except Exception as e:
      #print("e is", e)
      scr.addstr(row,col, "e is" + str(e))
      time.sleep(3)
      scr.clear()
      ser.close()
    except:
      # print(" Bye! (ctrl + c)")
      scr.addstr(row,col, " Bye! (ctrl + c)")
      time.sleep(6)
      scr.clear()
      ser.close()
      print(" Bye! (ctrl + c)")

wrapper(main)
