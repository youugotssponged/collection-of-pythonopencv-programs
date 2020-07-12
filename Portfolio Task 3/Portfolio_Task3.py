'''

File: Portfolio_Task3.py
Author: Jordan McCann
Student ID: 23571144

Purpose: To create a program that recognises a user's gestures

'''

# Library Imports
import cv2
import numpy as np

# Open Camera
camera = cv2.VideoCapture(0)
camera.set(0, 100)

# LOADED CLASSIFIERS
face = cv2.CascadeClassifier('haarcascades/face.xml')
hand = cv2.CascadeClassifier('haarcascades/Hand.Cascade.1.xml')
eye = cv2.CascadeClassifier('haarcascades/haar-cascade-extra-github/haarcascade_eye.xml')

# Function for simulating a fun little program prompting the user to put their hands up and reacts to the user's actions
# registering:
#	hands, eyes, faces -> gestures
#	reacts upon what's happening within the window	
def hands_up(img, colourScale):
	# Detects every frame if there is an object of type hand, face, eye from the loaded classifiers
    hands = hand.detectMultiScale(colourScale, 1.3, 5)
    faces = face.detectMultiScale(colourScale, 1.3, 5)
    eyes = eye.detectMultiScale(colourScale, 1.3, 5)

    # Draw Initial Text Prompt
    img = cv2.putText(img, "Put your hands up!", (120, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 1, cv2.LINE_AA)
    
	# Create and set initial variables
    isRight = False
    isLeft = False
    isHiding = False
    
	# For each hand
    for (x, y, w, h) in hands:
		# Draw the hand's bounds
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
		# Draw text on the hand's bounds signifying it's a hand
        img = cv2.putText(img, "HAND", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
			
		# If the hand is placed on the right hand side of the window
        if x > 320:
            isRight = True # set the isRight variable to true
            print("RIGHT SIDE") # Print for debugging
		
		# If the hand is placed on the left hand side of the window
        if x < 320:
            isLeft = True # set the isLeft variable to true
            print("LEFT SIDE") # Print for debugging
            
        # If both hands are shown and are placed on the top part of the window 
        if isLeft and isRight and y < 240:
			# Show prompt text
            img = cv2.putText(img, "YOU'RE UNDER ARREST", (120, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            # Reset isLeft and isRight
            isLeft = False 
            isRight = False
        
		# If both hands are shown and are placed on the bottom part of the window 		
        if isLeft and isRight and y > 240:
			# Show prompt text
            img = cv2.putText(img, "PUT THEM BACK UP!", (120, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
			# Reset isLeft and isRight
            isLeft = False
            isRight = False
    
	# For each face
    for (x, y, w, h) in faces:
		# Draw face bounds
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
		# Add and render text on the face bounds
        img = cv2.putText(img, "FACE", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
		# Set isHiding to True simulating the user isn't hiding - by default
        isHiding = True       
    
	# For each eye
    for(ex ,ey, ew, eh) in eyes:
		# draw eye bounds
        img = cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        isHiding = False # Set false simulating the user isn't hiding upon eyes being detected
		
    # If the user is hiding 
    if isHiding:
        print("WHERED YOU GO?!") # Debug
        img = cv2.putText(img, "Where did you go?!", (120, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 1, cv2.LINE_AA) # Draw prompt
		
	# If the user is not hiding 
    elif isHiding == False:
        print("I SEE YOU!") # Debug
        img = cv2.putText(img, "I SEE YOU!", (120, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 1, cv2.LINE_AA) # Draw prompt
 
        
    
# While the camera is open / recieving feed
while camera.isOpened():
	# Read from the camera
    ret, img = camera.read()

	# If ret is true
    if(ret):
		# Set the colour scale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
		# Run the hands_up function
        hands_up(img, gray)
        
		# Show to the screen
        cv2.imshow('23571144 - Portfolio Task 3', img)
		
		# Listen for a keypress
        k = cv2.waitKey(10)
		
		# If the key pressed was the escape key, exit program
        if k == 27:  # press ESC to exit
            break
    else:
        break
    
    
# Clean up any current window data and close the window
camera.release()
cv2.destroyAllWindows()