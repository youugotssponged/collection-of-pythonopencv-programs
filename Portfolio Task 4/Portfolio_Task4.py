'''

File: Portfolio_Task4.py
Author: Jordan McCann
Student ID: 23571144

Purpose: To utilise the user's gestures in filling a 
			pre-drawn shape with a colour.
            
'''

# Library Imports
import cv2
import numpy as np

# Initialise Camera
camera = cv2.VideoCapture(0)
camera.set(0, 100)

# Set hand classifier
hand = cv2.CascadeClassifier('haarcascades/Hand.Cascade.1.xml')

# is the Shape filled Variables
isSquareFilled = False
isRectFilled = False
isCircleFilled = False
isEllipseFilled = False
isTriangleFilled = False

# Reset area
isResetArea = False

# Colors to switch to
squareColour = (0, 0, 255) # Red
circleColour = (0, 255, 0) # Green
ellipseColour = (0, 255, 255) # Yellow
rectangleColour = (255, 0, 0) # Blue
triangleColour = (255, 255, 0) # Cyan



##################################
# While the camera is open / on
while camera.isOpened():
    ret, img = camera.read()
    
    if(ret):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Draw Shapes and their colors and check if they have been filled or not
        if isSquareFilled == False:
            cv2.rectangle(img, (20, 20), (150, 150), (255, 255, 255), -1) # Square
        else:
            cv2.rectangle(img, (20, 20), (150, 150), squareColour, -1) # Square
        
        if isCircleFilled == False:
            cv2.circle(img, (250, 90), 70, (255, 255, 255), -1) # Circle
        else:
            cv2.circle(img, (250, 90), 70, circleColour, -1) # Circle
            
        if isEllipseFilled == False:
            cv2.ellipse(img, (400, 90), (50, 50), 0, 0, 180, (255, 255, 255), -1) # Ellipse
        else:
            cv2.ellipse(img, (400, 90), (50, 50), 0, 0, 180, ellipseColour, -1) # Ellipse
            
        if isRectFilled == False:
            cv2.rectangle(img, (500, 20), (550, 150), (255, 255, 255), -1) # Rectangle
        else:
            cv2.rectangle(img, (500, 20), (550, 150), rectangleColour, -1) # Rectangle
        
        
        # Define triangle points
        trianglePoints = np.array([[60, 250], [10, 350], [120, 350]], np.int32)
        # Reshape array
        pts = trianglePoints.reshape((-1, 1, 2))
        # Draw lines within the triangle points
        cv2.polylines(img, [pts], True, (100, 100, 100), 2)
        
        
        if(isTriangleFilled):
            cv2.fillPoly(img, [pts], triangleColour)
        else:
            cv2.fillPoly(img, [pts], (255, 255, 255))
        
        # Draw Reset area and reset text
        cv2.rectangle(img, (500, 350), (640, 480), (0, 0, 255), -1)
        cv2.putText(img, "RESET", (520, 425), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        
        
        # Detect hand
        hands = hand.detectMultiScale(gray, 1.3, 5)
        
        # For every hand
        for (x, y, w, h) in hands:
            # Draw hand bounds
            img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
            
            # Reset Area
            if (y+h) >= 350 and (x+w) >= 500:
                print("RESETTING...")
                # Reset bools
                isRectFilled = False
                isCircleFilled = False
                isEllipseFilled = False
                isTriangleFilled = False
                isSquareFilled = False
                
            
            # Check if Square should be filled
            if(isSquareFilled == False):
                # If the hand is inside the square shape bounds
                if x >= 20 and y >= 20 and (x+w) <= 150 and (y+h) <= 150:
                    isSquareFilled = True
                    print("Square has been filled")
            
            # Check if Circle should be filled
            if(isCircleFilled == False):
                # if hand is within bounds of the circle
                if x >= 180 and x <= 320 and y >= 20 and y <= 90:
                    print("Circle has been filled") # debug
                    isCircleFilled = True # set True

            # Check if Ellipse should be filled                    
            if(isEllipseFilled == False):
                # if hand is within bounds of the Ellipse
                if x >= 350 and x <= 400 and y >= 40 and y <= 90:
                    print("Ellipse has been filled")
                    isEllipseFilled = True
            
            # Check if Rectangle should be filled
            if(isRectFilled == False):
                # if hand is within bounds of the Rectangle
                if x >= 500 and x <= 550 and y >= 20 and y <= 150:
                    print("Rect has been filled")
                    isRectFilled = True
            
            # Check if Triangle should be filled
            if(isTriangleFilled == False):
                # if hand is within bounds of the Triangle
                if x >= 10 and x <= 60 and y >= 250 and y <= 350:
                    print("Triangle has been filled")
                    isTriangleFilled = True
            
            # Prompt user if they fill in all the shapes with
            # A well done message
            if(isTriangleFilled and 
               isRectFilled and 
               isEllipseFilled and 
               isCircleFilled and 
               isSquareFilled):
                cv2.putText(img, "WELL DONE!", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
            
                
        
        
        # Render image
        cv2.imshow('23571144 - Portfolio Task 4', img)
        # Register Key Press
        k = cv2.waitKey(10)
        
        # If escape has been pressed, exit program
        if k == 27:
            break
    else:
        break
###########################    

# Release any cam data that's stored in memory
camera.release()
# Destroy the window
cv2.destroyAllWindows()
