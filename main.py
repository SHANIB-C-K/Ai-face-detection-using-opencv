import cv2 as cv

video = cv.VideoCapture(0)

# Load the face cascade classifier
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    success, frame = video.read()

    if not success:
        print("Cannot read video")
        break

    # Fix font parameter from ACCESS_MASK to FONT_HERSHEY_SIMPLEX
    cv.putText(frame, "Press q to quit", (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 4)

    # Only print faces if any are detected
    if len(faces) > 0:
        print(faces)

    for x,y,w,h in faces:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2)
        cv.putText(frame, 'Face', (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    cv.flip(frame, 1)

    cv.imshow("Face detection", frame)

    if cv.waitKey(1) == ord('q'):
        break

video.release()
cv.destroyAllWindows()