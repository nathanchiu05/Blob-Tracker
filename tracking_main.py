import cv2
import numpy as np

#choose file
video_path = "input/input3.mov"

cap = cv2.VideoCapture(video_path)

#vid info
fps = int(cap.get(cv2.CAP_PROP_FPS))
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#video out
out = cv2.VideoWriter("output/output3.mov", cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))

#load trackers
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
car_cascade  = cv2.CascadeClassifier("cars.xml")


while True: #while cap is opened (vid is playing)
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)  #2 pixel thick

    # #blur the face
    #     face_roi = frame[y:y+h, x:x+w]
    #     face_roi = cv2.GaussianBlur(face_roi, (99, 99), 30)
    #     frame[y:y+h, x:x+w] = face_roi

    # detect cars
    cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 225, 0), 2) 

    #detect light change (fireworks etc)
    hsv =  cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 100, 150]) 
    upper = np.array([179, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for i,contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        if cv2.contourArea(contour) > 500: #min area to be considered
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
            
            label = f"ID {i+1}"
            cv2.putText(frame, label, (x, y-10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 
                        0.6, (0, 0, 255), 2)

    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("Frame", result)
    cv2.imshow("Mask", mask)
    cv2.imshow("Highlighted", result)

    #write to vieo
    out.write(frame)

    #Show live preview
    cv2.imshow("Processing", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()