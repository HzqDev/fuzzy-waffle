import cv2
import cv2.data
import tkinter as tk
from tkinter import simpledialog, messagebox

def detect_faces():
    image_name = simpledialog.askstring("Image Input", "Enter the image file name (with extension):")
    if not image_name:
        messagebox.showerror("Error", "No image name provided.")
        return

    image = cv2.imread(image_name)
    if image is None:
        messagebox.showerror("Error", "Could not read the image. Check the file name and location.")
        return

    scaling = 600 / image.shape[1]
    new_width = 600
    new_height = int(image.shape[0] * scaling)
    resized = cv2.resize(image, (new_width, new_height))

    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    messagebox.showinfo("Result", f"We detected {len(faces)} face(s) in the image.")

    for (x, y, w, h) in faces:
        cv2.rectangle(resized, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Faces Detected", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Tkinter window
root = tk.Tk()
root.title("Face Detector")
root.geometry("300x200")

# Set a professional neon red-blue gradient background using a Canvas
canvas = tk.Canvas(root, width=300, height=200)
canvas.pack(fill="both", expand=True)

# Create gradient effect by drawing colored rectangles
for i in range(0, 200):
    r = int(255 * (i / 200))
    b = int(255 * (1 - i / 200))
    color = f'#{r:02x}00{b:02x}'
    canvas.create_rectangle(0, i, 300, i+1, outline=color, fill=color)

# Custom neon-style button using a Canvas window
button_canvas = tk.Canvas(root, width=160, height=40, bg="#000000", highlightthickness=0)
button_canvas_window = canvas.create_window(150, 120, window=button_canvas)
button_canvas.create_rectangle(2, 2, 158, 38, outline="#ff0055", fill="#111111", width=2)

# Add label and button on top of canvas
label = tk.Label(root, text="Click below to detect faces", font=("Arial", 12), bg="#000000", fg="#ffffff")
label_window = canvas.create_window(150, 60, window=label)

# Button inside button_canvas
button = tk.Button(button_canvas, text="Detect Faces", command=detect_faces, font=("Arial", 10), bg="#111111", fg="#ff0055", activebackground="#ff0055", activeforeground="#ffffff", relief="flat", highlightthickness=0)
button.place(x=20, y=5, width=120, height=30)

root.mainloop()