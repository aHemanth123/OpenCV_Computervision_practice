import cv2 as cv

# Function to rescale a frame (for displaying  -----------  existing/downloaded  videos or when changeRes isn't used)
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

# --- Live Video (Webcam) Example ---
print("--- Starting Live Webcam Feed ---")
capture_live = cv.VideoCapture(0) # Open default webcam

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