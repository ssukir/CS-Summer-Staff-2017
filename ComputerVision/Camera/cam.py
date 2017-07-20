# import cv2

# cv2.NamedWindow("w1", cv2.CV_WINDOW_AUTOSIZE)
# camera_index = 0
# capture = cv2.CaptureFromCAM(camera_index)

# def repeat():
#     global capture #declare as globals since we are assigning to them now
#     global camera_index
#     frame = cv.QueryFrame(capture)
#     cv.ShowImage("w1", frame)
#     c = cv.WaitKey(10)
#     if(c=="n"): #in "n" key is pressed while the popup window is in focus
#         camera_index += 1 #try the next camera index
#         capture = cv2.CaptureFromCAM(camera_index)
#         if not capture: #if the next camera index didn't work, reset to 0.
#             camera_index = 0
#             capture = cv2.CaptureFromCAM(camera_index)

# while True:
#     repeat()

'''
Simply display the contents of the webcam with optional mirroring using OpenCV
via the new Pythonic cv2 interface.  Press <esc> to quit.
'''

import cv2

def demo1(mirror=False):
    """
        just run it to see the video from the built-in webcam
        if CAPTURE_NUM = 0 doesn't work, try -1, 1, 2, 3
        (if none of those work, the webcam's not supported!)
    """
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        if mirror:
            img = cv2.flip(img, 1)
        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) == 27:
            break  # esc to quit
    cv2.destroyAllWindows()


import numpy as np






def demo3():
    """
        to demo:  click to bring focus to the messi image
        move mouse around and hit 'r' (lowercase r)
        a cyan rectangle should appear at your mouse
        hit spacebar to clear

        drawing reference:
          http://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html
    """
    # Create a black image, a window and bind the function to window
    # this is from here:
    FILE_NAME = "messi5.jpg"
    image_orig = cv2.imread(FILE_NAME, cv2.IMREAD_COLOR)
    #image_orig = cv2.cvtColor(image_orig, cv2.COLOR_BGR2RGB)
    image = image_orig.copy()
    current_mouse_pos = [0,0]  # not true yet...

    def mouse_handler(event,x,y,flags,param):
        """ a function that gets called on mouse events
            reference:
        """
        current_mouse_pos[0] = x
        current_mouse_pos[1] = y
        #print("The mouse is currently at", current_mouse_pos)
        if event == cv2.EVENT_LBUTTONDOWN: print("Left button clicked!")
        if event == cv2.EVENT_RBUTTONDOWN: print("Right button clicked!")

    cv2.namedWindow('image')
    cv2.setMouseCallback('image',mouse_handler)

    while True:
        cv2.imshow('image',image)

        """ key-press handling """
        k = cv2.waitKey(20) & 0xFF
        k_char = chr(k)
        if k_char == 'm': print('mmmm!')   # fun!
        if k_char == 'r':
            x, y = current_mouse_pos  # adjusted by the mouse_handler!
            DELTA = 42
            UL = (x-DELTA,y-DELTA)  # Upper Left
            LR = (x+DELTA,y+DELTA)  # Lower Right
            CLR = (255,255,0)  # color
            WIDTH = 1  # rectangle width
            cv2.rectangle( image, UL, LR, CLR, WIDTH )  # draw a rectangle
        if k_char == ' ': image = image_orig.copy() # clear by re-copying!
        if k == 27: # escape key has value 27 (no string represetation...)
            print("Quitting!")
            break
        """ end of key-press handling """

    # outside of the while True loop...
    cv2.destroyAllWindows()





if __name__ == '__main__':
    #demo3()
    #demo2()
    demo1()
