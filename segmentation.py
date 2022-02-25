import cv2

background = None

def run_avg(img, avgWeight):
    global background
    
    if background is None:
        # Initialize the background
        background = img.copy().astype("float")
        return
    
    # Compute the Weighted Average
    cv2.accumulateWeighted(img, background, avgWeight)

def segment(img, threshold=25):
    global background
    
    # Calculate absolute difference between background and current frame
    diff = cv2.absdiff(background.astype("uint8"), img)
    
    # Threshold the difference to obtain foreground
    thresholded = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)[1]
    
    # Obatin the contours in the thresholded image
    (cnts, _) = cv2.findContours(thresholded.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Return None when no contours detected
    if len(cnts) == 0:
        return
    else:
        segmented = max(cnts, key=cv2.contourArea)
        return thresholded, segmented

def findTop(segmented):
    max_x = 0
    max_y = 0
    
    for x, y in segmented[0]:
        if (x > max_x):
            max_x = x
            max_y = y
    
    return max_x, max_y
