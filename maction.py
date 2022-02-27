from numpy import absolute
import mouse

prev_x = 0
prev_y = 0
clicked = 0
frame = 0

def mouseAction(pList, max_x, max_y):
    global clicked, frame
    if(frame <= 120):
        frame = frame + 1
    else:
    
        if(clicked == 0):
            clicked = 1
            if(pList[0][0] >= 0.95):
                mouse.click('left')
            elif(pList[0][2] >= 0.95):
                mouse.click('right')
            else:
                clicked = 0
    
        if(pList[0][1] >= 0.85):
            mouseMove(max_x, max_y)
            clicked = 0
        elif(pList[0][3] >= 0.85):
            pass
        elif(pList[0][4] >= 0.85):
            pass
        elif(pList[0][5] >= 0.85):
            pass
        

def mouseMove(max_x, max_y):
    global prev_x, prev_y
    x_neg, y_neg = 1, 1    
    x_diff = (max_x - prev_x)
    y_diff = (max_y - prev_y)
    if(x_diff <= 30 and y_diff <= 30):
        if(x_diff < 0):
            x_neg = -1
        if(y_diff < 0):
            y_neg = -1
            
        move_x = x_neg * (x_diff ** 2) / 2
        move_y = y_neg * (y_diff ** 2) / 2
        
        mouse.move(move_x, move_y, absolute = False)
    
    prev_x = max_x
    prev_y = max_y
