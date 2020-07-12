'''

File: Portfolio_Task2.py
Author: Jordan McCann
Student ID: 23571144

Purpose: To leverage OpenCV's Drawing Functions 
         in compilance with CW1's Portfolio Task 2

'''

# Library Imports 
import numpy as np
import cv2 # OpenCV

# Create Empty Image - Data Array - 1024
cv2.line(img, (0, 0), (1024, 1024), (30, 230, 0), 5)
cv2.line(img, (1024, 0), (0, 1024), (30, 230, 0), 5)

# Draw ellipse to image
cv2.ellipse(img, (256, 256), (120, 90), 0, 0, 180, 255, -1)

# Draw 3 Cricles to the Image
cv2.circle(img,(500, 75), 70, (0,0,255), -1)
cv2.circle(img,(350, 75), 70, (0,0,255), -1)
cv2.circle(img,(650, 75), 70, (0,0,255), -1)

# Draw Rectangle to Image
cv2.rectangle(img, (275, 5), (725, 150), (255, 255, 0), 3)


# Selected Font
font = cv2.FONT_HERSHEY_COMPLEX
name = "Jordan McCann - 23571144"
prompt = "Press Q to Quit Application"

# Draw Text
cv2.putText(img, name, (540, 525), font, 1, (255, 255, 255), 1, cv2.LINE_AA) # Draws the name to the image
cv2.putText(img, prompt, (0, 525), font, 1, (0, 0, 255), 2, cv2.LINE_AA) # Draws a prompt for the user to quit the application


# Polygon Shape
pts = np.array([[600, 200], [400, 500], [70, 20], 
                [600, 50], [650, 75], [875, 40]], np.int32) # 6 points 

# Draw Polygon onto Image
cv2.polylines(img, [pts], True, (0, 255, 255))

# Render the Image to the Window
cv2.imshow('Portfolio Task 2 - Jordan McCann - 23571144', img)
# While Forever (While the window is open)
while(True):    
    # If 'Q' key is pressed, close window and exit application
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

# Destroy the Window (All Windows that are open) - EXIT
cv2.destroyAllWindows()