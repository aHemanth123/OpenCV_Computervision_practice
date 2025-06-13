import cv2

# Load Haar cascade classifier
face_cascade = cv2.CascadeClassifier('17_haarcascade_frontalface.xml')

# Load the video
video_path = 'videos/group_people.mp4'  # Replace with your video file name
cap = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Total face count (non-unique, cumulative)
total_faces_detected = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break  # End of video

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors= 3)

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        total_faces_detected += 1
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('Face Detection', frame)

    # Press 'q' to quit early
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

# Show final count
print(f"Total face detections (non-unique): {total_faces_detected}")
