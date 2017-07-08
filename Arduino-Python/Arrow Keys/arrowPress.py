#up: '\x1b[A'
#down: '\x1b[B'
#right: '\x1b[C'
#left: '\x1b[D'

import sys
import serial
import time

ARDUINO =  "/dev/cu.usbmodemFA121"
ser =  serial.Serial(ARDUINO, 115200, timeout=5)

# key Presses
try:
    import tty, termios
except ImportError:
    # Probably Windows.
    try:
        import msvcrt
    except ImportError:
        # FIXME what to do on other platforms?
        # Just give up here.
        raise ImportError('getch not available')
    else:
        getch = msvcrt.getch
else:
    def getch():
        """getch() -> key character

        Read a single keypress from stdin and return the resulting character.
        Nothing is echoed to the console. This call will block if a keypress
        is not already available, but will not wait for Enter to be pressed.

        If the pressed key was a modifier key, nothing will be detected; if
        it were a special function key, it may return the first character of
        of an escape sequence, leaving additional characters in the buffer.
        """
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch




while True:
    result = getch()
    print(result)
    if result == 'o':
        ser.write(b"1")
    elif result == 'p':
        ser.write(b"0")
    if result == 'Q':
        break



# if getch() == '\x1b[A':
#     print('up')
