from numpy import absolute
import mouse

prev_x = 0
prev_y = 0
action = 0


def mouseAction(pList, max_x, max_y):
    global action
    if(pList[0][1] >= 0.85):
        action = 1
    
    if (action == 1):
        mouseMove(max_x, max_y)

def mouseMove(max_x, max_y):
    global prev_x, prev_y
    x_neg, y_neg = 1, 1    
    x_diff = (max_x - prev_x)
    y_diff = (max_y - prev_y)
    if(x_diff <= 20 and y_diff <= 20):
        if(x_diff < 0):
            x_neg = -1
        if(y_diff < 0):
            y_neg = -1
            
        move_x = x_neg * (x_diff ** 2) / 2
        move_y = y_neg * (y_diff ** 2) / 2
        
        mouse.move(move_x, move_y, absolute = False)
    
    prev_x = max_x
    prev_y = max_y