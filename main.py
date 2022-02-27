import cv2
import predict
import segmentation
import maction


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
            segmentation.run_avg(gray, avgWeight)
        else:
            # Segment the hand region
            hand = segmentation.segment(gray)
            
            # Check for segmentaion
            if hand is not None:
                # Get the thresholded image and the segmented region
                (thresholded, segmented) = hand
                
                # Show the segmented image
                cv2.drawContours(clone, [segmented + (R, T)], -1, (0, 0, 255))
                max_x, max_y = segmentation.findTop(segmented)
                cv2.circle(clone, (max_x + R, max_y + T), 3, (255, 0, 0), -1)
                cv2.imshow("Thresholded Image", thresholded)
                predicted_vals, pList = predict.predict(thresholded)
                cv2.putText(clone, predicted_vals,(10, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (125, 125, 125), 2, cv2.LINE_AA)
                
                maction.mouseAction(pList, max_x, max_y)
            
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