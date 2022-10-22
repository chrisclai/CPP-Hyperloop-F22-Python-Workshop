import numpy as np
import cv2
import imutils
import time
import json
from arucodetect import *

# Global Variables
a_id = -1

# Define webcam used
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Check for compatibility. If not, force search webcam
_, frame = webcam.read()
# print(frame)
try:
    if frame == None:
        webcam = cv2.VideoCapture(-1)
except:
    print("Webcam Detected First Try.")

while(True):
    start = time.time()
    # Grabbing frame from webcam
    _, frame = webcam.read()

    # Apply Grayscale
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur
    blur = cv2.GaussianBlur(grayscale, (9,9), 0)

    # Create Mask/Threshold
    threshold = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 23, 3)

    # Find AR Markers
    try:
        corners, ids = findArucoMarkers(frame, 6, 50)
        centerloc(frame, corners, ids)
    except Exception as e:
        #print(f"Exception! {e}")
        pass

    a_id = -1
    if not (ids is None):
        a_id = ids[0]
    text = ""
    
    match a_id:
        case 0:
            text = "State 0 detected. Rotating 360 degrees!"
        case 1:
            text = "State 1 detected. Bounce action initiated"
        case 2:
            text = "State 2 detected. Sequence of flips initiated"
        case 3:
            text = "State 3 detected. Landing the drone!"
            land = True
        case _:
            text = "No marker detected!"

    # place action on frame
    cv2.putText(frame, text, (10, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)

    # Find contours and filter using contour area
    cnts = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        area = cv2.contourArea(c)
        if area > 10:
            cv2.drawContours(frame, [c], -1, (36,255,12), 1)

    stop = time.time()

    seconds = stop - start

    # Calculate frames per second
    fps = 1 / seconds

    # Fps display
    cv2.putText(frame,"FPS: " + str(round(fps,2)), (50,450) ,cv2.FONT_HERSHEY_SIMPLEX, 0.75,(255,0,0),2)

    # Show frame
    # cv2.imshow('mask', threshold)
    cv2.imshow('webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('c'):
        cv2.imwrite('captured.jpg', frame)
        cv2.imwrite('mask.jpg', threshold)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Safely close all windows
webcam.release()
cv2.destroyAllWindows()