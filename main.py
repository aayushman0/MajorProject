import cv2
import predict

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

if __name__ == "__main__":
    # Initialize Running Average Weight
    avgWeight = 0.5

    cam = cv2.VideoCapture(0)
    
    # Co ordinates for Region of Interest
    T = 10
    B = 250
    R = 350
    L = 650
    
    # Initialize no. of frames
    frame_no = 0
    
    while(True):
        # Get the current frame
        (_, frame) = cam.read()
        
        #Resize and flip the frame
        (height, width) = frame.shape[:2]
        ratio = width / height
        w = 700
        h = int(w / ratio)
        
        frame = cv2.resize(frame, (w, h))
        frame = cv2.flip(frame, 1)
        
        clone = frame.copy()
        
        # Get the region of interest
        roi = frame[T:B, R:L]
        
        #Convert the roi to grayscale and apply Gaussian blur
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray,(7, 7), 0)
        
        if (frame_no < 30):
            # Use the first 30 frames to set the background
            run_avg(gray, avgWeight)
        else:
            # Segment the hand region
            hand = segment(gray)
            
            # Check for segmentaion
            if hand is not None:
                # Get the thresholded image and the segmented region
                (thresholded, segmented) = hand
                
                # Show the segmented image
                cv2.drawContours(clone, [segmented + (R, T)], -1, (0, 0, 255))
                cv2.imshow("Thresholded Image", thresholded)
                predicted_vals = predict.predict(thresholded)
                cv2.putText(clone, predicted_vals,(10, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (125, 125, 125), 2, cv2.LINE_AA)
            
         # Represent the Region of Interest
        cv2.rectangle(clone, (L, T), (R, B), (0, 255, 0), 2)
            
        frame_no += 1
            
        # Show a video output
        cv2.imshow("Video Output", clone)
            
        #End the loop when 'f' is pressed
        end = cv2.waitKey(1) & 0xFF
        if end == ord('f'):
            break
            
    cam.release()
    cv2.destroyAllWindows()