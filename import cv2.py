import cv2
import time

cap = cv2.VideoCapture(0)
start = time.time()
frames = 0

while frames < 100:
    ret, frame = cap.read()
    if not ret:
        break
    frames += 1
    cv2.imshow('Original Frame', frame)

end = time.time()
print(f"FPS: {frames / (end - start)}")
cap.release()