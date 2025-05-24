import cv2, cv2.data

adding = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
image = cv2.imread("download.jpg")#enter the name of the imgea
if image is None:
    print("sorry we wasnt able to read the iamge to detec face")
    exit()
scaling = 600 / image.shape[1]
new_width = 600
new_height = int(image.shape[0] * scaling)
resizing = cv2.resize(image, (new_width, new_height))

graying = cv2.cvtColor(resizing, cv2.COLOR_BGR2GRAY)

face_detecting  = adding.detectMultiScale(graying, scaleFactor=1.1, minNeighbors=5)

print(f"we were able to detect {len(face_detecting)} face(s)")

for (x, y, w, h) in face_detecting:
    cv2.rectangle(resizing, (x, y), (x+w, y+h), (0, 255, 0), 5)

cv2.imshow("faces detected", resizing)
cv2.waitKey(0)
cv2.destroyAllWindows()