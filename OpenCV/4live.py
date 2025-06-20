import cv2 as cv

 def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Function to change resolution for --------------    live video (webcam)
# This method works by setting the capture object's properties directly
def changeRes(capture_obj, width, height):
    capture_obj.set(3, width) # 3 corresponds to CAP_PROP_FRAME_WIDTH
    capture_obj.set(4, height) # 4 corresponds to CAP_PROP_FRAME_HEIGHT

# Here's more about the commonly used propId values:

# Property ID	Constant	Description
# 0	cv.CAP_PROP_POS_MSEC	Current position of the video file in milliseconds.
# 1	cv.CAP_PROP_POS_FRAMES	0-based index of the next frame to be captured.
# 2	cv.CAP_PROP_POS_AVI_RATIO	Relative position of the video file: 0 = start, 1 = end.
# 3	cv.CAP_PROP_FRAME_WIDTH	Width of the frames in the video stream.
# 4	cv.CAP_PROP_FRAME_HEIGHT	Height of the frames in the video stream.
# 5	cv.CAP_PROP_FPS	Frame rate (frames per second).
# 6	cv.CAP_PROP_FOURCC	4-character code of codec (e.g., 'MJPG').
# 7	cv.CAP_PROP_FRAME_COUNT	Total number of frames in the video file.
# 10	cv.CAP_PROP_BRIGHTNESS	Brightness of the image (only for cameras).
# 11	cv.CAP_PROP_CONTRAST	Contrast of the image (only for cameras).
# 12	cv.CAP_PROP_SATURATION	Saturation (only for cameras).
# 13	cv.CAP_PROP_HUE	Hue (only for cameras).
# 14	cv.CAP_PROP_GAIN	Gain (camera-specific setting).
# 15	cv.CAP_PROP_EXPOSURE	Exposure (camera-specific setting).

# Set property 0: Position in milliseconds (for videos)
# capture_obj.set(0, 5000)  # Jump to 5000 ms (5 seconds) in the video

# Set property 1: Position in frames (for videos)
# capture_obj.set(1, 100)   # Jump to the 100th frame

# Set property 2: Relative position (0.0 = start, 1.0 = end)
# capture_obj.set(2, 0.5)   # Jump to the middle of the video

# Set property 3: Frame width (for camera)
# capture_obj.set(3, 640)   # Set width to 640 pixels

# Set property 4: Frame height (for camera)
# capture_obj.set(4, 480)   # Set height to 480 pixels

# Set property 5: Frames per second (some cameras may ignore this)
# capture_obj.set(5, 30)    # Attempt to set FPS to 30

# Set property 6: FOURCC codec (used only when writing video)
# Must be set using cv.VideoWriter, not usually useful here

# Set property 7: Total number of frames – cannot be set (read-only)

# Set property 10: Brightness (0–255 range, varies by camera)
# capture_obj.set(10, 150)  # Increase brightness

# Set property 11: Contrast (range varies)
# capture_obj.set(11, 50)   # Set contrast

# Set property 12: Saturation
# capture_obj.set(12, 100)  # Adjust saturation

# Set property 13: Hue
# capture_obj.set(13, 50)   # Adjust hue

# Set property 14: Gain
# capture_obj.set(14, 30)   # Set gain

# Set property 15: Exposure
# capture_obj.set(15, -5)   # Lower value = longer exposure (may require auto exposure off)

# ---------------------------------------------------------


# --- Live Video (Webcam) Example ---
print("--- Starting Live Webcam Feed ---")
capture_live = cv.VideoCapture(0)  

# Check if webcam opened successfully
if not capture_live.isOpened():
    print("Error: Could not open webcam for live feed.")
else:
    # Use changeRes to set a specific resolution for the live feed
    # Note: Not all webcams support all resolutions. It will try its best.
    print(f"Attempting to set live feed resolution to 640x480...")
    changeRes(capture_live, 640, 480) # Set desired resolution for live stream

    while True:
        isTrue, frame_live = capture_live.read()

        if not isTrue:
            print("Error: Could not read frame from live webcam. Exiting...")
            break

        # For live feed, if you used changeRes, the 'frame_live' is already at the new resolution.
        # So, 'rescaleFrame' might be used for further scaling if needed, or just display the current 'frame_live'.
        # Here, we'll display the frame obtained after changeRes and a further rescaled one.
        frame_live_rescaled_further = rescaleFrame(frame_live, scale=0.75) # Further scale down for display

        cv.imshow('Live Feed (After changeRes)', frame_live)
        cv.imshow('Live Feed (Further Rescaled)', frame_live_rescaled_further)

        if cv.waitKey(1) & 0xFF == ord('d'): # Shorter waitKey for live video responsiveness
            break

    capture_live.release()
    cv.destroyAllWindows() # Close windows opened by live feed

# --- Existing Video File Example (for comparison) ---
print("\n--- Starting Existing Video File Example ---")
capture_file = cv.VideoCapture('videos/Waterfall.mp4') # Make sure this path is correct

if not capture_file.isOpened():
    print("Error: Could not open video file.")
else:
    while True:
        isTrue, frame_file = capture_file.read()

        if not isTrue:
            print("Video file ended or could not read frame. Exiting...")
            break

        # For existing video files, you CANNOT use changeRes().
        # The resolution is fixed by the video file itself.
        # You can only rescale the frame *after* reading it.
        frame_file_rescaled = rescaleFrame(frame_file, scale=0.5)

        cv.imshow('Original Video File', frame_file)
        cv.imshow('Rescaled Video File', frame_file_rescaled)

        if cv.waitKey(20) & 0xFF == ord('d'):
            break

    capture_file.release()
    cv.destroyAllWindows() # Close windows opened by video file
