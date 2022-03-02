from numpy import absolute
import mouse

prev_x = 0
prev_y = 0
pressed = 0
pressed_btn = ''
frame = 0

def mouseAction(pList, max_x, max_y):
    global frame, pressed
    if(frame <= 20):
        frame = frame + 1
    else:
        if(pList[0][0] >= 0.97):
            buttonPress('left', max_x, max_y)    
        elif(pList[0][2] >= 0.95):
            mouse.right_click()
        elif(pList[0][4] >= 0.97):
            buttonPress('middle', max_x, max_y)    
        elif(pressed == 1):
            buttonRelease()
            
        if(pList[0][1] >= 0.85):
            mouseMove(max_x, max_y)
        elif(pList[0][3] >= 0.85):
            pass
        elif(pList[0][5] >= 0.85):
            scroll(max_x, max_y)
    

def buttonPress(mbutton, max_x, max_y):
    global pressed_btn, pressed
    if(pressed == 0):
            pressed_btn = mbutton
            pressed = 1
            mouse.press(button = pressed_btn)
    else:
        mouseMove(max_x, max_y)

def buttonRelease():
    global pressed_btn, pressed
    pressed = 0
    mouse.release(button = pressed_btn)

def mouseMove(max_x, max_y):
    global prev_x, prev_y
    x_neg, y_neg = 1, 1    
    x_diff = (max_x - prev_x)
    y_diff = (max_y - prev_y)
    if(absolute(x_diff) <= 20 and absolute(y_diff) <= 20):
        if(x_diff < 0):
            x_neg = -1
        if(y_diff < 0):
            y_neg = -1
            
        move_x = x_neg * (x_diff ** 2)
        move_y = y_neg * (y_diff ** 2)
        
        mouse.move(move_x, move_y, absolute = False)
    
    prev_x = max_x
    prev_y = max_y

def scroll(max_x, max_y):
    global prev_x, prev_y
    diff = max_y - prev_y
    mouse.wheel(diff)
    prev_x = max_x
    prev_y = max_y