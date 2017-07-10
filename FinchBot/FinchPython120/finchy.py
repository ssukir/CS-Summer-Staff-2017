import curses
from curses import wrapper
import time
from finch import Finch
from time import sleep, time

finch = Finch()
finch.led(255, 0, 0)

def main(scr):
    # Clear screen
    scr.clear()

    row = 2
    col = 2

    while True:
        c = scr.getkey()
        if c == 'KEY_RIGHT':
            # scr.addstr(row,col, "Right")
            finch.led(0, 0, 255)
            finch.wheels(2.0, -0.5)
        elif c == 'KEY_LEFT':
            # scr.addstr(row,col, "Left")
            finch.led(0, 0, 255)
            finch.wheels(-0.5, 2.0)
        elif c == 'KEY_UP':
            # scr.addstr(row,col, "Up")
            finch.led(0, 0, 255)
            finch.wheels(1.0, 1.0)
        elif c == 'KEY_DOWN':
            # scr.addstr(row,col, "Down")
            finch.led(0, 0, 255)
            finch.wheels(-1.0, -1.0)
        elif c == 'Q':
            finch.wheels(0, 0)
            finch.led(255, 0, 0)
            scr.addstr(row, col, "Bye!")
            scr.refresh()
            time.sleep(1)
            break
        row += 1
        scr.refresh()

wrapper(main)
finch.led(0, 0, 0)
finch.wheels(0, 0)
