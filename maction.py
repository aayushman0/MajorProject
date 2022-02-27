from numpy import absolute
import mouse

prev_x = 0
prev_y = 0
action = 0
clicked = 0

def mouseAction(pList, max_x, max_y):
    global action, clicked
    if(pList[0][0] >= 0.85 and clicked == 0):
        #mouse.click('left')
        clicked = 1
    elif(pList[0][1] >= 0.85):
        action = 1
        clicked = 0
    elif(pList[0][2] >= 0.85):
        #mouse.click('right')
        clicked = 1
    elif(pList[0][5] >= 0.85):
        action = 2
        
        
    if(action == 1):
        mouseMove(max_x, max_y)
    elif(action == 2):
        scroll(max_x, max_y)

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
    
def scroll(max_x, max_y):
    global prev_x, prev_y
    x_diff = max_x - prev_x
    
    if(x_diff > 2):
        mouse.wheel(1)
    elif(x_diff <-2):
        mouse.wheel(-1)
    
    prev_x = max_x
    prev_y = max_y