import cv2
import time

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('Original Frame', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  # pressing q breaks the loop anf allows for the next commands to run shutting it all down 
cap.release()
cv2.destroyAllWindows()