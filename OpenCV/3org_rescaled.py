#  your task is to see large video and also small rescaled video 

import cv2 as cv

# Function to rescale a frame
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Open video file or webcam (0 for default webcam)
# capture = cv.VideoCapture(0)
capture = cv.VideoCapture('videos/Waterfall.mp4')

while True:
    isTrue, frame = capture.read()

    if not isTrue:
        break  # Stop if video ends or cannot read frame

    # Rescale the frame
    frame_rescaled = rescaleFrame(frame, scale=0.5)  # You can adjust scale here

    # Show the original frame
    cv.imshow('Original Video', frame)

    # Show the rescaled frame
    cv.imshow('Rescaled Video', frame_rescaled)

    # Break the loop if 'd' key is pressed
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# Release the video capture object and close all windows
capture.release()
cv.destroyAllWindows()