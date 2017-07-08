import curses
from curses import wrapper
import time

def main(scr):
    # Clear screen
    scr.clear()

    row = 2
    col = 2

    while row < curses.LINES:
        c = scr.getkey()
        if c == 'KEY_RIGHT':
            scr.addstr(row,col, "Right")
        elif c == 'KEY_LEFT':
            scr.addstr(row,col, "Left")
        elif c == 'KEY_UP':
            scr.addstr(row,col, "Up")
        elif c == 'KEY_DOWN':
            scr.addstr(row,col, "Down")
        elif c == 'Q':
            scr.addstr(row,col, "Bye!")
            scr.refresh()
            time.sleep(1)
            break
        row += 1
        scr.refresh()


wrapper(main)
