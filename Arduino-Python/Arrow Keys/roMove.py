import curses
from curses import wrapper
import time
import serial

ARDUINO =  "/dev/cu.usbmodemFA121"
ser =  serial.Serial(ARDUINO, 115200, timeout=5)

def main(scr):
    # Clear screen
    scr.clear()

    row = 2
    col = 2

    while True:
        c = scr.getkey()
        if c == 'KEY_RIGHT':
            ser.write(b'3')
        elif c == 'KEY_LEFT':
            ser.write(b'2')
        elif c == 'KEY_UP':
            ser.write(b'0')
        elif c == 'KEY_DOWN':
            ser.write(b'1')
        elif c == 'Q':
            scr.addstr(row, col, "Bye!")
            scr.refresh()
            time.sleep(1)
            break
        row += 1
        scr.refresh()

wrapper(main)
