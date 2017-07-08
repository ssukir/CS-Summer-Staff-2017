from curses import wrapper

from random import choice



def main(scr):
    # Clear screen
    scr.clear()
    row = choice( range(2,10) )
    col = choice( range(2,10) )
    scr.addstr(row,col, 'X')
    scr.refresh()

    x = 0
    while x < 24:
        x += 1

        c = scr.getkey()
        if c in 'iw': row -= 1
        if c in 'sk': row += 1
        if c in 'aj': col -= 1
        if c in 'dl': col += 1
        scr.addstr(row,col, '*')
        scr.refresh()



        dir = choice('NEWS')




wrapper(main)
