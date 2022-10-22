import numpy as np
import cv2
import imutils
import time
import json

# Define my webcam
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Compatibility checker
# 1. Try to read a frame from the webcam
# 2. If it doesn't exist, switch webcam references
_, frame = webcam.read() 
print(frame)
try:
    if not frame:
        webcam = cv2.VideoCapture(-1)
except Exception as e:
    print(f"Webcam detected first try: {e}")

while True:
    start = time.time()
    
    # Grab a frame from the webcam
    _, frame = webcam.read()

    # Apply Grayscale Filter
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur to get rid of null values
    blur = cv2.GaussianBlur(grayscale, (9,9), 0)

    # Apply Adaptive Threshold Filter
    threshold = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 23, 3)

    # Find contours
    cnts = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        area = cv2.contourArea(c)
        if area > 10: # 10 being a threshold value in pixels
            cv2.drawContours(frame, [c], -1, (36, 255, 12), 1)

    stop = time.time()

    deltatime = stop - start

    # Calculate frames per second
    if not deltatime:
        fps = 0
    else:
        fps = 1 / deltatime

    # Display FPS on the screen
    cv2.putText(frame, "FPS: " + str(round(fps, 2)), (50, 450), cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 0, 0), 2)

    # shows the current frame to the screen
    cv2.imshow('webcam', frame)
    cv2.imshow('filter', threshold)

    # Failsafe (If we want to quit the program)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Safely close all windows
webcam.release()
cv2.destroyAllWindows()
