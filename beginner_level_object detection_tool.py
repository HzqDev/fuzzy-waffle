from ultralytics import YOLO
import cv2

# Load YOLOv8 nano pretrained on COCO dataset (80 common classes)
model = YOLO("yolov8n.pt")

# Load your image
img_path = ""
img = cv2.imread(img_path)

# Run inference (results is a list, so take first element)
results = model(img)
result = results[0]

# Show the image with detected objects and bounding boxes
result.show()
