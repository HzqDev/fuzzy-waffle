import cv2
import threading
from ultralytics import YOLO
from PIL import Image, ImageTk
import tkinter as tk

# Load YOLO model
model = YOLO("yolov8n.pt")

# Create GUI window
root = tk.Tk()
root.title("YOLO Object Detection")
root.geometry("900x700")

# Label to show video
video_label = tk.Label(root)
video_label.pack()

# Global variables
running = False
cap = None

def start_camera():
    global running, cap
    if not running:
        running = True
        cap = cv2.VideoCapture(0)
        thread = threading.Thread(target=update_frame)
        thread.start()

def stop_camera():
    global running, cap
    running = False
    if cap:
        cap.release()

def update_frame():
    global running, cap
    while running:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Run YOLO detection
        results = model(frame)
        annotated_frame = results[0].plot()

        # Convert frame to Tkinter format
        img = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(image=img)

        video_label.config(image=img)
        video_label.image = img

    stop_camera()

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

start_btn = tk.Button(btn_frame, text="Start Detection", command=start_camera, bg="green", fg="white", font=("Arial", 12))
start_btn.grid(row=0, column=0, padx=10)

stop_btn = tk.Button(btn_frame, text="Stop Detection", command=stop_camera, bg="red", fg="white", font=("Arial", 12))
stop_btn.grid(row=0, column=1, padx=10)

root.mainloop()
