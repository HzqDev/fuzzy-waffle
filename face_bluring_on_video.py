import cv2

# Load the Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Start video capture from file
cap = cv2.VideoCapture("") # enter the actual file name of the video

# Set fast forward speed (e.g., skip every 3 frames for 3x speed)
skip_frames = 2  # Change this number for different speeds (1 = normal, 2 = 2x, 3 = 3x)

while True:
    # Read frame from the video
    ret, frame = cap.read()

    if not ret:
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Blur each detected face
    for (x, y, w, h) in faces:
        face_roi = frame[y:y+h, x:x+w]
        blurred_face = cv2.GaussianBlur(face_roi, (99, 99), 30)
        frame[y:y+h, x:x+w] = blurred_face

    # Display the resulting frame
    cv2.imshow("Blured Face Video", frame)

    # Skip the next 'skip_frames - 1' frames for fast forward
    for _ in range(skip_frames - 1):
        cap.read()

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()
