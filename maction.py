from numpy import absolute
import pyautogui as pg

prev_x = 0
prev_y = 0
md = 0
pg.FAILSAFE = False

def mouseAction(pList, max_x, max_y):
    global md
    if(pList[0][0] >= 0.85 and md == 0):
        pg.mouseDown()
        md = 1
    elif(pList[0][0] >= 0.85 and md == 1):
        mouseMove(max_x, max_y)
    else:
        md = 0
        pg.mouseUp()
    
    if(pList[0][1] >= 0.85):
        mouseMove(max_x, max_y)
    elif(pList[0][2] >= 0.85):
        pg.rightClick()
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
        
        pg.move(move_x, move_y)
    
    prev_x = max_x
    prev_y = max_y
    
