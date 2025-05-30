import cv2
import cv2.data
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

if face_cascade.empty():
    raise IOError("cannot load 'haarcascade_frontalface_default.xml'")

cap = cv2.VideoCapture("Guy Counts To 1 Million In One Take [ World Record ].mp4")

frame_count = 0

while True:
    ret,frame = cap.read()
    if not ret:
        messagebox.showinfo("Info","end of the video cannot read any more frames")
        break
    frame_count += 1

    # if frame_count % 3 == 0:
    small_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5 )
    gray = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.8, minNeighbors=2)

    for (x, y, w, h) in faces:
            x1, y1, w1, h1 = int(x*2), int(y*2), int(w*2), int(h*2)
            cv2.rectangle(frame, (x1,y1),(x1+w1,y1+h1),(0, 244, 0), 5)

    cv2.imshow("Face Detection on Video", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        messagebox.showinfo("warning", "User interrupted")
        break
root.destroy()
cap.release
cv2.destroyAllWindows()